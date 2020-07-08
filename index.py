from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, CompositeAudioClip
import os

files = []

directory = "./"
for filename in os.listdir(directory):
    if filename.endswith(".mp4"): 
        # print(os.path.join(directory, filename))
        files.append(str(filename))
    else:
    	continue

max_length = 33000 #550 minutes
print(files)

clip = VideoFileClip(files[0])
for i in range(1, 1+len(files[1:])):
	print("-"*10 + "Processing Video: "+ str(files[i]) + "-"*10)
	print("Duration of Clip before merge: ", clip.duration)
	right_merge = VideoFileClip(files[i])
	clip = concatenate_videoclips([clip,right_merge])

	print("Duration of Clip after merge: ", clip.duration)
	if clip.duration > max_length:
		print("need to split from video =>", files[i])

final = clip.audio
final.fps = 44100
final.write_audiofile("new.mp3")