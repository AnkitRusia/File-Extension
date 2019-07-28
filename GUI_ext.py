from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QWidget, QVBoxLayout, QGroupBox, QComboBox, QDialogButtonBox, QLabel, QLineEdit, QFileDialog, QPushButton, QHBoxLayout, QScrollArea, QMessageBox
from PyQt5.QtGui import QIcon
import sys
import base64 as B

global g_filename, g_cn
g_filename = ''
g_cn = ''


class CustomWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Converter")
        self.setWindowIcon(QIcon("rl.png"))
        self.setStyleSheet("QDialog {background: rgb(0,64,128);}")
        tabs = QTabWidget()
        tabs.setStyleSheet('''
                           QTabBar::tab:selected
                           { 
                            color: #4FA600;
                            background-color: rgb(255,255,255);
                            }

                QTabBar::tab:!selected {
                color: rgb(255,255,255);
                background-color: #4FA600;
                border-bottom-color: #4FA600;
                }
                QTabWidget{
                background-color: rgb(255,255,255);
                font: 35 10pt "Rockwell";
                }

                QTabBar::tab { 
                border: 2px solid rgb(0,149,48); 
                border-bottom-color: rgb(255,255,255);
                border-top-left-radius: 2px; 
                border-top-right-radius: 30px; 
                height: 30px;
                width: 100px;
                background-color: rgb(255,255,255);
                    }

                QTabWidget::pane {
                        border: 4px solid #C4C4C3;
                	border-bottom-color: #C2C7CB; 
                	border-top-left-radius: 10px;
                	border-top-right-radius: 20px;
                	min-width: 5em; 
                	min-height: 75px;
                	padding: 4px;
                	margin-left: 0px;
                	margin-top: 5px;
                	background-color: white;
                             }
                                        ''')
        
        tabs.addTab(Tab1(), "Home")
        tabs.addTab(Tab2(), "Help")
        tabs.addTab(Tab3(), "About")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)
        self.resize(650, 400)
        self.setFixedSize(650, 450)
        
        

class Tab1(QWidget):
    def __init__(self) :
        
        super().__init__()
        fnl = QLabel("File Name : ")
        font1 = fnl.font()
        font1.setPointSize(12)
        fnl.setFont(font1)

        fn2 = QLabel("Change To : ")
        font2 = fn2.font()
        font2.setPointSize(12)
        fn2.setFont(font2)
        
        self.name = QLineEdit()
        self.name.setStyleSheet('''
                        QLineEdit {
                        border: 4px solid blue;
                        border-width: 3px;
                        padding: 4px;
                        border-radius: 21px;
                        background-color : rgb(255,255,255)}''')
        font = self.name.font()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.resize(150,40)
        self.name.setPlaceholderText("File Name")

        self.cn = QLineEdit()
        self.cn.setStyleSheet('''
                        QLineEdit {
                        border: 4px solid blue;
                        border-width: 3px;
                        padding: 4px;
                        border-radius: 21px;
                        background-color : rgb(255,255,255)}''')
        fontcn = self.cn.font()
        fontcn.setPointSize(12)
        self.cn.setFont(fontcn)
        self.cn.resize(150,40)
        self.cn.setPlaceholderText("File Name")

        btn = QPushButton(" * ")
        btn.setToolTip("<b> Choose File </b>")
        btn.clicked.connect(self.pressed)
        btn.setStyleSheet('''
                            QPushButton{
                            color: white;
                            font: 35 14pt "Rockwell";
                            Text-align:top;
                            border: 3px solid black;
                            border-width: 1px;
                            border-radius: 13px;
                            height: 25px;
                            width: 35px;
                            background-color : #4FA600                            
                            }
                            ''')


        gptake = QGroupBox("Input File")
        gphbox = QHBoxLayout()
        gphbox.addWidget(fnl)
        gphbox.addWidget(self.name)
        gphbox.addWidget(btn)
        gptake.setLayout(gphbox)

        gpput = QGroupBox("Output File")
        gphbox1 = QHBoxLayout()
        gphbox1.addWidget(fn2)
        gphbox1.addWidget(self.cn)
        gpput.setLayout(gphbox1)


        self.cvt = QPushButton("Change ")
        self.cvt.clicked.connect(self._convert)
        self.cvt.setStyleSheet('''
                            QPushButton{
                            color: rgb(255, 255, 255);
                            border: 3px solid black;
                            border-width: 3px;
                            border-radius: 33px 33px 33px 33px;
                            height:60px;
                            width: 20px;
                            font: 35 15pt "Rockwell";
                            background-color : rgb(0,64,128)                           
                            }

                            QPushButton::hover
                            {
                               
                               color: white;
                               font: 40 20pt "Rockwell";
                               bordercolor: green;
                               background-color : rgb(0,64,198)
                               
                            }
                            ''')
        
        
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(gptake)
        mainlayout.addWidget(gpput)
        mainlayout.addWidget(self.cvt)

        self.setLayout(mainlayout)
        
    def pressed(self):
        global g_filename
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        fname, _ = dlg.getOpenFileName()
        g_filename = fname
        
        _pn = fname.split('/')
        _pn = _pn[-1]
        self.name.setText(_pn)

    def _convert(self):
        try : 
            global g_filename, g_cn
            if g_filename == '' :
                g_filename = self.name.text()
            g_cn = self.cn.text()
            
            po = {
                'img' : ['png (recommended)', 'jpeg', 'ico', 'bmp', 'gif'],
                'audio' : ['mp3 (recommended)', 'wav', 'wma'],
                'video' : ['mp4 (recommended)', 'mkv', '3gp', 'flv'],
                'code': ['txt', 'c', 'cpp', 'py', 'java', 'js', 'xml', 'html']
                }
            
            ext = g_filename.split('.')[-1]
            filename = "".join(g_filename.split('.')[:-1])
            nf = g_cn
            loc = "/".join(g_filename.split('/')[:-1])
            
            g_cn = loc +'/'+g_cn
            
            

            f = open(g_filename, 'rb').read()
            #f = B.b64encode(f)
            q = open(g_cn, 'wb')
            q.write(f)
            q.close()
            print('done')
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Information)
            mb.setWindowTitle('Done :) ')
            if len(loc) <= 1 :
                loc = "Current Folder"
            mb.setText("File name : {}\nLocation : {}\nSuccessFull".format(nf, loc))
            mb.setStandardButtons(QMessageBox.Ok)
            mb.buttonClicked.connect(self.msgbtn)
            mb.exec_()
            self.name.setText('')
            self.cn.setText('')

        except Exception as e:
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Warning)
            mb.setWindowTitle('Error')
            mb.setText(str(e))
            mb.setStandardButtons(QMessageBox.Ok)
            mb.buttonClicked.connect(self.msgbtn)
            mb.exec_()
            
             

    def msgbtn(self):
        global g_filename, g_cn
        g_filename = ''
        g_cn = ''


        
        

