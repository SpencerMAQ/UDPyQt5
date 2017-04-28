# 3 positional layouts available in Qt

# Linear Position
# - QHBox
# - QVBox

# Grid Position
# - QGridLayout

# Stacked (z) - i.e. in front of one another
# - QStackedLayout

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('008_widgets')

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()

        #layout1.setContentsMargins(0,0,0,0)
        # sets margins at outside edges of the window

        colorWidget = Color('red')
        layout2.addWidget(colorWidget)
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('green'))
        layout1.addWidget(Color('blue'))


        widget = QWidget()
        widget.setLayout(layout1)

        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

sys.exit(app.exec_())