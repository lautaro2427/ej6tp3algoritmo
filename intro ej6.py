ckm=float(input("cantidad de km que desea recorrer"))

precio=50

if ckm>=10:
    precio=50+15*ckm
    
else:
    if ckm<10:
        precio=50+20*ckm
print("el precio a pagar es de",precio)            
