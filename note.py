import pyaudio
import wave
from music21 import *

# open the audio file
audio = wave.open("beat.wav", "rb")

# get the audio file properties
sample_rate = audio.getframerate()
num_frames = audio.getnframes()
num_channels = audio.getnchannels()
audio_data = audio.readframes(num_frames)

# close the audio file
audio.close()

# create a stream object to hold the musical notation
stream_obj = stream.Stream()

# # create a pitch object for each note in the audio data
# for i in range(0, len(audio_data), num_channels * 2):
#     data = audio_data[i:i + num_channels * 2]
#     sample = int.from_bytes(data, byteorder='little', signed=True)
#     pitch = int(440 * 2 ** ((sample + 6900) / (12 * 4096)))
#     duration = 0.5  # set the duration of each note to 0.5 seconds
#     note_obj = note.Note()
#     note_obj.pitch.frequency = pitch
#     note_obj.duration.quarterLength = duration
#     stream_obj.append(note_obj)

# # show the musical notation
# stream_obj.show()

for i in range(0, len(audio_data), num_channels * 2):
    data = audio_data[i:i + num_channels * 2]
    sample = int.from_bytes(data, byteorder='little', signed=True)
    pitch = int(440 * 2 ** ((sample + 6900) / (12 * 4096)))
    duration = 0.5  # set the duration of each note to 0.5 seconds
    note_obj = note.Note()
    note_obj.pitches = [pitch.Pitch(frequency=pitch)]
    note_obj.duration.quarterLength = duration
    stream_obj.append(note_obj)

# show the musical notation
stream_obj.show()