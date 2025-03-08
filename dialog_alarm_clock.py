# sub6.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic  # Ensure you import uic
import sys
import pygame  

class Ui_Dialog(object):
    def setupUi(self, Dialog, main_window):  # Accept main_window as a parameter
        self.dialog = Dialog  # Store a reference to the dialog
        self.main_window = main_window  # Store a reference to the main window

        # Load the ui file
        uic.loadUi("dialog_alarm_clock.ui", self.dialog)  # Pass Dialog to loadUi
        
        # --------------------------------------------
        self.button_ok = self.dialog.findChild(QtWidgets.QPushButton, "btn_ok")
        self.label_dialog = self.dialog.findChild(QtWidgets.QLabel, "label_dialog")
        

        # Connect button clicks to methods
        self.button_ok.clicked.connect(self.clicker_ok)
        pygame.mixer.music.load(self.main_window.music_path)
        pygame.mixer.music.play()

        # --------------------------------------------

        #self.label_dialog.setText("Alarm? Time's up!")
        self.label_dialog.setText(f"Alarm for {self.main_window.alarm_show} !")
        

    def clicker_ok(self):
        self.label_dialog.setText("close")
        
        # Stop the timer
        pygame.mixer.music.stop()
         
        self.dialog.close()  


      

# Initialize The App
if __name__ == "__main__":  # Corrected name check
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
