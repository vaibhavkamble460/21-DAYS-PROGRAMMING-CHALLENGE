import pafy
url = "https://youtu.be/wK3TgKAwHS8"
video = pafy.new(url)
streams = video.streams
for i in streams:
    print(i)

best = video.getbest()
print(best.resolution,best.extension)

best.download()
print("video downloaded successfully")
