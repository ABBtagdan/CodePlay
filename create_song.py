#Tage

from pydub import AudioSegment
import os

def concat_sound(sound_list):
    export = AudioSegment.from_mp3(sound_list[0]+".mp3")[:250]
    for s in sound_list[1:]:
        export += AudioSegment.from_mp3(s+".mp3")[:250]
    os.remove("./sounds/temp.mp3")
    export.export("./sounds/temp.mp3")
    return ["./sounds/temp"]