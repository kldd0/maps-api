import sys

import requests

from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow

MAP_API_SERVER = 'http://static-maps.yandex.ru/1.x/'
GEOCODE_API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spn = 0.01
        self.ll = [37.617635, 55.755814]
        self.map_view.addItems(['схема', 'спутник', 'гибрид'])
        self.map_params = {'ll': f'{self.ll[0]},{self.ll[1]}',
                           'l': 'map',
                           'size': '600,400',
                           'spn': f'{self.spn},{self.spn}'
                           }
        self.pixmap = QPixmap()
        self.load_map()
        self.map_view.activated[str].connect(self.change_map_view)
        self.search.clicked.connect(self.find_object)
        self.reset_btn.clicked.connect(self.reset_search_query)

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

    def change_map_view(self, text):
        if text == 'схема':
            self.map_params['l'] = 'map'
        elif text == 'спутник':
            self.map_params['l'] = 'sat'
        else:
            self.map_params['l'] = 'sat,skl'
        self.load_map()

    def find_object(self):
        value = self.text_query.text()
        geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={GEOCODE_API_KEY}&geocode={value}&format=json'
        resp = requests.get(geocoder_request)
        if not resp:
            print("Ошибка выполнения запроса:")
            print(geocoder_request)
            print("Http статус:", resp.status_code, "(", resp.reason, ")")
        else:
            json_resp = resp.json()
            obj = json_resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
            obj_coords = obj["Point"]["pos"].split()
            self.map_params['ll'] = ','.join(obj_coords)
            self.map_params['pt'] = ','.join([obj_coords[0], obj_coords[1], 'pm2rdm'])
            self.load_map()

    def reset_search_query(self):
        self.map_params['ll'] = '37.620070,55.753630'
        self.map_params.pop('pt', None)
        self.load_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
