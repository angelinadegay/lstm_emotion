# To run this file, you must first clone the CMU Multimodal SDK repository:
# https://github.com/CMU-MultiComp-Lab/CMU-MultimodalSDK.git
#
# Follow instructions there to install dependencies (either into this or a separate virtual environment).
# Then, execute this script to download the CMU-MOSEI dataset

from mmsdk import mmdatasdk

source = {
    "labels": {
        "All Labels": "http://immortal.multicomp.cs.cmu.edu/CMU-MOSEI/labels/CMU_MOSEI_Labels.csd"
    },
    "raw": {
        "words": "http://immortal.multicomp.cs.cmu.edu/CMU-MOSEI/language/CMU_MOSEI_TimestampedWords.csd",
        "phones": "http://immortal.multicomp.cs.cmu.edu/CMU-MOSEI/language/CMU_MOSEI_TimestampedPhones.csd",
    },
    "highlevel": {
        "COVAREP": "http://immortal.multicomp.cs.cmu.edu/CMU-MOSEI/acoustic/CMU_MOSEI_COVAREP.csd"
    },
}

for key in source:
    print(f"Downloading {key}")
    # Download dataset
    mmdatasdk.mmdataset(source[key], f"../data/CMU-MOSEI/{key}/")
