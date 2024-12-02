#Kood on mõeldud sammukeerukuse mõõtmiseks
import time
import math

def HüppeOtsing(massiiv, otsing):
    start = time.time()
    l = 0
    hüpe = round(math.sqrt(len(massiiv)))

    for i in range(0, len(massiiv)-1, hüpe):
        l = l+1
        if massiiv[i] > otsing:
            break
        if massiiv[i] == otsing:
            end = time.time()
            return end-start
            return l
            return i 
        else:
            i = i + hüpe

    otsingu_lõpp = massiiv[i-hüpe:i]
    for k in otsingu_lõpp:
        l=l+1
        if k == otsing:
            end = time.time()
            return end-start
            return l
            return k+i+hüpe


mass = range(1, 100000)

z = 0
for t in mass:
    z = z + HüppeOtsing(mass, t)
vastus = (z)
print(round(vastus, 3))

#kasutades iteratsiionde mõõtmise viisi, siis oli Jump Search Linear Searchist
#selle dataseti näol pea 2 korda aeglasem, seega on peaagu alati parem, kui Lin Search.
#samas ei suuda ma välja mõelda pea ühtegi võimalikku kasutust, kus oleks mõtekam kasutada
#Jump Searchi