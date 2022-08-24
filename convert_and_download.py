from pathlib import Path
import youtube_dl
import requests
import os

def downloadVideosFromIds(urls):
    SAVE_PATH = str(os.path.join(Path.home(), "Downloads/songs"))
    try:
        os.mkdir(SAVE_PATH)
    except:
        print("download folder exists")
    
    ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192',}], 'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s'}

    for url in urls:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)


# check for a single url
# downloadVideosFromIds(['https://www.youtube.com/watch?v=eZQyVUTcpM4'])