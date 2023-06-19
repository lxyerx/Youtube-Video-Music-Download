from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def Download(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject.streams.get_highest_resolution().download()
        video_title = youtubeObject.title
        mp4_file_path = f"{video_title}.mp4"
        mp3_file_path = f"{video_title}.mp3"
        
        clip = VideoFileClip(mp4_file_path)
        clip.audio.write_audiofile(mp3_file_path)
        clip.close()
        
        os.remove(mp4_file_path)  # MP4 dosyasını siler
        
        print("İndirme başarılı.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))

link = input("Youtube Video URL'sini Girin: ")
Download(link)
