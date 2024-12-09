from bs4 import BeautifulSoup

def HTML_txt(file):
    temp = file.removesuffix('.html')
    markdown = open(file)
    soup = BeautifulSoup(markdown.read())
    markdown.close()
    f = open ((temp + '.txt'),'w')
    f.write(soup.get_text())
    f.close()
    with open (temp + '.txt', 'r+') as file:
        read = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(read[64:])

f = open('Attributes.txt', 'r+')
tekst = f.read()
f.truncate(0)
f.close()
tekst = tekst.replace('\t', ',')
tekst = tekst.replace(' ','_')


print(tekst)
file = open('Attributes.txt', 'w')
print(tekst)
file.write(tekst)
file.close()
#tegin ühekordseks kaustamiseks, et csv failist kopeeritud andmed saaksid txt faili