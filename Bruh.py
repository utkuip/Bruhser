from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

urlList = ["https://www.google.com"]


class MainWindow(QMainWindow):
    controller = len(urlList)
    x = 1
    y = 1

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.browser.urlChanged.connect(self.updateUrlbar)
        self.browser.loadFinished.connect(self.updateTitle)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtab = QToolBar("Navigation")
        navtab.setIconSize(QSize(25, 25))
        self.addToolBar(navtab)

        backButton = QAction(QIcon(os.path.join('icons', 'rounded__left_arrow-512.png')), "Back", self)
        backButton.setStatusTip("Back to previous page")
        backButton.triggered.connect(self.back)
        navtab.addAction(backButton)

        forwardButton = QAction(QIcon(os.path.join('icons', 'Media-Controls-Fast-Forward-icon.png')), "Forward", self)
        forwardButton.setStatusTip("Forward to next page")
        forwardButton.triggered.connect(self.forward)
        navtab.addAction(forwardButton)

        reloadButton = QAction(QIcon(os.path.join('icons', 'refresh-512.png')), "Reload", self)
        reloadButton.setStatusTip("Reload page")
        reloadButton.triggered.connect(self.refresh)
        navtab.addAction(reloadButton)

        homeButton = QAction(QIcon(os.path.join('icons', 'home-512.png')), "Home", self)
        homeButton.setStatusTip("Go home")
        homeButton.triggered.connect(self.homeAdress)
        navtab.addAction(homeButton)

        navtab.addSeparator()

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.enteringUrl)
        navtab.addWidget(self.urlbar)

        self.show()

        self.setWindowIcon(QIcon(os.path.join('icons', '782.jpg')))

    def updateTitle(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Bruhser" % title)

    def homeAdress(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def enteringUrl(self):
        url = self.urlbar.text()
        self.browser.setUrl(QUrl(url))
        urlList.append(url)
        print(urlList)

    def updateUrlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def refresh(self):
        url = QUrl(self.browser.url())
        self.browser.setUrl(url)

    def back(self):
        if (len(urlList) - 1 - self.x) < -1:
            pass
        else:
            self.browser.setUrl(QUrl(urlList[self.controller - 1 - self.x]))
            self.x += 1
            self.y -= 1

    def forward(self):
        if (len(urlList) - 1 + self.y) >= len(urlList):
            pass
        else:
            self.browser.setUrl(QUrl(urlList[self.controller - 1 + self.y]))
            self.y += 1
            self.x -= 1



app = QApplication(sys.argv)
app.setApplicationName("Bruhser")
window = MainWindow()

app.exec_()
