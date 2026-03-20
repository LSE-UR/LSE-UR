# LSE-UR Dataset


This repository contains the necessary code to obtain the data presented in the paper "LSE-UR dataset, the dataset for the Spanish Sign Language"

## Download

The full dataset can be downloaded at this website xx. The corresponding compressed folders (.zip). This link does NOT include other data than that in the reference paper.


## Overview

The LSE-UR is an online, public, and available dataset for the Spanish Sign Language (LSE, acronym in Spanish). It has a variety of modalities and, as far as we know, is an order of magnitude larger than any other LSE dataset in terms of the number of videos and recording duration. It is remarkable the fact that it is built in different scenarios, it has multiple perspectives of the same action from a multi-camera system, which allows us to have diversity in the quality of the videos, which enables multimodal learning.

The LSE-UR dataset provides a considerable variety of data modalities compared to existing datasets. Four types of simultaneous data are supplied: RGB frames, Depth maps, IR frames, and Skeleton data.

These data allow the research community to make consistent comparisons among processing approaches or machine learning approaches by using one or more data modalities. Researchers in computer vision and machine learning can use/reuse the data for different investigations in different application domains, such as sign language translation, sign language recognition, human action recognition, etc. 

![lse](https://github.com/LSE-UR/LSE-UR/blob/main/samples_dataset_blurred.png)


## Dataset details

The dataset includes 35 signs performed by 43 subjects for 30 signs, corresponding to the LSE alphabet composed of fingerspelled  letters, and five selected signs were based on daily life social activities, which are Buenos días, Buenas tardes, Buenas noches, Gracias, and Aplausos. For translation in English, these actions are Good morning, Good afternoon, Good night, Thank you, and Clapping.


## Acquisition setup

The acquisition experiment took place in two scenarios where an acquisition area at the University of La Rioja was reserved for the experimental setup. We present the _Library scenario_ and the _White scenario_. In the _Library scenario_, an Orbbec Femto Mega camera is placed in front of the operator and the table where two cameras are placed on both sides: Microsoft LifeCam HD-3000 USB and Logitech Brio Webcam 4k UltraHD. In the _White scenario_, an  Intel RealSense Depth Camera D457 camera is placed in front of the operator and the table, where two cameras are placed on both sides: Microsoft LifeCam HD-3000 USB and Logitech Brio Webcam 4k UltraHD. The frontal camera is placed on a tripod at a distance of 1 meter. The next figure shows the sketch of the acquisition setup. (a) On the top, _Library scenario_, on the right, the devices and their corresponding distances are detailed. (b) On the bottom, the _White scenario_, on the right, the devices and their corresponding distances are detailed.


<img width="960" height="540" alt="scenarios_dataset" src="https://github.com/user-attachments/assets/72ccc024-d67b-416e-9ac8-d4b481fa7bbb" />


## Repository Structure

The repository contains all scripts used in the creation and processing of the dataset. They are commented on in order of their use in the paper. First, those used during data acquisition, https://github.com/LSE-UR/LSE-UR/blob/main/dual_camera_modify_record2Cams.py and https://github.com/LSE-UR/LSE-UR/blob/main/realsense_and_dual_camera_modify_final.py. As detailed in Section 4.3 "Collected Data" of the paper, these two scripts manage the video recording process.

Following video acquisition, a preprocessing step is required to ensure proper visualisation. Video preprocessing is performed using the Fiji tool and involves executing the script located at https://github.com/LSE-UR/LSE-UR/blob/main/Macro_CambioContraste_GenerarVideo.ijm. As outlined in Section 4.3 "Collected Data" of the paper, this script normalises video contrast to facilitate viewing. Subsequently, the script https://github.com/LSE-UR/LSE-UR/blob/main/cambiar_nombre.py renames the videos in accordance with the established annotation scheme, also detailed in Section 4.3 "Collected Data".

With all videos prepared, the script https://github.com/LSE-UR/LSE-UR/blob/main/extract_full_body_skeleton_landmarks_videos_txt.py can then be executed. This script will store the full-body skeletons of subjects present in the videos within the designated output directory.

For the scripts to run correctly, it's advisable to follow the same dataset structure.

An Argilla instance was deployed on HuggingFace to validate the recorded signs. This platform facilitated the annotation of videos containing potentially ambiguous signs. The setup of this environment is managed by the https://github.com/LSE-UR/LSE-UR/blob/main/argilabueno.py script. Through a collaborative effort with the _Asociación de Personas Sordas de La Rioja (ASR)_, we successfully confirmed the accuracy of the questionable signs.


## Dataset Structure
```
BBDD_PATH
├── Macro_CambioContraste_GenerarVideo.ijm
├── argilabueno.py
├── cambiar_nombre.py
├── dual_camera_modify_record2Cams.py
├── extract_full_body_skeleton_landmarks_videos_txt.py
├── realsense_and_dual_camera_modify_final.py
├── VIDEOS
│   ├── *.avi
│   ├── *.mkv
│   └── *.mp4
└── skeleton
    └── *.txt
```

## Acknowledgements

The authors would like to thank XXXX.

## Cite this dataset

Please cite this paper if you want to use this dataset in your research (papers, book chapters, conference proceedings, software, etc)
xxx


