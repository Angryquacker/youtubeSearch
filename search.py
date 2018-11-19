from __future__ import unicode_literals
import requests
import youtube_dl
from bs4 import BeautifulSoup
from playsound import playsound

#Get Keyword
query = input("Enter Query: ")

#Get the source code of the youtube search page
data = requests.get("https://www.youtube.com/results?search_query=" + query)
source_code = BeautifulSoup(data.text, features="html.parser")

#Get the link to the youtube video
for a in source_code.findAll('a'):
    video = a.get('href')
    if video[:4] == '/wat':
        video = 'https://www.youtube.com' + video
        break


#Have the youtube-dl download only the video's audio track
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    "outtmpl": './audio.m4a'
}


#Download the audio
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video])


#play the audio
playsound('./audio.mp3')




