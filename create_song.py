#Tage

from pydub import AudioSegment
import os

soundrange = {"doo": (4000, 4250), "ree": (3000, 3250), "mii": (2000, 2250), "faa": (1000, 1250), "sol": (0,250)}

def concat_sound(sound_list, instrument):
    uncut_audio = AudioSegment.from_mp3(f"./sounds/{instrument}.mp3")
    export = uncut_audio[soundrange[sound_list[0][-3:]][0]:soundrange[sound_list[0][-3:]][1]]
    for s in sound_list[1:]:
        print(s[-3:])
        export += uncut_audio[soundrange[s[-3:]][0]:soundrange[s[-3:]][1]]
    os.remove("./sounds/temp.mp3")
    export.export("./sounds/temp.mp3")
    return ["./sounds/temp"]