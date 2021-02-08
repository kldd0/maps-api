import sys

import requests

from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow

MAP_API_SERVER = 'http://static-maps.yandex.ru/1.x/'


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.map_params = {'ll': '37.617635,55.755814',
                           'l': 'map',
                           'z': 14,
                           'size': '600,400'
                           }
        self.pixmap = QPixmap()
        self.load_map()

    def load_map(self):
        response = requests.get(MAP_API_SERVER, params=self.map_params)
        self.pixmap.loadFromData(QByteArray(response.content))
        self.label.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.map_params['z'] < 17:
                self.map_params['z'] += 1
                self.load_map()
        if event.key() == Qt.Key_PageDown:
            if self.map_params['z'] > 2:
                self.map_params['z'] -= 1
                self.load_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
