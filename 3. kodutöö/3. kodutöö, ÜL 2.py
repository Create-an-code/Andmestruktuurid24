def BinOtsing(massiiv, otsitav):
    
    algus = 0
    lõpp = len(massiiv) - 1
    i = 0

    while algus <= lõpp:
        i = i+1

        keskmine = algus + ((lõpp - algus) // 2)
        if massiiv[keskmine] == otsitav:
            return i
            return (str(otsitav) + ' asub indeksil ' + str(keskmine))
        
        elif massiiv[keskmine] < otsitav:
            algus = keskmine + 1
        else:
            lõpp = keskmine - 1
    return('Pole elementi massiivis')
mass = [1,2,3,4,5,6,7,8,9,10,11,12,13.14,15,16,17,18,19,
        20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,
        36,37,38,39,40] 





def LinOtsing(massiiv, otsitav):
    s = 0
    for i in range(len(massiiv)):
        s = s +1
        if massiiv[i] == otsitav:
            return(s)
            return(str(otsitav) + ' asub ' + str(i) + ' indeksil')

        else:
            i = i + 1
    return ('Kahjuks ei ole massiivis')

x = 0
for t in mass:
    x = x + BinOtsing(mass, t)
vastus = (x/len(mass))
print(round(vastus ,2))

y = 0
for t in mass:
    y = y + LinOtsing(mass, t)
vastus = (y/len(mass))
print(round(vastus ,2))


#------

#Aegkomplekksus Binaty Searchil on sarnane tulemus log[2]n, kasutades antud testikoodi. 
#Lin search on lineaarne, O = n
# 
#Antud benchmarki juures on näha, et Lin search võtab keskmiselt aega 20 tsüklit per otsing, 
#Binary searchi kasutades aga ainult 4.54. 
#
#Binary search on kasulikum, kui on soteeritud andmehulk, kuna saame ära kasutada eelmisest
#benchmarkist nähtud kiiruse eelist.
