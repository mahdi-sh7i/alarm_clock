# alarm_clock
# Alarm Clock Application

This repository contains two Python scripts that implement an alarm clock application using PyQt5 for the user interface and Pygame for audio playback.

## Code Overview

### 1. main_alarm_clock.py
    

**Functionality:**
- This script sets up the main window of the alarm clock application.
- It allows users to set an alarm time.
- When the alarm time is reached, it opens a dialog window to notify the user.

**Key Components:**
- **PyQt5**: Used for creating the GUI.
- **QTimer**: Used to check the current time and compare it with the set alarm time.
- **Pygame**: Used to play an alarm sound when the alarm goes off.

**How It Works:**
1. The user inputs the desired alarm time.
2. A timer checks every minute whether the current time matches the set alarm time.
3. If it matches, a dialog window is opened, and an alarm sound is played.

### 2. dialog_alarm_clock.py
        

**Functionality:**
- This script defines the dialog that appears when the alarm goes off.
- It displays a message to the user and provides a button to acknowledge the alarm.

**Key Components:**
- **Dialog**: A simple UI that shows the alarm message and an "OK" button.
- **Music Control**: Stops the alarm sound when the user acknowledges it by clicking the button.

**How It Works:**
1. When the dialog is opened, it displays a message indicating that the alarm has gone off.
2. The user can click the "OK" button to stop the alarm sound and close the dialog.

## Requirements

To run this application, you need:
- Python 3.x
- PyQt5
- Pygame

You can install the required packages using pip:

pip install PyQt5 pygame


## Usage

1. Run main_alarm_clock.py to start the main application.
2. Set your desired alarm time and wait for the notification.
3. When the alarm goes off, acknowledge it in the dialog by clicking "OK".


