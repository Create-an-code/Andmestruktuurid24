    # for line_number, line in enumerate(players):
    #     x = []
    #     i = 4
    #     for reanumber , rida in enumerate(stats):
    #         while i < 47:
    #             x.append((int(line[i])) * (int(rida[i])))
    #             i += 1
    #         print(x)     
 
    
    
    
    #df = pd.read_csv('players')
    #content = df['Name'][:2].to_string()
    #print(content, file=open('my_file.txt', 'w'))
    
    
    
    
    
    
    # reader = csv.reader(players)
    # for row in reader:
    #     print(row[4])
    #rows = list(reader)
    #print(rows[3])
    # reader = csv.reader(players, delimiter="\t")
    # for i, line in enumerate(reader):
        
    #     a =(line)
    #     print(a)


def pigeonhole_sort(a): 
    # size of range of values in the list 
    # (ie, number of pigeonholes we need) 
    my_min = min(a) 
    print(my_min)
    my_max = max(a) 
    print(my_max)
    size = my_max - my_min + 1
  
    # our list of pigeonholes 
    holes = [0] * size 
  
    # Populate the pigeonholes. 
    for x in a: 
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
    print(holes)
    # Put the elements back into the array in order. 
    i = 0
    for count in range(size): 
        while holes[count] > 0: 
            holes[count] -= 1
            a[i] = count + my_min 
            i += 1
              
  
a = [8, 3, 2, 7, 4, 6, 7,7,8] 
print("Sorted order is : ", end =" ") 
  
pigeonhole_sort(a) 
          
for i in range(0, len(a)): 
    print(a[i], end =" ")

    
                                #mängija_tulemuse_list.append()
                                #print(mängija_tulemuse_list)
                #print(mängija_tulemuse_list)            

                #for atribuut in mängija_atribuudid:

    #sorteeritud = sorted(lõpp, key=lambda x: x[0])
    #def sorteeri(lst):
        #x = [item[0] for item in lst]
        #x = list(set(x))
        #return x
    #print(lõpp)

        # for element in massiiv:
    #     print(len(element))
    #     if len(element) == 1:
    #         lõpumassiv.append(element)
    #         return(lõpumassiv)
    #     if len(element) == 0:
    #         None
    #         #kui mängijaid on ainult 1 või 0, siis ei ole ju mõtet sortida

    #     else:
    #         mängijate_kogum = {}
    #         for player in element:
    #             print(element)
    #             print(player)
    #             print(element[2])
    #             mängijate_kogum.update({element[2] : element.index(player)})
    #         peaaegu = sorting(mängijate_kogum)
    #         kogum = []
    #         print(peaaegu)
    #         for i in peaaegu:
    #             kogum.append(element[i])
    #         return kogum
                