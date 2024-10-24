from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QLayout, QVBoxLayout

from widgets.category import CategoryItem


class CategoriesPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = self.__set_up_layout()
        self.setLayout(self.layout)

    def __set_up_layout(self) -> QLayout:
        item0 = CategoryItem("Seafood", "assets/seafood.png", 356, 149, reverse_title_and_photo=True)
        item1 = CategoryItem("Lunch", "assets/lunch.png", 160, 145)
        item2 = CategoryItem("Breakfast", "assets/breakfast.png", 160, 145)
        item3 = CategoryItem("Dinner", "assets/dinner.png", 160, 145)
        item4 = CategoryItem("Vegan", "assets/vegan.png", 160, 145)
        item5 = CategoryItem("Dessert", "assets/dessert.png", 160, 145)
        item6 = CategoryItem("Drinks", "assets/drinks.png", 160, 145)
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout = QGridLayout()
        layout.setHorizontalSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(item1, 0, 0)
        layout.addWidget(item2, 0, 1)
        layout.addWidget(item3, 1, 0)
        layout.addWidget(item4, 1, 1)
        layout.addWidget(item5, 2, 0)
        layout.addWidget(item6, 2, 1)
        main_layout.addWidget(item0)
        main_layout.addLayout(layout)
        return main_layout
