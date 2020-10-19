from tkinter import *
from matplotlib import pyplot as plt
window=Tk()
window.title("function plotter")
window.geometry("400x200")
def plot():
    v1=a.get()
    v2=int(b.get())
    v3=int(c.get())
    steps=(v2-v3)/1000
    

    coun1=0
    z=v3
    x_axis=[v3]
    while coun1<1000:
        z += steps
        x_axis.append(z)

        coun1+=1

    #lb7 = Label(window, text="max or min value is not correct").place(x=20, y=150)
    h=len(v1)
    coun2=0
    while coun2<h:
        if v1[coun2]=="^":
           p =int(v1[coun2+1])

           w=v1[coun2-1:coun2+2]
           coun3=0
           d="1"
           while coun3<p:
               d+="*x"
               coun3+=1

           v4=v1.replace(w,d)



        coun2+=1

    y_axis=[]
    for var in x_axis:

        x=var
        m=v1.count("^")
        if m==0:
            v=v1
        else:
            v=v4
        s=eval(v)
        y_axis.append(s)

    plt.plot(x_axis,y_axis)
    plt.show()


a=StringVar()
b=StringVar()
c=StringVar()
lb0=Label(window,text="fun(x)").place(x=20,y=20)
lb1=Label(window,text="=").place(x=55,y=20)
lb2=Label(window,text="max").place(x=20,y=40)
lb3=Label(window,text="=").place(x=55,y=40)
lb4=Label(window,text="min").place(x=20,y=60)
lb5=Label(window,text="=").place(x=55,y=60)
lb7=Label(window,text="please enter function with variable x").place(x=20,y=150)
btn=Button(window,text="plot",fg="blue",bg="green",width=20,command=plot).place(x=100,y=100)
fun=Entry(window,textvariable=a,width=40).place(x=70,y=20)
max_f=Entry(window,textvariable=b,width=40).place(x=70,y=40)
min_f=Entry(window,textvariable=c,width=40).place(x=70,y=60)

window.mainloop()

