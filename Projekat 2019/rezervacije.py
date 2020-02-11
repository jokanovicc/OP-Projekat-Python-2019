import autododaj
from datetime import date
from datetime import datetime
import random
import ocene

#-----------------------------------UI za rezervacije----------------------------------------
def meni_rezervacije():
    print("```````````````````````````````````````")
    print("[1] Kreiraj rezervaciju             ```")
    print("[2] Pregled rezervacija             ```")
    print("[3] Oceni rezervaciju               ```")
    print("[4] Pregled Automobila              ```")
    print("[5] Pretraga Automobila             ```")
    print("[6] Prikaz najbolje ocenjenih auta  ```")
    print("[x] Izlaz                           ```")
    print("```````````````````````````````````````")

    x = input(">>Unesi opciju: ").lower()
    if x == "1":
        cuvanje()
    #if x == "3":
        #cuvanje()
    if x== "2":
        pregled_rezervacije()
        return meni_rezervacije()
    if x=="3":
        oceni_pocetna()

    if x =="4":
        autododaj.ispisi_auto()
        return meni_rezervacije()
    if x =="5":
        autododaj.pretraga_automobila()
    if x=="6":
        ocene.svi_auti()
        ocene.rejting()
        meni_rezervacije()
    if x == "x":
        return 0

def sifra():
    kod = random.randint(100000,999999)
    return kod

#-----------------------------------------------------Nova rezervacija---------------------------------------------------------------------
def nova_rezervacija():
    ras = raspolozivo()
    print("`````````````````````````````````````````")
    print("`````Popunjavanj nove rezervacije````````````````````````````````")
    id_1 = input("Unesite ID Auta")
    f = open("rezervacije.txt","r")
    lines = f.readlines()
    for line in lines:
        spliti = line.split("|")
        if id_1 in spliti:
            print("Zauzeto")
            nova_rezervacija()
            break
        else:
            pass
    id = str(provera_id())
    user = str(provera_username())
    user1 = input("Unesite kontakt username na koga se vodi rezervacija: ")
    #prolaz = vreme_operacije.vreme_prolaz()
    kod = sifra()
    datumi1 = okej_datumi()
    splitovano1 = datumi1[0]
    splitovano2 = datumi1[1]
    #sve_okej = str(okej_datumi())
    print(">>Uspesno Kreirana Rezervacija!`````````````````````````````````")
    sve = str(kod)+"|"+id_1+"|"+user1 +"|" +splitovano1+"|"+splitovano2+"\n"
    #print(sve)
    #dalje = meni_rezervacije()
    jos_jednom = rez_opet()
    return sve
    return id_1

#-------------------------------Raspoloziva auta---------------------------------------------------------
def raspolozivo():
    x = input("Zelite li videti raspolozive auto da/ne: ")
    if x == "da":
        autododaj.ispisi_auto()
        return
    else:
        pass

#---------------------------------------------Pokretanje ponovone rezervacije-----------------------------------------------
def rez_opet():
    x = input("Da li zelite izvrsiti jos jednu rezervaciju: Da/Ne: ").lower()
    if x == "da":
        nova_rezervacija()
    elif x== "ne":
        pass
    else:
        print("Unesite nesto od ponudjenog")

def cuvanje():
    #datum = vreme()
    date = vreme_sada()
    tu = nova_rezervacija()
    f_in = open("rezervacije.txt","a")
    sve = date + "|"+tu
    print(sve)
    stamp =f_in.write(sve)
    dalje = meni_rezervacije()


#---------------------------------------------------------Da li je rezervacija prosla-------------------------------
def pregled_rezervacije():
    print("````````````````````````````````````````")
    print(">>Provera")
    id = ispis_provera()


#------------------------------------------------------Trenutni datum------------------------------------------
def vreme():
    datum = str(date.today())
    return datum


def vreme_sada():
    datum = str(datetime.now())
    date = datum.split()[0]
    h,m = [datum.split()[1].split(":")[0],datum.split()[1].split(":")[1]]

    return date + " " + h + ":" + m


