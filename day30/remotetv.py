import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt

class RemoteTV(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Remote TV")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.channelLabel = QLabel("Channel: 1")
        layout.addWidget(self.channelLabel)

        self.volumeLabel = QLabel("Volume: 50")
        layout.addWidget(self.volumeLabel)

        self.channelSlider = QSlider(Qt.Horizontal)
        self.channelSlider.setMinimum(1)
        self.channelSlider.setMaximum(100)
        self.channelSlider.valueChanged.connect(self.channelChanged)
        layout.addWidget(self.channelSlider)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.valueChanged.connect(self.volumeChanged)
        layout.addWidget(self.volumeSlider)

        self.channelButton = QPushButton("Channel Up")
        self.channelButton.clicked.connect(self.channelUp)
        layout.addWidget(self.channelButton)

        self.volumeButton = QPushButton("Volume Up")
        self.volumeButton.clicked.connect(self.volumeUp)
        layout.addWidget(self.volumeButton)

        self.setLayout(layout)

    def channelChanged(self):
        currentChannel = self.channelSlider.value()
        self.channelLabel.setText(f"Channel: {currentChannel}")

    def volumeChanged(self):
        currentVolume = self.volumeSlider.value()
        self.volumeLabel.setText(f"Volume: {currentVolume}")

    def channelUp(self):
        currentChannel = int(self.channelLabel.text().split(":")[1])
        if currentChannel < 100:
            self.channelLabel.setText(f"Channel: {currentChannel + 1}")
        else:
            self.channelLabel.setText("Channel: 1")

    def volumeUp(self):
        currentVolume = int(self.volumeLabel.text().split(":")[1])
        if currentVolume < 100:
            self.volumeLabel.setText(f"Volume: {currentVolume + 1}")
        else:
            self.volumeLabel.setText("Volume: 50")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    remoteTV = RemoteTV()
    remoteTV.show()
    sys.exit(app.exec_())