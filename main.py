import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QDialog, QStyle

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.licznik)
        self.show()

    i = 0
    def licznik(self):

        i = self.i
        kalorie = self.ui.kalorie.text()
        kaloriefinal = int(kalorie)
        nazwa = self.ui.nazwa.text()
        wynik = self.ui.wynik
        kobieta = self.ui.kobieta
        menszczyzna = self.ui.meszczyzna
        malo = self.ui.mala
        srednie = self.ui.srednia
        duzo = self.ui.duza
        lista = self.ui.lista
        len = str(lista.__len__())
        leni = int(len)
        item = "kalorie: "+ kalorie + " zjadłeś :" + nazwa
        lista.addItem(item)
        wynik.setText(kalorie)
        
















if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
