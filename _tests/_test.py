############# Decorators ##########
# import sys
# folder = '/home/zoy/git/learn/courses/Python Tutorial'
# if folder not in sys.path:
#     sys.path.append(folder)

# from decorators_pycon import CountCalls
###################################

from TTS.api import TTS
from pydub import AudioSegment

# Load a pre-trained English model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# Convert text to WAV
tts.tts_to_file(text="Hello, this is a test to check audio quality and prevent cutoff.", file_path="output.wav")

# Convert to MP3
sound = AudioSegment.from_wav("output.wav")
sound.export("output.mp3", format="mp3")
