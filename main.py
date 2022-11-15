import sys
import os


from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QFileDialog
)

from PyQt6.QtCore import (
    Qt
)

from window import Ui_MainWindow

from jsonHandling import (
    createModDotjson, createEventDotjson
)
from soundFileHandling import (
    handleAudioFileMP3, handleAudioFileWAV
)


def loadFile(fileName):
    listOfEvents = []
    with open(fileName, 'r') as infile:
        for line in infile:
            listOfEvents.append(line.rstrip(line[-1]))
    return listOfEvents


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.addSoundButton.clicked.connect(self.AddSoundButtonCallback)
        self.browseModPathButton.clicked.connect(self.AddModPathButtonCallback)
        self.browseFilePathButton.clicked.connect(self.AddFilePathButtonCallback)
        self.findEventButton.clicked.connect(self.AddFindEventButtonCallback)
        self.audioEventComboBox.addItems(loadFile("resources\\audioEventNames.txt"))
        self.SelectRandom.setChecked(True)

    def AddSoundButtonCallback(self): #THIS STARTS EVERYTHING
        self.successReportLabel.setText("")
        modFolderPath = self.modFolderPath.text()
        filePath = self.soundFilePath.text()

        if not modFolderPath or len(modFolderPath.strip()) == 0:
            self.modPathWarningLabel.setText("Please select a valid path.")
            return

        if not filePath or len(filePath.strip()) == 0:
            self.soundPathWarningLabel.setText("Please select a valid path.")
            return

        generalAudioFolderPath = modFolderPath+"/audio"
        audioEventFolderPath = generalAudioFolderPath+"/"+self.audioEventComboBox.currentText()

        modName = modFolderPath.split('/')[-1]
        soundFileName = filePath.split('/')[-1]
        #soundFileType = filePath.split('.')[-1]

        if not os.path.exists(os.path.join(os.getcwd(), generalAudioFolderPath)): #create audio folder if nonexistent
            #self.addSoundButton.setText("audiofolder")
            os.mkdir(generalAudioFolderPath)

        if self.jsonCreateCheckBox.isChecked():
            createModDotjson(modName, modFolderPath) #get the mod name from folder path earlier

        if not os.path.exists(os.path.join(os.getcwd(), audioEventFolderPath)): #create audio event folder if nonexistent
            os.mkdir(audioEventFolderPath)

        if soundFileName.endswith(".mp3"): 
            handleAudioFileMP3(filePath, audioEventFolderPath+"/"+soundFileName.removesuffix(".mp3")+".wav")

        elif soundFileName.endswith(".wav"):
            handleAudioFileWAV(filePath, audioEventFolderPath+"/"+soundFileName)

        else:
            self.soundPathWarningLabel.setText("Incorrect file extension.")
            return
        
        if self.SelectSequential.isChecked():
            selectionStrategy = "sequential"
        else:
            selectionStrategy = "random"

        createEventDotjson(str(self.audioEventComboBox.currentText()), generalAudioFolderPath, selectionStrategy)

        self.successReportLabel.setText("Successfully added " + soundFileName)


    def AddModPathButtonCallback(self):
        #fname = QtWidgets.getOpenFileName(self, 'Open file', '/home')
        self.modPathWarningLabel.setText("")
        modPath = QFileDialog.getExistingDirectory(None, 'Select folder:', 'C:\\', QFileDialog.Options.ShowDirsOnly) 
        self.modFolderPath.setText(modPath)

    def AddFilePathButtonCallback(self):
        self.soundPathWarningLabel.setText("")
        filePath = QFileDialog.getOpenFileName(None, 'Select file:', 'C:\\', "Sound files(*.wav *.mp3)") #QFileDialog.setFileMode(1)
        self.soundFilePath.setText(filePath[0])

    def AddFindEventButtonCallback(self):
        self.findWarningLabel.setText("")
        textToSeek = self.findEventTextBox.text()
        textIndex = self.audioEventComboBox.findText(textToSeek, flags=Qt.MatchFlags.MatchContains) 
        if not textIndex == -1:
            self.audioEventComboBox.setCurrentIndex(textIndex)
        else:
            self.findWarningLabel.setText("Event not found!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
