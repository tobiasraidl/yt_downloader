from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_youtube_video(video_url, save_path="./"):
    yt = YouTube(video_url, on_progress_callback = on_progress)
    print(yt.title)
    
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=save_path)

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    save_path = "./out"
    download_youtube_video(video_url, save_path)
