from pytube import YouTube


def download(video_link):
    youtube_object = YouTube(video_link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download(r'C:\Users\Forbidden\Desktop\Downloads')
    except ValueError:
        return "There has been an error in downloading your youtube video!"
    return "This download has completed!"


video_link = input("Put your youtube link here: ")
download(video_link)

