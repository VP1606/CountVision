import sys
from PyQt5 import QtWidgets, uic
from pynput.keyboard import Controller
import UI_Adapter
import JSON_Contractor
from datetime import datetime
import csv
import os.path
from os import path

class RunUI(QtWidgets.QMainWindow):

    runMode = "NORMAL"
    running = False
    count = 0

    startTime = ""
    endTime = ""

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

                now = datetime.now()
                self.startTime = now.strftime("%d/%m/%Y %H:%M:%S")
                print("Start Date: " + self.startTime)

                self.startBtn.setText("STOP")
                UI_Adapter.RUN(self.count, self)

            elif self.startBtn.text() == "STOP":
                self.running = False
                print("STOP PRESS")

                self.startBtn.setText("START")
                Controller().press('q')

                now = datetime.now()
                self.endTime = now.strftime("%d/%m/%Y %H:%M:%S")
                print("End Date: " + self.endTime)

        else:
            print("TRAIN NOT SET YET...")

    def resetAction(self):
        if self.running is False:
            self.count = 0
            self.countText.setText(str(self.count))
            self.startTime = ""
            self.endTime = ""

    def saveAction(self):
        if self.running == False:
            print("SAVE")

            directory = JSON_Contractor.CSV_Target() + "/CountVision_Records.csv"

            exists = path.exists(directory)

            if exists is True:
                print("Directory Exists!")
            else:
                print("Directory doesn't exist.")

            try:
                with open(directory, 'a', newline='') as file:
                    fields = ["Start Time", "End Time", "Count"]
                    writer = csv.DictWriter(file, fieldnames=fields)

                    if exists is False:
                        writer.writeheader()

                    writer.writerow({
                        'Start Time': self.startTime,
                        "End Time": self.endTime,
                        "Count": self.countText.text()
                    })

            except:
                print("CSV ERROR")

            else:
                print("SUCCESS")

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