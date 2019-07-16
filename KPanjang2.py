import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class KPanjang2(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(300,150)
		self.move(300,300)
		self.setWindowTitle('Konversi Panjang')

		self.label1=QLabel()
		self.label1.setText('Masukkan Meter')
		self.linepertama=QLineEdit()
		horizontalLine=QFrame();
		horizontalLine.setFrameShape(QFrame.HLine)
		horizontalLine.setFrameShadow(QFrame.Sunken)


		self.KM=QRadioButton()
		self.KM.setText('KM')
		self.HM=QRadioButton()
		self.HM.setText('HM')
		self.DAM=QRadioButton()
		self.DAM.setText('DAM')
		self.DM=QRadioButton()
		self.DM.setText('DM')
		self.M=QRadioButton()
		self.M.setText('M')
		self.CM=QRadioButton()
		self.CM.setText('CM')
		self.MM=QRadioButton()
		self.MM.setText('MM')


		self.myfont=QFont()
		self.myfont.setBold(True)
		self.hasil=QLabel()
		self.hasil.setFont(self.myfont)
		self.hasil.setText('Hasil')
		self.hitung=QPushButton()
		self.hitung.setText('Hitung')

		layout = QGridLayout()
		layout.addWidget(self.label1,0,0)
		layout.addWidget(self.linepertama,0,1,1,7)
		layout.addWidget(self.KM,2,0)
		layout.addWidget(self.HM,2,1)
		layout.addWidget(self.DAM,2,2)
		layout.addWidget(self.DM,2,4)
		layout.addWidget(self.CM,2,5)
		layout.addWidget(self.MM,2,6)
		layout.addWidget(self.M,2,3)

		layout.addWidget(horizontalLine,4,0,1,7)
		layout.addWidget(self.hasil,5,0,1,7)
		layout.addWidget(self.hitung,6,0,1,7)

		self.hitung.clicked.connect(self.hitungan)
		self.setLayout(layout)

	def hitungan(self):
		a = float(self.linepertama.text())

		if self.KM.isChecked():
			hitt=a/1000
			self.hasil.setText('Hasil Konversi ke Kilometer : '+str(hitt))
		elif self.HM.isChecked():
			hitt=a/100
			self.hasil.setText('Hasil Konversi ke Hektometer : '+str(hitt))
		elif self.DAM.isChecked():
			hitt=a/10
			self.hasil.setText('Hasil Konversi ke Dekameter : '+str(hitt))
		elif self.DM.isChecked():
			hitt=a*10
			self.hasil.setText('Hasil Konversi ke Desimeter : '+str(hitt))
		elif self.CM.isChecked():
			hitt=a*100
			self.hasil.setText('Hasil Konversi ke Centimeter : '+str(hitt))
		elif self.MM.isChecked():
			hitt=a*1000
			self.hasil.setText('Hasil Konversi ke Milimeter : '+str(hitt))
		elif self.M.isChecked():
			hitt=a
			self.hasil.setText('Hasil Konversi ke Meter : '+str(hitt))
		else:
			self.hasil.setText('Belum memilih operasi Panjang')

if __name__ == '__main__':
	a = QApplication(sys.argv)
	form = KPanjang2()
	form.show()
	a.exec_()
