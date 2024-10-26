import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea

from pages.categories import CategoriesPage
from widgets.bottom_navigation import BottomNavigationBar
from widgets.top_navigation import TopNavigationBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 - Birinchi qadamlar")
        self.setFixedSize(430, 932)
        self.setGeometry(100, 100, 430, 932)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__set_up_layout()
        self.setStyleSheet("background-color: #1C0F0D;")

    def __set_up_layout(self) -> None:
        top_navigation_bar = TopNavigationBar()
        page = CategoriesPage()
        bottom_navigation_bar = BottomNavigationBar()
        bottom_navigation_bar.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(top_navigation_bar)
        self.main_layout.addWidget(page)
        self.main_layout.addWidget(bottom_navigation_bar, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.main_layout)


app = QApplication(sys.argv)
app.setStyleSheet("* {padding: 0px; margin: 0px;}")
window = MainWindow()
window.show()

sys.exit(app.exec())
