from moviepy.editor import VideoFileClip
import os

def convert_mp4_to_mp3(mp4_file_path):
    try:
        # Memastikan file MP4 ada
        if not os.path.exists(mp4_file_path):
            print("File MP4 tidak ditemukan.")
            return

        # Load video menggunakan moviepy
        video_clip = VideoFileClip(mp4_file_path)

        # Tentukan nama file MP3 output (berdasarkan nama file MP4)
        mp3_file_path = os.path.splitext(mp4_file_path)[0] + '.mp3'

        # Ekstraksi audio dan simpan sebagai file MP3
        video_clip.audio.write_audiofile(mp3_file_path)

        # Menutup video clip
        video_clip.close()

        print(f"Konversi selesai! File MP3 disimpan sebagai: {mp3_file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Masukkan path file MP4 yang ingin dikonversi
mp4_file_path = input("Masukkan path file MP4: ")
convert_mp4_to_mp3(mp4_file_path)
