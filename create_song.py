#Tage

from pydub import AudioSegment
import os

soundrange = {"doo": (1000, 1250), "ree": (750, 1000), "mii": (500, 750), "faa": (250, 500), "sol": (0,250)}

def concat_sound(sound_list):
    uncut_audio = AudioSegment.from_mp3("./sounds/Drums.mp3")
    export = uncut_audio[soundrange[sound_list[0][-3:]][0]:soundrange[sound_list[0][-3:]][1]]
    for s in sound_list[1:]:
        export += uncut_audio[soundrange[s[-3:]][0]:soundrange[s[-3:]][1]]
    os.remove("./sounds/temp.mp3")
    export.export("./sounds/temp.mp3")
    return ["./sounds/temp"]