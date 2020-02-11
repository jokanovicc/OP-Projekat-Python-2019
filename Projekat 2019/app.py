import register
import autododaj
import azuriranje
import rezervacije
import ocene
import izvestaji
#-------------------------------UI Pocetni login meni za prijavu--------------------------------------------------------
def login_meni():
    while(True):
        print("Salon Automobila ~~~~~~~~~~~~")
        print("~~~~~ [1] Uloguj se     ~~~~~")
        print("~~~~~ [2] Registruj se    ~~~")
        print("~~~~~ [3] Rezim gosta    ~~~~")
        print("~~~~~ [4] Izlaz        ~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        x = input("~~~~~~~~>>Unesite datu opciju: ")

        if x == "1":
            print("Ulogujte se...")
            loginovanje()

            pass
        elif x == "2":
            register.registrovanje()
            return meni_registrovani()
            pass
        elif x=="3":
            print("Prelazak u rezim gosta...")
            menigost()
            break
        elif x == "4":
            print("Izlaz")
            exit()
        else:
            print(">>Molimo vas unesite opciju 1-4...")
            pass

#-------------------------------------UI Meni za neregistrovane korisnike------------------------------------------------------------------

def menigost():
    print("******************************************")
    print("[1 Registruj se]                     *****")
    print("[2]Pregled automobila                 ****")
    print("[3]Pretraga automobila                 ***")
    print("[4]Prikaz najbolje ocenjenih automobila **")
    print("[5]Izlaz                                 *")
    print("******************************************")
    x = input("\n>>Unesite opciju...")
    if x == "1":
        register.registrovanje()
        meni_registrovani()
    if x == "2":
        autododaj.ispisi_auto()
        return menigost()
    if x == "3":
        autododaj.pretraga_zaposleni_meni()
        x = input("~~Zelite li nazad da ne~~da/ne: ").lower()
        if x=="da":
            menigost()
        else:
            autododaj.pretraga_automobila()
    if x == "4":
        ocene.rejting()
        return menigost()
    if x=="5":
        login_meni()
    else:
        print("Unesite nesto od ponudjenog")
        menigost()

#---------------------------------------------UI Meni za registrovane korisnike---------------------------------------
def meni_registrovani():
    print("**********************************************")
    print("[1] Rezervacije                      *********")
    print("[2] Pregled Automobila                 *******")
    print("[3] Pretraga Automobila                  *****")
    print("[4] Najbolje ocenjeni automobili          ****")
    print("[5] Odjava sa sistema                      ***")
    print("**********************************************")
    x = input(">>Unesite opciju...")
    if x == "1":
        rezervacije.meni_rezervacije()
        x = input("Zelite li nazad?da ne ")
        if x == "da":
            meni_registrovani()
        else:
            rezervacije.meni_rezervacije()
    if x == "2":
        autododaj.ispisi_auto()
        meni_registrovani()
    if x == "3":
        autododaj.pretraga_zaposleni_meni()
        x = input("Zelite li nazad da ne")
        if x=="da":
            meni_registrovani()
        else:
            autododaj.pretraga_automobila()
    if x == "4":
        autododaj.ispisi_auto()
        ocene.rejting()
        meni_registrovani()

    if x =="5":
        login_meni()
    else:
        print("Molimo vas unesite nesto od opcija!!!")
        return meni_registrovani()


#---------------------------------------------------UI Meni za admine--------------------------------------------------------
def meni_admin():
    print("************************************************")
    print("[S] Informacije o salonu                    ***")
    print("\n[1] Dodavanje novih automobila              ***")
    print("\n[2] Dodavanje novih zaposlenih              ***")
    print("\n[3] Pregled Automobila                      ***")
    print("\n[4] Pretraga Automobila                     ***")
    print("\n[5] Azuriranje salona                       ***")
    print("\n[6] Brisanje Automobila                     ***")
    print("\n[7] Brisanje zaposlenih                     ***")
    print("\n[8] Pretraga zaposlenih                     ***")
    print("\n[X] Odjava                                  ***")
    print("************************************************")
    x = input("\n>>Unesi neku od opcija: ")
    if x == "s":
        azuriranje.info_salon()
        x = input("Dalje? da ne")
        if x=="da":
            meni_admin()
        else:
            return
    if x == "1":
        autododaj.main()
        g = input("Zelite li videti raspolozive automobile? ")
        if g == "da":
            autododaj.ispisi_auto()
            meni_admin()
    if x == "2":
        register.dodavanje_zaposlenih()
        return meni_admin()
    if x=="3":
        autododaj.ispisi_auto()
        meni_admin()
    if x=="4":
        autododaj.pretraga_automobila()
        x = input("Zelite li nazad da ne")
        if x=="da":
            meni_admin()
        else:
            autododaj.pretraga_automobila()
    if x=="5":
        register.korisnici_ispis()
        register.pretraga_zaposlenih()
    if x == "6":
        autododaj.obrisi_auto()
        print("******>>Uspesno Obrisano!***************")
        g = input("Zelite li nazad: ")
        if g== "da":
            meni_admin()
    if x == "7":
        register.obrisi_zaposlenog()
        return meni_admin()
    if x=="8":
        register.pretraga_zaposlenih()
        return meni_admin()
    if x == "x":
        login_meni()
    else:
        print("Molimo vas unesite neku od opcija!!")
        return meni_admin()


#-----------------------------------------------UI Meni za zaposlene---------------------------------------------------------------------
def meni_zaposleni():
    print("************************************************")
    print("[1] Pretraga automobila")
    print("[2] Pretraga rezervacija")
    print("[3] Izvestavanje")
    print("[4] Izlaz")
    print("*************************************************")
    x = input(">>Unesi neku od opcija")
    if x=="1":
        autododaj.pretraga_zaposleni_meni()
        x = input("Zelite li nazad da ne")
        if x=="da":
            meni_zaposleni()
        else:
            autododaj.pretraga_automobila()
    if x == "2":
        rezervacije.prikaz_svih_rezervacija()
        rezervacije.zaposleni_rezervacije()
        x = input("Zelite li nazad? da/ne")
        if x == "da":
            meni_zaposleni()
        else:
            rezervacije.zaposleni_rezervacije()

    if x=="3":
        print("Not Implemented...")
        meni_zaposleni()
    if x=="4":
        login_meni()
    else:
        print("Molimo vas unesi nesto od ponudjenog! ")
        meni_zaposleni()

#----------------------------------------Algoritam za loginovanje---------------------------------
def loginovanje():
    f_in = open("korisnici.txt","r")
    clanovi = f_in.readlines()
    ime = input("Unesite vase korisnicko ime: ")
    sifra = input("Unesite vasu sifru: ")
    uspesno_log = ""
    for clan in clanovi:
        clan = clan.strip().split("|")

        clan_ime = clan[0]
        clan_sifra = clan[1]                #hvata stringove
        clan_uloga = clan[6]
        uspesno_log = False
        if ime == clan_ime and sifra==clan_sifra:   #provera

            print("`````````````````````````````````````````")
            print(">>Uspesno Ulogovani")
            uspesno_log =True
            #print(clan_uloga)
            if clan_uloga == "1":           #U zavisnovi od uloge prosledjuje funkcije
                #print(clan_uloga)
                print(meni_registrovani())
            elif clan_uloga == "2":
                #print(clan_uloga)
                print(meni_zaposleni())
            else:
                print(meni_admin())
            break                     #Ako je if neuspesan, znaci da takav korisnik ne postoji

    if uspesno_log == False:
        print("***********************************************")
        print("\nPogresno korisnicko ime ili lozinka...")
    print("\nProbajte ponovo....")
    loginovanje()
#----------------------------Pokretanje-----------------------------------------------------------------
def main():
    login_meni()
main()        #Poziv programa

__name__ = "__main__"
