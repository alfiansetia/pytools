import yt_dlp
import os

def download_video(url):
    try:
        # Tentukan folder Downloads di dalam direktori proyek
        download_folder = os.path.join(os.getcwd(), "videos")

        # Membuat folder Downloads jika belum ada
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Membuat opsi untuk mengatur format dan lokasi penyimpanan
        ydl_opts = {
            'format': 'best',  # Mendownload video dengan kualitas terbaik
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Menyimpan ke folder Downloads di proyek
        }

        # Mengunduh video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Video berhasil diunduh di folder: {download_folder}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# URL video YouTube yang ingin diunduh
video_url = input("Masukkan URL video YouTube: ")
download_video(video_url)
