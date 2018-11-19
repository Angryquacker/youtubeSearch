from __future__ import unicode_literals
import requests
import youtube_dl
import os
from bs4 import BeautifulSoup
from playsound import playsound
from random import randint

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

#create a random string as the name of the new file as the prevent replaying self/wrong song
def gen_random_name():
    global name
    string = []
    s = ''
    for i in range(10):
        string.append(chr(randint(65, 90)))
    name = s.join(string)
    return name

#Have the youtube-dl download only the video's audio track
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    "outtmpl": './' + gen_random_name() + '.m4a'
}


#Download the audio
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video])


#Try/Catch block ensures video is deleted even if program is exited early
try:
    #play the audio
    playsound('./' + name +'.mp3')
except:
    # Delete the file when done
    os.remove('./' + name + '.mp3')


#Delete the file when done
os.remove('./' + name + '.mp3')
