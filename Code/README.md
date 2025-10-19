# Code Setup Instructions

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

Now, create a new Python file in the same project folder. This is where you will put the main code. I called this file "HART_DSP_FINAL_PROJECT" (.py as the file extension).

In this file, paste in the code.

OR, FOR WINDOWS OS: 
> python -m venv myenv
> myenv\Scripts\activate
> pip install mediapipe
