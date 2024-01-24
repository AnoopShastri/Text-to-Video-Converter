'''from moviepy.editor import VideoFileClip, AudioFileClip
import os

def merge_video_with_voiceover(video_folder, voiceover_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mp4"):
            video_path = os.path.join(video_folder, video_file)
            voiceover_file = video_file.replace(".mp4", ".mp3")
            voiceover_path = os.path.join(voiceover_folder, voiceover_file)

            if os.path.exists(voiceover_path):
                # Load video and audio clips
                video_clip = VideoFileClip(video_path)
                audio_clip = AudioFileClip(voiceover_path)

                # Set the audio of the video clip to the loaded voiceover audio
                video_clip = video_clip.set_audio(audio_clip)

                # Write the merged video with voiceover to the output folder
                output_filename = f"merged_{video_file}"
                output_path = os.path.join(output_folder, output_filename)
                video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")


video_folder = "./videos"
voiceover_folder = "./voiceovers"
os.makedirs("./output_voiceover_video",exist_ok=True)
output_folder = "./output_voiceover_video"
merge_video_with_voiceover(video_folder, voiceover_folder, output_folder)
'''
'''
from moviepy.editor import VideoFileClip, AudioFileClip
import os

video_folder = r".\videos"
voiceover_folder = r".\voiceovers"
output_folder = r".\output_voiceover_video"
video_file = "video_1.mp4"
os.makedirs(output_folder, exist_ok=True)

video_path = os.path.join(video_folder, video_file)
voiceover_file = video_file.replace(".mp4", ".mp3")
voiceover_path = os.path.join(voiceover_folder, voiceover_file)
print(video_path)
print(voiceover_path)
if os.path.exists(voiceover_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(voiceover_path)
    video_clip = video_clip.set_audio(audio_clip)

    output_filename = f"merged_{video_file}"
    output_path = os.path.join(output_folder, output_filename)
    print(output_path)
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")'''

'''
from moviepy.editor import VideoFileClip, AudioFileClip
import os

def merge_video_with_voiceover(video_folder, voiceover_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mp4"):
            video_path = os.path.join(video_folder, video_file)
            
            # Assuming voiceover files have the same name as video files
            voiceover_file = video_file.replace(".mp4", ".mp3")
            voiceover_path = os.path.join(voiceover_folder, voiceover_file)

            if os.path.exists(voiceover_path):
                # Load video and audio clips
                video_clip = VideoFileClip(video_path)
                audio_clip = AudioFileClip(voiceover_path)

                # Calculate the number of times the video should be looped
                loop_count = int(audio_clip.duration / video_clip.duration) + 1

                # Loop the video to match the audio duration
                video_clip = video_clip.fx(vfx.audio_loop, n=loop_count)

                # Set the audio of the video clip to the loaded voiceover audio
                video_clip = video_clip.set_audio(audio_clip)

                # Write the merged video with voiceover to the output folder
                output_filename = f"merged_{video_file}"
                output_path = os.path.join(output_folder, output_filename)
                video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
video_folder = "./videos"
voiceover_folder = "./voiceovers"
os.makedirs("./output_voiceover_video", exist_ok=True)
output_folder = "./output_voiceover_video"
merge_video_with_voiceover(video_folder, voiceover_folder, output_folder)
'''
'''
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment
import os

def merge_video_with_voiceover(video_folder, voiceover_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mp4"):
            video_path = os.path.join(video_folder, video_file)
            
            # Assuming voiceover files have the same name as video files
            voiceover_file = video_file.replace(".mp4", ".mp3")
            voiceover_path = os.path.join(voiceover_folder, voiceover_file)
            #print(voiceover_path)
            if os.path.exists(voiceover_path):
                # Load video and audio clips
                video_clip = VideoFileClip(video_path)
                
                # Use pydub to loop the audio
                audio_clip = AudioSegment.from_file(voiceover_path, format="mp3")
                looped_audio = audio_clip * (video_clip.duration / audio_clip.duration)

                # Set the audio of the video clip to the looped audio
                video_clip = video_clip.set_audio(looped_audio)

                # Write the merged video with voiceover to the output folder
                output_filename = f"merged_{video_file}"
                output_path = os.path.join(output_folder, output_filename)
                video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    video_folder = r".\videos"
    voiceover_folder = r".\voiceovers"
    os.makedirs("./output_voiceover_video", exist_ok=True)
    output_folder = r".\output_voiceover_video"
    merge_video_with_voiceover(video_folder, voiceover_folder, output_folder)'''
from moviepy.editor import VideoFileClip, AudioFileClip, vfx
import os

video_folder = r".\videos"
voiceover_folder = r".\voiceovers"
output_folder = r".\output_voiceover_video"
video_file = "video_1.mp4"
os.makedirs(output_folder, exist_ok=True)

video_path = os.path.join(video_folder, video_file)
voiceover_file = video_file.replace(".mp4", ".mp3")
voiceover_path = os.path.join(voiceover_folder, voiceover_file)
print(video_path)
print(voiceover_path)
if os.path.exists(voiceover_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(voiceover_path)

    # Calculate the number of times to loop the video
    num_loops = int(audio_clip.duration / video_clip.duration) + 1
    
    # Loop the video
    video_clip = video_clip.fx(vfx.loop, n=num_loops)

    # Trim the video to match the duration of the audio
    video_clip = video_clip.subclip(0, audio_clip.duration)

    # Set the audio of the video to the provided audio clip
    video_clip = video_clip.set_audio(audio_clip)

    output_filename = f"merged_{video_file}"
    output_path = os.path.join(output_folder, output_filename)
    print(output_path)
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

