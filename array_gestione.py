import numpy as np
import random


#lista=[0, 0, 0]
#vettore=np.array(lista)
#print(vettore)

#altro modo
#vettore =np.zeros(3)
#print(vettore)

def crea_vettore(dimensione) -> np.ndarray:
    vettore = np.zeros(dimensione)
    return vettore
vettore = crea_vettore(3)
print(vettore)

def inserisci_elemento(vettore: np.ndarray, elemento: int, posizione: int ) -> np.ndarray:
    
    vettore[posizione]=elemento
    return vettore

elemento=3
posizione=1

inserisci_elemento(vettore, elemento, posizione )
print(vettore)


for i in range(3):
    elemento=random.randint(1,10)
    vettore_aggiornato=inserisci_elemento(vettore, elemento, posizione)
    print(vettore)

#trova il minimo del vettore
def trova_minimo(vettore: np.ndarray)-> int:
    minimo=vettore[0]
    posizione_minimo=0
    for i in range(len(vettore)):
        if vettore[i] <minimo:
            minimo=vettore[i]
            posizione_minimo=i
    return minimo
print(trova_minimo(vettore))


#da finire
