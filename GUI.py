import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QIcon
import pickle


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 App")
        self.setWindowIcon(QIcon("icon.png"))
        self.setStyleSheet(open("E:\programming\python\pythonProject6\styles.css").read())  # Load CSS styles from the file

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add your widgets here
        self.label = QLabel("Label")
        self.label.setStyleSheet("color: black;")  # Set label text color to black
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
        self.button.setStyleSheet("	background-color: rgb(35, 40, 49);")
        self.button.clicked.connect(self.on_button_clicked)  # Connect the clicked signal to a slot
        layout.addWidget(self.edit1)
        layout.addWidget(self.edit2)
        layout.addWidget(self.edit3)
        layout.addWidget(self.edit4)
        layout.addWidget(self.edit5)
        layout.addWidget(self.edit6)
        layout.addWidget(self.edit7)
        layout.addWidget(self.edit8)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

    def on_button_clicked(self):
        pregnancies = int(self.edit1.text())
        glucose = int(self.edit2.text())
        blood_pressure = int(self.edit3.text())
        skin_thickness = int(self.edit4.text())
        insulin = int(self.edit5.text())
        bmi = float(self.edit6.text())
        diabetes_pedigree = float(self.edit7.text())
        age = int(self.edit8.text())

        model = loadModel(r"E:\programming\python\pythonProject6\model.pkl")
        input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, diabetes_pedigree, bmi, age]]
        prediction = model.predict(input_data)

        if prediction == [1]:
            prediction_result = "Diabetic"
        else:
            prediction_result = "Non-Diabetic"

        self.label.setText("Prediction Result: " + prediction_result)

def loadModel(fileName):
    try:
        with open(fileName, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print("Model file not found.")
    except Exception as e:
        print("Error while loading the model.", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
