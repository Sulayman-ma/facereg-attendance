""""CUSTOM FUNCTIONS AND OBJECTS TO REUSE AND WRAP AROUND WHAT DOES NOT GIVE ME THE RESULTS I WANT: INCLUDES FOR OPENPYXL AND PYQT5."""

from PyQt5.QtWidgets import QMessageBox
import cv2 as cv


"""OpenCV Object Instances for recognition"""
# Face coordinates classifier
HAAR_CASCADE = cv.CascadeClassifier(r'.\facereg\haar_face.xml')
# Face recognizer object instance, reads trained face coordinates
FACE_RECOG = cv.face.LBPHFaceRecognizer.create()
FACE_RECOG.read(r'.\facereg\face_trained.yml')

def get_max_row(sheet):
        """Get maximum row in Excel sheet counting created but empty cells.""" 
        max_row = 0
        for row in sheet.iter_rows():
            if any([cell.value is not None for cell in row]):
                max_row += 1
        return max_row

def get_max_col(sheet):
    """"Get maximum column in Excel sheet counting created but empty cells."""
    max_col = 0
    for col in sheet.iter_cols():
        if any([cell.value is not None for cell in col]):
            max_col += 1
    return max_col

def showdialog(message: str):
    """Shows a dialog with the message passed as the parameter."""
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(f"{message}")
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()