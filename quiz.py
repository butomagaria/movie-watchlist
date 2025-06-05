import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QRadioButton
from quiz_design import Ui_mainWindow

class MyApp(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.data = {
            'საქართველო': 'თბილისი', 'საფრანგეთი': 'პარიზი', 'გერმანია': 'ბერლინი',
            'იტალია': 'რომი', 'ესპანეთი': 'მადრიდი', 'საბერძნეთი': 'ათენი',
            'პორტუგალია': 'ლისაბონი', 'ბრიტანეთი': 'ლონდონი'
        }

        self.radiobuttons = [self.radioButton, self.radioButton_2, self.radioButton_3, self.radioButton_4,
                        self.radioButton_5, self.radioButton_6, self.radioButton_7, self.radioButton_8]

        self.radio_group = QButtonGroup()

        for each in self.radiobuttons:
            self.radio_group.addButton(each)

        keys = list(self.data.keys())

        self.label.setText('აირჩიე ქვეყანა ჩამონათვალიდან და შეუსაბამე დედაქალაქი')
        self.label_2.setText('⭐⭐⭐')
        self.pushButton.setText('შემოწმება')
        self.pushButton_2.setText('ახლიდან')
        self.pushButton.setStyleSheet('background-color: white;')
        self.pushButton_2.setStyleSheet('background-color: white;')
        self.setStyleSheet('background-color: lavender; '
                           'border: 3px solid plum; '
                           'border-radius: 10px;')

        for each in self.data:
            self.comboBox.addItem(each)
        for i in range(0, 8):
            self.radiobuttons[i].setText(self.data[keys[i]])

        self.stars = 3

        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton_2.clicked.connect(self.try_again)


    def button_clicked(self):
        if self.radio_group.checkedButton() == None:
            self.label_2.setText('⭐⭐⭐')
        elif self.data[self.comboBox.currentText()] == self.radio_group.checkedButton().text():
            self.label_2.setText('⭐' * self.stars)
        else:
            self.stars -= 1
            self.label_2.setText('⭐' * self.stars)
        if self.stars == 0:
            self.fail()

    def try_again(self):
        temporary = QRadioButton()
        self.radio_group.addButton(temporary)
        temporary.setChecked(True)
        self.stars = 3
        self.label_2.setText('⭐' * self.stars)
        for button in self.radio_group.buttons():
            button.setCheckable(True)

    def fail(self):
        temporary = QRadioButton()
        self.radio_group.addButton(temporary)
        temporary.setChecked(True)
        self.label_2.setText('უპს, ახლიდან სცადე :(')
        for button in self.radio_group.buttons():
            button.setCheckable(False)



app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())