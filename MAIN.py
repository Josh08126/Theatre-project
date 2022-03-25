import pyodbc
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from seats import *
from selection import *
from search import *
cs = (
                #  "Driver={SQL Server};"
                #  "Server=svr-cmp-01;"
                #  "Database=21HeffernaJN42;"
                #  "Trusted_Connection=yes;"
                #  "UID=COLLYERS\21HeffernaJN42;"
                #  "pwd=SY219842"
                #  )
               "Driver={SQL Server};"
               "Server=DESKTOP-MDD6DGU\SQLEXPRESS01;"
               "Database=Theatre;"
               "Trusted_Connection=yes;"
               )
class SearchWindow(QDialog): #GUI to search for bookings and gain attendants information
  def __init__ (self):
        super(QDialog, self).__init__()
        self.ui = Ui_Search()
        self.ui.setupUi(self)
        self.ui.pbsearch.clicked.connect(self.search_clicked)

  def search_clicked(self): #function to output search results
      query = "SELECT"


  

  def runquery(self, query, header): #query to run sql query and siplay on table
        self.ui.twViewers.setRowCount(50)
        self.ui.twViewers.setColumnCount(50)
        
        self.ui.twViewers.clear()
        self.ui.twViewers.setHorizontalHeaderLabels(header)
        cnxn = pyodbc.connect(cs)
        cursor = cnxn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        noRow = 0
        for tuple in rows:
            noCol=0
            for column in tuple:
                data = QTableWidgetItem(str(column))
                self.ui.twViewers.setItem(noRow, noCol, data)
                noCol+=1
            noRow+=1
        self.ui.twViewers.setRowCount(noRow)
        self.ui.twViewers.setColumnCount(noCol)
        cnxn.close()


class SelectionWindow(QDialog): #GUI to select what decide whether you want to book, collect, search, etc.
  def __init__ (self):
        super(QDialog, self).__init__()
        self.ui = Ui_Selectionscreen()
        self.ui.setupUi(self)


        self.ui.pbCreate.clicked.connect(self.create_clicked)
        self.ui.pbSearch.clicked.connect(self.search_clicked)

  def search_clicked(self): #when search button clicked, search GUI is opened
      widget.setCurrentIndex(2)
      

  def create_clicked(self): #when create button is clicked, create booking GUI is opened
      widget.setCurrentIndex(0)

