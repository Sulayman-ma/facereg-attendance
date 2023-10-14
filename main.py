from PyQt5.QtWidgets import QApplication
import sys
import os
from facereg.attendance import Attendance
from facereg.ui import UI



# List of students
dir = r'.\facereg\faces\train'
students: list = []
for person in os.listdir(os.path.abspath(dir)):
    students.append(person)

# test_dir = r'.\facereg\faces\captures'
att = Attendance(students)
att.new_date()

# Main QT application instance
app = QApplication(sys.argv)
ui = UI(att)

sys.exit(app.exec_())