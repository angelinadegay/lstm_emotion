import pandas as pd
import os
import wave
from tqdm import tqdm

target_emotions = ["neutral", "happy", "sad", "anger", "surprise", "disgust", "fear"]
target_columns = ["source", "path", *target_emotions]

RAVDESS_PATH = "./data/RAVDESS_Audio_Speech"
CMU_MOSEI_PATH = "./data/CMU-MOSEI-RAW"
OUTPUT_DF_PATH = "./data/result.csv"

"""
The output folder will hold the chunked audio data. It will be structured as follows:

.
|-  data.csv    # with columns (source, path, *emotions)
                # Here, source represents the original dataset, path represents the path to wav file
                # And *emotions is a list of the above target emotions.
|-  Audio
    |- *.wav    # corresponding to each of the paths above.
"""
MOSEI_OUTPUT_PATH = "./data/CMU-MOSEI-CHUNKED"

if not os.path.exists(MOSEI_OUTPUT_PATH):
    os.makedirs(MOSEI_OUTPUT_PATH)


"""
Process the CMU-MOSEI Dataset. Data is split into 3 tables: test, train,
validation. First, we combine them all so we can perform our own train-test
split.

Each video is used multiple times with different timestamps. We chunk the
appropriate segments to reduce storage requirements.

We should then normalize each of the target emotions (so that they represent
probabilities)
"""

mosei_df = pd.concat(
    [
        # Here, we ignore the testing since the timestamps are unaligned.
        # There is still sufficient data from the other two files
        # pd.read_csv(os.path.join(CMU_MOSEI_PATH, "Data_Test_original.csv")),
        pd.read_csv(os.path.join(CMU_MOSEI_PATH, "Data_Train_modified.csv")),
        pd.read_csv(os.path.join(CMU_MOSEI_PATH, "Data_Val_modified.csv")),
    ],
    axis=0,
)[
    [
        "video",
        "start_time",
        "end_time",
        "happy",
        "sad",
        "anger",
        "surprise",
        "disgust",
        "fear",
    ]
]

# The "neutral" class does not exist. Here, we engineer it based on whether to
# other emotions are sufficiently expressed or not.
mosei_df["neutral"] = 0
mosei_df["neutral"] = mosei_df[target_emotions].apply(
    lambda r: 1.0 if r.sum() < 1 else 0.0, axis=1
)


mosei_df["path"] = mosei_df[["video", "start_time", "end_time"]].apply(
    lambda row: os.path.join(
        MOSEI_OUTPUT_PATH,
        f"Audio/{row['video']}-{row['start_time']}-{row['end_time']}.wav",
    ),
    axis=1,
)
mosei_df["source"] = "MOSEI"

for i, (path, id, start, end) in tqdm(
    mosei_df[["path", "video", "start_time", "end_time"]].iterrows(),
    total=mosei_df.shape[0],
):
    # Don't recompute when re-running file
    if os.path.exists(path):
        continue

    # file to extract the snippet from
    with wave.open(
        os.path.join(CMU_MOSEI_PATH, "Audio/Audio/WAV_16000", f"{id}.wav"), "rb"
    ) as i, wave.open(path, "w") as o:
        # Read from input file
        nchannels = i.getnchannels()
        framerate = i.getframerate()
        sampwidth = i.getsampwidth()
        i.setpos(int(start * framerate))
        data = i.readframes(int((end - start) * framerate))

        # Write to output file
        o.setnchannels(nchannels)
        o.setframerate(framerate)
        o.setsampwidth(sampwidth)
        o.setnframes(int(len(data) / sampwidth))
        o.writeframes(data)

mosei_df = mosei_df[target_columns]


"""
Process RAVDESS dataset. This data is already prepared and trimmed.
We just need to convert it to a DataFrame of the same shape as the MOSEI data.
"""

ravdess_df = pd.DataFrame([], columns=target_columns)
for dir in os.listdir(RAVDESS_PATH):
    dir_path = os.path.join(RAVDESS_PATH, dir)
    if not os.path.isdir(dir_path):
        continue

    for file in os.listdir(dir_path):
        path = os.path.join(dir_path, file)

        [_, _, emotion, intensity, _, _, _] = os.path.basename(file).split("-")

        emotion, intensity = int(emotion), float(intensity)

        ravdess_df.loc[len(ravdess_df)] = [
            "RAVDESS",
            path,
            intensity if emotion in [1, 2] else 0.0,  # neutral / calm
            intensity if emotion == 3 else 0.0,  # happy
            intensity if emotion == 4 else 0.0,  # sad
            intensity if emotion == 5 else 0.0,  # angry
            intensity if emotion == 8 else 0.0,  # surprise
            intensity if emotion == 7 else 0.0,  # disgust
            intensity if emotion == 6 else 0.0,  # fear
        ]

result_df = pd.concat([mosei_df, ravdess_df], axis=0)

result_df.to_csv(OUTPUT_DF_PATH, index=False)
