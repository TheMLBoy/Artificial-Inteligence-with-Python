import ffmpeg
import os
import speech_recognition as sr

command2mp3 = "ffmpeg -i temp.mp4 temp.mp3"
command2wav = "ffmpeg -i temp.mp3 temp.wav"
os.system(command2mp3)
os.system(command2wav)
filename = "temp.wav"
r = sr.Recognizer()
f = open("Dialogue.txt", "w")
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    f.write(r.recognize_google(audio_data))
f.close()

print("\nPlease Speak the dialogue you wanna search in this video: ")
inp=""
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
try:
    text = r.recognize_google(audio_data)
    inp+=text
except:
	inp=""
	

with open('Dialogue.txt', 'r') as file:
	found=False
	for line in file:
		if inp in line:
			found=True
			break


if inp=="":
	found=False
	
			
if found==True:
    print (inp+" is present in this video.")
else:
    print (inp+" is not present in this video.")
	
	
os.remove("temp.mp3")
os.remove("temp.wav")
os.remove("Dialogue.txt")