import random
#generálj 100 véletlen egész számot [-50,150] között
#a függvény térjen vissza a listával
def lista_letrehozasa():
    lista=[]
    for i in range (0,100,1):
        szam:int=int(random.random()*(151+50)-50)
        lista.append(szam)
    return lista

#a listában lévő számokat fűzd össze sztringgé,

def szovegge_alakit(lista):
    szoveg:str=""
    for i in range (0,len(lista),1):
        if (i<len(lista)-1):
            szoveg+=f"{lista[i]}; "
        else:
            szoveg+=f"{lista[i]}"

    return szoveg



def fajlba_mentes(szoveg):
    fajlom=open("adatok.txt","w",encoding='utf8')
    fajlom.write(szoveg)
    fajlom.close()

def fajlbol_olvas():
    fajlom=open("adatok.txt","r",encoding='utf8')
    szoveg_fajlbol:str=fajlom.read()
    szoveg_lista=szoveg_fajlbol.split(";")
    lista=[]
    for i in range(0,len(szoveg_lista),1):
        szam:int=int(szoveg_lista[i].strip())
        lista.append(szam)
    """    
    print(szoveg_fajlbol)
    print(lista)"""
    fajlom.close()
    return lista

"""lista=lista_letrehozasa()
print(lista)
szoveges_lista=szovegge_alakit(lista)
print(szoveges_lista)
fajlba_mentes(szoveges_lista)"""