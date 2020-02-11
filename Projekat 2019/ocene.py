import statistics
import autododaj

def svi_auti():
    autododaj.ispisi_auto()


def rejting():
    print("\n Prikaz svih automobila: ")
    svi_auti()
    f_in = open("ocene.txt","r")
    lines = f_in.readlines()
    ocene_lista = []

    ocenjena_lista = []
    for line in lines:
        grades = []
        line = line.split("|")

        id_auta = line[0]
        auto_ocene = line[1].strip("\n").split(",")
        for ocena_auta in auto_ocene:
            ocena = float(ocena_auta)
            grades.append(ocena)
        ocena = sum(grades)/len(grades)
        #print("{0:.2f}".format(grade))
        print("\n|   ID   |**************| Prosek Ocena |****************")
        print("|",id_auta,"                ","{0:.2f}".format(ocena))


    print("\nOcene su prikaze od 1-5")
    print("\nSvaki korisnik je dao ocenu")
    #menigost()
