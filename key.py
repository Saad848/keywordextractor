# 13/09/2020 OOP practice number one working with class. making keword stracting app
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from rake_nltk import Metric,Rake

class Key():
	def __init__(self):
		self.win_title = 'KEYWORD Version 0.0.1'
		self.win_app = QApplication([])
		self.win = QWidget()
		self.text_edit = QTextEdit()
		self.retrived_text = QTextEdit()
		self.combo_box = QComboBox()
		self.r = Rake(min_length=1, max_length=1)

	def helpwindow(self,w):
		"""Window to be displayed when help id clicked"""
		self.w = QWidget()
		self.w.setWindowTitle(self.win_title)
		self.w.setWindowIcon(QIcon ('C:\exe\K.png'))
		self.w.setGeometry(300,300,800,500)
		self.w.setFixedSize(800, 500)
		return self.w.show()
    
	def keys(self):
		self.win = QWidget()
		self.win.setWindowTitle("Extractor")
		self.win.setWindowIcon(QIcon ('C:\exe\K.png'))
		self.win.setGeometry(300,300,950,500)
		self.win.setFixedSize(950, 500)

		# Creating QMenuBar 
		mainMenu = QMenuBar(self.win)
		mainMenu.setGeometry(1,1,1000,20)
        
        # Addinf File item to QMenuBar
		fileMenu = mainMenu.addMenu('File')

		# Adding Items to File
		fileMenu.addAction("New")
		fileMenu.addAction("Open")
		fileMenu.addAction("Save")

        # Adding Action to Exit
		exitAction = QAction('&Exit')
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(qApp.quit)

		# Adding Exit To file
		fileMenu.addAction(exitAction)

        # Adding more items to MenueBar
		fileMenu.addSeparator()
		editMenu = mainMenu.addMenu('Edit')
		viewMenu = mainMenu.addMenu('View')
		searchMenu = mainMenu.addMenu('Search')
		toolsMenu = mainMenu.addMenu('Tools')
		helpMenu = mainMenu.addMenu('Help')

        # Adding help window to help
		helpAction = QAction('&Help')
		helpAction.setShortcut('Ctrl+H')
		helpAction.setStatusTip('Open Help Window')
		helpAction.triggered.connect(self.helpwindow)

		# adding helpAction to Help
		helpMenu.addAction(helpAction)

		#Text_edit where paragraph is pasted.
		self.text_edit = QTextEdit(self.win)
		self.text_edit.setPlaceholderText("Enter some text here. Maximum words limit is 300 only.")
		self.text_edit.setGeometry(30,50,430,300)
		self.text_edit.setAcceptRichText(False)	

        #retrived text where result is displayed
		self.retrived_text = QTextEdit(self.win)
		self.retrived_text.setPlaceholderText("Keywords are extracted here")
		self.retrived_text.setGeometry(490,50,430,300)

        #b1 button connected with the funcition rake to display result on click
		b1 = QPushButton(self.win)
		b1.setText('Extract')
		b1.setToolTip('Click to extract keywords from text')
		b1.setGeometry(30,370,100,40)
		b1.clicked.connect(self.rake)
		b1.clicked.connect(self.number)	
		
		#b2 button connect with the function clear to clear text of widgets
		b2 = QPushButton(self.win)
		b2.setText('CLEAR')
		b2.setToolTip('Click to clear the Text')
		b2.setGeometry(150,370,100,40)
		b2.clicked.connect(self.clear)

		#label for combo box
		label_1 = QLabel(self.win)
		label_1.setText("WORDS TO EXTRACT")
		label_1.adjustSize()
		label_1.move(500,380)

		# Combo box for number of wrods to be extratcted
		self.combo_box = QComboBox(self.win) 
		self.combo_box.setGeometry(610, 372, 60, 35) 

		# number of word to be extracted list 
		# number_list = ["1", "2","3","4","5"] 
		self.combo_box.addItems(["1", "2","3","4","5"])
		# creating editable combo box
		self.combo_box.setEditable(False)
		
		# self.combo_box.activated[int].connect(self.number)


		self.win.show()
		sys.exit(self.win_app.exec_())

	def number(self, no):
		no = int(self.combo_box.currentText())
		return print(no)

	def clear(self):
		self.text_edit.clear()
		self.retrived_text.clear()

    
	def rake(self):
		b = self.r.extract_keywords_from_text(self.text_edit.toPlainText()) , self.r.get_ranked_phrases()
		return print(self.retrived_text.setPlainText(str(b)))


	
a = Key()
a.rake()
a.keys()






# self.r = Rake(min_length=1, max_length=1)
		# for i in self.r.extract_keywords_from_text(self.text_edit) , self.r.get_ranked_phrases():
		# 	print(i)	

		# r = Rake(min_length=1, max_length=1)
			# print(rake.extract_keywords_from_text(text_edit.toPlainText()))
# return print(self.retrived_text.setPlainText(self.text_edit.toPlainText()))