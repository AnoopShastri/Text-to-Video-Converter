from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, concatenate_videoclips
from gtts import gTTS
import os
from paragraphs_array import paragraphs

def generate_voiceover(text, output_path):
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)

def combine_images_and_audio(images_folder, text_array, output_video_path):
    clips = []

    for i, image_file in enumerate(os.listdir(images_folder)):
        image_path = os.path.join(images_folder, image_file)
        text = text_array[i]

        # Generate voiceover for the current text
        voiceover_path = f"voiceover_{i}.mp3"
        generate_voiceover(text, voiceover_path)

        # Create TextClip with the image file and the generated voiceover
        image_clip = VideoFileClip(image_path, audio=False, fps_source='fps')
        voiceover_clip = AudioFileClip(voiceover_path, fps=image_clip.fps)
        text_clip = TextClip(text, fontsize=20, color='white', bg_color='black')

        # Combine the image, text, and voiceover
        combined_clip = CompositeVideoClip([image_clip, text_clip.set_pos('bottom').set_duration(image_clip.duration)])
        combined_clip = combined_clip.set_audio(voiceover_clip)

        clips.append(combined_clip)

    # Concatenate all clips into a final video
    final_clip = concatenate_videoclips(clips)

    # Write the final video to the output path
    final_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

    # Clean up temporary voiceover files
    for i in range(len(clips)):
        os.remove(f"voiceover_{i}.mp3")

if __name__ == "__main__":
    images_folder = "./images"
    text_array = paragraphs
    output_video_path = "output_video.mp4"

    combine_images_and_audio(images_folder, text_array, output_video_path)
