import tkinter as tk
import time
import threading

from PIL import ImageTk, Image

import glob

import csv
import os
import sys

#def ServoState(tk.Tk):

green_light_img_path = "green-circle-hi.png"
red_light_img_path = "red-circle-icon-hi.png"


def loadCSV(filename):
    file = open(filename, 'r')
    csvCursor = csv.reader(file)

    data = []
    for row in csvCursor:
        data.append(row)
        #print(row)

    file.close()
    return data

class Mainframe(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = FirstFrame(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget() # delete currrent frame

        self.frame = frame(self)
        self.frame.pack() # make new frame

class FirstFrame(tk.Frame):   


    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Main frame")
        master.geometry("800x600")

        #self.inputField = tk.Entry(self)
        #self.inputField.grid(row=0, column=1, columnspan=6)

        self.grid()
        self.sel0 = -1 # a initial value

        path = red_light_img_path
        img0 = Image.open(path)
        img0.thumbnail((30,30))
        #>>> im = Image.open( "sample01.jpg" )
#>>> im.thumbnail( (400,100) )
#>>> im.save( "thumbnail.jpg" )
#>>> print im.size
        img = ImageTk.PhotoImage(img0)
        self.panel = tk.Label(self, image = img)#, height = 450, width=450)
        #panel = tk.Label(image = img)  # 不加self, 就會在所有視窗放上圖片!!!
        self.panel.image = img # keep a reference, why???
        #print(panel)
        #The Pack geometry manager packs widgets in rows or columns.
        self.panel.grid(row=0,column=0,sticky=tk.W)#, padx=30, pady=30)#side = "bottom", fill = "both", expand = "yes")       


        self.v = tk.StringVar()
        self.lb1 = tk.Label(self,textvariable=self.v)
        self.v.set("Servo: not nonnect")
        self.lb1.grid(row=0,column=1,rowspan=1,columnspan=1, sticky=tk.W)



        self.lb2 = tk.Label(self,text="請選擇機型")
        self.lb2.grid(row=1,column=0,columnspan=2,sticky=tk.W)

        self.lb3 = tk.Label(self, text="按下 Servo On 前安全須知\n1. 為了防止暴衝，確認另一人員手放在breaker 上隨時斷電\n2. 機台須與極限位置有一段安全距離")
        #self.lb4 = tk.Label(self, text="1. 為了防止暴衝，確認另一人員手放在breaker 上隨時斷電")
        #self.lb5 = tk.Label(self, text="2. 機台須與極限位置有一段安全距離")
        self.lb3.grid(row=2,column=2,sticky=tk.W)
        #self.lb4.grid(row=3,column=2)#
        #self.lb5.grid(row=4,column=2)#

        self.btn_motion = tk.Button(self, text="動作測試", command=lambda: master.change(MotionTest)) 
        self.btn_laser = tk.Button(self, text="雷射干涉", command=lambda: master.change(LaserInterferometerTest))
        #self.btn_motion.grid(row=5,column=2)
        #self.btn_laser.grid(row=6,column=2)

        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=2,column=0,columnspan=2,sticky=tk.W)

        #tk.e
        #listbox.insert(tk.END, "a list entry")



        self.textarea = tk.Text(self,width=20,height=10)
        #self.recipe = recipe
        self.recipe = glob.glob("*.csv")
        for item in self.recipe:
            self.listbox.insert(tk.END, item)       

        self.textarea.grid(row=4,column=0,rowspan=1,columnspan=6, sticky=tk.W)

        btn=tk.Button(self,text="下一步",command=self.RunButton)
        #btn.grid(row=16,column=0,sticky=tk.W)

        self.btn2 = tk.Button(self, text="Servo On",command=self.ServoOn)
        self.btn2.grid(row=17,column=0,sticky=tk.W)


        #btn3 = tk.Button(self, text="hello",command=self.hello)
        #btn3.grid(row=18,column=0,sticky=tk.W)

        #self.btn_f = tk.Button(self, text="下一頁", command=self.Forward)
        #self.btn_f.grid(row=18,column=0,sticky=tk.W)

        self.poll()
    def ServoOn(self):
        #
        if True:
            path = green_light_img_path
            img0 = Image.open(path)
            img0.thumbnail((30,30))
            img = ImageTk.PhotoImage(img0)
            self.panel = tk.Label(self, image = img)#, height = 450, width=450)
            #panel = tk.Label(image = img)  # 不加self, 就會在所有視窗放上圖片!!!
            self.panel.image = img # keep a reference, why???
            #print(panel)
            #The Pack geometry manager packs widgets in rows or columns.
            self.panel.grid(row=0,column=0,sticky=tk.W)
            self.v.set("Servo: nonnect")

            self.listbox.grid_forget()
         #   self.btn_f.grid_forget()

            self.btn_b = tk.Button(self, text="Servo Off", command=self.Backward)
            self.btn_b.grid(row=18,column=0,sticky=tk.W)

            self.btn_motion.grid(row=5,column=2)
            self.btn_laser.grid(row=6,column=2)

            self.lb3.grid_forget()
            self.btn2.grid_forget()

    def Forward(self):
        print("hello")
        #self.Frame.grid_forget()
        #self.textarea.grid_forget()
        self.listbox.grid_forget()
        self.btn_f.grid_forget()

        self.btn_b = tk.Button(self, text="上一頁", command=self.Backward)
        self.btn_b.grid(row=18,column=0,sticky=tk.W)

        self.btn_motion.grid(row=5,column=2)
        self.btn_laser.grid(row=6,column=2)
        btn2.grid(row=17,column=0,sticky=tk.W)
    def Backward(self):
        self.listbox.grid(row=2,column=0,columnspan=2,sticky=tk.W)
        self.btn_b.grid_forget()

        #self.btn_f = tk.Button(self, text="返回", command=self.Forward)
        #self.btn_f.grid(row=18,column=0,sticky=tk.W)

        self.btn_motion.grid_forget()
        self.btn_laser.grid_forget()
        self.lb3.grid(row=2,column=2,sticky=tk.W)
        self.btn2.grid(row=17,column=0,sticky=tk.W)

    def poll(self):
        self.lb2.after(200, self.poll)
        sel = None
        try:
            sel = self.listbox.curselection()[0]
            self.lb2.config(text="你選擇的是"+self.recipe[sel])
            recipe = loadCSV(self.recipe[sel])

            if sel != self.sel0:
                self.textarea.delete(1.0,tk.END)
                for row in recipe:
                    self.textarea.insert(tk.END,row)
                    self.textarea.insert(tk.END,"\n")
                #print(row)

        except IndexError:
            sel = None

        #print(sel.type)
        #print(sel)


    def RunButton(self):
        self.master.change(SecondFrame)

class SecondFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("otherFrame")
        master.geometry("800x600")
        self.grid()
        self.var = tk.StringVar(self)
        lbl = tk.Label(self, textvariable=self.var)
        lbl.pack(anchor='w')
        btn = tk.Button(self, text="上一頁", command=lambda: master.change(FirstFrame))
        btn.pack()

        btn2 = tk.Button(self, text="動作測試", command=lambda: master.change(MotionTest))
        btn2.pack()

        btn3 = tk.Button(self, text="雷射干涉", command=lambda: master.change(LaserInterferometerTest))
        btn3.pack()

        btn4 = tk.Button(self, text="Servo ON", command=lambda: master.change(MotionTest))
        btn4.pack()
        #t = threading.Thread(target=self.process)
        #t.start()

        path = 'G3.png'
        photoimage = Image.open(path)

        #print(photoimage.size())
        #photoimage = photoimage.resize((900,0))#, Image.BILINEAR)
        #Image.resize(photoimage,(10,10), Image.BILINEAR)
        #photoimage.r
        img = ImageTk.PhotoImage(photoimage)
        #img.zo
        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(self, image = img)

        #The Pack geometry manager packs widgets in rows or columns.
        panel.pack()#side = "bottom", fill = "both", expand = "yes")



    def process(self):
        b=0
        for a in range(0,20):
            b=a
            print (b)
            self.var.set("Current value is {}".format(b))
            time.sleep(0.2)


class MotionTest(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("MotionTest")
        master.geometry("800x600")
        self.var = tk.StringVar(self)
        lbl = tk.Label(self, textvariable=self.var)
        lbl.pack(anchor='w')
        btn = tk.Button(self, text="上一頁", command=lambda: master.change(SecondFrame))
        btn.pack()

class LaserInterferometerTest(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("MotionTest")
        master.geometry("800x600")
        self.var = tk.StringVar(self)
        lbl = tk.Label(self, textvariable=self.var)
        lbl.pack(anchor='w')
        btn = tk.Button(self, text="上一頁", command=lambda: master.change(SecondFrame))
        btn.pack()
        path = "G3.png"
 #       image = Image.open(path)
#        photo = ImageTk.PhotoImage(image)
 #       label = tk.Label(image=photo)
#        label.image=photo # keep a reference
#        label.pack()
        photoimage = Image.open(path)
        photoimage.thumbnail((150,150))
        img = ImageTk.PhotoImage(photoimage)
      #  img.zoom(100,100)
        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(self,image = img)#, height = 450, width=450)
        #panel = tk.Label(image = img)  # 不加self, 就會在所有視窗放上圖片!!!
        panel.image = img # keep a reference, why???
        #print(panel)
        #The Pack geometry manager packs widgets in rows or columns.
        panel.pack()#side = "bottom", fill = "both", expand = "yes")

if __name__=="__main__":
    app=Mainframe()
    app.mainloop()
