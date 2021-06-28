import pandas as pd
import numpy as np
model_1=pd.read_pickle("car_v1")
model_2=pd.read_pickle("car_v2")
model_3=pd.read_pickle("car_v3")

from tkinter import *
a=Tk()
a.geometry("500x500")

entryText1=IntVar()
entryText2=IntVar()
entryText3=IntVar()
entryText4=IntVar()
entryText5=IntVar()
entryText6=IntVar()
                                    
   
label=Label(a)
def selection():
    c=radio.get()
    selection="Your selection choice is "+str(radio.get())
    label.config(text=selection)
    if(c==1 or c==2):
        
        l=Label(a,text="Year").place(x=20,y=120)
        e1=Entry(a,textvariable=entryText1).place(x=190,y=120)
        l2=Label(a,text="transmission").place(x=20,y=150)
        e2=Entry(a,textvariable=entryText2).place(x=190,y=150)
        l3=Label(a,text="mileage").place(x=20,y=180)
        e3=Entry(a,textvariable=entryText3).place(x=190,y=180)
        l4=Label(a,text="tax").place(x=20,y=210)
        e4=Entry(a,textvariable=entryText4).place(x=190,y=210)
        l5=Label(a,text="mpg").place(x=20,y=240)
        e5=Entry(a,textvariable=entryText5).place(x=190,y=240)
        l6=Label(a,text="engineSize").place(x=20,y=270)
        e6=Entry(a,textvariable=entryText6).place(x=190,y=270)
        b=Button(a,text="submit",bg="green",fg="white",command=func).place(x=20,y=300)
        lbl.place(x=20,y=330)
    elif(c==3):
        

        l=Label(a,text="Year").place(x=20,y=120)
        e1=Entry(a,textvariable=entryText1).place(x=190,y=120)
        l2=Label(a,text="transmission").place(x=20,y=150)
        e2=Entry(a,textvariable=entryText2).place(x=190,y=150)
        l3=Label(a,text="mileage").place(x=20,y=180)
        e3=Entry(a,textvariable=entryText3).place(x=190,y=180)
        l4=Label(a,text="tax").place(x=20,y=210)
        e4=Entry(a,textvariable=entryText4).place(x=190,y=210)
        b=Button(a,text="submit",bg="green",fg="white",command=func).place(x=20,y=240)
        lbl.place(x=20,y=270)




lbl=Label(a)
def func():
    
    o=radio.get()
    if(o==1):
        x=entryText1.get()
        y=entryText2.get()
        z=entryText3.get()
        t=entryText4.get()
        u=entryText5.get()
        n=entryText6.get()
        k=np.array([x,y,z,t,u,n]).reshape((1,6))
        d=pd.DataFrame(k,columns=['year', 'transmission', 'mileage','tax', 'mpg','engineSize'])
        p=model_1.predict(d)
        j=p[0][0]
        r="Predicted price of selected model is "+str(j)
        lbl.config(text=r)
    elif(o==2):
        x=entryText1.get()
        y=entryText2.get()
        z=entryText3.get()
        t=entryText4.get()
        u=entryText5.get()
        n=entryText6.get()
        k=np.array([x,y,z,t,u,n]).reshape((1,6))
        d=pd.DataFrame(k,columns=['year', 'transmission', 'mileage','tax', 'mpg','engineSize'])
        p=model_2.predict(d)
        j=p[0][0]
        r="Predicted price of selected model is "+str(j)
        lbl.config(text=r)
    elif(o==3):
        x=entryText1.get()
        y=entryText2.get()
        z=entryText3.get()
        t=entryText4.get()
        k=np.array([x,y,z,t]).reshape((1,4))
        d=pd.DataFrame(k,columns=['year', 'transmission', 'mileage','engineSize'])
        p=model_3.predict(d)
        j=p[0][0]
        r="Predicted price of selected model is "+str(j)
        lbl.config(text=r)
       
    
    
radio=IntVar()
l=Label(a,text="The different car companies are given below.Click any one to predict its price.").pack()
r1=Radiobutton(a,text="Audi",variable=radio,value=1,command=selection).pack()
r2=Radiobutton(a,text="Bmw",variable=radio,value=2,command=selection).pack()
r3=Radiobutton(a,text="Cclass",variable=radio,value=3,command=selection).pack()



label.pack()
a.mainloop()
    
