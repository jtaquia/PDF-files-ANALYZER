# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:50:41 2018

@author: jtaquia
"""

from __future__ import print_function
import os
import glob
import io
import sys
from tkinter.colorchooser import askcolor
from contextlib import redirect_stdout
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
import subprocess
from tkinter import filedialog
from tkinter import *
import numpy as np
import argparse
import cv2


    

class ClassA(object):
    def __init__(self):
        currdir = os.getcwd()
        self.var1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Favor seleccione un directorio')   
       
        
    def abrir1(tempdir,tempdir2):
       
   
       currdir = os.getcwd()
       tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Favor seleccione un directorio')   
     
       
       if len(tempdir) > 0:
          
          messagebox.showinfo("Information","Usted eligió la carpeta  %s" % tempdir + " donde estan los pdf a analizar")
        
       else:
           messagebox.showwarning("Warning","Ingrese una ruta")
    
  
       messagebox.showinfo("Information","Seleccione la carpeta donde se guardará los resultados")
       
       currdir = os.getcwd()
       tempdir2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Favor seleccion donde guardará el resultado')   
     
       
       if len(tempdir2) > 0:
           
           messagebox.showinfo("Information","Usted eligió %s" % tempdir2)
           
        
       
       pdfDir = tempdir.replace('/','//')+ "//" 
       txtDir = tempdir2.replace('/','//')+ "//" 
       
       print(pdfDir, txtDir)     
          
       convertMultiple(pdfDir, txtDir)
    
def convertMultiple(pdfDir, txtDir):
   
    import os
   
    if pdfDir == "": pdfDir = os.getcwd() + "\\" 
    for pdf in os.listdir(pdfDir): 
            fileExtension = pdf.split(".")[-1]
            if fileExtension == "pdf":
                pdfFilename = pdfDir + pdf 
               
                text = layout(open(pdfFilename,'rb'),txtDir,pdf) 
    
    messagebox.showwarning("Warning","Se culminó con la extracción de texto de los pdf colocados en la carpeta : " + pdfDir + " y los resultados estan en : " + txtDir)

def layout(pdf_file, txtDir2,pdf2):
    
    from pdfminer.pdfparser import PDFParser, PDFDocument
    from pdfminer.layout import LAParams
    from pdfminer.converter import PDFPageAggregator
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.layout import LTTextBox, LTTextLine
    
    parser = PDFParser(pdf_file)
    doc = PDFDocument(pdf_file)
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    
 
    rsrcmgr = PDFResourceManager()
   
    laparams = LAParams()
   
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    textFilename = txtDir2 + pdf2 + ".txt"
    text_file = open(textFilename, "w")
    
  
    for page in doc.get_pages():
        interpreter.process_page(page)
        print(page.pageid)
        print(page.mediabox)
       
        layout = device.get_result()
    
        for element in layout:
                 if isinstance(element, LTTextBox) or isinstance(element, LTTextLine):
                    text =element.get_text().encode('utf-8')
                   
                    text_file.write("%s" % text)


    messagebox.showwarning("Warning","Se extrajo el texto en" + textFilename)


def hello():
    print ("hello!")

def salida():
    root.quit()
    root.destroy()

class myDict(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value
    
class GUI3():
    
    def __init__(self,root3):
        self.label3 = tk.Label(root3,text="Analizador de imágenes vrs 1. Diseño y programación: José Antonio Taquía Gutiérrez", width = 120, height=4, fg = "blue", font=("Helvetica",10,"bold"))
        self.label3.place(x=3, y  = 2)                    
 
class GUI2():
    
  
    
    def __init__(self,root2):
            
           
               
            self.root2 = root2 
         
            self.Entry = tk.Entry(root2, width = 30)
            self.Entry.place(x=250, y = 40)
          
            self.canvas = tk.Canvas()
            
            self.label2 = tk.Label(self.root2, text="Ingrese búsqueda:", width = 20, height=4, font=("Helvetica", 12))
            self.label2.place(x =40 , y =20)
            
            self.button2 = tk.Button(self.root2, text='Empezar', command= self.printing1, width = 10, height=2, font=("Helvetica", 12))
            self.button2.place(x =500 , y =20)

            self.button3 =  tk.Button(self.root2, text='Reiniciar', command= self.Reinicio, width = 10, height=2, font=("Helvetica", 12))
            self.button3.place(x =500 , y =80)
            
            self.button4 =  tk.Button(self.root2, text='Mostrar', command= self.mostrar100, width = 10, height=2, font=("Helvetica", 12))
            self.button4.place(x =500 , y =140)
            
            self.button5 =  tk.Button(self.root2, text='Pixels', command= self.ejecuta, width = 10, height=2, font=("Helvetica", 12))
            self.button5.place(x =500 , y =200)
            
            self.button6 =  tk.Button(self.root2, text='Salir', command= self.removethis2, width = 10, height=2, font=("Helvetica", 12))
            self.button6.place(x =500 , y =260)
         
            color = '#fee2a1'
            self.Text = tk.Text(root2, height=10, width=40, bg = color)
            self.Text.place(x =40 , y =120)
            
            self.lstbox = tk.Listbox(self.root2,height=10, width=80,bg = color,selectmode=EXTENDED)
            self.lstbox.place(x =40 , y =320)
          
            
            self.w = self.lstbox 
            self.index = int(self.w.curselection()[0])
            self.value = self.w.get(self.index)
            
            
    def pixels(self):
    
        import matplotlib
        from matplotlib import pyplot as plt
        matplotlib.use("TkAgg")
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
        from matplotlib.figure import Figure
        import matplotlib.patches as mpatches
        
        def _quit():
            master.quit()    
            master.destroy()  

       
        master = tk.Tk()
        master.wm_title("Pixels en la imagen: Espacio Red, Green, Blue. ")
        master.tkraise()
     
        
        
        color = '#fee2a1'
        self.canvas = Canvas(self.canvas, width=3, height=3)
        self.canvas.config(bg = color)
        self.canvas.pack()
            
        image = cv2.imread("D://Users//jtaquia//.spyder-py3//escena2.jpg")
        
        chans = cv2.split(image)
        colors = ("b", "g", "r")
        self.f = plt.figure()
            
        self.f = Figure(figsize=(3,3), dpi=150)
        self.a = self.f.add_subplot(111)

        for (chan, color) in zip(chans, colors):
            hist = cv2.calcHist([chan], [0], None, [250], [0, 250])
            self.a.plot(hist, color = color)
            self.a.plot([0, 256])
            self.a.plot([0, 15256])
    

        self.canvas = FigureCanvasTkAgg(self.f,master)
        self.canvas.show()

        self.canvas.get_tk_widget().pack()

        self.toolbar = NavigationToolbar2TkAgg(self.canvas,master)
        self.toolbar.update()
        self.canvas._tkcanvas.pack() 
        
       
    
    
            
    def Reinicio(self):
            self.Text.delete('1.0', END)
    
            
    def mostrar100(self):
            import os
            import re
         
            w = self.lstbox 
            index = int(w.curselection()[0])
            value = w.get(index)
            print ('You selected item %d: "%s"' % (index, value))
                
            
            self.lstbox.bind('<<ListboxSelect>>')
            
         
            s = value
            print('El valor de s es : ' + s)
            start = s.find('página :') + 8
            end = s.find('esta', start)
            r = s[start:end]              
            
            self.words = r.split()
            
            self.sfile = value
            start_sfile = self.sfile.find('archivo:') + 9
            end_sfile = self.sfile.find(':', start_sfile)
            global r_file
            r_file = self.sfile[start_sfile:end_sfile]            
            r_file = r_file.strip()
            self.words_file = r_file 
            
            Jjose = 'AcroRd32.exe'
            for root, dirs, files in os.walk(r'C://Program Files (x86)//Adobe//'):
                                       for name in files:
                                           if name == Jjose:
                                               path1 = os.path.abspath(os.path.join(root, name))
                                               
                                   
            path_to_acrobat = os.path.abspath(path1) 
           
            #print(path_to_acrobat)
            
            from subprocess import check_output,Popen, PIPE
                        
            for m in self.words:
               
                path_to_pdf = os.path.abspath(os.path.join( self.claves, str(self.words_file) ))    
                txtPathPdf = path_to_pdf.replace('/','//')
                
                try:
                    lsout=Popen(['lsof',txtPathPdf],stdout=PIPE, shell=False)
                    check_output(["grep",txtPathPdf], stdin=lsout.stdout, shell=False)
                except:
                
                    process = subprocess.Popen([path_to_acrobat, '/A', 'page=' + str(m), path_to_pdf], shell=False, stdout=subprocess.PIPE)
            
    
    def removethis2(self):
        
            self.root2.destroy()
            root.deiconify()
            
    def ejecuta(self): 
            
            
       
            from PyPDF2 import PdfFileWriter, PdfFileReader
            from tkinter import filedialog
            import os
         
          
            w = self.lstbox 
            index = int(w.curselection()[0])
            value = w.get(index)
                
            
            self.lstbox.bind('<<ListboxSelect>>') 
            
         
            s = value
            start = s.find('página :') + 8
            end = s.find('esta', start)
            r = s[start:end]              
            
            self.words = r.split()
            print('El valor de words es : ' +  " ".join([str(x) for x in self.words] ))
            self.sfile = value
            start_sfile = self.sfile.find('archivo:') + 9
            end_sfile = self.sfile.find(':', start_sfile)
            global r_file
            r_file = self.sfile[start_sfile:end_sfile]            
            r_file = r_file.strip()
            self.words_file = r_file 
            
            
    
            messagebox.showwarning("Warning","Va a realizar un análisis de composición de imágenes y su impacto en la venta. " )
            
            currdir = os.getcwd() 
            
            tempdir3 = filedialog.askdirectory( initialdir= currdir, title='Seleccione donde guardará el resultado')
            
            txtDir100 = tempdir3.replace('/','//')+ "//" 
            txtDir = tempdir3.replace('/','//')+ "//" + r_file
            
          
            path_mari = os.path.abspath(txtDir) 
                        
         
            inputpdf = PdfFileReader(open( path_mari, "rb"))
         
            newpath = txtDir100 + 'Analisis8' 
            if not os.path.exists(newpath):
                os.makedirs(newpath)
    
            os.chdir(newpath)
            
            
            for i in range(0, inputpdf.getNumPages()):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                with open("document-page%s.pdf" % i, "wb") as outputStream:
                    output.write(outputStream)
                    
            
            if   len(self.words)>1 :
                        
                messagebox.showwarning("Warning","Hay varias páginas en la selección elegida. Ingrese el número de página a analizar. " )    
                root4 = Tk()
                root4.title("Análisis de imagen en catálogo.")
                root4.geometry("350x150")
                label22 = tk.Label(root4, text="Ingrese página:", width = 20, height=2, font=("Helvetica", 12))
                label22.place(x =5 , y =20)
                root4.attributes("-topmost", True)
                color = '#f6b06f'
                root4.config(bg = color)
                var_jat = StringVar()
                e = Entry( root4, textvariable=var_jat)
                e.place(x=200, y = 40)
                button22 = tk.Button(root4, text='Continuar',width = 10,command =  Activa.__init__, height=2, font=("Helvetica", 12))
                button22.place(x =120 , y =80)
                
            else:
                
                
                inicio = self.words[0]
                print('el valor de la variable inicio es : ' + str(inicio))
                txtPathfile = os.path.abspath(os.getcwd() + '\document-page'+ str(inicio) + '.pdf')
                from wand.image import Image
                with Image(filename= txtPathfile) as img:
                    print('pages = ', len(img.sequence))
                    with img.convert('png') as converted:
                                converted.save(filename='document-page'+ str(inicio) + '.png')
       
    
            
    def printing1(self):
            import os
            import PyPDF2
            import re
            
            currdir = os.getcwd()
            
            tempdir2 = filedialog.askdirectory( initialdir= currdir, title='Favor seleccion donde guardará el resultado')   
            self.claves = tempdir2
            os.chdir(tempdir2)
            
            k= glob.glob('*.txt')
            
            size=10
            trazos = 100
            
            size_total=[]
            trazos_total=[]
          

            for i in k:
                
                txtDir0902 = tempdir2.replace('/','//')+ "//" + i 
                
                size_total.append(size)
                trazos_total.append(trazos)
                import mmap
            
            
                fp = open(txtDir0902,'rb')
               
                with fp as file, \
                 mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
                 v = self.Entry.get().encode('utf-8')
                 
                 if s.find(v) != -1:
                        
                        
                        
                        buffer = io.StringIO()
                        
                        print('La palabra: ' + self.Entry.get() + ' ,si esta en el archivo: ' + i, file=buffer)
                        
                        
                        output = buffer.getvalue()
                        
                       
                        self.Text.insert(END, output)
                         
                
                 else:
                    
                        
                        buffer = io.StringIO()
                        
                        print('La palabra: ' +  self.Entry.get() +  ' ,no se encuentra en el archivo: ' + i, file=buffer)
                        
                        
                        output = buffer.getvalue()
                        
                       
                        self.Text.insert(END, output)
                        
            myd = myDict()
            
            Dict_pickin = {}
            os.chdir(tempdir2)
            t= glob.glob('*.pdf')
            
          
                               
            for j in t:
                            Lista_pickin = []
                            pdfDir0902 = tempdir2.replace('/','//')+ "//" + j  
                            #print(pdfDir0902)
                             
                            PageFound = -1
                            pdfDoc = PyPDF2.PdfFileReader(open(pdfDir0902, "rb"))
                            counter =0
                            for i in range(0, pdfDoc.getNumPages()):
                                counter += 1
                                #print(pdfDoc.getNumPages())r
                                content = ""
                                content += pdfDoc.getPage(i).extractText() + "\n"
                                #print(type(content))
                                content1 = content.encode('utf-8') #, 'ignore').lower()
                                #content1 = content.encode('ascii', 'ignore').lower()
                                ResSearch = re.search(self.Entry.get().encode('utf-8') , content1)
                                
                                if ResSearch is not None:
                                   PageFound = i
                                   #var101 = i+1
                                   var101 = i
                                   Lista_pickin.append(var101)
                                   Dict_pickin.update({ str(j):var101}) # default_data.items() + {'item3': 3}.items()) 
                                   
                                   part1 = 'En el archivo: '+ j
                                   #part2 = 'En la página : '+ str(var101)
                                   part2 = 'En la página : '+ " ".join([str(x) for x in Lista_pickin] ) #+ str(len(Lista_pickin))
                                   #print(part2)
                                   myd.add(part1 , part2)
                                   #Resumen1 = dict(zip(t,counter))                
                                   print(' el resultado SI esta en la página: '+ str(PageFound))
                                   path_to_pdf = os.path.abspath( pdfDir0902 )
                                   
                                   Jjose = 'AcroRd32.exe'
                                   for root, dirs, files in os.walk(r'C://Program Files (x86)//Adobe//'):
                                       for name in files:
                                           if name == Jjose:
                                               path1 = os.path.abspath(os.path.join(root, name))
                                               
                                   
                                   path_to_acrobat = os.path.abspath(path1) 
                                   var = PageFound + 1
                                
                                else:
                                 
                                     print('No se encontró en el archivo : ' + pdfDir0902 + ' en la página ' + str(counter) + ' la palabra que ingreso.')

            for key in sorted(myd):    
                self.lstbox.insert(END, '{}: {}'.format(key, myd[key])+ ' esta la palabra '+ self.Entry.get())
            
            messagebox.showwarning("Warning","Se culminó con la búsqeda en los pdf colocados en la carpeta. " )

class Activa():
            
             

        def _init_(self):
            global inicio 
            inicio = GUI2.ejecuta.e.get()
            print(inicio.decode('utf-8'))
            
            new_path2 = os.path.abspath( os.getcwd() + '//document-page'+ inicio + '.pdf')    
            txtPathfile = new_path2.replace('/','//')
            print(txtPathfile)
            root4.destroy()
            self.root2.deiconify()
            from wand.image import Image
     
            with Image(filename= txtPathfile) as img:
                print('pages = ', len(img.sequence))
                with img.convert('png') as converted:
                            converted.save(filename='document-page'+ str(inicio) + '.png')
            
            return txtPathfile         
                
class GUI1:


        def __init__(self, menubar):
            
            from PIL import ImageTk, Image

            tempdir = "jat"
            tempdir2 = "kari"
            image = Image.open('D://Yanbal_DLO//PROYECTO COMPUTER VISION//RESULTADOS//GIF_1.gif')
            image2 = Image.open('D://Yanbal_DLO//PROYECTO COMPUTER VISION//RESULTADOS//GIF_3.gif')
            photo = ImageTk.PhotoImage(image)
            photo2 = ImageTk.PhotoImage(image2)
            self.label = tk.Label(image=photo)
            self.label.image = photo 
            self.label.place(x=210,y=90)
            self.label2 = Label(image=photo2)
            self.label2.image2 = photo2 
            self.label2.place(x=400,y=90)
            self.label3 = tk.Label(root,text="Fase 1: Analítica con imágenes:", width = 30, height=4, fg = "red", bg = "white",font=("Helvetica",12,"bold"))
            self.label3.place(x=180, y  = 2)
                    
                    
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Procesar pdfs", command=lambda: ClassA.abrir1(tempdir,tempdir2))

            filemenu.add_command(label="Guardar resultados", command=hello)
            filemenu.add_command(label="Búsqueda", command= entry_fields)
            
            filemenu.add_separator()
            filemenu.add_command(label="Salir", command= salida)
            menubar.add_cascade(label="File", menu=filemenu)
            
            editmenu = tk.Menu(menubar, tearoff=0)
            editmenu.add_command(label="Cut", command=hello)
            editmenu.add_command(label="Copy", command=hello)
            editmenu.add_command(label="Paste", command=hello)
            menubar.add_cascade(label="Edit", menu=editmenu)
            
            helpmenu = tk.Menu(menubar, tearoff=0)
            helpmenu.add_command(label="About", command=hello)
            helpmenu.add_command(label="Info", command=Informacion)
            menubar.add_cascade(label="Help", menu=helpmenu)
            color = '#fee2a1'
            root.config(menu=menubar, bg=color)
            root.title("Aplicación que busca texto en múltiples PDF´s")
            root.geometry("700x400")
            root.attributes("-topmost", True)
            
        def removethis(self):
            self.frame.destroy()

def Informacion():
        
            root3 = Tk()
            root3.title("Información")
            root3.geometry("800x100")
            root3.attributes("-topmost", True)
            #color = '#F57723'
            #root3.config(bg = 'white')
            color = '#fee2a1'
            root3.config(bg = color)
            window = GUI3(root3)


            
def entry_fields():
        
            root.withdraw()
            root2 = Tk()
            root2.title("Búsqueda")
            root2.geometry("650x550")
            root2.attributes("-topmost", True)
            color = '#f6b06f'
            #color = '#F57723'
            root2.config(bg = color)
            #root2.tkraise()
            menu = tk.Menu(root2) #, tearoff=0)
            root2.config(menu= menu)        
            menu.add_command(label="Espacio RGB", command=setBgColor)
            menu.add_command(label="Composición", command= hello)
            menu.add_command(label="Textos", command=hello)
            window = GUI2(root2)
          

     
def setBgColor():
            (triple, hexstr) = askcolor()
            if hexstr:
                print (hexstr)
     
           
        
def cambios():
        
        root.deiconify()

      
root = Tk()     
menubar = tk.Menu(root)
window = GUI1(menubar)
root.mainloop()







