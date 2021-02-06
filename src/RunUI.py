import sys
from PyQt5 import QtWidgets, uic
from pynput.keyboard import Controller
import UI_Adapter
import JSON_Contractor

class RunUI(QtWidgets.QMainWindow):

    runMode = "NORMAL"
    running = False
    count = 0

    version = JSON_Contractor.VersionDetail()

    def normalSelect(self):
        if self.running is False and self.runMode != "NORMAL":
            self.runMode = "NORMAL"
            self.runModeDisplay.setText("NORMAL")

    def trainSelect(self):
        if self.running is False and self.runMode != "TRAIN":
            self.runMode = "TRAIN"
            self.runModeDisplay.setText("TRAIN")

    def startSys(self):

        if self.runModeDisplay.text() == "NORMAL":
            if self.startBtn.text() == "START":
                self.running = True
                print("START PRESS")

                self.startBtn.setText("STOP")
                UI_Adapter.RUN(self.count, self)

            elif self.startBtn.text() == "STOP":
                self.running = False
                print("STOP PRESS")

                self.startBtn.setText("START")
                Controller().press('q')

        else:
            print("TRAIN NOT SET YET...")

    def resetAction(self):
        if self.running is False:
            self.count = 0
            self.countText.setText(str(self.count))
        JSON_Contractor.VersionDetail()

    def saveAction(self):
        if self.running == False:
            print("SAVE")


    def __init__(self):
        super(RunUI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('runUI.ui', self) # Load the .ui file

        self.countText.setText(str(self.count))
        self.runModeDisplay.setText("NORMAL")
        self.versionString.setText(str(self.version))

        self.resetBtn.clicked.connect(self.resetAction)
        self.startBtn.clicked.connect(self.startSys)
        self.saveBtn.clicked.connect(self.saveAction)


        self.normalBtn.clicked.connect(self.normalSelect)
        self.trainBtn.clicked.connect(self.trainSelect)

        self.show() # Show the GUI



app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = RunUI() # Create an instance of our class
app.exec_() # Start the application