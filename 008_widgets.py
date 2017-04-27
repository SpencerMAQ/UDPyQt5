from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('008_widgets')

        widget = QLabel('Hello')
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #widgetCbox = QCheckBox()
        #widgetCbox.setChecked(True)
        #Partially checked = neither yes or no
        #widgetCbox.setCheckState(Qt.PartiallyChecked)
        #widgetCbox.stateChanged.connect(self.show_state)

        comboBox = QComboBox()
        comboBox.addItems(['One', 'Two', 'Three'])
        comboBox.currentIndexChanged.connect(self.index_changed)
        #sends index to the function
        comboBox.currentIndexChanged[str].connect(self.text_changed)
        #sends text to the function

        #QListWidget = similar to combobox except not a drop-down, everything is listed

        #QLineEdit
        #textChanged - programmatic change
        #textEdited - user Edit

    #def show_state(self, s):
        #print(s)
        #checked = 2, uncheked = 0, partial = 1


        '''
        layout = QVBoxLayout()

        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLabel,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QRadioButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit]

        for w in widgets:
            layout.addWidget(w() )

        widget = QWidget()
        widget.setLayout(layout)
        '''

        self.setCentralWidget(comboBox)

        #self.show()

app = QApplication([])

window = MainWindow()
window.show()

sys.exit(app.exec_())