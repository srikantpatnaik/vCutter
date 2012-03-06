from PyQt4 import QtCore,QtGui
import vcutter_menu,os,sys

class TestApp(QtGui.QMainWindow):
    def __init__(shelf):
        QtGui.QMainWindow.__init__(shelf)
        atom = vcutter_menu.Ui_MainWindow()
        atom.setupUi(shelf)
        shelf.connect(atom.video_1_1,QtCore.SIGNAL("clicked()"),shelf.inputFile)
        shelf.connect(atom.vformat,QtCore.SIGNAL("activated(QString)"),shelf.currentFormat)
        shelf.connect(atom.execute,QtCore.SIGNAL("clicked()"),shelf.convertfile)
        shelf.connect(atom.here_1,QtCore.SIGNAL("clicked()"),shelf.outputFile)
        
        shelf.name1 = atom.vformat


    def inputFile(shelf):
        global infile
        infile=QtGui.QFileDialog.getOpenFileName(shelf,"Open Video File",QtCore.QDir.homePath(),"Any Files (*.*)")

    def outputFile(shelf):
        global outfile
        outfile=QtGui.QFileDialog.getOpenFileName(shelf,"Open Video File",QtCore.QDir.homePath(),"Any Files (*.*)")

    def currentFormat(shelf):
        global fmt
        fmt = shelf.name1.currentText()

    def convertfile(shelf):
        text= str('ffmpeg -i ' + infile + ' ' + outfile + '.' + fmt)
        os.system(text)
        print 'done conversion'
        



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = TestApp()
    window.show()
    sys.exit(app.exec_())

