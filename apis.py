from wsgiref import headers
from dotenv import load_dotenv
import requests
import base64
from json import dumps, loads
load_dotenv()
import os


def api_1_shazam():
    shazam_key = os.getenv("SHAZ_KEY")
    shazam_host = os.getenv("SHAZ_HOST")
    file_binary = open("recording.wav", "rb").read()
    payload = base64.b64encode(file_binary).decode('utf-8')
    url = "https://shazam.p.rapidapi.com/songs/v2/detect"

    querystring = {"timezone":"America/Chicago","locale":"en-US"}
    headers = {
        'X-RapidAPI-Key': shazam_key,
        'X-RapidAPI-Host': shazam_host,
        'Content-Type': "text/plain"
    }

    response = requests.post(url, data=payload, headers=headers, params=querystring)

    data = response.json()

    song_name = data['track']['title']
    artist = data['track']['subtitle']
    cover_art = data['track']['images']['coverart']

    # print("🎵 Song:", song_name)
    # print("🎤 Artist:", artist)
    # print("🖼️ Cover Art URL:", cover_art)

    return {
        "song": song_name,
        "artist": artist,
        "cover_art": cover_art
    }
