from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
from link_converter import convert_url
import pyperclip
import sys

class LinkConverter(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ensemblevideo Link Converter - Dennis Farmer")
        self.resize(600,300)

        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("Convert to Download Link")
        self.btnPress3 = QPushButton("Clear Field Contents")
        self.btnPress2 = QPushButton("Copy to Clipboard")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.btnPress3)
        self.setLayout(layout)

        self.textEdit.setPlainText("https://cloud.ensemblevideo.com/hapi/v1/contents/e5ee9fb7-8a1e-48f2-9e4d-2ac8a77c2478/launch?embedAsThumbnail=false&displayTitle=True&displaySharing=False&autoplay=False&showCaptions=False&hideControls=True&audioPreviewImage=False&displayEmbedCode=False&displayAttachments=True&displayLinks=True&displayCredits=False&displayVideoDuration=False&displayNotes=True&displayCaptionSearch=True&displayMetaData=false&displayDownloadIcon=False&displayViewersReport=False&displayAxdxs=False&idn_content=e5ee9fb7-8a1e-48f2-9e4d-2ac8a77c2478&idn_init=False&idn_sig=62NO%2FKLkev7ZUVK696RTOVkjP1Q%3D")
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)

    def btnPress1_Clicked(self):
        old_url = self.textEdit.toPlainText()
        new_url = convert_url(old_url)
        self.textEdit.setPlainText(new_url)

    def btnPress2_Clicked(self):
        url = self.textEdit.toPlainText()
        pyperclip.copy(url)

    def btnPress3_Clicked(self):
        self.textEdit.setPlainText("")

def Start():
    lc = LinkConverter()
    lc.show()
    return lc

def main():
    app = QApplication(sys.argv)
    win = Start()
    app.exec_()
    #sys.exit(app.exec_())

if __name__ == '__main__':
    main()
