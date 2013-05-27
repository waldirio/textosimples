import gtk
import gtk.glade
import pygtk
import sys

class TextoSimples:
    def __init__(self):
        self.xml = gtk.glade.XML('textosimples.glade')
        
        dic = { "on_btncopy_clicked":   self.btncopy_clicked,
                "on_btnreset_clicked":  self.btnreset_clicked,
                "on_btnsoma_clicked":   self.btnsoma_clicked,  
                "on_btnsobre_clicked":  self.btnsobre_clicked,
                "on_btnfechar_clicked":  self.btnfechar_clicked,             
               }
        self.xml.signal_autoconnect(dic)
        self.window = self.xml.get_widget('MainWindow')
        self.window.show()
        
        textA = self.xml.get_widget('texta').get_text()
        textB = self.xml.get_widget('textb').get_text()
        #textSoma = self.xml.get_widget('textsoma')
        
        
    def btnfechar_clicked(self,widget):
        print 'close do sobre'    
        self.xml.get_widget('sobre').hide()

    def btnsobre_clicked(self,widget):
        print 'sobre'
        self.xml.get_widget('sobre').show()

    def btnsoma_clicked(self,widget):
        #global textSoma, textA, textB
        self.xml.get_widget('textsoma').set_text(str(int(self.xml.get_widget('texta').get_text()) + int(self.xml.get_widget('textb').get_text())))
        
    def btncopy_clicked(self,widget):
        print 'copy'
        textA = self.xml.get_widget('texta').get_text()
        self.xml.get_widget('textb').set_text(textA)
        #self.xml.get_widget('texta').set_text('xxxxxxx')
        
    def btnreset_clicked(self,widget):
        print 'reset'
        self.xml.get_widget('texta').set_text('')
        self.xml.get_widget('textb').set_text('')
        self.xml.get_widget('textsoma').set_text('')
        

if __name__ == "__main__":
    Texto = TextoSimples()
    gtk.main()