
"""
from math import sin, cos,  atan, sqrt, degrees

def decimalDeg2dms(decimalDeg):
    '''
    Metoda przelicza wartość kąta podaną w dziesiętnych stopnia 
    do wartości kata wyrażonej w stopniach, minutach i sekundach
    INPUT:
        decimalDeg [float]: decimal degree (np, 185.209060574544st)
    OUTPUT: 
        (d, m, s) [tuple]: (stopnie, minuty, sekundy) (np.(185st, 12min, 32.62sec))
    '''
    d = int(decimalDeg)
    m = int((decimalDeg - d) * 60)
    s = (decimalDeg - d - m / 60.) * 3600.0
    return (d, m, s) 
 
 
 
 
def dms2decimalDeg(st, minut, sec):
    '''
    Metoda przelicza wartość kąta podaną w w stopniach, minutach i sekundach 
    do wartości kata wyrażonej dziesiętnych stopnia 
    INPUT:
        st    [int]
        minut [int]
        sec     [float]
    OUTPUT: 
        deg    [float] : wartośc kąta w dziesiętnych stopnia
    '''
    deg = st + minut/60 + sec / 3600.
    return deg 
 
 
 
 
if __name__=='__main__':
    '''
     __name__, przechowuje nazwę modułu
    Nazwa modułu może się różnić od sposobu uruchomienia skryptu. 
    W momencie uruchomienia bezpośrednio skryptu (nie z importu), 
    moduł przyjmuje nazwę __main__. 
    '''
    wynik1 = decimalDeg2dms(185.20906057454428) # wynik: (185, 12, 32.618068359413385)
    print('wynik1 z main', wynik1)
 
    wynik2 = dms2decimalDeg(wynik1[0], wynik1[1], wynik1[2])
    print('wynik2 z main', wynik2)
    
def Np(B, a, e2):
    '''Compute East-West Radius of curvature at current position'''
    N = a/(1-e2*(sin(B))**2)**(0.5)
    return N
 
def hirvonen(X, Y, Z, a = 6378137., e2 = 0.00669438002290):
    r  = sqrt(X**2 + Y**2)          # promień
    B  = atan(Z / (r * (1 - e2)))    # pierwsze przyblizenie 
    # 1) pętla for: iteracyjne wyznaczenie B
    B_next = B
  
    i=1
    while i<=20:
        B_prev = B_next
        N  = Np(B_prev, a, e2)
        H  = (r/cos(B_prev))- N
        B_next = atan(Z/(r *(1 - (e2 * (N/(N + H))))))
        B_next = B_next
        i+=1
        if   abs(B_next - B_prev) <(0.0000001/206265): # warunek iteracji(rho'' =206265)
            break
    B = B_prev
    L = atan(Y/X)
    N = Np(B, a, e2)
    H = (r/cos(B))- N
    return degrees(B), degrees(L), H  


Bs=[]; Hs=[]; Ls=[]
a=open('hirv_data.txt','r')
for line in a.readlines()[1:]:
    X, Y, Z = line.split(',')
    B, L, H = hirvonen(float(X), float(Y), float(Z))
    #print('\nB', decimalDeg2dms(B))
    #print('L', decimalDeg2dms(L))
    #print('H', H)
    Bs.append(decimalDeg2dms(B))
    Hs.append(H)
    Ls.append(decimalDeg2dms(L))
a.close()

#zapisywanie do pliku
c=open('hirv_out.txt','a')
c.write(154*'-'+'\n')
c.write('|{:^50}|{:^50}|{:^50}|'.format('szerokosc','dlugosc','wysokosc')+'\n')
c.write(154*'-'+'\n')

degree_sign  ="\u00b0"
for i in range(len(Bs)):
    b="{:.0f}{}{}’{:.2f}’’".format(  Bs[i][0],  degree_sign,  Bs[i][1],  Bs[i][2])
    l="{:.0f}{}{}’{:.2f}’’".format(  Ls[i][0],  degree_sign,  Ls[i][1],  Ls[i][2])
    h="{:.2f} m".format(Hs[i])
    c.write('|{:^50}|{:^50}|{:^50}|'.format(b,l,h)+'\n')
c.write(154*'-'+'\n')
c.close() #zamkinj
