import matplotlib.pyplot as plt
import librosa
import librosa.display
import os

RAVDESS_PATH = "../data/RAVDESS_Audio_Speech"

data, sampling_rate = librosa.load(os.path.join(RAVDESS_PATH, "Actor_01/03-01-01-01-01-01-01.wav"))
data, _ = librosa.effects.trim(data)
plt.figure(figsize=(25, 5))
plt.plot(data)