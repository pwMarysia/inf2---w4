import math
import tkinter as tk
a=0 
def GCTJD(okno_rodzic,e1,e2,e3,e4,e5,e6):
  okno=tk.Toplevel(okno_rodzic)
  okno.title('wynik')
  R=int(e1.get())
  M=int(e2.get())
  D=int(e3.get())
  G=int(e4.get())
  m=int(e5.get())
  S=int(e6.get())
  JDN=math.floor((1461*(R+4800+(M-14)/12))/4+(367*(M-2-12*((M-14)/12)))/12-(3*((R+4900+(M-14)/12)/100))/4+D-32075)
  FJD=JDN+(G-12)/24+m/1440+S/86400
  tk.Label(okno, text=FJD).pack()
  
  
def GCTMJD(okno_rodzic,h1,h2,h3,h4,h5,h6):
  okno=tk.Toplevel(okno_rodzic)
  okno.title('wynik')
  R=int(e1.get())
  M=int(e2.get())
  D=int(e3.get())
  G=int(e4.get())
  m=int(e5.get())
  S=int(e6.get())
  JDN=math.floor((1461*(R+4800+(M-14)/12))/4+(367*(M-2-12*((M-14)/12)))/12-(3*((R+4900+(M-14)/12)/100))/4+D-32075)
  FJD=JDN+(G-12)/24+m/1440+S/86400
  MJD=FJD-2400000.5
  tk.Label(okno, text=MJD).pack()

def GCTGPS(okno_rodzic,e1,e2,e3,e4,e5,e6):
  okno=tk.Toplevel(okno_rodzic)
  okno.title('wynik')
  R=int(e1.get())
  M=int(e2.get())
  D=int(e3.get())
  G=int(e4.get())
  m=int(e5.get())
  S=int(e6.get())
  JDN=math.floor((1461*(R+4800+(M-14)/12))/4+(367*(M-2-12*((M-14)/12)))/12-(3*((R+4900+(M-14)/12)/100))/4+D-32075)
  FJD=JDN+(G-12)/24+m/1440+S/86400
  WCJ=-(math.floor((1461*(1980+4800+(1-14)/12))/4+(367*(1-2-12*((1-14)/12)))/12-(3*((1980+4900+(1-14)/12)/100))/4+6-32075))+(G-12)/24+m/1440+S/86400+(math.floor((1461*(R+4800+(M-14)/12))/4+(367*(M-2-12*((M-14)/12)))/12-(3*((R+4900+(M-14)/12)/100))/4+D-32075))+(G-12)/24+m/1440+S/86400
  GPSWN=math.ceil(WCJ/7)
  DOY=-(math.floor((1461*((R)+4800+(1-14)/12))/4+(367*(1-2-12*((1-14)/12)))/12-(3*(((R)+4900+(1-14)/12)/100))/4+1-32075))+(0-12)/24+0/1440+0/86400+(math.floor((1461*(R+4800+(M-14)/12))/4+(367*(M-2-12*((M-14)/12)))/12-(3*((R+4900+(M-14)/12)/100))/4+D-32075))+(G-12)/24+m/1440+S/86400
  WOY=math.ceil(DOY/7)
  DOW=(math.floor(FJD+0.5)+0.5+1.5) % 7
  if DOW==1:
    a='niedziela'
  elif DOW==2:
    a='poniedziałek'
  elif DOW==3:
    a='wtorek'
  elif DOW==4:
    a='sroda'
  elif DOW==5:
    a='czwartek'
  elif DOW==6:
    a='piątek'
  else:
    a='sobota'
    
  if a=='sobota':
      SOW=(6*24*3600)+S+m*60+G*3600-24*3600
  else:
      SOW=(DOW*24*3600)+S+m*60+G*3600-24*3600
  SOD=S+m*60+G*3600
  tk.Label(okno, text=GPSWN).pack()
  tk.Label(okno, text=WOY).pack()
  tk.Label(okno, text=a).pack()
  tk.Label(okno, text=SOW).pack()
  tk.Label(okno, text=SOD).pack()
  
  
def JDTGC(okno_rodzic,g1):
  okno=tk.Toplevel(okno_rodzic)
  okno.title('wynik')
  JD=float(g1.get())
  W=JD+0.5
  X=math.floor(W)
  U=W-X
  Y=math.floor((X+32044.5)/36524.25)
  Z=X+Y-math.floor(Y/4)-38
  A=Z+1524
  B=math.floor((A-122.1)/365.25)
  C=A-math.floor(365.25*B)
  E=math.floor(C/30.61)
  F=math.floor(E/14)
  R=B-4716+F
  M=E-1-12*F
  D=C+U-math.floor(153*E/5)
  G=math.floor((D-math.floor(D))*24)
  m=math.floor((G-math.floor(G))*60)
  S=math.floor((m-math.floor(m))*60)
  D=math.floor(D)
  tk.Label(okno, text=R).pack()
  tk.Label(okno, text=M).pack()
  tk.Label(okno, text=D).pack()
  tk.Label(okno, text=G).pack()
  tk.Label(okno, text=m).pack()
  tk.Label(okno, text=S).pack()
# glowne okno
root = tk.Tk() 
 
l1 = tk.Label(root, text="Rok")
e1 = tk.Entry(root, width = 5)
l2 = tk.Label(root, text="Miesiąc")
e2 = tk.Entry(root, width = 5)
l3 = tk.Label(root, text="Dzien")
e3 = tk.Entry(root, width = 5)
l4 = tk.Label(root, text="Godzina")
e4 = tk.Entry(root, width = 5)
l5 = tk.Label(root, text="Minuta")
e5 = tk.Entry(root, width = 5)
l6 = tk.Label(root, text="Sekunda")
e6 = tk.Entry(root, width = 5)
 
f1=tk.Label(root, text="JD")
g1=tk.Entry(root, width=5)


#command = lambda:nowe(root)  - lambda aby podac argument funkcji
b1 = tk.Button(root, text="przelicz na dzień juliański", command =lambda:GCTJD(root,e1,e2,e3,e4,e5,e6))
b2 = tk.Button(root, text="przelicz na datę gregoriańską", command =lambda:JDTGC(root,g1))
b3 = tk.Button(root, text="przelicz na zmodyfikowany dzień juliański", command =lambda:GCTMJD(root,e1,e2,e3,e4,e5,e6))
b4 = tk.Button(root, text="przelicz na czas GPS", command =lambda:GCTGPS(root,e1,e2,e3,e4,e5,e6))
# grid potrzebuje argumentów (wiersz,kolumna)
b1.grid(row=6, column=0)
b2.grid(row=11, column=0)
b3.grid(row=7,column=0)
b4.grid(row=8, column=0)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l3.grid(row=2, column=0)
e3.grid(row=2, column=1)
l4.grid(row=3, column=0)
e4.grid(row=3, column=1)
l5.grid(row=4, column=0)
e5.grid(row=4, column=1)
l6.grid(row=5, column=0)
e6.grid(row=5, column=1)
 
f1.grid(row=10, column=0)
g1.grid(row=10, column=1)

#uruchamia petle wydarzen!
root.mainloop()