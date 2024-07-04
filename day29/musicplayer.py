import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Simple Music Player')
        self.setGeometry(300, 300, 300, 150)
        
        self.label = QLabel('No Music Selected', self)
        self.label.setGeometry(50, 30, 200, 30)
        
        self.openButton = QPushButton('Open', self)
        self.openButton.setGeometry(50, 70, 80, 30)
        self.openButton.clicked.connect(self.open_file)
        
        self.playButton = QPushButton('Play', self)
        self.playButton.setGeometry(140, 70, 80, 30)
        self.playButton.clicked.connect(self.play_music)
        
        self.player = QMediaPlayer()
    
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Music File', '', 'Music Files (*.mp3 *.wav)')
        if file_name != '':
            self.label.setText(file_name)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
    
    def play_music(self):
        self.player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())