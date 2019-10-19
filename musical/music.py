from pydub import AudioSegment
from pydub.playback import play
import sys

def stupid_func():
    print("very simple music player on pydub")
    print("need ffmpeg to work")
    print("Usage: music format_of_file filename")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        stupid_func()
        quit(0)
    try:
        print(len(sys.argv))
        sound = AudioSegment.from_file(sys.argv[2], format=sys.argv[1])
        play(sound)
    except KeyboardInterrupt:
        print("Goodbye!")
