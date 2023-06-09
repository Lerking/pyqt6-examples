'''pyqt6 example'''

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)
import common
class MainWindow(QMainWindow):
    '''MainWindow Class'''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App "+common.VERSION)
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        # Set the central widget of the Window.
        self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        '''Slot/signal'''
        print("Clicked!")
        
    def the_button_was_toggled(self, checked):
        '''Slot/signal'''
        print("Checked?", checked)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
