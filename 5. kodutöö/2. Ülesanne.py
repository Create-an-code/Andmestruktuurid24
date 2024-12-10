#Min heap - Iga parent on väiksem kui tema lapsed (või võrdne)
#Max heap - Iga parent on suurem kui tema lapsed (või võrdne)
#lapse indeksid: vasak 2i+1, parem 2i+2

#Mõlema ruumikulu on O(n)
#Ajakulu on O(logn)

#Kuhjad töötavad hästi prioriteetjärjekordade jaoks, sest saab leida kiiresti kõige prioriteetsema elemendi (max-heap, teoorias ka ehitatav min-heap kui panna väiksem arv = suurem prioriteet)
#Kuhjasid kasutatakse ka Djiikstra algoritmis, et leida lühim tee kahe punkti vahel (pathfinding)