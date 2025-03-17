import librosa
import matplotlib.pyplot as plt
import os

data, sampling_rate = librosa.load("./data/RAVDESS_Audio_Speech/Actor_01/03-01-01-01-01-01-01.wav")
data, _ = librosa.effects.trim(data)
plt.figure(figsize=(25, 5))
plt.plot(data)
