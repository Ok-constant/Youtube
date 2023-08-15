import vlc
import asyncio
#import keyboard
from yt_dlp import YoutubeDL


# 720 m4a
# 480
settings = {
	"format_sort":["res:480", "ext:webm:weba"]
}

id = input("Insert youtube id: ")
d = YoutubeDL(settings).extract_info(f"https://youtu.be/{id}", download=False)

media = None
instance = vlc.Instance()
try:
	formats = d["requested_formats"]
	video = formats[0]["url"]
	audio = formats[1]["url"]
	media = instance.media_new(video)
	media.slaves_add(vlc.MediaSlaveType.audio, True, audio)
	print(video, audio)
except Exception as e:
	media = instance.media_new(d["url"])

player = instance.media_player_new()

player.audio_set_volume(70)
player.set_media(media)

#pos = input("pos: ")

#player.set_position(float(pos))
"""
async def run():
	player.play()
	while True:
		keyboard.wait("n")
		print("n pressed")
		pos = player.get_position()
		player.set_position(pos + 0.01)"""

#asyncio.run(run())
player.play()
while True:
	pass
