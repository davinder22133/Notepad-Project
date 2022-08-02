#from tkinter import *
#import time
import tkinter as tk
import time
import tkinter.font as tkFont
from tkinter.scrolledtext import ScrolledText

from tkinter.font import Font

from tkinter import filedialog as fd


root=tk.Tk()
root.title("Colored Notepad")

def new_clicked():
   text1.config(state='normal')
   text1.delete(1.0,tk.END)
   root.title("Untitled - Notepad")
   
   #fileobj = None
   
   
def save_clicked():
    
    file = fd.asksaveasfile()
    
    a = text1.get("1.0", tk.END) #getting all text from textbox
    
    
    
    fileobj = open(file.name ,"w")

    fileobj.write(a)
    fileobj.close()



def open_clicked():
    file = fd.askopenfile()
    
    fileobj = open(file.name, "r") 
    data = fileobj.read()
    fileobj.close()

    text1.insert(tk.END,data)
    

 



def black_theme():
    
   
    
    #root.config(bg="black")
    text1.config(bg="black",fg="white")
    file_menu.config(bg="black",fg="white")
    theme.config(bg="black",fg="white")
    #Size.config(bg="black",fg="white")
    #Font.config(bg="black",fg="white")
    transparency.config(bg="black",fg="white")
    
    
    
def white_clicked():
    #root.config(bg="white")
    text1.config(bg="white",fg="black")
    file_menu.config(bg="white",fg="black")
    theme.config(bg="white",fg="black")
    #Size.config(bg="White",fg="black")
    #Font.config(bg="white",fg="black")
    transparency.config(bg="white",fg="black")

def grey_clicked():
    #root.config(bg="grey")
    
    text1.config(bg="grey",fg="white")
    file_menu.config(bg="grey",fg="white")
    theme.config(bg="grey",fg="white")
    #Size.config(bg="grey",fg="white")
    #Font.config(bg="grey",fg="white")
    transparency.config(bg="grey",fg="white")
    

    
def Mid_Transparent():
    root.attributes('-alpha',0.5)
    #menubar.attributes('-alpha',0.5)
    #file_menu.config('-alpha',0.5)

def No_Transparent():
    root.attributes('-alpha',1)
    

def Low_Transparent():
    root.attributes('-alpha',0.3)


def close():
      ret = tk.messagebox.askyesno("Colored Notepad", "Do you want to close this application?" )
      if(ret==True):
          root.destroy()
 

   

def Fix_Screen():
    check=tk.messagebox.askyesno("Resizability","Do You Want to Fix the Notepad Size ?")
    if(check==True):
        root.resizable(False,False)


def Not_fix_screen():
    check=tk.messagebox.askyesno("Resizability","Do You Want  to Resizable the Notepad Size ?")
    if(check==True):
        root.resizable(True,True)

    

    
 
    
 
    


menubar=tk.Menu(root)
root.config(menu=menubar)



file_menu=tk.Menu(menubar)

transparency=tk.Menu(menubar)
theme=tk.Menu(menubar)
other=tk.Menu(menubar)





menubar.add_cascade(menu=file_menu,label="File")
menubar.add_cascade(menu=theme,label="Theme")
menubar.add_cascade(menu=transparency,label="Transparency")
menubar.add_cascade(menu=other,label="Other")


#menubar.add_cascade(menu=Font,label="Font")




file_menu.add_command(label="New",command=new_clicked)
file_menu.add_command(label="Open",command=open_clicked)
file_menu.add_command(label="Save",command=save_clicked)



theme.add_command(label="Black",command=black_theme)
theme.add_command(label="Grey",command=grey_clicked)
theme.add_command(label="White",command=white_clicked)


transparency.add_command(label="Mid-Transparent",command=Mid_Transparent)
transparency.add_command(label="No-Transparent",command=No_Transparent)
transparency.add_command(label="Low-Transparent",command=Low_Transparent)
#transparency.add_cascade(menu=transparency,label="Advanced")

