# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:45:42 2022

@author: William_W
"""
# use auto-py-to-exe to make into an executable file

global x
global y
import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
import shutil
import math
import numpy as np
import matplotlib.pyplot as plt
from stats.basefunc.xsum import *
from stats.univar import *
from stats.bivar import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#functions

#frame1
def movedata(root,SrcInput):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    src=SrcInput.get()
    src = src.replace("\x0c", "\\f")
    shutil.copy(src,dir_path + r'\data')
    
def importdata(root,Input):
    global x
    global y
    filename=Input.get()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv (r''+dir_path+'\data'+filename+'.csv')   #read the csv file 
    namex=df.columns[0]
    namey=df.columns[1]
    x=df[namex].tolist()
    y=df[namey].tolist()

#frame2
class Table:
     
    def __init__(self,tab):
        # code for creating table
        for i in range(len(x)):
                self.e = ttk.Label(tab,text=i+1)
                self.e.grid(row=i+4, column=1,padx=5,pady=5)
        for i in range(len(x)):
                self.e = ttk.Label(tab,text='%s' % float('%.4g' % x[i]))                 
                self.e.grid(row=i+4, column=2,padx=5,pady=5)
        for i in range(len(y)):                
                self.e = ttk.Label(tab,text='%s' % float('%.4g' % y[i]))                
                self.e.grid(row=i+4, column=3,padx=5,pady=5)      
                
def update2():
    for widgets in frame2.winfo_children():
        widgets.destroy()
    indexlabel = ttk.Label(frame2,text="Index")                 
    indexlabel.grid(row=3, column=1,padx=5,pady=5)
    xlabel = ttk.Label(frame2,text="X Data")                 
    xlabel.grid(row=3, column=2,padx=5,pady=5)
    ylabel = ttk.Label(frame2,text="Y Data")                 
    ylabel.grid(row=3, column=3,padx=5,pady=5)
    sep1=ttk.Separator(frame2,orient="horizontal")
    sep1.grid(column=0,row=3,columnspan=4,sticky='wes')
    t=Table(frame2)
    sepx=ttk.Separator(frame2,orient="vertical")
    sepx.grid(column=1,row=4,rowspan=len(x),sticky='nse')
    sepy=ttk.Separator(frame2,orient="vertical")
    sepy.grid(column=2,row=4,rowspan=len(x),sticky='nse')
    
#frame3
def update3():
    size3.config(text='n='+str(len(x)))
    xmean_val.config(text='%s' % float('%.4g' % mean(x)))
    ymean_val.config(text='%s' % float('%.4g' % mean(y)))
    xsstddev_val.config(text='%s' % float('%.4g' % Sstddev(x)))
    ysstddev_val.config(text='%s' % float('%.4g' % Sstddev(y)))
    xpstddev_val.config(text='%s' % float('%.4g' % Pstddev(x)))
    ypstddev_val.config(text='%s' % float('%.4g' % Pstddev(y)))
    xmedian_val.config(text='%s' % float('%.4g' % median(x)))
    ymedian_val.config(text='%s' % float('%.4g' % median(y)))
    xmode_val.config(text= mode(x))
    ymode_val.config(text=mode(y))
    xrange_val.config(text='%s' % float('%.4g' % srange(x)))
    yrange_val.config(text='%s' % float('%.4g' % srange(y)))
    
#frame4
def update4():
    logx=x[:]
    logy=y[:]
    invx=x[:]
    for i in range(len(x)):
        logx[i]=math.log10(x[i])
        logy[i]=math.log10(y[i])
        invx[i]=1/x[i]
    size4.config(text='n='+str(len(x)))
    s_rank_val.config(text='%s' % float('%.4g' % spearmans(x,y)))
    p_rank_val.config(text='%s' % float('%.4g' % pearsons(x,y)))
    grad_val.config(text='%s' % float('%.4g' % gradient(x,y)))
    int_val.config(text='%s' % float('%.4g' % intercept(x,y)))
    pp_rank_val.config(text='%s' % float('%.4g' % pearsons(logx,logy)))
    pgrad_val.config(text='%s' % float('%.4g' % gradient(logx,logy)))
    pint_val.config(text='%s' % float('%.4g' % intercept(logx,logy)))
    ep_rank_val.config(text='%s' % float('%.4g' % pearsons(x,logy)))
    egrad_val.config(text='%s' % float('%.4g' % gradient(x,logy)))
    eint_val.config(text='%s' % float('%.4g' % intercept(x,logy)))  
    ep_rank_val2.config(text='%s' % float('%.4g' % pearsons(invx,logy)))
    egrad_val2.config(text='%s' % float('%.4g' % gradient(invx,logy)))
    eint_val2.config(text='%s' % float('%.4g' % intercept(invx,logy))) 
    
#frame5
def update5():
    size5.config(text='n='+str(len(x)))
    
#frame6
def update6():
    size6.config(text='n='+str(len(x)))
    
#frame7
def scatter():
    fig=plt.Figure(figsize=(6,4))
    ax=fig.add_axes([0.15,0.15,0.75,0.75])
    ax.scatter(x, y, color='r',label="Data Points")
    ax.set_title(titlelbl.get())
    ax.set_xlabel(xlbl.get(),fontsize=14)
    ax.set_ylabel(ylbl.get(),fontsize=14)
    chart_type = FigureCanvasTkAgg(fig,frame7)
    chart_type.get_tk_widget().grid(column=1,columnspan=5,row=1,rowspan=10,padx=5,pady=5)
    logx=x[:]
    logy=y[:]
    invx=x[:]
    for i in range(len(x)):
        logx[i]=math.log10(x[i])
        logy[i]=math.log10(y[i])
        invx[i]=1/x[i]
    xfit=np.linspace(min(x), max(x))
    plots=linearplot.get()+powerplot.get()+expplot.get()+exp2plot.get()
    if linearplot.get()==1:
        yfit=xfit*gradient(x,y)+intercept(x,y)
        ax.plot(xfit,yfit,label="Linear Fit")
        if plots==1:
            ax.text(0.4*(max(x)-min(x))+min(x),0.9*(max(y+yfit.tolist())-min(y+yfit.tolist()))+min(y+yfit.tolist()),"R^2="+str("{:.3f}".format(pearsons(x,y)**2)))
    if powerplot.get()==1:
        yfit=yfit=(xfit**gradient(logx,logy))*(10**(intercept(logx,logy)))
        ax.plot(xfit,yfit,label="Power Law Fit")
        if plots==1:
            ax.text(0.4*max(x),0.9*max(y+yfit.tolist()),"R^2="+str("{:.3f}".format(pearsons(logx,logy)**2)))
    if expplot.get()==1:
        yfit=10**(intercept(x,logy))*10**(xfit*gradient(x,logy))
        ax.plot(xfit,yfit,label="Exponential Fit")
        if plots==1:
            ax.text(0.4*max(x),0.9*max(y+yfit.tolist()),"R^2="+str("{:.3f}".format(pearsons(x,logy)**2)))
    if exp2plot.get()==1:
        yfit=10**(gradient(invx,logy)/xfit)*10**(intercept(invx,logy))
        ax.plot(xfit,yfit,label="Exponential of Inverse X Fit")
        if plots==1:
            ax.text(0.4*max(x),0.9*max(y+yfit.tolist()),"R^2="+str("{:.3f}".format(pearsons(invx,logy)**2)))
    
    if legendcorner.get() != "None" or '':
        ax.legend(loc=legendcorner.get())  
    if plotsave.get()==1:
        fig.savefig(r'.\graph\ '+name.get()+'.jpg',bbox_inches='tight',dpi=150)
    plt.show()
    
def reset():
    if str(frame7.winfo_children()[len(frame7.winfo_children())-2]) == ".!notebook.!frame7.!button2":
        frame7.winfo_children()[len(frame7.winfo_children())-1].destroy()

def update():
    
    update2()
    update3()
    update4()
    update5()
    update6()    
    
def importdata(root,Input):
    global x
    global y
    filename=Input.get()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv (r''+dir_path+'\data'+filename+'.csv')   #read the csv file 
    namex=df.columns[0]
    namey=df.columns[1]
    x=df[namex].tolist()
    y=df[namey].tolist()
    update()
    



    
# root window
root = tk.Tk()
root.geometry('500x500')
root.title('Statistics')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
# create a notebook
notebook = ttk.Notebook(root)
notebook.grid(pady=10)

# create frames
frame1 = ttk.Frame(notebook, width=500, height=500)
frame2 = ttk.Frame(notebook, width=500, height=500)
frame3 = ttk.Frame(notebook, width=800, height=500)
frame4 = ttk.Frame(notebook, width=500, height=500)
frame5 = ttk.Frame(notebook, width=500, height=500)
frame6 = ttk.Frame(notebook, width=500, height=500)
frame7 = ttk.Frame(notebook, width=500, height=500)

frame1.grid()
frame2.grid()
frame3.grid()
frame4.grid()
frame5.grid()
frame6.grid()
frame7.grid()

# add frames to notebook
notebook.add(frame1, text='Import')
notebook.add(frame2, text='Data')
notebook.add(frame3, text='Univariate')
notebook.add(frame4, text='CorrelTests')
notebook.add(frame5, text='UniProbTests')
notebook.add(frame6, text='Bivariate')
notebook.add(frame7, text='Graphics')

#frame1
Srclabel=ttk.Label(frame1,text=r'input"C:\dir\filename.csv"')
Srclabel.grid(column=1,row=1,columnspan=2,padx=5,pady=5)
SrcInput=ttk.Entry(frame1)
SrcInput.grid(column=3,row=1,padx=5,pady=5)
SrcImport=ttk.Button(frame1,text="Move Data",command=lambda: movedata(frame1, SrcInput))
SrcImport.grid(column=4,row=1,padx=5,pady=5)
label=ttk.Label(frame1,text=r'input"\filename"')
label.grid(column=1,row=3,columnspan=2,padx=5,pady=5)
Input=ttk.Entry(frame1)
Input.grid(column=3,row=3,padx=5,pady=5)
Import=ttk.Button(frame1,text="Import Data",command=lambda: importdata(frame1,Input))
Import.grid(column=4,row=3,padx=5,pady=5)
Quit = ttk.Button(frame1, text='Quit',command=root.destroy)
Quit.grid(column=3,padx=5,pady=5)
                 

#frame2

#frame3
size3=ttk.Label(frame3,text='n= ...')
size3.grid(column=1,row=1,padx=5,pady=5)
xmean=ttk.Label(frame3,text='X Mean')
xmean.grid(column=1,row=2,padx=5,pady=5)
xmean_val=ttk.Label(frame3,text='...')
xmean_val.grid(column=2,row=2,padx=5,pady=5)
ymean=ttk.Label(frame3,text='Y Mean')
ymean.grid(column=3,row=2,padx=5,pady=5)
ymean_val=ttk.Label(frame3,text='...')
ymean_val.grid(column=4,row=2,padx=5,pady=5)
xsstddev=ttk.Label(frame3,text='X Sample StdDev')
xsstddev.grid(column=1,row=3,padx=5,pady=5)
xsstddev_val=ttk.Label(frame3,text='...')
xsstddev_val.grid(column=2,row=3,padx=5,pady=5)
ysstddev=ttk.Label(frame3,text='Y Sample StdDev')
ysstddev.grid(column=3,row=3,padx=5,pady=5)
ysstddev_val=ttk.Label(frame3,text='...')
ysstddev_val.grid(column=4,row=3,padx=5,pady=5)
xpstddev=ttk.Label(frame3,text='X Population StdDev')
xpstddev.grid(column=1,row=4,padx=5,pady=5)
xpstddev_val=ttk.Label(frame3,text='...')
xpstddev_val.grid(column=2,row=4,padx=5,pady=5)
ypstddev=ttk.Label(frame3,text='Y Population StdDev')
ypstddev.grid(column=3,row=4,padx=5,pady=5)
ypstddev_val=ttk.Label(frame3,text='...')
ypstddev_val.grid(column=4,row=4,padx=5,pady=5)
xmedian=ttk.Label(frame3,text='X Median')
xmedian.grid(column=1,row=5,padx=5,pady=5)
xmedian_val=ttk.Label(frame3,text='...')
xmedian_val.grid(column=2,row=5,padx=5,pady=5)
ymedian=ttk.Label(frame3,text='Y Median')
ymedian.grid(column=3,row=5,padx=5,pady=5)
ymedian_val=ttk.Label(frame3,text='...')
ymedian_val.grid(column=4,row=5,padx=5,pady=5)
xmode=ttk.Label(frame3,text='X Mode')
xmode.grid(column=1,row=6,padx=5,pady=5)
xmode_val=ttk.Label(frame3,text='...')
xmode_val.grid(column=2,row=6,padx=5,pady=5)
ymode=ttk.Label(frame3,text='Y Mode')
ymode.grid(column=3,row=6,padx=5,pady=5)
ymode_val=ttk.Label(frame3,text='...')
ymode_val.grid(column=4,row=6,padx=5,pady=5)
xrange=ttk.Label(frame3,text='X Range')
xrange.grid(column=1,row=7,padx=5,pady=5)
xrange_val=ttk.Label(frame3,text='...')
xrange_val.grid(column=2,row=7,padx=5,pady=5)
yrange=ttk.Label(frame3,text='Y Range')
yrange.grid(column=3,row=7,padx=5,pady=5)
yrange_val=ttk.Label(frame3,text='...')
yrange_val.grid(column=4,row=7,padx=5,pady=5)


#frame4
size4=ttk.Label(frame4,text='n= ...')
size4.grid(column=1,row=1,padx=5,pady=5)
corr=ttk.Label(frame4,text="Correlation Tests:",font=('Arial',9,'bold','underline'))
corr.grid(column=1,row=2,columnspan=2,padx=5,pady=5)
spearmansrank=ttk.Label(frame4,text="Spearmans Rank:")
spearmansrank.grid(column=1,row=3,padx=5,pady=5)
s_rank_val=ttk.Label(frame4,text='...')
s_rank_val.grid(column=2,row=3,padx=5,pady=5)
#linear tests
linear=ttk.Label(frame4,text="Linear Relationship Tests: Y=BX+A",font=('Arial',9,'bold','underline'))
linear.grid(column=1,row=4,columnspan=2,padx=5,pady=5)
pearsonsrank=ttk.Label(frame4,text="Pearsons Rank:")
pearsonsrank.grid(column=1,row=5,padx=5,pady=5)
p_rank_val=ttk.Label(frame4,text='...')
p_rank_val.grid(column=2,row=5,padx=5,pady=5)
grad=ttk.Label(frame4,text="Gradient(B):")
grad.grid(column=1,row=6,padx=5,pady=5)
grad_val=ttk.Label(frame4,text='...')
grad_val.grid(column=2,row=6,padx=5,pady=5)
inter=ttk.Label(frame4,text="Intercept(A):")
inter.grid(column=3,row=6,padx=5,pady=5)
int_val=ttk.Label(frame4,text='...')
int_val.grid(column=4,row=6,padx=5,pady=5)
#power tests
power=ttk.Label(frame4,text="Power Relationship Tests: Y=A*X^(B)",font=('Arial',9,'bold','underline'))
power.grid(column=1,row=7,columnspan=2,padx=5,pady=5)
ppearsonsrank=ttk.Label(frame4,text=r"Pearsons Rank of Log X/Log Y:")
ppearsonsrank.grid(column=1,row=8,padx=5,pady=5)
pp_rank_val=ttk.Label(frame4,text='...')
pp_rank_val.grid(column=2,row=8,padx=5,pady=5)
pgrad=ttk.Label(frame4,text="Power(B):")
pgrad.grid(column=1,row=9,padx=5,pady=5)
pgrad_val=ttk.Label(frame4,text='...')
pgrad_val.grid(column=2,row=9,padx=5,pady=5)
pinter=ttk.Label(frame4,text="Coefficient(A):")
pinter.grid(column=3,row=9,padx=5,pady=5)
pint_val=ttk.Label(frame4,text='...')
pint_val.grid(column=4,row=9,padx=5,pady=5)
#exponential tests
exp=ttk.Label(frame4,text="Exponential Relationship Tests: Y=A*10^(BX)",font=('Arial',9,'bold','underline'))
exp.grid(column=1,row=10,columnspan=2,padx=5,pady=5)
epearsonsrank=ttk.Label(frame4,text=r"Pearsons Rank of X/Log Y:")
epearsonsrank.grid(column=1,row=11,padx=5,pady=5)
ep_rank_val=ttk.Label(frame4,text='...')
ep_rank_val.grid(column=2,row=11,padx=5,pady=5)
egrad=ttk.Label(frame4,text="X Coefficient(B):")
egrad.grid(column=1,row=12,padx=5,pady=5)
egrad_val=ttk.Label(frame4,text='...')
egrad_val.grid(column=2,row=12,padx=5,pady=5)
einter=ttk.Label(frame4,text="Coefficient(A):")
einter.grid(column=3,row=12,padx=5,pady=5)
eint_val=ttk.Label(frame4,text='...')
eint_val.grid(column=4,row=12,padx=5,pady=5)
#exponential2 tests
exp2=ttk.Label(frame4,text="Exponential2 Relationship Tests: Y=A*10^(B/X)",font=('Arial',9,'bold','underline'))
exp2.grid(column=1,row=13,columnspan=2,padx=5,pady=5)
epearsonsrank2=ttk.Label(frame4,text=r"Pearsons Rank of (1/X)/Log Y:")
epearsonsrank2.grid(column=1,row=14,padx=5,pady=5)
ep_rank_val2=ttk.Label(frame4,text='...')
ep_rank_val2.grid(column=2,row=14,padx=5,pady=5)
egrad2=ttk.Label(frame4,text="1/X Coefficient(B):")
egrad2.grid(column=1,row=15,padx=5,pady=5)
egrad_val2=ttk.Label(frame4,text='...')
egrad_val2.grid(column=2,row=15,padx=5,pady=5)
einter2=ttk.Label(frame4,text="Coefficient(A):")
einter2.grid(column=3,row=15,padx=5,pady=5)
eint_val2=ttk.Label(frame4,text='...')
eint_val2.grid(column=4,row=15,padx=5,pady=5)

#frame5
size5=ttk.Label(frame5,text='n= ...')
size5.grid(column=1,row=1,padx=5,pady=5)


#frame6

size6=ttk.Label(frame6,text='n= ...')
size6.grid(column=1,row=1,padx=5,pady=5)

#frame7

titlelbll=ttk.Label(frame7,text="Title:",font=('Arial',8,'bold','underline'))
titlelbll.grid(column=1,row=1,padx=5,pady=5)
titlelbl=ttk.Entry(frame7)
titlelbl.grid(column=2,row=1,padx=5,pady=5)
xlbll=ttk.Label(frame7,text="Xlabel:",font=('Arial',8,'bold','underline'))
xlbll.grid(column=1,row=2,padx=5,pady=5)
xlbl=ttk.Entry(frame7)
xlbl.grid(column=2,row=2,padx=5,pady=5)
ylbll=ttk.Label(frame7,text="Ylabel:",font=('Arial',8,'bold','underline'))
ylbll.grid(column=1,row=3,padx=5,pady=5)
ylbl=ttk.Entry(frame7)
ylbl.grid(column=2,row=3,padx=5,pady=5)
bestfitlbl=ttk.Label(frame7,text="Best Fit Curves",font=('Arial',8,'bold','underline'))
bestfitlbl.grid(column=1,row=4,columnspan=2,padx=5,pady=5)
linearplot=tk.IntVar()
linearcheck=ttk.Checkbutton(frame7,text="Linear",variable=linearplot)
linearcheck.grid(column=1,row=5,padx=5,pady=5)
powerplot=tk.IntVar()
powercheck=ttk.Checkbutton(frame7,text="Power Law",variable=powerplot)
powercheck.grid(column=2,row=5,padx=5,pady=5)
expplot=tk.IntVar()
expcheck=ttk.Checkbutton(frame7,text="Exponential",variable=expplot)
expcheck.grid(column=1,row=6,padx=5,pady=5)
exp2plot=tk.IntVar()
exp2check=ttk.Checkbutton(frame7,text="Exponential Inverse",variable=exp2plot)
exp2check.grid(column=2,row=6,padx=5,pady=5)
legendcornerlbl=ttk.Label(frame7,text="Legend Corner:",font=('Arial',8,'bold','underline'))
legendcornerlbl.grid(column=3,row=4,padx=5,pady=5)
legendcorner=ttk.Combobox(frame7,values=("None","upper right","upper left","lower right","lower left"))
legendcorner.grid(column=3,row=5,padx=5,pady=5)
plotsave=tk.IntVar()
saveplotcheck=ttk.Checkbutton(frame7,text="Save Plot?",variable=plotsave)
saveplotcheck.grid(column=3,row=1,padx=5,pady=5)
namelbl=ttk.Label(frame7,text="Filename:")
namelbl.grid(column=3,row=2,padx=5,pady=5)
name=ttk.Entry(frame7)
name.grid(column=3,row=3,padx=5,pady=5)
sep2=ttk.Separator(frame7,orient="vertical")
sep2.grid(column=2,row=0,rowspan=7,sticky='nse')
sep3=ttk.Separator(frame7,orient="horizontal")
sep3.grid(column=0,row=3,columnspan=4,sticky='wes')
sep4=ttk.Separator(frame7,orient="horizontal")
sep4.grid(column=0,row=6,columnspan=4,sticky='wes')
sep5=ttk.Separator(frame7,orient="vertical")
sep5.grid(column=4,row=0,rowspan=7,sticky='nse')
create7=ttk.Button(frame7,text="Create Scatter Graph",command=scatter)
create7.grid(column=1,row=7,columnspan=2,padx=5,pady=5)
cleanbutton=ttk.Button(frame7,text="Reset",command=reset)
cleanbutton.grid(column=1,row=8,columnspan=2,padx=5,pady=5)



root.mainloop()