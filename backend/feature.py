import playsound as playsound
import eel

@eel.expose

def playAssistantSound():
    music_dir = "frontend\\assets\\audio\\start_sound.mp3"
    playsound.playsound(music_dir)