file_menu.add_separator()

file_menu.add_command(label="Exit",command=close)



# RESIZABLE FUNCTIONS

Resizability=tk.Menu(other)


v1=tk.StringVar()


lbl132=tk.Label(root,text="Title")
lbl132.place(x=100,y=880)

ent1=tk.Entry(root,textvariable=v1)
ent1.place(x=100,y=900)



other.add_cascade(menu=Resizability,label="Resizability")
Resizability.add_command(label="Not Resizable",command=Fix_Screen)
Resizability.add_command(label="Resizable",command=Not_fix_screen)


title=tk.StringVar()

def save_at_server():
    """
    newroot=tk.Tk()
    lbl1=tk.Label(newroot,text="Title")
    v11=tk.StringVar()
    ent1=tk.Entry(newroot,textvariable=v11)
    ent1.place(x=80,y=40)
    
    lbl1.place(x=40,y=40)
    
    newroot.config(width=300,height=100)
    """
    import pyodbc

    con = pyodbc.connect("driver={SQL Server};Server=Sanju;database=notepad;uid=sa;pwd=5911")

    cur = con.cursor()
    
    a = text1.get("1.0", tk.END)
    
    
    #title=v11.get()
    
    #print(title)
    
    #if(len(a)==0):
      #  tk.messagebox.showwarning("about notepad","empty")
    print(v1.get())
    abc=v1.get()
    
    
    
    if(len(abc)==0):
        tk.messagebox.showwarning("title","please enter title to save at server")
    cur.execute("Insert into notepad values(?,?)",abc,a)
    con.commit()
    print("Record added")
   # print(v11.get())
        #print(title12)
        
    #btn1=tk.Button(newroot,text="Save")
    #btn1.place(x=40,y=60)
    
   
    
   
    

    
    #newroot.mainloop()

#print(title)
other.add_command(label="Save at Server",command=save_at_server)





def zoom(size):
    font1.configure(size=size)

zoom_scale = tk.Scale(root, orient='vertical', from_=1, to=400)
zoom_scale.config(command=zoom)
#text1 = tk.Text(root, font=font)

zoom_scale.pack(fill='y', side='right')

#text = tk.Text(root, font=font)

#zoom_scale.pack(fill='y', side='right')
#text1.pack(side="left", fill="both", expand=True)

#zoom_scale.set(10)


font1 = Font(family="Courier", size=10)
text1 = ScrolledText(root,width=100,height=400,font=font1)
#text1.pack(padx=5, pady =5)
text1.pack(side="left", expand=True)





sec = tk.StringVar()
ent1=tk.Entry(root, textvariable=sec, width = 2, font = 'Helvetica 14')
ent1.place(x=1850, y=850)
sec.set('00')
lbl3=tk.Label(root,text="Sec")
lbl3.place(x=1850,y=880)
mins= tk.StringVar()
ent2=tk.Entry(root, textvariable = mins, width =2, font = 'Helvetica 14')
ent2.place(x=1810, y=850)
mins.set('00')
lbl4=tk.Label(root,text="Min")
lbl4.place(x=1810,y=880)
hrs= tk.StringVar()
ent3=tk.Entry(root, textvariable = hrs, width =2, font = 'Helvetica 14')
ent3.place(x=1770, y=850)
lbl4=tk.Label(root,text="Hrs")
lbl4.place(x=1770,y=880)
hrs.set('00')
#Define the function for the timer



def countdowntimer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   #text1.config(state='normal')
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      #Update the time
      root.update()
      
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
         tk.messagebox.showinfo("", "Time's Up")
         text1.configure(state='disabled')
      times -= 1
lbl1=tk.Label(root, font =('Helvetica bold',20), text = 'Set the Timer',bg='burlywood1')
lbl1.place(x=1710,y=810)
btn1=tk.Button(root, text='START', bd ='2', bg = 'IndianRed1',font =('Helveticabold',10), command = countdowntimer)
btn1.place(x=1800, y=910)












root.mainloop()


