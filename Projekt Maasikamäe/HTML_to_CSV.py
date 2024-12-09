from pathlib import Path
import pandas
import os
import csv
import re

def CSV(url,output):
    temporary = output + "_temp.csv"
    fail = (output + ".csv")
    tabelid = pandas.read_html(url)[0]
    tabelid.to_csv(temporary)
    f = open (temporary,'r+',encoding = 'utf-8')
    f2 = open (fail, "w", encoding = 'iso-8859-1')
    for data in f:
        data = data.replace('Ã¡','á' )
        data = data.replace('Ã§','ç')
        data = data.replace('Ã­','í')
        data = data.replace('Ã©','é')
        data = data.replace('Ãº','ú')
        data = data.replace('Ã£','ã')
        
        data = data.replace('â,¬,','')
        #Python on väärakas ^^^^^^
        #df[]
        print(data)
        f2.write(data)   

    # for row in csv_input:
    #     row[4] = row[4].replace('K','000')
    #     print(row[4])
    #     csv_output.writerow(row)
    # ma proovisin  mitu korda seda lahendada, see on 
    # üks võimalikke lahendusi mida proovisin
        
    f.close()
    f2.close()
    os.remove(temporary)

#CSV('CasaPiaAndmestrukt.html','stats')