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

        layout = QGridLayout()

        # since layout is a grid, second argument is position of the
        # widget to be added in coordinates
        layout.addWidget( Color('red'), 0,0 )
        layout.addWidget( Color('green'), 1,0 )
        layout.addWidget( Color('blue'), 1,1 )


        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

sys.exit(app.exec_())