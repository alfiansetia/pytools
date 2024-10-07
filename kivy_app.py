import os
import yt_dlp
from moviepy.editor import VideoFileClip
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup

# Fungsi untuk mengonversi MP4 ke MP3
def convert_mp4_to_mp3(mp4_file_path):
    try:
        if not os.path.exists(mp4_file_path):
            return "File MP4 tidak ditemukan."

        video_clip = VideoFileClip(mp4_file_path)
        mp3_file_path = os.path.splitext(mp4_file_path)[0] + '.mp3'
        video_clip.audio.write_audiofile(mp3_file_path)
        video_clip.close()

        return f"Konversi selesai! File MP3 disimpan sebagai: {mp3_file_path}"
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

# Fungsi untuk mengunduh video YouTube
def download_video(url):
    try:
        download_folder = os.path.join(os.getcwd(), "videos")

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_file_path = ydl.prepare_filename(info_dict)

            mp3_conversion_status = convert_mp4_to_mp3(video_file_path)
            return f"Video berhasil diunduh di: {video_file_path}\n{mp3_conversion_status}"
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

# Kelas untuk Aplikasi Kivy
class YouTubeDownloaderApp(App):
    def build(self):
        # Mengatur ukuran jendela
        Window.size = (600, 400)
        
        # Membuat layout utama
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Label untuk judul aplikasi
        self.title_label = Label(text='YouTube MP4 to MP3 Downloader', font_size=20, size_hint=(1, 0.2))
        layout.add_widget(self.title_label)
        
        # Input field untuk URL YouTube
        self.url_input = TextInput(hint_text='Masukkan URL video YouTube di sini...', multiline=False, size_hint=(1, 0.2))
        layout.add_widget(self.url_input)

        # Tombol untuk memulai unduhan
        self.download_button = Button(text='Unduh & Konversi', size_hint=(1, 0.2))
        self.download_button.bind(on_press=self.on_download_press)
        layout.add_widget(self.download_button)

        # Scroll view untuk menampilkan log hasil unduhan
        self.result_label = Label(text='', size_hint_y=None)
        self.result_label.bind(texture_size=self.result_label.setter('size'))

        scrollview = ScrollView(size_hint=(1, 1))
        scrollview.add_widget(self.result_label)
        layout.add_widget(scrollview)

        return layout

    def on_download_press(self, instance):
        # Mendapatkan URL dari input
        url = self.url_input.text

        if url:
            # Tampilkan popup saat memproses unduhan
            popup = Popup(title='Mengunduh dan Mengonversi',
                          content=Label(text='Proses sedang berjalan...'),
                          size_hint=(0.6, 0.4))
            popup.open()

            # Mulai unduhan di latar belakang dan perbarui hasil
            download_result = download_video(url)

            # Tutup popup setelah unduhan selesai
            popup.dismiss()

            # Perbarui teks log dengan hasil unduhan dan konversi
            self.result_label.text += f"\n{download_result}\n"
        else:
            self.result_label.text += "Masukkan URL yang valid.\n"

# Menjalankan aplikasi
if __name__ == '__main__':
    YouTubeDownloaderApp().run()
