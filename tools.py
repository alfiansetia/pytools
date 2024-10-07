import yt_dlp
from moviepy.editor import VideoFileClip
import os

# Fungsi untuk mengonversi MP4 ke MP3
def convert_mp4_to_mp3(mp4_file_path):
    try:
        if not os.path.exists(mp4_file_path):
            print("File MP4 tidak ditemukan.")
            return

        video_clip = VideoFileClip(mp4_file_path)
        mp3_file_path = os.path.splitext(mp4_file_path)[0] + '.mp3'
        video_clip.audio.write_audiofile(mp3_file_path)
        video_clip.close()

        print(f"Konversi selesai! File MP3 disimpan sebagai: {mp3_file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk mengunduh video YouTube
def download_video(url):
    try:
        # Tentukan folder untuk menyimpan video
        download_folder = os.path.join(os.getcwd(), "videos")

        # Membuat folder jika belum ada
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Membuat opsi dasar
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        }

        # Cek daftar format yang tersedia untuk video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)  # Hanya ekstrak info, tanpa download
            formats = info_dict.get('formats', None)

            # Tampilkan daftar format yang tersedia
            # print("Daftar format yang tersedia:")
            # for f in formats:
            #     # Dapatkan informasi format (dengan pengecekan keberadaan atribut)
            #     format_code = f.get('format_id', 'N/A')
            #     ext = f.get('ext', 'N/A')
            #     resolution = f.get('resolution', 'N/A')
            #     fps = f.get('fps', 'N/A')
            #     vcodec = f.get('vcodec', 'N/A')

            #     print(f"Format code: {format_code} - {ext} - {resolution} - {fps} fps - {vcodec}")

            # # Meminta user memilih format
            # format_code = input("Masukkan kode format yang ingin diunduh: ")

            # Update opsi dengan format yang dipilih
            # ydl_opts['format'] = format_code

            # Mengunduh video dengan format yang dipilih
            info_dict = ydl.extract_info(url, download=True)
            video_file_path = ydl.prepare_filename(info_dict)

            print(f"Video berhasil diunduh di: {video_file_path}")
            print('Mengonversi ke MP3...')

            # Konversi MP4 ke MP3
            convert_mp4_to_mp3(video_file_path)
            print('Konversi ke MP3 berhasil!')
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# URL video YouTube yang ingin diunduh
video_url = input("Masukkan URL video YouTube: ")
download_video(video_url)
