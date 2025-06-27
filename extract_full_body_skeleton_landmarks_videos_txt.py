"""
Extract landmarks from MediaPipe Holistic model
and export a txt file per video

Total landmarks 553
Pose 33, Face 478, Hands 21 per each.
and visibility value (in case)
Thur 20/06/25 13:45 CET
@uthor: maalvear
"""
import cv2
import mediapipe as mp
import os

# Initialize MediaPipe Holistic
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(static_image_mode=False, model_complexity=2, refine_face_landmarks=True)

# Input/output folders
input_folder = "./path/to/videos"
output_folder = "./path/to/save/landmarks"
os.makedirs(output_folder, exist_ok=True)

def extract_body_id(filename):
    """Extract body ID from characters 2 to 6 from the end of filename (excluding extension)."""
    name_no_ext = os.path.splitext(filename)[0]
    parts = name_no_ext.split("_")
    if len(parts) >= 2:
        return parts[-2]  # e.g., '001'
    return "unknown"

def write_landmarks(f, landmarks, model, frame_idx, body_id, use_visibility=True):
    if landmarks:
        for idx, lm in enumerate(landmarks.landmark):
            visibility = lm.visibility if use_visibility and hasattr(lm, 'visibility') else 1.0
            f.write(f"{body_id},{frame_idx},{model},{idx},{lm.x:.6f},{lm.y:.6f},{lm.z:.6f},{visibility:.4f}\n")

def process_video(video_path, output_path, body_id):
    cap = cv2.VideoCapture(video_path)
    frame_idx = 0

    with open(output_path, "w") as f:
        # Write header
        f.write("BodyID,Frame,Model,LandmarkIndex,X,Y,Z,Visibility\n")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(rgb)

            # Pose
            write_landmarks(f, results.pose_landmarks, "pose", frame_idx, body_id, use_visibility=True)
            # Face
            # write_landmarks(f, results.face_landmarks, "face", frame_idx, body_id, use_visibility=False)
            # Left Hand
            write_landmarks(f, results.left_hand_landmarks, "lh", frame_idx, body_id, use_visibility=False)
            # Right Hand
            write_landmarks(f, results.right_hand_landmarks, "rh", frame_idx, body_id, use_visibility=False)

            frame_idx += 1

    cap.release()

# Process all videos
list_name= ["J", "GRACIAS"]

for name in list_name:
    for filename in os.listdir(input_folder):
        if ("_RGB_"+name+"_" in filename) and (filename.lower().endswith((".mp4", ".avi", ".mov", ".mkv"))):
            video_path = os.path.join(input_folder, filename)
            body_id = extract_body_id(filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
            print(f"📹 Processing {filename} (Body ID: {body_id})...")
            process_video(video_path, output_path, body_id)

# Close Holistic model
holistic.close()

print("FINISHED!! All videos processed with Holistic model and saved to:", output_folder)
