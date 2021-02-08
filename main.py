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
        self.spn = 0.01
        self.ll = [37.617635, 55.755814]
        self.map_params = {'ll': f'{self.ll[0]},{self.ll[1]}',
                           'l': 'map',
                           'size': '600,400',
                           'spn': f'{self.spn},{self.spn}'
                           }
        self.pixmap = QPixmap()
        self.load_map()

    def load_map(self):
        response = requests.get(MAP_API_SERVER, params=self.map_params)
        self.pixmap.loadFromData(QByteArray(response.content))
        self.label.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.spn > 0.0001:
                self.spn *= 0.1
                self.map_params['spn'] = f'{self.spn},{self.spn}'
                self.load_map()
        elif event.key() == Qt.Key_PageDown:
            if self.spn < 1:
                self.spn /= 0.1
                self.map_params['spn'] = f'{self.spn},{self.spn}'
                self.load_map()
        elif event.key() == Qt.Key_Left:
            self.ll[0] -= self.spn
            self.map_params['ll'] = f'{self.ll[0]},{self.ll[1]}'
            self.load_map()
        elif event.key() == Qt.Key_Right:
            self.ll[0] += self.spn
            self.map_params['ll'] = f'{self.ll[0]},{self.ll[1]}'
            self.load_map()
        elif event.key() == Qt.Key_Up:
            self.ll[1] += self.spn
            self.map_params['ll'] = f'{self.ll[0]},{self.ll[1]}'
            self.load_map()
        elif event.key() == Qt.Key_Down:
            self.ll[1] -= self.spn
            self.map_params['ll'] = f'{self.ll[0]},{self.ll[1]}'
            self.load_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
