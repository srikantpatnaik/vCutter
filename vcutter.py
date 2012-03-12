from PyQt4 import QtCore,QtGui  
import vcutter_menu,os,sys

class vcutter(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uifile = vcutter_menu.Ui_MainWindow()
        uifile.setupUi(self)

        self.connect(uifile.video_1_1,QtCore.SIGNAL("clicked()"),self.inputFile)
        self.connect(uifile.vformat,QtCore.SIGNAL("activated(int)"),self.changeFormat)
        self.connect(uifile.here_1,QtCore.SIGNAL("clicked()"),self.outputFile)
        self.connect(uifile.execute1,QtCore.SIGNAL("clicked()"),self.convertOne)
        self.vformatImported = uifile.vformat

        self.connect(uifile.video_2_1,QtCore.SIGNAL("clicked()"),self.inputFile)  
        self.connect(uifile.end,QtCore.SIGNAL("activated(int)"),self.beginningEnd)
        self.connect(uifile.video_2_2,QtCore.SIGNAL("clicked()"),self.clipingFile)
        self.connect(uifile.here_2,QtCore.SIGNAL("clicked()"),self.outputFile)
        self.connect(uifile.execute2,QtCore.SIGNAL("clicked()"),self.convertTwo)
        self.endImported = uifile.end
        
        self.connect(uifile.video_3_1,QtCore.SIGNAL("clicked()"),self.inputFile)  
        self.connect(uifile.videoclip,QtCore.SIGNAL("clicked()"),self.clipingFile) 
        self.connect(uifile.here_3,QtCore.SIGNAL("clicked()"),self.outputFile)     
        self.connect(uifile.execute3,QtCore.SIGNAL("clicked()"),self.convertThree)
        self.connect(uifile.time_from, QtCore.SIGNAL('textEdited(QString)'), self.grabFrom)        
        self.connect(uifile.time_to, QtCore.SIGNAL('textEdited(QString)'), self.grabto)        

        self.connect(uifile.video_4_1,QtCore.SIGNAL("clicked()"),self.inputFile)  
        self.connect(uifile.here_4,QtCore.SIGNAL("clicked()"),self.outputFile)     
#        self.connect(uifile.execute4,QtCore.SIGNAL("clicked()"),self.convertFour)
        self.connect(uifile.time_from_4, QtCore.SIGNAL('textEdited(QString)'), self.grabFrom)        
        self.connect(uifile.time_to_4, QtCore.SIGNAL('textEdited(QString)'), self.grabto)        

        self.connect(uifile.video_5_1,QtCore.SIGNAL("clicked()"),self.inputFile)  
        self.connect(uifile.here_5,QtCore.SIGNAL("clicked()"),self.outputFile)     
        self.connect(uifile.execute5,QtCore.SIGNAL("clicked()"),self.convertFive)
        self.connect(uifile.time_from_5, QtCore.SIGNAL('textEdited(QString)'), self.grabFrom)        
        self.connect(uifile.time_to_5, QtCore.SIGNAL('textEdited(QString)'), self.grabto)        

#################################  1.  Video conversions    ################################################

    def inputFile(self):
        global infile
        infile=QtGui.QFileDialog.getOpenFileName(self,"Open Video File",QtCore.QDir.homePath(),"Any Files (*.*)")

    def outputFile(self):
        global outfile
        outfile=QtGui.QFileDialog.getOpenFileName(self,"Open Video File",QtCore.QDir.homePath(),"Any Files (*.*)")

    def changeFormat(self):
        global fmt
        fmt = self.vformatImported.currentText()

    def convertOne(self):
        text= str('ffmpeg -i ' + infile + ' ' + outfile + '.' + fmt)
        os.system(text)
        print 'done conversion'

        
################################  2.  Adding video at the end/beginning of other video ######################


    """ inputFile & outputFile functions are same hence used from above """

    def clipingFile(self):
        global clipfile
        clipfile=QtGui.QFileDialog.getOpenFileName(self,"Open Video File",QtCore.QDir.homePath(),"Any Files (*.*)")

    def beginningEnd(self):
        global beginEnd
        beginEnd = self.endImported.displayText()

    def convertTwo(self):
        if beginEnd == 'end':
            vAdd = str('mencoder -oac copy -ovc copy -idx ' + clipfile + ' ' + infile + ' -o ' + outfile)
        elif beginEnd == 'beginning':
            vAdd = str('mencoder -oac copy -ovc copy -idx ' + infile + ' ' + clipfile + ' -o ' + outfile)
        os.system(vAdd)
        print 'stiching done !'
            

################################  3.  Cutting and inserting new video      ##################################

     
    def grabFrom(self,fromStringImported):    # As textChanged(QString) passes an arguement.
        global t1
        t1 = fromStringImported
        return t1

    def grabto(self,toStringImported):
        global t2
        t2 = toStringImported
        return t2
        
    def convertThree(self):
        text= str('ffmpeg -i ' + infile + ' -sameq -ss ' + t1 + ' -t ' + t2 + ' ' + outfile)
        os.system(text)
        print 'done conversion'




###############################  4. stich back original video after removing unwanted part ###################


###############################  5. save the removed portion as new video ####################################

    def convertFive(self):
        text= str('ffmpeg -i ' + infile + ' -sameq -ss ' + t1 + ' -t ' + t2 + ' ' + outfile)
        os.system(text)
        print 'done editing'




##############################################################################################################

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = vcutter()
    window.show()
    sys.exit(app.exec_())

