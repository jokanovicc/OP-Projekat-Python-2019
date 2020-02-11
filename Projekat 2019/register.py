#--------------------------Registrovanje novih korisnika--------------------------------------------------
def registrovanje():
    print("******Molimo vas registrujte se!******")
    username = str(provera_username())
    sifra = input("Unesite sifru: ")
    ime = input("Unesite vase ime: ")
    prezime = input("Unesi prezime: ")
    telefon = str(provera_telefon())
    email = str(provera_mail())
    uloga = "1"
    k = registrovanje_recnik(username,sifra,ime,prezime,telefon,email,uloga)
    print("Uspesno registrovani!")
    print("_____________________________________________")
    print("Pozdrav",ime,"dobrodosli!")
    print("_____________________________________________")
    file = open("korisnici.txt","a")
    korisnici_fajl = open("korisnici.txt","a")
    sve = username+"|"+sifra+"|"+ime+"|"+prezime+"|"+telefon+"|"+email +"|"+uloga +"\n"
    sve = username+"|"+sifra+"|"+ime+"|"+prezime
    n = korisnici_fajl.write(sve)
    korisnici_fajl.close()
    return k

#------------------------------------Recnik korisnika----------------------------------------------------------------------------
def registrovanje_recnik(username,sifra,ime,prezime,telefon,email,uloga):
    k = {"username":username,"sifra":sifra,"ime":ime,"prezime":prezime,"telefon":telefon,"email":email,"uloga":uloga}
    return k
#---------------------------------------------Dodavanje novog zaposlenog------------------------------------------------------------------
def dodavanje_zaposlenih():
    print("*****************Dodavanje zaposlenog***********")
    username = str(provera_username())
    sifra = input("Unesite sifru: ")
    ime = input("Unesite ime zaposlenog: ")
    prezime = input("Unesite prezime zaposlenog: ")
    telefon = str(provera_telefon())
    email = str(provera_mail())
    salon_id = input("Unesite sifru salona u kom su zaposleni")
    uloga = "2"
    opet = opet_dodavanje()
    print("*******Zaposleni uspesno dodat!****************")
    korisnici_fajl = open("korisnici.txt", "a")
    zaposleni_fajl = open("zaposleni.txt", "a")
    sve = username+"|"+sifra+"|"+ime+"|"+prezime+"|"+telefon+"|"+email+"|"+uloga+"|"+salon_id + "\n"
    n = korisnici_fajl.write(sve)
    v = zaposleni_fajl.write(sve)
    korisnici_fajl.close()
    zaposleni_fajl.close()

def opet_dodavanje():
    x = input(">>Zelite li ponoviti postupak? Da/Ne: ").lower()
    if x == "da":
        dodavanje_zaposlenih()
    else:
        pass

#----------------------------------------Brisanje zaposlenih---------------------------------------------------------------------------
def obrisi_zaposlenog():
    zaposleni_id = input("Username zaposlenog kog zelite obrisati: ")
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
#--------------------------------------UI Za pretragu--------------------------------------------------------------------------------------
def pretraga_zaposlenih():
    print(">>Opcije za pretragu zaposlenih")
    print("[1] Pretraga po jednom kriterijumu")
    print("[2] Pretraga po vise kriterijuma")
    print("[0] Izlaz")

    x = input("Unesite opciju>>:")

    if x=="1":
        zaposleni_pretraga1()
        return pretraga_zaposlenih()
    if x=="2":
        zaposleni_visestruka()
        return pretraga_zaposlenih()
#----------------------------------Provere i unosi------------------------------------------------------------------------------
def provera_username():
    f_in = open("korisnici.txt","r")
    username = input("Unesite username koji zelite: ")
    lines = f_in.readlines()
    for line in lines:
        spliti = line.split("|")
        if username in spliti:
            print("Korisnicko ime zauzeto!")
            provera_username()
        else:
            pass
    return username

def provera_mail():
    email = input("Unesite vas email: ")
    if not "@" in email:
        print("Email nije validan!")
        provera_mail()
    else:
        pass
    return email

def provera_telefon():
    telefon = input("Unesite vas broj telefon: ")
    if len(telefon)<4:
        print("Vas broj telefona nije validan, mora imati vise cifri...")
        provera_telefon()
    else:
        pass
    return telefon

#----------------------------------------------------Jednostruka pretraga zaposlenih----------------------------------------------------------------
def zaposleni_pretraga1():
    f_in = open("zaposleni.txt","r")
    lines = f_in.readlines()
    print(">>Pretraga po jednom kriterijum\n (ime, prezime, korisničko ime, email adresa, uloga)")
    opcija = input("Unesite opciju za pretragu: ")
    for line in lines:
        split = line.split("|")
        uspesnost = False
        if opcija in split:
            print('{0:<12}{1:<17}{2:<15}{3:<25}{4:<25}{5:<30}{6:<21}'.format("Username","Password","Ime","Prezime","Broj telefona","Email","Rola"))
            print(130*'*')
            ident,brtab,naziv,mesta,klima,motor,boja= split[0], split[1], split[2],split[3],split[4],split[5],split[6],
            print('{0:<12}{1:<17}{2:<15}{3:<25}{4:<25}{5:<30}{6:<21}'.format(ident,brtab,naziv,mesta,klima,motor,boja))
            uspesnost = True
    if uspesnost == False:
        print("Nema takvog zaposlenog!")
        pretraga_zaposlenih()


#-------------------------------------------Visestruka pretraga zaposlenih---------------------------------------------------------------
def zaposleni_visestruka():
    f_in = open("zaposleni.txt","r")
    lines = f_in.readlines()
    print(">>Pretraga po jednom kriterijum\n (ime, prezime, korisničko ime, email adresa, uloga)")
    opcija1 = input("Unesite opciju1 za pretragu: ")
    opcija2 = input("Unesite opciju 2 za pretragu: ")
    for line in lines:
        split = line.split("|")
        uspesnost = False
        if opcija1 in split and opcija2 in split:
            print('{0:<12}{1:<17}{2:<15}{3:<25}{4:<25}{5:<30}{6:<21}'.format("Username","Password","Ime","Prezime","Broj telefona","Email","Rola"))
            print(130*'*')
            ident,brtab,naziv,mesta,klima,motor,boja= split[0], split[1], split[2],split[3],split[4],split[5],split[6],
            print('{0:<12}{1:<17}{2:<15}{3:<25}{4:<25}{5:<30}{6:<21}'.format(ident,brtab,naziv,mesta,klima,motor,boja))
            uspesnost = True
    if uspesnost == False:
        print("Nema takvog zaposlenog!")
        pretraga_zaposlenih()




#------------------------------------Ispis korisnika--------------------------------------------------------------------------------------
def korisnici_ispis():
	korisnici = open("zaposleni.txt", "r")
	print('{0:<12}{1:<17}{2:<15}{3:<25}{4:<25}{5:<30}{6:<21}'.format("Username","Password","Ime","Prezime","Broj telefona","Email","Rola"))
	print(130*'*')
	for i, korisnik in enumerate(korisnici):
		podaci = korisnik.split('|')
		ident,brtab,naziv,mesta,klima,motor,boja= podaci[0], podaci[1], podaci[2],podaci[3],podaci[4],podaci[5],podaci[6],
		print('{0:<12}{1:<17}{2:<15}{3:<25}{4:<25}{5:<30}{6:<21}'.format(ident,brtab,naziv,mesta,klima,motor,boja))
	korisnici.close()
