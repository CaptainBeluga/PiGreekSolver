import pigreco
import sys

print("App Developed by BELUGA")      #Credits to CapBeluga
print()

while True:
    try:
        
        print("Digita 1 per TROVARE la CIRCONFERENZA")
        print("Digita 2 per TROVARE il DIAMETRO")
        print("Digita 3 per TROVARE il RAGGIO")
        choose=int(input("Scegli > "))
        print()

        if choose==1:
            diametro=int(input("Inserisci DIAMETRO: "))
            alfa=pigreco.formula1(diametro,pigreco)
            print(alfa)
            print()
            print("RICORDA CHE...... Circonferenza = Diametro x Pi Greco (3,14)")
            print()
            print()


        if choose==2:
            circ=int(input("Inserisci CIRCONFERENZA: "))
            beta=pigreco.formula2(circ,pigreco)
            print(beta)
            print()
            print("RICORDA CHE...... Diametro = Circonferenza : Pi Greco (3,14)")
            print()
            print()

        if choose==3:
            circ=int(input("Inserisci CIRCONFERENZA: "))
            trio=pigreco.formula3(circ,pigreco)
            print(trio)
            print()
            print("RICORDA CHE...... Raggio = Circonferenza : Pi Greco x 2 (6,28)")
            print()
            print()
        
    except ValueError:
            print()
            errore="RICORDA DI INSERIRE SOLO NUMERI!!!\n"
            errore_colore=sys.stdout.shell
            errore_colore.write(errore,"stderr")
            print()
            print()

#by SP27
        
