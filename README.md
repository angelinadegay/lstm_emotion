# Audio Emotion Analysis

## Datasets

### RAVDESS
The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) has recorded snippets
from 24 actors (12 M, 12 F) reading one of two statements in various different tones.

Filenames are structured as follows as per their docs. Each token below is hyphen-separated.
* Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
* Vocal channel (01 = speech, 02 = song).
* Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
* Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.
* Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").
* Repetition (01 = 1st repetition, 02 = 2nd repetition).
* Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).

Download URL: https://zenodo.org/record/1188976
The samples were extracted to `data/RAVDESS_Audio_Speech/Actor_*/*.wav`

### CMU-MOSEI
The CMU Multimodal Opinion Sentiment and Emotion Intensity (CMU-MOSEI) is a large dataset including
recorded snippets from various online sites (e.g, YouTube).

The CMU portal is slow, and so data was downloaded instead from kaggle: https://www.kaggle.com/datasets/maunberg/cmu-mosei
The samples were extracted to `data/CMU-MOSEI-RAW/Audio/Audio/WAV_16000/*.wav`