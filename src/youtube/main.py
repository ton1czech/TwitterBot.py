# Import modules
from pytube import YouTube
from pytube import Channel

# Get title and link of my latest YouTube video
def get_youtube_video():
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
    except FileNotFoundError:
        read_checker = open('checker.txt', 'r')

    latest_title = read_checker.readline()

    if latest_title == title:
        title = link = None
        return
    else:
        try:
            update_checker = open('src/youtube/checker.txt', 'w')
        except:
            update_checker = open('checker.txt', 'w')
        update_checker.write(title)

get_youtube_video()