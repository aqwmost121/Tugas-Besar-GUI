import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Konversi(QWidget):
    def __init__ (self):
        QWidget.__init__(self)
        self.setWindowTitle("Konversi Suhu")
        self.resize(450, 300)
        self.posisi = self.frameGeometry()
        self.tengah = QDesktopWidget().availableGeometry().center()
        self.posisi.moveCenter(self.tengah)


        self.label1()
        self.label2()
        self.label3()
        self.label4()
        self.push1()
        self.push2()


        self.kolom1()
        self.kolom2()
        self.kolom3()
        self.kolom4()

    def label1(self):
        cf = QLabel("Celcius",self)
        cf.move(90, 40)

    def label2(self):
        cf = QLabel("Celcius ke Fahrenheit",self)
        cf.move(90, 90)

    def label3(self):
        cr = QLabel("Celcius ke Reamur",self)
        cr.move(90, 140)
    def label4(self):
        cr = QLabel("Celcius ke Kelvin",self)
        cr.move(90, 190)

    def push1(self):
        hapus = QPushButton('Hapus',self)
        hapus.clicked.connect(self.clear)
        hapus.move(260, 250)

    def push2(self):
        proses = QPushButton('Process',self)
        proses.clicked.connect(self.proses)
        proses.move(120, 250)

    def kolom1(self):
        self.line1 = QLineEdit(self)
        self.line1.move(240, 40)

    def kolom2(self):
        self.line2 = QLineEdit(self)
        self.line2.setReadOnly(True)
        self.line2.move(240, 90)

    def kolom3(self):
        self.line3 = QLineEdit(self)
        self.line3.setReadOnly(True)
        self.line3.move(240, 140)
    def kolom4(self):
        self.line4 = QLineEdit(self)
        self.line4.setReadOnly(True)
        self.line4.move(240, 190)

    def proses(self):
        if self.kolom1 == 2:
            QMessageBox.information(self,'Alert', 'Kolom Tidak Boleh Kosong')
        else:
            Fah = float(self.line1.text())*(9./5)+32
            Ream = float(self.line1.text())*(4./5)
            kel = float(self.line1.text())+273

            self.line2.setText(str(Fah))
            self.line3.setText(str(Ream))
            self.line4.setText(str(kel))

    def clear(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")


if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Konversi()
    ex.show()
    sys.exit(app.exec_())
