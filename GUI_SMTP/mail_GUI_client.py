import sys
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

app = QApplication(sys.argv)


class MyGUI:
    def __init__(self) -> None:
        ui_file = QFile("mail_gui_client.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            raise RuntimeError("Could not open mail_gui_client.ui")

        loader = QUiLoader()
        self.window = loader.load(ui_file)  # QMainWindow <- .ui
        ui_file.close()

        if self.window is None:
            raise RuntimeError("Failed to load UI")

        self.window.setWindowTitle("Mail Client")
        self.window.show()

        # Functionality: Buttons
        self.pushButton = self.window.findChild(QPushButton, "pushButton")
        self.pushButton_2 = self.window.findChild(QPushButton, "pushButton_2")
        self.pushButton_3 = self.window.findChild(QPushButton, "pushButton_3")

        if not self.pushButton or not self.pushButton_2 or not self.pushButton_3:
            raise RuntimeError("Could not find button!")

        self.lineEdit = self.window.findChild(QLineEdit, "lineEdit")
        self.lineEdit_2 = self.window.findChild(QLineEdit, "lineEdit_2")
        self.lineEdit_3 = self.window.findChild(QLineEdit, "lineEdit_3")
        self.lineEdit_4 = self.window.findChild(QLineEdit, "lineEdit_4")
        self.lineEdit_5 = self.window.findChild(QLineEdit, "lineEdit_5")
        self.lineEdit_6 = self.window.findChild(QLineEdit, "lineEdit_6")

        if not all(
            [
                self.lineEdit,
                self.lineEdit_2,
                self.lineEdit_3,
                self.lineEdit_4,
                self.lineEdit_5,
                self.lineEdit_6,
            ]
        ):
            raise RuntimeError("Could not find one or more line edits")

        self.textEdit = self.window.findChild(QTextEdit, "textEdit")
        self.label_8 = self.window.findChild(QLabel, "label_8")

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.attach_sth)
        self.pushButton_3.clicked.connect(self.send_mail)

    def login(self):
        try:
            self.server = smtplib.SMTP(
                self.lineEdit_3.text(), int(self.lineEdit_4.text())
            )
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.lineEdit.text(), self.lineEdit_2.text())

            # Disable the 4 top elements and enable the down elements
            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.pushButton.setEnabled(False)

            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.textEdit.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)

            self.msg = MIMEMultipart()
        except smtplib.SMTPAuthenticationError:
            message_box = QMessageBox()
            message_box.setText("Invalid Login Info!")
            message_box.exec()
        except:
            message_box = QMessageBox()
            message_box.setText("Login failed!")
            message_box.exec()

    def attach_sth(self):
        # options = QFileDialog.Options()
        filenames, _ = QFileDialog.getOpenFileNames(
            self.window, "Open File", "", "All files (*.*)"
        )
        if filenames != []:
            for filename in filenames:
                attachment = open(filename, "rb")

                filename = filename[filename.rfind("/") + 1 :]

                payload = MIMEBase("application", "octet-stream")
                payload.set_payload(attachment.read())
                encoders.encode_base64(payload)
                payload.add_header(
                    "Content-Disposition", f"attachment; filename={filename}"
                )
                self.msg.attach(payload)
                if not self.label_8.text().endswith(":"):
                    self.label_8.setText(self.label_8.text() + ",")
                self.label_8.setText(self.label_8.text() + " " + filename)

    def send_mail(self):
        dialog = QMessageBox(self.window)
        dialog.setWindowTitle("Confirm")
        dialog.setText("Do you want to send this mail?")

        yes_btn = QPushButton("Yes", dialog)
        no_btn = QPushButton("No", dialog)

        dialog.addButton(yes_btn, QMessageBox.YesRole)
        dialog.addButton(no_btn, QMessageBox.NoRole)

        dialog.exec()  # PySide6: bruk exec(), ikke exec_()

        if dialog.clickedButton() is not yes_btn:
            return  # user chose No / closed

        try:
            self.msg["From"] = "Philipef"
            self.msg["To"] = self.lineEdit_5.text()
            self.msg["Subject"] = self.lineEdit_6.text()
            self.msg.attach(MIMEText(self.textEdit.toPlainText(), "plain"))

            text = self.msg.as_string()
            self.server.sendmail(self.lineEdit.text(), self.lineEdit_5.text(), text)

            message_box = QMessageBox(self.window)
            message_box.setText("Mail sent!")
            message_box.exec()
        except Exception:
            message_box = QMessageBox(self.window)
            message_box.setText("Sending Mail Failed!")
            message_box.exec()


gui = MyGUI()
sys.exit(app.exec())
