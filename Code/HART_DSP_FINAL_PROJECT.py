# Spencer Hart
# spencer.hart@uvm.edu
# EE 3530 - Digital Signal Processing
# Final Project



# Importing necessary libraries
import cv2 # OpenCV (image recognition / ML library)

# MediaPipe (hand recognition/tracking library)
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Utilize delays
import time

# Utilize squareroot function
import math

# AppleScript interface library (to control Apple device values (ex. screen brightness, volume, etc.))
from subprocess import call



# MediaPipe Hand Landmarker requires a trained model (model that has been 'trained' on many pictures of hands) in order to be able to recognize new hands
model_path = '/Users/spencerhart/Desktop/Digital Signal Processing/Final Project/myenv/hand_landmarker.task'

# Creating "objects" to be used for hand recognition from MediaPipe
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands



# Turn on camera
cap = cv2.VideoCapture(0)

# Set values for minimum confidence value and minimum tracking value to determine if hands were detected and tracked (with landmarks) successfully
# Also set max number of hands to only 1 hand (for this application)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1) as hands:
  while cap.isOpened():
    success, image = cap.read() # Checking to see if camera is working
    if not success: 
      print("Ignoring empty camera frame.") # Print if camera is not working, otherwise move on
      continue

    

# Draw the hand annotations on the image.
    # Mark the image as writeable to --> can add annotations onto image
    image.flags.writeable = True
    
    # Convert the BGR image to RGB before processing. (NOTE: It seems like the Apple MacBook camera does this automatically? Therefore not needed...)
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    results = hands.process(image)

    # If there are multiple hands
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
      handlandmarks = results.multi_hand_landmarks[0]
      thumb = handlandmarks.landmark[4] # Thumbtip location (x, y, z)
      index = handlandmarks.landmark[8] # Indextip location (x, y, z)
      middle = handlandmarks.landmark[10] # Middle 2nd knuckle location (x, y, z)
      wrist = handlandmarks.landmark[0] # Wrist location (x, y, z)
      
      
      dist = math.sqrt((thumb.x - index.x)**2 + (thumb.y - index.y)**2) # Calculate distance between index and thumb
      print("index-thumb distance: ", dist)
      
      base = math.sqrt((middle.x - wrist.x)**2 + (middle.y - wrist.y)**2) # Calculate distance between middle 2nd knuckle and wrist
      print("middle 2nd knuckle-wrist distance: ", base)

      ratio = dist/base # This is to ensure that we volume control is accurate from any distance away
      print("ratio: ", ratio)

      vol = ratio * 100 # Convert to AppleSciprt percentage value for volume
      print("vol: ", vol)
      
      call(["osascript", "-e", f"set volume output volume {vol}"]) # Implement volume change


    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1)) #cv2.flip(image, 0) will flip the image upside-down
    if cv2.waitKey(5) & 0xFF == 27: # wait 5 milliseconds, check for escape key press (if key = 27 (ESC in ASCII)), kill livestream if pressed, kill video window if pressed again
      break


cap.release()
