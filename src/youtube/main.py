# Import modules
from pytube import YouTube
from pytube import Channel

# Get title and link of my latest YouTube video
def fetch_youtube():
    global title, link
    title = link = None

    channel = Channel('https://www.youtube.com/channel/UCblA_CnykG2Dw_6IMwZ9z9A/videos')
    link = channel.video_urls[0]

    video = YouTube(link)
    title = video.title

    try:
        read_checker = open('src/youtube/checker.txt', 'r')
    except FileNotFoundError:
        read_checker = open('youtube/checker.txt', 'r')

    latest_title = read_checker.readline()

    if latest_title == title:
        title = link = None
    else:
        try:
            update_checker = open('src/youtube/checker.txt', 'w')
        except FileNotFoundError:
            update_checker = open('youtube/checker.txt', 'w')

        update_checker.write(title)
        
    return title, link