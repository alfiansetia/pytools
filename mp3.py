import yt_dlp
import os

def download_mp3(youtube_url):
    # Opsi untuk mengunduh audio dalam format MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,  # Ekstrak audio
        'audioformat': 'mp3',  # Format audio yang diinginkan
        'outtmpl': os.path.join('mp3', '%(title)s.%(ext)s'),
        'postprocessors': [{  # Proses pasca pengunduhan
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Format output
            'preferredquality': '192',  # Kualitas output
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    url = input("Masukkan URL video YouTube: ")
    download_mp3(url)
