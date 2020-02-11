#-------------------------Dodavanje auta--------------------------------------------------------------------------
def dodaj_auto():
    print("Molimo vas unesite informacije!********************")
    ident = str(provera_ident())
    brtab = input("Unesite registracione oznake: ")
    naziv = input("Unesite proizvodjaca: ")
    model = input("Unesite model")
    mesta = input("Unesite broj mesta za sedenje: ")
    klima = input("Postoji li klima: ")
    motor = input("Unesite tip motora? dizel/benzin/gas: ")
    boja = input("Unesite boju karoserije: ")
    km = input("Unesite predjenu kilometrazu: ")
    cena = input("Unesite cenu po danu")
    opet = opet_dodavanje_auto()

    #k = auto_recnik(ident,brtab,naziv,mesta,klima,motor,boja,km,cena)
    print("**************Dodato*********************************")
    automobili_fajl = open("automobilii.txt","a")
    sve = ident + "|" + brtab+ "|" +naziv+ "|"+model+"|" +mesta+ "|" +klima+ "|" +motor+ "|" +boja+ "|" +km+ "|" +cena + "\n"
    n = automobili_fajl.write(sve)
    automobili_fajl.close()
    return ident

#------------------------------Ponovno dodavanje auta----------------------------------------------------
def opet_dodavanje_auto():
    x = input(">>Zelite li ponoviti postupak>>Da/Ne?: ").lower()
    if x == "da":
        dodaj_auto()
    if x == "ne":
        pass
    else:
        print("Unesite bar nesto")

#---------------------------------------Prikaz auta-----------------------------------------------------------------------------------
def ispisi_auto():
	automobili = open("automobilii.txt", "r")
	print('{0:<10}{1:<17}{2:<20}{3:<15}{4:<10}{5:<15}{6:<17}{7:<17}{8:<17}{9:<17}'.format("ID","Tablice","Naziv","Model","Broj Mesta","Klima","Motor","Boja","Kilometraza","Cena"))
	print(150*'*')
	for i, auto in enumerate(automobili):
		podaci = auto.split('|')
		ident,brtab,naziv,model,mesta,klima,motor,boja,km,cena= podaci[0], podaci[1], podaci[2],podaci[3],podaci[4],podaci[5],podaci[6],podaci[7],podaci[8],podaci[9],
		print('{0:<10}{1:<17}{2:<20}{3:<15}{4:<10}{5:<15}{6:<17}{7:<17}{8:<17}{9:<17}'.format(ident,brtab,naziv,model,mesta,klima,motor,boja,km,cena))

	automobili.close()


#--------------------------------Brisanje auta-------------------------------------------------------------------------------------------------
def obrisi_auto():
    car_id_to_delete = input("Id koji zelis obrisati: ")     #Uzima ID
    file = open("automobilii.txt", "r")
    cars = file.readlines()
    file.close()
    allLines = ""
    for car in cars:
        clanovi = car.split("|")
        car_id = clanovi[0]
        if car_id != car_id_to_delete:          #Ako unet ID odgovara stringu
            allLines += car                     #Uzima ga i vrsi rewrite bez tog stringa
    file = open("automobilii.txt","w")
    file.write(allLines)
    file.close()

#-----------------------------------------------UI Pretrage----------------------------------------------------------------------
def pretraga_automobila():
    print("Unesite kriterijum koji zelite da trazite")
    print("Filter pretrage: ")
    print("[1] PRETRAGA Po Jednom kriterijumu")
    print("[1] Filter po Boji")
    print("[3] Visestruka pretraga")
    print("[x] nazad")
    x = input("Unesite dati filter:")
    if x == "0":
        return
    if x == "1":
        pretraga_kriterujum_jedan()
    if x== "3":
        meni_visestruka()
    if x=="x":
        pretraga_zaposleni_meni()
    else:
        print("Molimo vas unesite nesto od ponudjenog!")
#-----------------------UI kriterijuma pretrage----------------------------------------------------------------------------
def pretraga_kriterujum_jedan():
    print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print(">>Izabrana je pretraga po jednom kriterijumu")
    print("Dostupna je pretraga po motoru, boji, registracionoj tablici,\nmotorom koji pokrece,markom,broju sedista...")
    print("Primer:\nZa boju unesite crvena, broj sedista 4 ili 5, motor benzin ili gas")
    print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print(">>")
    pretraga_opcija1()

