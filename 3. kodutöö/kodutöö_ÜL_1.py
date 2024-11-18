def LinOtsing(massiiv, otsitav):
    for i in range(len(massiiv)):
        if massiiv[i] == otsitav:
            return(str(otsitav) + ' asub ' + str(i) + ' indeksil')

        else:
            i = i + 1
    return ('Kahjuks ei ole massiivis')


x = [1,2,3,4,5,6,7,8,9]
print(LinOtsing(x,11))

#-------

# Ajakomplekssus on O = n, sest et loopime massiivi läbi x korda, seega algoritm skaleerub lineaarselt.
# Saame kasutada Lin.searchi, kui massiiv on sorteerimata, kuid sorteeritud andmete korral on mõtekam 
# kasutada nt Binary searachi, mille O = (log)n