class Tab2(QWidget):
    def __init__(self) :
        super().__init__()
        
        lhelp = QLabel("HELP !")
        font1 = lhelp.font()
        font1.setPointSize(12)
        lhelp.setFont(font1)
        e0 = QLabel('')
        e1 = QLabel('')
        e2 = QLabel('')
        e3 = QLabel('')
        e4 = QLabel('')
        e5 = QLabel('')
        e6 = QLabel('')
        e7 = QLabel('')
        e8 = QLabel('')
        e9 = QLabel('')
        e10 = QLabel('')

        sg = QGroupBox("")
        sg.setStyleSheet(
            '''
            QGroupBox
            {
                background-color : rgb(255,255,255)
            }

            ''')
        

        
        ag = QGroupBox("Audio File Type")
        ag.setStyleSheet(""" QGroupBox{
                            border: 1px solid black;
                            border-width: 3px;
                            font: 35 11pt "Rockwell";
                            border-radius: 15px 15px 15px 15px
                            } """)
        aghbox = QVBoxLayout()
        wav = QLabel("wav: Used in audio recorders")
        mp3 = QLabel("mp3: Used to play songs (recommended)")
        wma = QLabel("wma: Windows Media Audio")
        aghbox.addWidget(e0)
        aghbox.addWidget(wav)
        aghbox.addWidget(e0)
        aghbox.addWidget(mp3)
        aghbox.addWidget(e0)
        aghbox.addWidget(wma)
        aghbox.addWidget(e0)
        ag.setLayout(aghbox)


        vg = QGroupBox(" Video File Type")
        vg.setStyleSheet(""" QGroupBox{
                            border: 1px solid black;
                            font: 35 11pt "Rockwell";
                            border-width: 3px;
                            border-radius: 15px 15px 15px 15px
                            } """)
        vghbox = QVBoxLayout()
        mp4 = QLabel("mp4: Used Commonly (recommended) syn:m4a, m4v")
        gp3 = QLabel("3gp: Used in low quality video")
        mkv = QLabel("mkv: Used in Anime's")
        flv = QLabel("flv: Flash Videos, VLC media player can play this file")
        vghbox.addWidget(e1)
        vghbox.addWidget(mp4)
        vghbox.addWidget(e1)
        vghbox.addWidget(gp3)
        vghbox.addWidget(e1)
        vghbox.addWidget(mkv)
        vghbox.addWidget(e1)
        vghbox.addWidget(flv)
        vg.setLayout(vghbox)

        pg = QGroupBox(" Programing Languages ")
        pg.setStyleSheet(""" QGroupBox{
                            border: 1px solid black;
                            border-width: 3px;
                            font: 35 11pt "Rockwell";
                            border-radius: 15px 15px 15px 15px
                            } """)
        pghbox = QVBoxLayout()

        c = QLabel("*.c : C Language")
        cpp = QLabel("*.cpp : C++ Language")
        py = QLabel("*.py : Python Language")
        java = QLabel("*.java : Java Language")
        js = QLabel("*.js : Java Script Language")
        html = QLabel("*.html : Hyper Text Markup Language")
        pghbox.addWidget(e2)
        pghbox.addWidget(c)
        pghbox.addWidget(e2)
        pghbox.addWidget(cpp)
        pghbox.addWidget(e2)
        pghbox.addWidget(java)
        pghbox.addWidget(e2)
        pghbox.addWidget(js)
        pghbox.addWidget(e2)
        pghbox.addWidget(html)
        pghbox.addWidget(e2)
        pg.setLayout(pghbox)


        ig = QGroupBox("Images")
        ig.setStyleSheet(""" QGroupBox{
                            border: 1px solid black;
                            border-width: 3px;
                            font: 35 11pt "Rockwell";
                            border-radius: 15px 15px 15px 15px
                            } """)
        ighbox = QVBoxLayout()

        jpg = QLabel("*.jpg/jpeg : Images cantains RGB value of pixel")
        png = QLabel("*.png : Images contain RGBA value of pixel (recommended)")
        ico = QLabel("*.ico : Icon type images. Use GIMP to open")
        bmp = QLabel("*.bmp : Very low quality image")
        gif = QLabel("*.gif : Graphics based Images.")
        ighbox.addWidget(e10)
        ighbox.addWidget(jpg)
        ighbox.addWidget(e6)
        ighbox.addWidget(png)
        ighbox.addWidget(e7)
        ighbox.addWidget(ico)
        ighbox.addWidget(e8)
        ighbox.addWidget(bmp)
        ighbox.addWidget(e9)
        ighbox.addWidget(gif)     
        ig.setLayout(ighbox)


        


        mainlayout = QVBoxLayout()
        mainlayout.addWidget(ag)
        mainlayout.addWidget(e3)
        mainlayout.addWidget(vg)
        mainlayout.addWidget(e4)
        mainlayout.addWidget(pg)
        mainlayout.addWidget(e5)
        mainlayout.addWidget(ig)
        mainlayout.addStretch(1)

        sg.setLayout(mainlayout)

        scrollarea = QScrollArea()
        scrollarea.setStyleSheet(
            '''
            QScrollArea
            {
                  
                  border-width: 10px;
                  border-style: solid;
                  background-color: rgb(255, 255, 255)
                  
                  
                
            }
            ''')
        scrollarea.setFixedWidth(580)
        scrollarea.setWidgetResizable(True)
        scrollarea.setWidget(sg)
        

        ml = QVBoxLayout()
        ml.addWidget(lhelp)
        ml.addWidget(scrollarea)
        
        self.setLayout(ml)
        

class Tab3(QWidget):
    def __init__(self) :
        super().__init__()
        name = QLabel("Name : File Extention Changer")
        version = QLabel("Version : V.0.1")
        update = QLabel("For update/bug cantact: rusia.kanha@gmail.com")
        support = QLabel("Support me through Paytm: +919827168348")
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(name)
        mainlayout.addWidget(version)
        mainlayout.addWidget(update)
        mainlayout.addWidget(support)
        self.setLayout(mainlayout)





app = QApplication(sys.argv)
window = CustomWindow()
window.show()
sys.exit(app.exec_())








##################################
##
##QTabWidget::pane {
##                        
##                      border: 4px solid #C4C4C3;
##                	border-bottom-color: #C2C7CB; 
##                	border-top-left-radius: 10px;
##                	border-top-right-radius: 20px;
##                	min-width: 5em; 
##                	min-height: 75px;
##                	padding: 4px;
##                	margin-left: 0px;
##                	margin-top: 5px;
##                	background-color: white;
##                             }
