def tabel():
    return [[] for i in range(11)]

def hashi(väärtus):
    indeks = väärtus
    while indeks > 10:
        indeks = indeks - 10
    return indeks

def Lisa_tabelisse(tabel, sisend):
    
    b = (hashi(sisend))
    a = tabel[b]
    a.append(sisend)
    return tabel

def Leia(tabel, x):
    b = hashi(x)
    for i in range(len(tabel[b])):
        if x in tabel[b]:
            return ('yes, ' + str(x) + ' on hashmapis')
        else:
            return ('no')
    
#------------------------------------


Tabel = tabel()
input = [2,66,56,99,59,666,78]
for k in input:
    Lisa_tabelisse(Tabel, k)
    
print(Tabel)
print(Leia(Tabel,66))

#Ajakomplekssus on lisamisel O(1), lugemisel O(n). O(1) seetõttu, et teame alati pärast häshi läbimist
#indeksit, ei pea hakkama loopima või edasi räsima, kui põrkumine toimub.
#Lugemisel on O(n), sest otsing alamlistist on lineaarne, Lin.Search on O(n)
#Ruumikomplekssus on O(n), sest kasutame alati ainult nii palju, kui vaja, võrreldes
#nt topelträsimisega, kus kustutamisel jätame pesa tühjaks mitte ei eemalda.
#Mõtekas on kasutada, kui hashist tulenevalt on palju põrkeid, lisaks kasutab
#vähem mälu, sest salvestatakse ainult olemasolevad väärtused.
