import librosa
import soundfile

sampleRate = 8000
file = 'NM - Baby 808.wav'
input = f'/Users/triddle/Dropbox/Music/Samples/Downsample/Source/{file}'
output = f'/Users/triddle/Dropbox/Music/Samples/Downsample/Destination/{file}_{sampleRate}Hz.wav'

data, sr = librosa.load(input, sr=sampleRate)
soundfile.write(output, data, sr, subtype='PCM_24')
