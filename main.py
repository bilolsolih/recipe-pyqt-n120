import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget

from pages.categories import CategoriesPage
from widgets.bottom_navigation import BottomNavigationBar
from widgets.top_navigation import TopNavigationBar
from utils.db import set_up_database


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recipes")
        self.setFixedSize(430, 800)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__set_up_layout()
        self.setStyleSheet("background-color: #1C0F0D;")

    def __set_up_layout(self) -> None:
        top_navigation_bar = TopNavigationBar()
        stacked_widgets = QStackedWidget()

        page = CategoriesPage()
        stacked_widgets.addWidget(page)

        bottom_navigation_bar = BottomNavigationBar()
        bottom_navigation_bar.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(top_navigation_bar, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(stacked_widgets, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(bottom_navigation_bar, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.main_layout)


set_up_database()
app = QApplication(sys.argv)
app.setStyleSheet("* {padding: 0px; margin: 0px;}")
window = MainWindow()
window.show()

sys.exit(app.exec())
