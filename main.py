import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import pickle


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 App")
        self.setWindowIcon(QIcon("icon.png"))
        self.setStyleSheet(open("assets/styles.css").read())  # Load CSS styles from the file

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add your widgets here
        self.label = QLabel("Label")
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()
        self.edit6 = QLineEdit()
        self.edit7 = QLineEdit()
        self.edit8 = QLineEdit()
        self.edit1.setPlaceholderText("Enter Pregnancies")
        self.edit2.setPlaceholderText("Enter Glucose")
        self.edit3.setPlaceholderText("Enter BloodPressure")
        self.edit4.setPlaceholderText("Enter SkinThickness")
        self.edit5.setPlaceholderText("Enter Insulin")
        self.edit6.setPlaceholderText("Enter BMI")
        self.edit7.setPlaceholderText("Enter DiabetesPedigreeFunction (between 0 and 1)")
        self.edit8.setPlaceholderText("Enter Age")

        self.button = QPushButton("Get Started")
        self.button.setText("Get Started")
        self.button.clicked.connect(self.on_button_clicked)  # Connect the clicked signal to a slot
        layout.addWidget(self.label)
        layout.addWidget(self.edit1)
        layout.addWidget(self.edit2)
        layout.addWidget(self.edit3)
        layout.addWidget(self.edit4)
        layout.addWidget(self.edit5)
        layout.addWidget(self.edit6)
        layout.addWidget(self.edit7)
        layout.addWidget(self.edit8)
        layout.addWidget(self.button)

    def on_button_clicked(self):
        pregnancies = self.edit1.text()
        glucose = self.edit2.text()
        blood_pressure = self.edit3.text()
        skin_thickness = self.edit4.text()
        insulin = self.edit5.text()
        bmi = self.edit6.text()
        diabetes_pedigree = self.edit7.text()
        age = self.edit8.text()
        #outcome = btnOnclick(pregnancies, glucose, blood_pressure, skin_thickness, insulin, diabetes_pedigree, bmi, age)
       # QMessageBox.information(self, "Prediction Result", "The predicted outcome is: " + str(outcome))
        loadModel(r"/model/model.pkl")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

def loadModel(fileName):
    try:
        with open(fileName, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print("Model file not found.")
    except Exception as e:
        print("Error while loading the model.",str(e))
