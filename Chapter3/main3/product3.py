from gtts import gTTS
from playsound import playsound
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# text = "안녕하세요. 전동윤입니다. 파이썬과 40개의 작품들을 진행중입니다."
file_path = 'mytext.txt'

with open(file_path, 'rt', encoding='UTF8') as f :
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save("mytext.mp3")
