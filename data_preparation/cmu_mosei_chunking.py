import os
import librosa
import pandas as pd
import matplotlib.pyplot as plt

CMU_MOSEI_PATH = "./data/CMU-MOSEI-RAW"

df = pd.concat(
    [
        pd.read_csv(os.path.join(CMU_MOSEI_PATH, "Data_Test_original.csv")),
        pd.read_csv(os.path.join(CMU_MOSEI_PATH, "Data_Train_modified.csv")),
        pd.read_csv(os.path.join(CMU_MOSEI_PATH, "Data_Val_modified.csv")),
    ],
    axis=0,
)

print(df.columns)

# data, sampling_rate = librosa.load(
#     os.path.join("", "Actor_01/03-01-01-01-01-01-01.wav")
# )
# data, _ = librosa.effects.trim(data)
# plt.figure(figsize=(25, 5))
# plt.plot(data)
