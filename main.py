from winsound import Beep
import pyttsx3
from time import sleep

minutes, secs = 0, 0

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.say("Start")
engine.runAndWait()

for _ in range(30):
    for i in range(60):
        print(f"{minutes}:{secs}")
        Beep(1500, 500)
        sleep(0.5)
        secs += 1
    minutes += 1
    engine.say(f"Minute {minutes}")
    engine.runAndWait()
    secs = 0