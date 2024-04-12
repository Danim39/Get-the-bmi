import sys
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*
from PyQt6.QtWidgets import QWidget

class Form(QWidget):
    def __init__(self) :
        super().__init__()
        
        self.resize(500 , 500)#set form size
        self.setWindowTitle("Bmi checker")#set title

        main_layout=QGridLayout()
        box_layout=QGridLayout()
        button_layout=QGridLayout()

        main_layout.addLayout(box_layout,0,0,1,1)
        main_layout.addLayout(button_layout,0,1,1,1)

        self.Height=QLabel("Height : ")
        box_layout.addWidget(self.Height,0,0,1,1)

        self.weight=QLabel("Weight : ")
        box_layout.addWidget(self.weight,1,0,1,1)

        self.txtheight=QLineEdit()
        box_layout.addWidget(self.txtheight,0,1,1,1)

        self.txtweight=QLineEdit()
        box_layout.addWidget(self.txtweight,1,1,1,1)

        self.button=QPushButton("Enter")
        
        
        button_layout.addWidget(self.button,0,0,1,1)
        self.button.clicked.connect(self.calculate_bmi) # connect Function to button


        self.setLayout(main_layout)
    
    def calculate_bmi(self):
        height_cm = int(self.txtheight.text())
        weight = int(self.txtweight.text())
        
        # Convert height from cm to meters
        height_m = height_cm / 100
        
        height_squared = height_m ** 2  # Squaring the height in meters
        bmi = weight / height_squared

        #set bmi zon

        if bmi <18.5: #set bmi zon
            message = QMessageBox()
            message.setText(f"Your BMI is {bmi:3.1f}\
                             You are underweight👽")
            message.exec()
        elif 18.5<=bmi<=24.7:
            message=QMessageBox()
            message.setText(f"Yor bmi its {bmi:3.1f} \
                            You are normal👽")
            message.exec()
        elif 25<=bmi<=29.9:
            message=QMessageBox()
            message.setText(f"Your bmi its {bmi:3.1f} \
                            You are overweight👽")
            message.exec()
        
        elif 30<=bmi<=39.9:
            message=QMessageBox()
            message.setText(f"Your bmi its {bmi:3.1f}\
                             You are fat👽")
            message.exec()

#run app
app=QApplication(sys.argv)

form=Form()#object from form
form.show()

sys.exit(app.exec())