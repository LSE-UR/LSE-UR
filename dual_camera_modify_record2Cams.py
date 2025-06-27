"""
Recording videos from a webcam in specific folders

Source
Course: Hand Sign Detection for vowels of the American Sign Language
Based on: Computer Vision Zone
Website: https://www.computervision.zone/courses/hand-sign-detection-asl/


@utor: maalvear
May, 07 2024 13:21h CET

This code make video recorder from 1 camera,
shows the number of frames in the corner.
Create two folders per classes and saved the corresponding video of the class.
Only saves the video without the text show in the recording process.
"""


# Import libraries
import cv2
import os
import time

# Source path
cameras_folders = ['CAMERA__1', 'CAMERA__2']
# cameras_folders = ['CAMERA_1']

person_id = "001"


# Classes
actions = ['BUENOS DIAS'] #, 'E', 'I', 'O', 'U'


# Capture the image from camera 0
vid_capture = cv2.VideoCapture(0)
vid_capture1 = cv2.VideoCapture(1)

# In case there is no camera
if (vid_capture.isOpened() == False):
  print("Unable to read camera feed")


# Parameters
frame_per_sec = 30
# Setting sizes and 3 and 4 are Id's
width = int(vid_capture.get(3))
height = int(vid_capture.get(4))
size = (width, height)

# Parameters to record video
# Number of videos worth of data
no_sequences = 6
# Videos are going to be 30 frames in length
sequence_length = 30


def record_video(classes, cam_folders):
    """
    Function to record a sequence of videos in a corresponding folder
    which each folder is created based on the class name

    :param classes: list of the classes name
    :param cam_folders: list of the camera names
    :return: two folders named CAMERA__1 and CAMERA__2 with 2 videos
             per class recorder in real-time
    """
    list_paths = []

    pTime = 0
    for folder in cam_folders:
        # source_path = os.path.join('.\PRUEBA/')
        source_path = os.path.join("." + "\\" + folder + "/")
        # Adding strings of the source paths
        list_paths.append(source_path)
        # Create folder per action
        for action in actions:
            try:
                os.makedirs(os.path.join(source_path, action))
            except:
                pass

    for object1 in classes:
        # Loop through sequences aka videos
        for sequence in range(no_sequences):

            # Get the dominant hand for video recording
            if(sequence<int(no_sequences/2)):
                hand="right"
            else:
                hand="left"

            # Loop through video length aka sequence length
            new = os.path.join(list_paths[0] + object1 + '/')
            new1 = os.path.join(list_paths[1] + object1 + '/')



            output = cv2.VideoWriter(new + "video_" + person_id + "_" + str(sequence) + '_' + "camera1_" + str(
                object1) + "_"+ hand +"Hand.mp4", cv2.VideoWriter_fourcc(*'mp4v'), frame_per_sec, (width, height))
            output1 = cv2.VideoWriter(new1 + "video_" + person_id + "_" + str(sequence) + '_' + "camera2_" + str(
                object1) +"_"+ hand +"Hand.mp4", cv2.VideoWriter_fourcc(*'mp4v'), frame_per_sec, (width, height))






            # Codec definition

            # Just to record 7 seconds of video
            for frame_num in range(sequence_length*7):

                # Chronometer
                sec = int(frame_num/sequence_length)

                # Capture each frame of webcam 1
                ret, frame = vid_capture.read()
                # Capture each frame of webcam 2
                ret1, frame1 = vid_capture1.read()
                output.write(frame)
                output1.write(frame1)

                # NEW Apply wait logic
                if frame_num == 0:
                    # Cam 1
                    cv2.putText(frame,  'STARTING COLLECTION 0', (120, 200),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.putText(frame, 'CAM_1 Class {} Number {}'.format(object1, sequence),
                                (20, 35),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)  # .format(list_paths[0], object1, sequence),
                    cv2.putText(frame, 'Hand {}'.format(hand),(20, 70),cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0, 255), 3,cv2.LINE_AA)  # .format(list_paths[0], object1, sequence),
                    # Cam 2
                    cv2.putText(frame1, 'STARTING COLLECTION 1', (120, 200),
                                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                    cv2.putText(frame1, 'CAM_2 Class {} Number {}'.format(object1, sequence),
                                 (20, 35),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
                    cv2.putText(frame1, 'Hand {}'.format(hand), (20, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0, 255), 3, cv2.LINE_AA)  # .format(list_paths[0], object1, sequence),
                    # Adding frame rate
                    cTime = time.time()
                    fps = 1 / (cTime - pTime)
                    pTime = cTime

                    # Visualize fps in cam 1
                    cv2.putText(frame, f'FPS:{int(fps)}', (473, 35), cv2.FONT_HERSHEY_PLAIN,
                                3, (0, 0, 255), 3)
                    # Visualize fps in cam 2
                    cv2.putText(frame1, f'FPS:{int(fps)}', (473, 35), cv2.FONT_HERSHEY_PLAIN,
                                 3, (0, 0, 255), 3)


                    # Show to screen
                    cv2.imshow('OpenCV Feed 1', frame)
                    cv2.imshow('OpenCV Feed 2', frame1)
                    cv2.waitKey(100)

                else:
                    cv2.waitKey(3)
                    # Cam 1
                    cv2.putText(frame, 'RECORDING', (120, 200),
                          cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                    cv2.putText(frame, 'CAM_1 Class {} Number {}'.format(object1, sequence),
                                (20, 35),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)  # .format(list_paths[0], object1, sequence),
                    cv2.putText(frame, 'Hand {}'.format(hand), (20, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0, 255), 3, cv2.LINE_AA)  # .format(list_paths[0], object1, sequence),
                    # Cam 2
                    cv2.putText(frame1, 'RECORDING', (120, 200),
                          cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                    cv2.putText(frame1, 'CAM_2 Class {} Number {}'.format(object1, sequence),
                                (20, 35),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
                    cv2.putText(frame1, 'Hand {}'.format(hand), (20, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0, 255), 3, cv2.LINE_AA)  # .format(list_paths[0], object1, sequence),

                    # Adding frame rate
                    cTime = time.time()
                    fps = 1 / (cTime - pTime)
                    pTime = cTime

                    # Visualize fps in cam 1
                    cv2.putText(frame, f'FPS:{int(fps)}', (473, 35), cv2.FONT_HERSHEY_PLAIN,
                                3, (0, 0, 255), 3)
                    #Visualize fps in cam 2
                    cv2.putText(frame1, f'FPS:{int(fps)}', (473, 35), cv2.FONT_HERSHEY_PLAIN,
                                 3, (0, 0, 255), 3)


                    # Chronometer cam 1
                    cv2.putText(frame, 'sec {} '.format(sec),
                                (width-110, height-20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3,
                                cv2.LINE_AA)

                    # Chronometer cam 2
                    cv2.putText(frame1, 'sec {} '.format(sec),
                                (width-110, height-20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3,
                                cv2.LINE_AA)


                    # Show to screen
                    cv2.imshow('OpenCV Feed 1', frame)
                    cv2.imshow('OpenCV Feed 2', frame1)

            # Close and break the loop after pressing "x" key
            if cv2.waitKey(1) & 0XFF == ord('x'):
                break

    # close the already opened cameras
    vid_capture.release()
    vid_capture1.release()
    # close the already opened files
    output.release()
    output1.release()
    # close the window and de-allocate any associated memory usage
    cv2.destroyAllWindows()


record_video(actions, cameras_folders)
