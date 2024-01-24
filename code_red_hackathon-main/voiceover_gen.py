from paragraphs_array import paragraphs
import os
from gtts import gTTS
os.makedirs("voiceovers",exist_ok=True)
z=0
for para in paragraphs:
    z+=1
    obj = gTTS(text=paragraphs[0], lang='en', slow=False)
    obj.save("./voiceovers/video_{}.mp3".format(z))