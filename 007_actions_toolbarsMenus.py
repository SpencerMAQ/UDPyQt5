from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle('007 Actions Toolbars')

        label = QLabel("dasdasd")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('Main Toolbar')
        # if you'd want to resize Icon sizes
        # toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # button_action = QAction(QIcon("bug.png")"Your button", self)   # if image
        self.button_action = QAction("Your button", self)
        self.button_action.setStatusTip("Your button hovered")   # text displayed on status bar
        self.button_action.triggered.connect(self.onMyToolBarButtonClick)
        # this will make the button be able to be toggled
        self.button_action.setCheckable(True)
        toolbar.addAction(self.button_action)

        toolbar.addSeparator()

        self.button_action2 = QAction('button 2', self)
        self.button_action2.setStatusTip('button 2 hovered')
        self.button_action2.triggered.connect(self.onMyToolBarButtonClick)
        self.button_action2.setCheckable(True)
        self.button_action2.setShortcut('Ctrl+P')
        toolbar.addAction(self.button_action2)

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())


        self.setStatusBar(QStatusBar(self))     # place where the status bar will go = self

        self.init_menubar()

        self.show()

    def init_menubar(self):
        menu = self.menuBar()   # call menuBar on QMainWindow
        #menu.setNativeMenuBar(False )

        file_menu = menu.addMenu("&File")
        file_menu.addAction(self.button_action)

        file_menu.addSeparator()

        file_submenu = file_menu.addMenu('Submenu')

        file_submenu.addAction(self.button_action2)

    # as explained in previous vid, the second arg is the return(toggle status) sent
    # by the event if the action is activated
    def onMyToolBarButtonClick(self, s):
        print('clicked', s)
        # check QAction documentation, signal Qaction has for signals: changed, hovered
        # toggled and triggered
        # if the button is uncheckable, 's' will always be false by default

app = QApplication([])
window = MainWindow()
sys.exit(app.exec_())

