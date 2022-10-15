import tkinter as tk
from tkinter import ttk
from random import randint

# inicializacie premennych
max_pocet_neuhadnutych = 10                     # toto číslo predstavuje počet zle zadaných písmenok, kedy vyhlásime prehru
x_zaciatok = 100                                # x-ová súradnica pozicie pre prvé písmenko
y_zaciatok = 50                                 # y-ová súradnica pozicie pre prvé písmenko
sirka_obdlznika = 45                            # šírka rámika pre písmenko
vyska_obdlznika = 100                           # výška rámika pre písmenko
medzera_medzi_obdlznikmi = 5                    # odstup medzi jednotlivými rámikmi
zoznam_slov = ["strom", "jahoda", "matematika", "zemegula", "traktor", "bager", "tchor"]    # zoznam slov
pocet_slov = len(zoznam_slov)                   # počet slov, z ktorých náhodne vyberieme jedno

# vyber konkretneho slova
por_cis_slova = randint(1, pocet_slov)          # náhodne vyberieme jedno slovo z intervalu 1 až počet slov
zvolene_slovo = list( zoznam_slov[por_cis_slova - 1].upper())  # táto premenná bude obsahovať jednotlivé velke písmená zvoleného slova
dlzka_slova = len(zvolene_slovo)                # dĺžka slova, ktoré sme vybrali
pocet_neuhadnutych = dlzka_slova                # táto premenná hovorí o tom, koľko ešte písmenok je neuhádnutých
pocet_zle_zadanych_pismenok = 0                 # tu budeme napočítavať zle zadané písmenká (aj opakovanie dobrého)

# definícia funkcie, ktorá zobrazí okno s gratuláciou, zahubí hlavné okno a potom aj seba (po stlačení Quit)
def vyhra():
    root2 = tk.Tk()                             # vytvorí nové okno - na správu o výhre
    root2.title("Gratulujem !")                 # dá mu názov "Gratulujem !"
    root2.geometry("400x100")                   # zadefinuje jeho veľkosť
    msg_label_2 = tk.Label(root2, text="Gratulujem, vyhrali ste !!!", font=("Acme 20 "), background="lightgray", foreground="green")  # Vytvorí text
    msg_label_2.pack(side="top", expand=False, fill="x", ipadx=10, ipady=10) # Zobrazí text
    root.destroy()                              # zahubí hlavné okno
    bttn_quit_2 = tk.Button(root2, text="Quit", command=root2.destroy)  # Vytvorí button "Quit"
    bttn_quit_2.pack(side="right", padx=10, pady=10, fill="x", expand=False)    # Po stlačení buttonu Quit zahubí vlastné okno a skončí

# definícia funkcie, ktorá zobrazí okno s info o prehre, zahubí hlavné okno a potom aj seba (po stlačení Quit)
def prehra():
    root3 = tk.Tk()                             # vytvorí nové okno - na správu o prehre
    root3.title("Smolka !")                     # dá mu názov "Smolka !"
    root3.geometry("400x100")                   # zadefinuje jeho veľkosť
    msg_label_3 = tk.Label(root3, text="Bohužiaľ, prehral si  (trapko) !!!", font=("Acme 20 "), background="yellow", foreground="red")  # Vytvorí text
    msg_label_3.pack(side="top", expand=False, fill="x", ipadx=10, ipady=10)    # Zobrazí text
    root.destroy()                              # zahubí hlavné okno
    bttn_quit_3 = tk.Button(root3, text="Quit", command=root3.destroy)  # Vytvorí button "Quit"
    bttn_quit_3.pack(side="right", padx=10, pady=10, fill="x", expand=False)    # Po stlačení buttonu Quit zahubí vlastné okno a skončí

# definícia funkcie, spracuje jedno zadané písmenko. Ak ich do formuláru zadáme viac, použije iba to posledné
def spracuj_pismenko( p ):
    global pocet_zle_zadanych_pismenok          # nechceme vo funkcii použiť novú, ale globálne deklarovanú premennú
    global pocet_neuhadnutych                   # nechceme vo funkcii použiť novú, ale globálne deklarovanú premennú
    global max_pocet_neuhadnutych               # nechceme vo funkcii použiť novú, ale globálne deklarovanú premennú
    # global zvolene_slovo                        # aby sme mohli vo funkcii aktualizovať reťazec - uhádnuté písmenká
    print(f"Funkcia: spracuj_pismenko( {p or 'Nic'} )")     # diagnostická správa na konzole
    pocet_zle_zadanych_pismenok += 1            # vopred navýšime počet zle zadaných písmenok
    pocet_neuhadnutych_pred = pocet_neuhadnutych    # toto budeme testovať po vyhodnotení, či bolo aspoň jedno uhádnuté
    if pocet_neuhadnutych > 0 and pocet_zle_zadanych_pismenok < max_pocet_neuhadnutych:
        for j in range(0, dlzka_slova ):        # preliezame vybran0 slovo jedno po druhom p9smenku
            if zvolene_slovo[j] == p:           # porovnávame so zadaným písmenkom
                pocet_neuhadnutych -= 1         # uhádnuté písmenko - znížíme počet neuhádnutých písmenok o jedno
                                                # a vpíšeme do obdĺžnička písmenko na dané miesto
                zvolene_slovo[j] = '?'          # prepíšeme písmenko v slove, aby sme neprofitovali z už uhádnutých - tu musím nájsť vhodn[ funkciu, ktorá to urobí
                # v texte vpíšeme písmenko vo štvorčekoch
                can.create_text(x_zaciatok + j * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika / 2,
                                y_zaciatok + vyska_obdlznika / 2, text=p, fill="green", font=("Acme 28 "))
                can.pack()                      # zobrazíme písmenko
    if pocet_neuhadnutych_pred > pocet_neuhadnutych:    # Ak sme uhádli aspoň jedno
        pocet_zle_zadanych_pismenok -=1         # vopred sme si zvýšili premennú s počtom zle zadaných, teraz znížime
        print("Zvolene slovo je ", zvolene_slovo)   # toto je len aby sme videli, ako vymiename uz uhadnute pismenka za otazniky
    if pocet_neuhadnutych == 0:                 # Ak sme už uhádli všetky
        vyhra()                                 # zavoláme funkciu s gratuláciou
    elif pocet_zle_zadanych_pismenok >= max_pocet_neuhadnutych:     # Ak sme prekročili maximum povolených neuhádnutých
        prehra()                                # zavoláme funkciu s kondolenciou :)
    print(f"-- pocet_zle_zadanych_pismenok = {pocet_zle_zadanych_pismenok} ")   # iba diagnostická správa do konzoly

