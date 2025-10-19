# Code Setup Instructions

## NOTE: The code utilizes an AppleScript interface library and will therefore be ineffective when running on a non-Mac OS. For Windows, NirCmd could replace AppleScript.

Create a folder in a known location on your system.

For me, this folder was called "Final Project". Its path was: /Users/spencerhart/Desktop/Digital Signal Processing/Final Project
You can choose your own folder name. This folder will hold both your design code and a subfolder containing Python libraries and other necessary files to run Mediapipe and OpenCV.

From VS Code (or your preferred coding environment), open this folder.

While inside this folder, open a terminal window in the coding environment. Next, you will create the subfolder within a virtual environment. To do this, enter the following into the terminal:

> python3 -m venv myenv

Here, I named my subfolder "myenv". Once again, you can choose your own subfolder name.

Next:

> source myenv/mybin/activate

> pip3 install mediapipe

Once mediapipe is installed, you can double-check the install and the version:

> pip list

Now, add HART_DSP_FINAL_PROJECT.py to the same project folder. Alternatively, create a new Python file in the same project folder, then paste in the code from HART_DSP_FINAL_PROJECT.py. This is the file you will run to activate the hand recognition, tracking, and volume control.

Next, add hand_landmarker.task to the virtual environment subfolder (once again, mine was called "myenv". Once this file has been added, try running the Python file in the main folder. You should see a live-feed video window appear. If you bring a hand into the frame, it should recognize the hand and overlay a skeleton-like structure with points at fingertips, knuckles, and the palm—these are known as hand landmarks. As you change the distance between your index fingertip and thumbtip, your computer volume should change.

Now try testing it in real-time as a song/audio is playing from your computer!
