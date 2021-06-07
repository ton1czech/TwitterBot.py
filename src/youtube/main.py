from pytube import YouTube, Channel

def fetch_youtube():
    channel = Channel('https://www.youtube.com/channel/UCblA_CnykG2Dw_6IMwZ9z9A/videos')

    link = channel.video_urls[0]
    title = YouTube(link).title

    # try - except just in case I want to run the code locally
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