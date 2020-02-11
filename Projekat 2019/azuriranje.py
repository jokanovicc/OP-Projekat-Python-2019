import autododaj
import register
import autododaj
#-----------------------------------------------UI Za opste informacije o salonu
def info_salon():
    print("Informacije o salonu: ")
    print("[1] Izmena podataka o zaposlenim")
    print("[2] Izmena podataka o automobilima")
    print("[3] Opste informacije o salonu")
    print("[4] Lista Automobila")
    print("Prosecna ocena salona")
    print("[x] Nazad")

    x = input("Unesi opciju: ")

    if x == "1":
        zaposleni_svi()
        izmena_zaposlenih()
        info_salon()
    if x == "2":
        izmena_automobila()
        info_salon()
    if x == "3":
        salon_opste()
    if x=="4":
        autododaj.ispisi_auto()
        info_salon()
    if x == "x":
        print("Izlazzz")
        return
    else:
        print("unesi bar nesto")

#-----------------------------------------Funkcija opstih informacija-------------------------------------
def salon_opste():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|Šifra salona|~~~~~~~~~|Naziv|~~~~~~~~~| Ulica |~~~~~~~~~~~~~~~~~|Grad|~~~~~ ")
    print("   ",10111,"           ","Salon023","      ","Ruže Šulman 51","          ","Zrenjanin")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    x = input("\nX za Nazad").lower()
    if x == "x":
        info_salon()
    else:
        print("Unesite validnu opciju")

#---------------------------------------Prikaz svih zaposlenih----------------------------------------
def zaposleni_svi():
    f_in = open("zaposleni.txt","r")
    cars = f_in.readlines()
    print("Prikaz svih zaposlenih")
    print('{0:<15}{1:<17}{2:<20}{3:<20}{4:<16}{5:<18}{6:<17}{7:<17}'.format("Username","Sifra","Ime","Prezime","Broj telefona","Imejl","Numeracija","ID"))
    print(130*'*')
    for car in cars:
        split = car.split("|")
        ident,brtab,naziv,model,mesta,klima,motor,jos= split[0], split[1], split[2],split[3],split[4],split[5],split[6],split[7],
        print('{0:<15}{1:<17}{2:<20}{3:<20}{4:<16}{5:<18}{6:<17}{7:<17}'.format(ident,brtab,naziv,model,mesta,klima,motor,jos))


#-------------------------Azuriranje pocetak------------------------------------------------------
def izmena_zaposlenih():
    print("Mozete izmeniti informacije tako sto ce te azurirati sve informacije")
    izmeni_zaposlenog()
    izmena()
    print("\nUneli ste nove informacije!")
    return


def izmeni_zaposlenog():
    zaposleni_id = input("Username zaposlenog kom zelite izmeniti informacije: ")
    file = open("korisnici.txt","r")
    zaposleni = file.readlines()
    allLines = ""
    for radnik in zaposleni:
        clanovi = radnik.split("|")
        radnik_ime = clanovi[0]
        if radnik_ime != zaposleni_id:
            allLines += radnik

    file = open("korisnici.txt", "w")
    file.write(allLines)
    file.close()


def izmena():
    print("******Molimo izmenite informacije o zaposlenog!!*****************************************")
    username = input("Unesite username")
    sifra = input("Unesite sifru: ")
    ime = input("Unesite ime: ")
    prezime = input("Unesi prezime: ")
    telefon = input("Unesite telefon")
    email = input("Unesite mejl")
    uloga = "2"
    print("Uspesno azurirano!")
    print("_____________________________________________")
    print("_____________________________________________")
    print("******************************************************************************************")
    file = open("korisnici.txt","a")
    korisnici_fajl = open("zaposleni.txt","a")
    sve = username+"|"+sifra+"|"+ime+"|"+prezime+"|"+telefon+"|"+email +"|"+uloga +"|10111" +"\n"
    v = file.write(sve)
    n = korisnici_fajl.write(sve)
    korisnici_fajl.close()
    zaposleni_svi()
    info_salon()


def izmena_automobila():
    print("Mozete izmeniti informacije tako sto ce te azurirati sve informacije")
    autododaj.ispisi_auto()
    izmeni_auta()
    izmena_auto()
    print("\nUneli ste nove informacije!")
    return

def izmeni_auta():
    car_id_to_delete = input("Id auta kog zelite izmeniti: ")     #Uzima ID
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

def izmena_auto():
    print("Molimo informacije za azuriranje!********************")
    ident = input("Unesite ID:")
    brtab = input("Unesite registracione oznake: ")
    naziv = input("Unesite proizvodjaca: ")
    model = input("Unesite model")
    mesta = input("Unesite broj mesta za sedenje: ")
    klima = input("Postoji li klima: ")
    motor = input("Unesite tip motora? dizel/benzin/gas: ")
    boja = input("Unesite boju karoserije: ")
    km = input("Unesite predjenu kilometrazu: ")
    cena = input("Unesite cenu po danu")

    #k = auto_recnik(ident,brtab,naziv,mesta,klima,motor,boja,km,cena)
    print("**************Dodato*********************************")
    automobili_fajl = open("automobilii.txt","a")
    sve = ident + "|" + brtab+ "|" +naziv+ "|"+model+"|" +mesta+ "|" +klima+ "|" +motor+ "|" +boja+ "|" +km+ "|" +cena + "\n"
    n = automobili_fajl.write(sve)
    automobili_fajl.close()
    autododaj.ispisi_auto()
    return ident

__name__ = "__main__"
