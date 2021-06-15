from pytube import YouTube, Channel

def fetch_latest_youtube_vid():
    channel = Channel('https://www.youtube.com/channel/UCblA_CnykG2Dw_6IMwZ9z9A/videos')

    link = channel.video_urls[0]
    title = YouTube(link).title

    read_checker = open('src/latest_youtube_vid/checker.txt', 'r')

    latest_title = read_checker.readline()

    if latest_title == title:
        title = link = None
    else:
        update_checker = open('src/latest_youtube_vid/checker.txt', 'w')
        update_checker.write(title)
        
    return title, link