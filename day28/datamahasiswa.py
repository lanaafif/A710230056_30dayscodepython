import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox

class MahasiswaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Mahasiswa')

        layout = QVBoxLayout()

        # Form input data mahasiswa
        formLayout = QHBoxLayout()
        
        self.nimInput = QLineEdit(self)
        self.nimInput.setPlaceholderText('NIM')
        formLayout.addWidget(QLabel('NIM:'))
        formLayout.addWidget(self.nimInput)
        
        self.namaInput = QLineEdit(self)
        self.namaInput.setPlaceholderText('Nama')
        formLayout.addWidget(QLabel('Nama:'))
        formLayout.addWidget(self.namaInput)

        self.jurusanInput = QLineEdit(self)
        self.jurusanInput.setPlaceholderText('Jurusan')
        formLayout.addWidget(QLabel('Jurusan:'))
        formLayout.addWidget(self.jurusanInput)

        layout.addLayout(formLayout)

        # Tombol tambah mahasiswa
        self.addButton = QPushButton('Tambah Mahasiswa', self)
        self.addButton.clicked.connect(self.addMahasiswa)
        layout.addWidget(self.addButton)

        # Tabel data mahasiswa
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['NIM', 'Nama', 'Jurusan'])
        layout.addWidget(self.table)

        # Tombol hapus mahasiswa
        self.deleteButton = QPushButton('Hapus Mahasiswa', self)
        self.deleteButton.clicked.connect(self.deleteMahasiswa)
        layout.addWidget(self.deleteButton)

        self.setLayout(layout)

    def addMahasiswa(self):
        nim = self.nimInput.text()
        nama = self.namaInput.text()
        jurusan = self.jurusanInput.text()

        if not nim or not nama or not jurusan:
            QMessageBox.warning(self, 'Error', 'Semua field harus diisi')
            return

        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition, 0, QTableWidgetItem(nim))
        self.table.setItem(rowPosition, 1, QTableWidgetItem(nama))
        self.table.setItem(rowPosition, 2, QTableWidgetItem(jurusan))

        self.nimInput.clear()
        self.namaInput.clear()
        self.jurusanInput.clear()

    def deleteMahasiswa(self):
        selectedRow = self.table.currentRow()
        if selectedRow >= 0:
            self.table.removeRow(selectedRow)
        else:
            QMessageBox.warning(self, 'Error', 'Pilih baris yang ingin dihapus')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MahasiswaApp()
    ex.show()
    sys.exit(app.exec_())