#-------------------------------------------------------Cuvanje u neki fajl-----------------------------------------
def oceni_pocetna():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nRezervacija se moze oceniti samo kad je zavrsena        ~")
    print("\nUnesite datum kada ste vratili automobil                ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    date1 = vreme()
    date2 = datum_vracanja()
    if date1>date2:
        print("Proslo je")
        ocenjivanje()
    else:
        print("Rezervacija i dalje traje....")
        oceni_pocetna()

#------------------------------------Ocenjivanje UI-------------------------------------------------------
def ocenjivanje():
    print("********************************************************")
    print("Ocenjivanje se vrsi od ocenom od 1-5                 ***")
    fajl = open("ocene.txt","a")
    ocena = str(unos_ocene())
    model = input("Unesite ID Auta kog ste iznajmili: ")
    sve = model + "|" + ","+ocena + "\n"
    #n = fajl.write(sve)
    print("Hvala vam sto se ocenili rezervaciju i time podrzali nas salon!")
    dalje = meni_rezervacije()
    return ocena



def unos_ocene():
    x = input("\nUnesi ocenu: ")
    if x=="1" or x=="2" or x =="3" or x=="4" or x =="5":
        print("~~~~~~~~~~~")
        pass
    else:
        print("Ocene moraju biti od 1-5")
        unos_ocene()
    return x



def datum_vracanja():
    print("\n`````````Unesite datum Kada ste vratili automobil````````````")
    print("Datum mora biti u\nformatu -Godina/Mesec/Dan-              ``")
    godina = str(2020)
    mesec = input("Unesite mesec: \nPrimer: *Januar-01*:\n")
    dan = input("Unesite dan-\n*Primer:28*:\n")
    sve2 = godina + "-" + mesec +"-" + dan +"\n"
    f = open("rezervacije.txt","r")
    lines = f.readlines()
    uspesnost = False
    for line in lines:
        spliti = line.split("|")
        if sve2 in spliti:
            print("\nPostoji takva rezervacija                    ``")
            ocenjivanje()
            uspesnost = True
            break
    if uspesnost == False:
        print("\nNe postoji takva rezervacija!")
        datum_vracanja()

    return sve2



#-------------------------------------------------------Ispis rezervacija--------------------------------------------------

def ispis_provera():
    f_in = open("rezervacije.txt","r")
    cars = f_in.readlines()
    print("Unesite username")
    print("<<")
    opcija = input("Opcija: ")
    for car in cars:
        split = car.split("|")
        uspesnost = False
        if opcija in split:
            print('{0:<30}{1:<25}{2:<25}{3:<25}{4:<25}{5:<25}'.format("Vreme izdavanja","Sifra","ID Auta","Korisnik","Vreme uzimanja","Vreme povratka"))
            print(80*'``')
            ident,brtab,naziv,model,mesta,mesta2= split[0], split[1], split[2],split[3],split[4],split[5],
            print('{0:<30}{1:<25}{2:<25}{3:<25}{4:<25}{5:<25}'.format(ident,brtab,naziv,model,mesta,mesta2))
            print("\n")
            uspesnost = True
            return
    if uspesnost == False:
        print("Nema")
        ispis_provera()

def ispis_provera2():
    f_in = open("rezervacije.txt","r")
    cars = f_in.readlines()
    print("*****************************************************************************************")
    print("Dostupne su visestruke pretrage po datumu, po vremenu izdavanje, po korisniku    ********")
    print("Unesite info")
    print("<<                                                                               ********")
    opcija1 = input("Opcija 1: ")
    opcija2 = input("Opcija 2:")
    print("*****************************************************************************************")
    for car in cars:
        split = car.split("|")
        uspesnost = False
        if opcija1 in split and opcija2 in split:
            print('{0:<30}{1:<25}{2:<25}{3:<25}{4:<25}{5:<25}'.format("Vreme izdavanja","Sifra","ID Auta","Korisnik","Vreme uzimanja","Vreme povratka"))
            print(80*'``')
            ident,brtab,naziv,model,mesta,mesta2= split[0], split[1], split[2],split[3],split[4],split[5],
            print('{0:<30}{1:<25}{2:<25}{3:<25}{4:<25}{5:<25}'.format(ident,brtab,naziv,model,mesta,mesta2))
            print("\n")
            uspesnost = True
            return
            break
    if uspesnost == False:
        print("Nema")
        return


def zaposleni_rezervacije():
    print("Dostupne je jednostruka i dvostruka pretraga***********************")
    print("[1] Jednostruka                             ***********************")
    print("[2] Dvostruka                               ***********************")
    print("[x] Nazad                                   ***********************")
    x = input(">Unesite opciju: ").lower()
    if x == "1":
        ispis_provera()
        zaposleni_rezervacije()
    if x=="2":
        ispis_provera2()
        zaposleni_rezervacije()
    if x=="x":
        return
    else:
        print("Unesite neku od opcija")
def provera_username():
    user = input(">>Unesite vas Username radi provere:")
    f_in = open("korisnici.txt","r")
    lines = f_in.readlines()
    for line in lines:
        sve = line.split("|")
        provera = False
        if user in sve:
            print("Validan")
            provera = True
            break
    if provera == False:
        print("Ne postoji takav korisnik")
        provera_username()

        return user


#------------------------------------------Da li postoji id------------------------------------------------------------------------
def provera_id():

    f_in = open("automobilii.txt","r")
    lines = f_in.readlines()
    id_auta = input("Potvrdite unos ID:")
    for line in lines:
        sve = line.split("|")
        provera = False
        if id_auta in sve:
            print("Postoji")
            provera = True
            break
    if provera == False:
        print("Nema")
        provera_id()
        return id_auta



#---------------------------------------------Kada si ga preuzeo------------------------------------------------
def preuzimanje_datum():
    print("````Unesite datum preuzimanja```````")
    print("Datum mora biti u\nformatu -Godina/Mesec/Dan-")
    godina = str(2020)
    mesec = input("Unesite mesec -\nPrimer *Januar je 01*\n: ")
    if int(mesec)>12:
        print("Nema toliko meseci")
        preuzimanje_datum()
    else:
        pass
    dan = input("Unesite dan- \n*Primer:28\n: ")
    if int(dan)>31:
        print("Nema toliko dana")
        preuzimanje_datum()
        False
    else:
        pass
    sve1 = godina + "-" + mesec +"-" + dan
    return sve1
#--------------------------------------------Kada ga vracas------------------------------------------------------
def povratak_datum():
    print("````Unesite datum Povratka```````")
    print("Datum mora biti u\nformatu -Godina/Mesec/Dan-")
    godina = str(2020)
    mesec = input("Unesite mesec: Januar-01:")
    if int(mesec)>12:
        print("Nema toliko meseci")
        povratak_datum()
    else:
        pass
    dan = input("Unesite dan-Primer:28:")
    if int(dan)>31:
        print("Nema toliko dana")
        povratak_datum()
    else:
        pass
    sve2 = godina + "-" + mesec +"-" + dan
    return sve2


def prikaz_svih_rezervacija():
	rezervacije = open("rezervacije.txt", "r")
	print('{0:<35}{1:<23}{2:<25}{3:<35}{4:<23}{5:<25}'.format("Vreme izdavanja","Sifra rezervacije","ID Auta","Na koga se vodi","Vreme preuzimanje","Vreme vracanja"))
	print(160*'*')
	for i, auto in enumerate(rezervacije):
		podaci = auto.split('|')
		ident,brtab,naziv,vodenje,sifra,sifra2= podaci[0], podaci[1], podaci[2],podaci[3],podaci[4],podaci[5],
		print('{0:<35}{1:<23}{2:<25}{3:<35}{4:<23}{5:<25}'.format(ident,brtab,naziv,vodenje,sifra,sifra2))


#--------------------------------------------Ispravni datumi---------------------------------------------------------
def okej_datumi():
    datesada = vreme()
    date1 = preuzimanje_datum()
    date2 = povratak_datum()
    if date1<date2 and date1>datesada:
        print("Datumi su okej")
    else:
        print("\nDatumi se ne podudaraju!!")
        print("Probajte ponovo!")
        okej_datumi()
    return date1,date2
