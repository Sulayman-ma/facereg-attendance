import os
from setuptools import setup
from PyQt5 import uic
from PyQt5.QtWidgets import *
from facereg.tools import *



class UI(QMainWindow):
    def __init__(self, att):
        super(UI, self).__init__()
        # attendance management instance
        self.att = att

        # load UI file
        uic.loadUi("guiProg.ui", self)

        # record arrival time; wraps att method
        def record():
            name = self.record_field.text()
            capture_dir = r'.\facereg\faces\captures'
            try:
                att.record_attendance(os.path.abspath(os.path.join(capture_dir, f'{name}.jpg')))
                self.record_field.set_text = ''
            except:
                showdialog('Student not found')

        # add new student name; wraps att method
        def new_student():
            name = self.insert_field.text()
            att.add_student(name)

        # define widgets
        self.label = self.findChild(QLabel, "label")
        
        # self.new_date = self.findChild(QPushButton, "newDateButton")
        self.record_time = self.findChild(QPushButton, "recordTimeButton")
        self.add_student = self.findChild(QPushButton, "addStudentButton")
        self.retrain = self.findChild(QPushButton, "retrainButton")

        self.record_field = self.findChild(QLineEdit, "recordField")
        self.insert_field = self.findChild(QLineEdit, "insertField")

        # self.new_date.clicked.connect(self.att.new_date)
        self.record_time.clicked.connect(record)
        self.add_student.clicked.connect(new_student)
        self.retrain.clicked.connect(self.att.retrain)

        self.show()
