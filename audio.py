import pyaudio
import wave
import timeit

# define stream chunk
chunk = 1000

# open a wav format music
f = wave.open("audio/snare.wav", "rb")

# instantiate PyAudio
p = pyaudio.PyAudio()

# open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)

# read data
data = f.readframes(chunk)

start = timeit.default_timer()

# play stream
while data:
    stream.write(data)
    data = f.readframes(chunk)

elapsed = timeit.default_timer() - start
print elapsed

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()
