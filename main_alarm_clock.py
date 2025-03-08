from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber, QLabel, QSpinBox, QPushButton, QComboBox ,QSlider
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
from PyQt5.QtCore import QTimer
from datetime import datetime
from dialog_alarm_clock import Ui_Dialog
import pygame 
import os

class UI(QMainWindow):
    def __init__(self):  # Corrected: changed 'init' to '__init__'
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("main_alarm_clock.ui", self)

        # Define our widgets
        self.lcd = self.findChild(QLCDNumber, "lcdNumber")
        self.label_main = self.findChild(QLabel, "label_main")

        self.slider_volume = self.findChild(QSlider, "Slider_volume")
        self.label_volume = self.findChild(QLabel, "label_volume")
        self.comboBox_list = self.findChild(QComboBox, "comboBox_list_music")  # Ensure this matches your UI

        # Set Slider Properties 
        self.slider_volume.setMinimum(0)
        self.slider_volume.setMaximum(100)
        self.slider_volume.setValue(60)  # Default volume at 60%
        self.slider_volume.setTickPosition(QSlider.TicksBelow)
        self.slider_volume.setTickInterval(5)
        self.slider_volume.setSingleStep(5) 

        # Move The Slider
        self.slider_volume.valueChanged.connect(self.slide_it)

        # Find buttons
        self.button_play = self.findChild(QPushButton, "Button_play_music")
        self.button_stop = self.findChild(QPushButton, "Button_stop_music")
        
        # Connect button clicks to methods
        self.button_play.clicked.connect(self.clicker_play)
        self.button_stop.clicked.connect(self.clicker_stop)
        
        # Replace QLineEdit with QSpinBox for alarm time inputs
        self.alarmHourInput = self.findChild(QSpinBox, "alarmHourInput")
        self.alarmMinuteInput = self.findChild(QSpinBox, "alarmMinuteInput")
        self.alarmSecondInput = self.findChild(QSpinBox, "alarmSecondInput")
        self.spinBox_4 = self.findChild(QSpinBox, "spinBox_4")


        
        # Set appropriate ranges for the spin boxes
        self.alarmHourInput.setRange(1, 12)  # Allow hours from 1 to 12
        self.alarmMinuteInput.setRange(0, 59)  # Allow minutes from 0 to 59
        self.alarmSecondInput.setRange(0, 59)  # Allow seconds from 0 to 59
        
        self.setAlarmButton = self.findChild(QPushButton, "setAlarmButton")

        # Add ComboBox for AM/PM selection
        self.amPmComboBox = self.findChild(QComboBox, "amPmComboBox")
        self.amPmComboBox.addItems(["AM", "PM"])

        # Initialize alarm time variable
        self.alarm_time = None

        # Create a Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)

        # Start the timer and update every second
        self.timer.start(1000)

        # Connect the button to set the alarm
        self.setAlarmButton.clicked.connect(self.set_alarm)

        # for Music
        self.button_play.clicked.connect(self.clicker_play)
        self.button_stop.clicked.connect(self.clicker_stop)

        # Call the lcd function initially
        self.lcd_number()

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Populate the music list from a specified directory
        self.populate_music_list("/home/mahdi/all_pro/alarm_clock/music/")
        

        # Show the App
        self.show()

    # ------------------------------------------------------------------------------  
    def slide_it(self, value):
        """Update volume based on slider position."""
        self.label_volume.setText(f"{value}%")
        pygame.mixer.music.set_volume(value / 100.0)  # Set the volume in pygame

    def populate_music_list(self, directory):
        """Populate the combo box with music files from the specified directory."""
        
        for file in os.listdir(directory):
            if file.endswith(".mp3") or file.endswith(".wav"):  # Add more formats if needed
                self.comboBox_list.addItem(file)  # Add music files to the combo box


    def clicker_play(self):
        """Play the selected music."""
        selected_music = self.comboBox_list.currentText()  # Get selected music file name
        if selected_music:
            self.music_path = os.path.join("/home/mahdi/all_pro/alarm_clock/music/", selected_music)  # Full path to the music file
                                            #/home/mahdi/all_pro/alarm_clock/
                                            #/home/mahdi/project/musix/
            # Load and play music
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(self.slider_volume.value() / 100.0)  # Set volume when playing

    def clicker_stop(self):
        """Stop the currently playing music."""
        pygame.mixer.music.stop()  # Stop the music playback
       

    # Def for Dialog
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window, self)
        self.window.exec_()  # Use exec_() to open as a modal dialog

    def lcd_number(self):
        # Get the current time
        time = datetime.now()
        formatted_time = time.strftime("%I:%M:%S %p")

        # Set number of LCD Digits
        self.lcd.setDigitCount(12)
        # Make Text Flat (no white outline)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        # Display The Time
        self.lcd.display(formatted_time)

        # Check if the current time matches the alarm time
        if self.alarm_time and datetime.now().strftime("%H:%M:%S") == self.alarm_time:
            print("Warning: Alarm! Time's up!")
            self.label_main.setText("Alarm! Time's up!")
            self.openWindow()
            self.alarm_time = None  # Reset alarm after it goes off
        #else:
            #self.label_main.setText("Timer")


    def set_alarm(self):
        
        try:
            hour = self.alarmHourInput.value()  # Get value from QSpinBox
            minute = self.alarmMinuteInput.value()  # Get value from QSpinBox
            second = self.alarmSecondInput.value()  # Get value from QSpinBox
            am_pm = self.amPmComboBox.currentText()  # Get AM/PM selection
            # self.alarmSecondInput.setValue(30)

            # Convert hour based on AM/PM selection
            if am_pm == "PM" and hour != 12:
                hour += 12  # Convert PM hour to 24-hour format
            elif am_pm == "AM" and hour == 12:
                hour = 0  # Convert 12 AM to 0 hours

            # Validate inputs (the ranges are already set in QSpinBox)
            if 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60:
                # Format alarm time as HH:MM:SS
                self.alarm_time = f"{hour:02}:{minute:02}:{second:02}"
                self.alarm_show = f"{hour:02}:{minute:02}:{second:02} {am_pm}"
                self.label_main.setText(f"Alarm set for {self.alarm_show}")
            else:
                self.label_main.setText("Invalid time entered!")
        except ValueError:
            self.label_main.setText("Please enter valid numbers!")
         
         
        
            
# Initialize the App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