class Booking(QDialog): #GUI to create bookings
  def __init__ (self):
        
        super(QDialog, self).__init__()
        self.ui = Ui_Seating()
        self.ui.setupUi(self)
        self.printseats()
        self.displayunavailable()
        self.ui.comboRegular.currentIndexChanged.connect(self.calcprice)  #when combobox for ticket selection is changed, function calcprice is ran
        self.ui.comboReduced.currentIndexChanged.connect(self.calcprice)
        self.ui.comboSpecial.currentIndexChanged.connect(self.calcprice)
        global checkedlist; checkedlist = [] # makes checkedlist accessible throughout class
        
        
        
        

  
        
  def calcprice(self): # function to calculate total price
      global numberofseats
      numberofseats = 0
      numberofseats = int(self.ui.comboRegular.currentIndex()) + int(self.ui.comboReduced.currentIndex()) + int(self.ui.comboSpecial.currentIndex())
      print(numberofseats)
      regularprice = ((self.ui.comboRegular.currentIndex())*10)
      reducedprice = (self.ui.comboReduced.currentIndex())*5
      totalprice = "{:.2f}".format(float(regularprice+reducedprice))
      self.ui.lblCost.setText("£{0}".format(totalprice))
      
      
        
  def printseats(self): # function to output the seats
      seatindex = 0
      for n in range(1,11): #loop to make 10 rows
        t=340
        for i in range(1,21): #loop to print 20 seats per row
          seatindex += 1
          exec("self.checkBox{0} = QtWidgets.QCheckBox(self)".format(seatindex))
          exec("self.checkBox{0}.setGeometry(QtCore.QRect({1}, {2}, 41, 41))".format(seatindex,t,(120+(40*n))))
          exec("""self.checkBox{0}.setStyleSheet("QCheckBox::indicator {{\\n"
                "    width: 30px;\\n"
                "    height: 30px;\\n"
                "}}\\n"
                "\\n"
                "QCheckBox::indicator:unchecked {{\\n"
                "    image: url(:/newPrefix/seatavailable.png);\\n"
                "}}\\n"
                "\\n"
                "QCheckBox::indicator:checked {{\\n"
                "    image: url(:/newPrefix/seatselected.png);\\n"
                
                "}}\\n"
                "QCheckBox::indicator:disabled {{\\n"
                "    image: url(:/newPrefix/seatoccupied.png);\\n"
                "}}")""".format(seatindex))
          exec("self.checkBox{0}.setText('')".format(seatindex))
          exec("self.checkBox{0}.setIconSize(QtCore.QSize(9, 8))".format(seatindex))
          exec("self.checkBox{0}.setObjectName('checkBox{0}')".format(seatindex))
          exec("self.checkBox{0}.stateChanged.connect(lambda: seatwindow.getselectedseat(str({0})))".format(seatindex))

          
          t=t+35
      t = 335
      print(seatindex)
      for index in range(1,21): #loop to print out the column numbers
        exec("self.labelnum{0} = QtWidgets.QLabel(self)".format(index))
        exec("self.labelnum{0}.setGeometry(QtCore.QRect({1}, {2}, 41, 41))".format(index,t,(50+(45*11))))
        exec("self.labelnum{0}.setText('{0}')".format(index))
        exec("self.labelnum{0}.setAlignment(QtCore.Qt.AlignCenter)".format(index))
        exec("self.labelnum{0}.setObjectName('labelnum{0}')".format(index))
        t +=35
  
  
  def displayunavailable(self): #function to disable and indicate which seats are booked
      seatnumber = ''
      cnxn = pyodbc.connect(cs)
      cursor = cnxn.cursor()
      unavailable = "SELECT SeatNo FROM Booking;"
      cursor.execute(unavailable)
      unavailableseatnumber = cursor.fetchall()
      print(unavailableseatnumber)
      counter = 0
      print(seatnumber)
      for i in range(1,len(unavailableseatnumber)): #loop to add stylesheets for seats that are booked and disable them
          seatnumber = (unavailableseatnumber[counter])[0]    
          exec("self.checkBox{0}.setEnabled(False)".format(seatnumber))
          exec("""self.checkBox{0}.setStyleSheet("QCheckBox::indicator {{\\n"
                "    width: 30px;\\n"
                "    height: 30px;\\n"
                "}}\\n"
                "\\n""QCheckBox::indicator:disabled {{\\n"
                "    image: url(:/newPrefix/seatoccupied.png);\\n"
                "}}")""".format(seatnumber))
          counter +=1
  def getselectedseat(self,seatnum): #output the location of the seat you have selected
    if len(checkedlist) < numberofseats: #only allows user to select number of seats in which they have stated (through combobox)
      self.ui.lblSelected.setText('')
      rows ="ABCDEFGHIJ"
      if eval("self.checkBox{0}.checkState()".format(seatnum)) == 0:
        row = rows[(int(seatnum)//20)]
        column = int(seatnum)%20
        if column == 0:
          column = 20
          row = rows[(int(seatnum)//20)-1]
        checkedlist.remove("{0}{1}".format(row,column))
      if eval("self.checkBox{0}.checkState()".format(seatnum)) == 2:
        row = rows[(int(seatnum)//20)]
        column = int(seatnum)%20
        if column == 0:
          column = 20
          row = rows[(int(seatnum)//20)-1]
        checkedlist.append("{0}{1}".format(row,column))
      else:
        pass
      for i in range(0,len(checkedlist)):
        self.ui.lblSelected.setText(', '.join(checkedlist))
    else:
      exec("self.checkBox{0}.setCheckState(0)".format(seatnum)) #if try toi select more than stated, the program will just deselect the latest seat that has been clicked
    
      



if __name__ == '__main__':
    import sys

    sys._excepthook = sys.excepthook
    def exception_hook(exctype, value, traceback):

        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    widget.setObjectName("widget")
    seatwindow = Booking()
    selectionwin = SelectionWindow()
    searchwin = SearchWindow()
    widget.addWidget(seatwindow) #this is done to allow multiple GUIs to show in one window
    widget.addWidget(selectionwin)
    widget.addWidget(searchwin)
    widget.setFixedWidth(1059)
    widget.setFixedHeight(735)
    widget.setStyleSheet("QObject{color: rgb(255, 255, 255);}\n"
"QObject#widget{background-color:rgb(0,0,33);}")
    widget.show()
    widget.setCurrentIndex(1)
    
