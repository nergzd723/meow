# Meow part
# Simple music player
# Copyright 2019, x0r3d(yeah, it's me)
# 19.10.19: Initial write
from pydub import AudioSegment
from pydub.playback import play
from sys import argv

def stupid_func():
    print("very simple music player on pydub")
    print("need ffmpeg to work")
    print("Usage: music format_of_file filename")
def play_music(type, path):
    sound = AudioSegment.from_file(path, format=type)
    play(sound)

if __name__ == "__main__":
    if len(argv) == 1:
        stupid_func()
<<<<<<< HEAD
        quit(0)
    else:
        play_music(sys.argv[1], sys.argv[2])

=======
        exit(0)
    try:
        print(len(argv))
        sound = AudioSegment.from_file(argv[2], format=argv[1])
        play(sound)
    except KeyboardInterrupt:
        print("Ctrl^C")
        exit()
>>>>>>> cc6323abe3eb837ae678386a580e32bd1ab02e19
