import openai
import re,os
import urllib.request
from gtts import gTTS
from moviepy.editor import *
from api_key import API_KEY
openai.api_key = API_KEY
from moviepy.config import change_settings
# Clear MoviePy's cache
change_settings({"IMAGEMAGICK_BINARY": "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})
os.environ["IMAGEIO_FFMPEG_EXE"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

with open("generated_text.txt", "r") as file:
    text = file.read()

paragraphs = re.split(r"[,.]", text)
os.makedirs("audio")
os.makedirs("images")
os.makedirs("videos")

i = 1
clips = []

for para in paragraphs[:-1]:
    response = openai.Image.create(
        prompt=para.strip(),
        n=1,
        size="1024x1024",
    )
    print("generate new ai image from paragraph...")
    image_url = response["data"][0]["url"]
    urllib.request.urlretrieve(image_url, f"images/image{i}.jpg")
    print("the generated image saved in images folder")

    tts = gTTS(text=para, lang='en', slow=False)
    tts.save(f"audio/voiceover{i}.mp3")
    print("the paragraph converted into voiceover and saved in audio folders")

    print("extract voiceover and get duration..")
    audio_clip = AudioFileClip(f"audio/voiceover{i}.mp3")
    audio_duration = audio_clip.duration

    print("extract image clip and set duration..")
    image_clip = ImageClip(f"images/image{i}.jpg").set_duration(audio_duration)

    print("customize the text clip")
    text_clip = TextClip(para, fontsize=50, color="white")
    text_clip = text_clip.set_pos('center').set_duration(audio_duration)

    print("concatenate audio, image to create a final clip")
    try:
        clip = image_clip.set_audio(audio_clip)
        final_clip = CompositeVideoClip([clip, text_clip])
        clips.append(final_clip)

        final_clip.write_videofile(f"videos/video_{i}.mp4", fps=24)
        print(f"The video {i} has been successfully created.")
    except Exception as e:
        print(f"Error creating video {i}: {e}")

    i += 1

if clips:
    print("concatenate all video clips to create a final video")
    final_video = concatenate_videoclips(clips, method="compose")
    final_video.fps = 24  # Set the desired frames per second
    final_video.write_videofile("final_video.mp4")
    print("the video has been created")
else:
    print("No valid clips to concatenate.")
