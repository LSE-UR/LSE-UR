# LSE-UR Dataset

This repository contains the code necessary to 


This repository contains the code necessary to obtain the data presented in the paper "LSE-UR dataset, the dataset for the Spanish sign language"


## Repository Structure

The repository contains all scripts used in the creation and processing of the dataset. They are commented in order of their use in the paper. First, those used during data acquisition, https://github.com/LSE-UR/LSE-UR/blob/main/dual_camera_modify_record2Cams.py and https://github.com/LSE-UR/LSE-UR/blob/main/realsense_and_dual_camera_modify_final.py. As detailed in Section 4.3 "Collected Data" of the paper, these two scripts manage the video recording process.

Following video acquisition, a preprocessing step is required to ensure proper visualization. Video preprocessing is performed using the Fiji tool and involves executing the script located at https://github.com/LSE-UR/LSE-UR/blob/main/Macro_CambioContraste_GenerarVideo.ijm. As outlined in Section 4.3 "Collected Data" of the paper, this script normalizes video contrast to facilitate viewing. Subsequently, the script https://github.com/LSE-UR/LSE-UR/blob/main/cambiar_nombre.py renames the videos in accordance with the established annotation scheme, also detailed in Section 4.3 "Collected Data".

With all videos prepared, the script https://github.com/LSE-UR/LSE-UR/blob/main/extract_full_body_skeleton_landmarks_videos_txt.py can then be executed. This script will store the full-body skeletons of subjects present in the videos within the designated output directory.

For the scripts to run correctly, it's advisable to follow the same dataset structure.

An Argilla instance was deployed on HuggingFace to validate the recorded signs. This platform facilitated the annotation of videos containing potentially ambiguous signs. The setup of this environment is managed by the https://github.com/LSE-UR/LSE-UR/blob/main/argilabueno.py script. Through a collaborative effort with the Asociación de personas sordas de La Rioja, we successfully confirmed the accuracy of the questionable signs.


## Dataset Structure
BBDD_PATH
├── videos
│   ├── train_labels.csv
│   ├── val_labels.csv
│   └── test_labels.csv
├── VIDEOS
│   ├── *.avi
│   ├── *.mp4
│   └── *.mp4
└── skeleton
    └── *.txt