#----------------------------------------------------------Pretraga JEDNOSTRUKA---------------------------------
def pretraga_opcija1():
    f_in = open("automobilii.txt","r")
    cars = f_in.readlines()
    print("Unesite neku stavku za pretragu")
    print("[1] Za nazad<<")
    opcija = input("Opcija: ").capitalize()
    print('{0:<10}{1:<17}{2:<20}{3:<15}{4:<15}{5:<15}{6:<17}{7:<17}{8:<20}{9:<17}'.format("ID","Tablice","Naziv","Model","Broj Mesta","Klima","Motor","Boja","Kilometraza","Cena"))
    print(170*'*')
    for car in cars:
        split = car.split("|")
        uspesnost = False
        if opcija in split:
            ident,brtab,naziv,model,mesta,klima,motor,boja,km,cena= split[0], split[1], split[2],split[3],split[4],split[5],split[6],split[7],split[8],split[9],
            print('{0:<10}{1:<17}{2:<20}{3:<15}{4:<15}{5:<15}{6:<17}{7:<17}{8:<20}{9:<17}'.format(ident,brtab,naziv,model,mesta,klima,motor,boja,km,cena))
            uspesnost = True
    if uspesnost == False:
        print("Nema takvog auta!")
        pretraga_zaposleni_meni()

#----------------------------------------------------Visestruka pretraga---------------------------------------------------------------
def meni_visestruka():
    f_in = open("automobilii.txt","r")
    cars = f_in.readlines()
    print("*Note \n Dostupna je dvostruka pretraga, mozete pretraziti\n tip motora ili boju zajedno, cenu ili kilometrazu...")

    opcija1 = input("Unesi opciju 1:").capitalize()
    opcija2 = input("Unesi opciju 2:").capitalize()
    print('{0:<10}{1:<17}{2:<20}{3:<15}{4:<15}{5:<15}{6:<17}{7:<17}{8:<17}{9:<17}'.format("ID","Tablice","Naziv","Model","Broj Mesta","Klima","Motor","Boja","Kilometraza","Cena"))
    print(140*'``')
    for car in cars:
        split = car.split("|")
        pretraga= False
        if opcija1 in split and opcija2 in split:
            ident,brtab,naziv,model,mesta,klima,motor,boja,km,cena= split[0], split[1], split[2],split[3],split[4],split[5],split[6],split[7],split[8],split[9],
            print('{0:<10}{1:<17}{2:<20}{3:<15}{4:<15}{5:<15}{6:<17}{7:<17}{8:<17}{9:<17}'.format(ident,brtab,naziv,model,mesta,klima,motor,boja,km,cena))
            pretraga = True
    if pretraga == False:
        print("`````````````````````````````````````!")
        #pretraga_zaposleni_meni()


#-----------------------------------------UI za neuspesnu pretragu--------------------------------------------
def neuspesna_pretraga():
    print("*********************************")
    print("NEMA NA STANJU!")
    print("*********************************")
    x = input("Zelite li probati ponovo? da/ne")
    if x== "da":
        pretraga_automobila()
    else:
        menigost()

#------------------------------------------------Meni za zaposlene----------------------------------------------------------------------
def pretraga_zaposleni_meni():
    print("Pretraga automobila: ")
    print("[1] Pretraga po jednoj opciji")
    print("[2] Visestruka pretraga")
    print("[0] Povratak nazad")
    x = input(">>Unesi opciju:")

    if x=="1":
        pretraga_kriterujum_jedan()
        #pretraga_zaposleni_meni()
    elif x == "2":
        meni_visestruka()
        pretraga_zaposleni_meni()
    elif x== "0":
        return

    else:
        print("Ukucajte nesto od ponudjenog!")
        pretraga_zaposleni_meni()

#-----------------------------------------------------RAZNE PROVERE----------------------------------------------------
def provera_ident():
    id = input("Unesite 6-cifreni ID auta: ")
    if len(id)!=6:
        print("Mora biti 6 cifren")
        provera_ident()
    else:
        pass
    return id


#-------------------------------------------------------------Pozivi----------------------------------------------------------
def main():
    dodaj_auto()
    #prikaz_auta(auto_lista)
