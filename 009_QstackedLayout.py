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

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        #tabs.setTabPosition(QTabWidget.East)
        tabs.setMovable(True)

        #pagelayout = QVBoxLayout()
        #button_layout = QHBoxLayout()
        #layout = QStackedLayout()

        #pagelayout.addLayout(button_layout)
        #pagelayout.addLayout(layout)

        # note: I think the for loop would still work even if placed before
        #pagelayout.addLayout(button_layout)
        for n, color in enumerate(['red','green','blue','yellow']):
            tabs.addTab( Color(color), color )
            #btn = QPushButton(str(color))
            #btn.pressed.connect(lambda n=n: layout.setCurrentIndex(n))
            #button_layout.addWidget(btn)
            #layout.addWidget( Color(color) )

        #widget = QWidget()
        #widget.setLayout(pagelayout)
        self.setCentralWidget(tabs)


app = QApplication([])

window = MainWindow()
window.show()

sys.exit(app.exec_())