# musíme si zadefinovať funkciu pre stlačenie Ok po zadaní písmenka
def ok_bttn():
    pism = pismenko.get()                       # Zoberieme si p9smenko
    print( f"Ok button: Písmenko = {pism or 'Nic'}" )       # iba diagnostická správa do konzoly
    dlzka_pismenka = len( pism )                # ošetrenie ak zadáme viac písmenok
    if( dlzka_pismenka == 1  ):                 # bolo zadané iba jedno
      spracuj_pismenko( pism[0].upper() )       # skonvertujeme na velke a spracujeme ho
    elif( dlzka_pismenka > 1 ):                 # bolo zadaných viacero písmenok
       spracuj_pismenko( pism[dlzka_pismenka-1] )   # zoberie sa iba posledné písmenko a spracujeme ho
    pism=""                                     # vymažeme premennú písmenko
    pismenko.set( "" )                          # vymažeme vstupné pole pre písmenko

def return_event(event):                        # toto je funkcia, ktorú zavoláme, ak buchneme na enter a
    ok_bttn()                                   # ona zavolá to isté, čo je Ok button

# program nam vyberie jedno z cisel z intervalu 1 a pocet slov v zozname
print("Pocet slov:", str(pocet_slov))
print("Zvolene cislo slova:", str(por_cis_slova))
print("Zvolene slovo je ", zvolene_slovo)
print("Dlzka slova je ", str(dlzka_slova))
print("Počet zadaných písmenok:", pocet_zle_zadanych_pismenok )

root = tk.Tk()                                  # Vytvorí sa hlavné okno
root.title("Hangman")                           # Názov hlavného okna
root.geometry("800x360")                        # Nastavíme veľkosť hlavného okna

# pomocne premenne
pismenko = tk.StringVar()                       # Zadeklarujeme si premennú pre vstup písmenka

main_frame = tk.Frame( root )                   # V hlavnom okne sa vytvorí rámik, ktorý je potrebný pre formátovanie
main_frame.pack( side="top", fill="both", expand=True )     # zobrazíme
label_1 = tk.Label( main_frame, text="HANGMAN", font=("Acme 40 "), background="yellow" )    # Vpíšeme aj text HANGMAN
label_1.pack(side="top", expand=False, fill="x", ipadx=10, ipady=10 )   # Zobrazíme
can = tk.Canvas( main_frame, background="#96DED1", width=800, height=180)   # Pripravíme si plachtu na kreslenie

for i in range(0, dlzka_slova ):                # Zobrazíme obdĺžničky
    can.create_rectangle( x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika),
                          y_zaciatok,
                          x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika,
                          y_zaciatok + vyska_obdlznika)
can.pack( side="top", expand=False, fill="x", ipadx=10, ipady=10  )

pism_label = tk.Label( root, text="Zadaj písmenko: " )          # Vypíšeme text "Zadaj písmenko"
pism_label.pack( side="left", padx=10, pady=10, fill="x" )      # Zobrazíme
pism_entry = ttk.Entry( root, width=1, textvariable=pismenko )  # Vytvoríme vstupné pole pre písmenko
pism_entry.pack( side="left" )                                  # Zobrazíme
pism_entry.focus()                                              # Nastavíme fokus na vstupné pole pre písmenko

root.bind( '<Return>', return_event )                           # tu nastavíme, čo má systém robiť, ak stlačíme Ener

bttn_quit = tk.Button( root, text="Quit", command=root.destroy )    # Stlačíme Quit: ukončenie - zahubíme hlavné okno
bttn_quit.pack( side="right", padx=10, pady=10, fill="x", expand=False )    # Zobrazíme

bttn_ok = tk.Button( root, text="Ok", command=ok_bttn )         # Vytvoríme Ok button
bttn_ok.pack( side="right", padx=10, pady=10, fill="x", expand=False )      # Zobrazíme

root.mainloop()  # Spustíme "hlavný cyklus", ktorý nerobí nič, iba čaká na vloženie písmenka, stlačenie buttonu, etc
