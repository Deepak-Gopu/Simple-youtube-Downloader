from pytube import YouTube
yt = YouTube(input("ENter the link:"))
print(yt.title)
stream = yt.streams.first()
stream.download("D:/")
