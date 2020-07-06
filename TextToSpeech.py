from gtts import gTTS
from pygame import mixer
from time import sleep

myobj = gTTS(text='Most Chinese students learn English in school from a young age, but the tutoring platforms give them access to native speakers, who help them refine their grammar, pronunciation, and listening comprehension skills', lang='en', slow=False)
myobj.save("welcome.mp3") 
sleep(50)

mixer.init()
mixer.music.load('welcome.mp3')
mixer.music.play()
sleep(30)
print('done')