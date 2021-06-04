from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QDialog, QGridLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 597)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        # Data Mahasiswa
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 410, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        # NIM
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QtCore.QRect(60, 410, 171, 20))
        self.lineEditNIM = QtWidgets.QLineEdit(Form)
        self.lineEditNIM.setGeometry(QtCore.QRect(130, 410, 401, 20))
        self.lineEditNIM.setObjectName("lineEdit")

        # Nama
        self.lineEditNama = QtWidgets.QLineEdit(Form)
        self.lineEditNama.setGeometry(QtCore.QRect(130, 440, 401, 20))
        self.lineEditNama.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 440, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Jurusan
        self.lineEditJurusan = QtWidgets.QLineEdit(Form)
        self.lineEditJurusan.setGeometry(QtCore.QRect(130, 470, 401, 20))
        self.lineEditJurusan.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 470, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # No.Telp
        self.lineEditNoTelp = QtWidgets.QLineEdit(Form)
        self.lineEditNoTelp.setGeometry(QtCore.QRect(130, 500, 401, 20))
        self.lineEditNoTelp.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 500, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        # PushButton TAMBAH
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 530, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addButtonClick)

        # PushButton EDIT
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 530, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.editButtonClick)

        # PushButton CLEAR
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 530, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        # PushButton HAPUS
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 530, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.deleteButtonClick)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(60, 80, 471, 311))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3.clicked.connect(self.listWidget.clear)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Data Mahasiswa"))
        self.label_2.setText(_translate("Form", "NIM"))
        self.label_3.setText(_translate("Form", "Nama"))
        self.label_4.setText(_translate("Form", "Jurusan"))
        self.label_5.setText(_translate("Form", "No.Telp"))
        self.pushButton.setText(_translate("Form", "TAMBAH"))
        self.pushButton_2.setText(_translate("Form", "EDIT"))
        self.pushButton_3.setText(_translate("Form", "CLEAR"))
        self.pushButton_4.setText(_translate("Form", "HAPUS"))

    def addButtonClick(self):
        self.listWidget.addItem(
            self.lineEditNIM.text() + ' - ' +#untuk line edit bagian nim
            self.lineEditNama.text() + ' - ' +#untuk line edit bagian nama
            self.lineEditJurusan.text() + ' - ' +#untuk line edit bagian jurusan
            self.lineEditNoTelp.text())#untuk line edit bagian notelp

    def editButtonClick(self):
        if self.listWidget.currentRow() < 0: return
        self.entryForm = EntryForm()
        s = str(self.listWidget.currentItem().text())
        idx = s.index('-')
        self.entryForm.nim.setText(s[:(idx - 1)])
        self.entryForm.nama.setText(s[(idx - 2):])
        self.entryForm.jurusan.setText(s[(idx - 3):])
        self.entryForm.telp.setText(s[(idx - 4):])

        if self.entryForm.exec_() == QDialog.Accepted:
            self.listWidget.currentItem().setText(
                self.entryForm.nim.text() + ' - ' +
                self.entryForm.nama.text() + ' - ' +
                self.entryForm.jurusan.text() + ' - ' +
                self.entryForm.telp.text())

    def deleteButtonClick(self):
        row = self.listWidget.currentRow()
        if row >= 0:
            self.listWidget.takeItem(row)
            
class EntryForm(QDialog):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 100)
      self.move(320, 280)
      self.setWindowTitle('Tambah/Ubah Kontak')
      
      self.okButton = QPushButton('OK')
      self.cancelButton = QPushButton('Batal')
      
      hbox = QHBoxLayout()
      hbox.addWidget(self.okButton)
      hbox.addWidget(self.cancelButton)
      
      self.label1 = QLabel("Nim :")
      self.nim = QLineEdit()
      self.label2 = QLabel("Nama :")
      self.nama = QLineEdit()
      self.label3 = QLabel("Jurusan :")
      self.jurusan = QLineEdit()
      self.label4 = QLabel("No.Telp :")
      self.telp = QLineEdit()

      
      layout = QGridLayout()
      layout.addWidget(self.label1, 0, 0)
      layout.addWidget(self.nim, 0, 1)
      layout.addWidget(self.label2, 1, 0)
      layout.addWidget(self.nama, 1, 1)
      layout.addWidget(self.label3, 2, 0)
      layout.addWidget(self.jurusan, 2, 1)
      layout.addWidget(self.label4, 4, 0)
      layout.addWidget(self.telp, 4, 1)
      layout.addLayout(hbox, 5, 1)      
      self.setLayout(layout)
      
      self.okButton.clicked.connect(self.accept)
      self.cancelButton.clicked.connect(self.reject)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
