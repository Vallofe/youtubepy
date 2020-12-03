import requests
import pafy
import sys
import json

API_YOUTUBEV3 = ""

def Youtube(search):
    r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={}&type=video&key={}".format(search,API_YOUTUBEV3))
    data = r.text
    a = json.loads(data)
    if a["items"] != []:
        for music in a["items"]:
            break
        dl = "https://www.youtube.com/watch?v={}".format(str(music['id']["videoId"]))
        splitin = dl.split("?v=")[1]
        IMG = "https://i.ytimg.com/vi/{}/default.jpg".format(splitin)
        vid = pafy.new(dl)
        stream = vid.streams
        print(stream)
        for s in stream:
            print("LINKIMAGE:\n{}\nURL:\n{}\nTITLE:\n{}\nDURATION:\n{}\nAUTHOR:\n{}\nDITONTON:\n{}\nLINKDOWNLOAD:\n{}".format(IMG,dl,vid.title,vid.duration,vid.author,vid.viewcount,s.url))