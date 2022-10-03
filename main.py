import tkinter as tk
from tkinter import ttk
from random import randint

# inicializacie premennych
max_pocet_neuhadnutych = 10
x_zaciatok = 100
y_zaciatok = 50
sirka_obdlznika = 45
vyska_obdlznika = 100
medzera_medzi_obdlznikmi = 5
zoznam_slov = ["strom", "jahoda", "matematika", "zemegula", "traktor", "bager", "tchor"]
pocet_slov = len(zoznam_slov)

# vyber konkretneho slova
por_cis_slova = randint(1, pocet_slov)
zvolene_slovo = zoznam_slov[por_cis_slova - 1]
dlzka_slova = len(zvolene_slovo)
pocet_neuhadnutych = dlzka_slova
pocet_zadanych_pismenok = 0

def spracuj_pismenko( p ):
    global pocet_zadanych_pismenok
    global pocet_neuhadnutych
    global max_pocet_neuhadnutych
    print(f"Funkcia: spracuj_pismenko( {p or 'Nic'} )")
    print(f"-- pocet_zadanych_pismenok = {pocet_zadanych_pismenok} ")
    pocet_zadanych_pismenok += 1
    pocet_neuhadnutych_pred = pocet_neuhadnutych
    if pocet_neuhadnutych > 0 and pocet_zadanych_pismenok < max_pocet_neuhadnutych:
        for j in range(0, dlzka_slova ):
            if zvolene_slovo[j] == p:
                pocet_neuhadnutych -= 1
    #           can.create_text(x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika / 2,
    #                            y_zaciatok + vyska_obdlznika / 2.25, text=".", fill="#96DED1", font=("Acme 28 "))
                can.create_text(x_zaciatok + j * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika / 2,
                                y_zaciatok + vyska_obdlznika / 2, text=p, fill="green", font=("Acme 28 "))
                can.pack()
    if pocet_neuhadnutych_pred > pocet_neuhadnutych:
        pocet_zadanych_pismenok -=1
    if pocet_neuhadnutych == 0:
        print("Gratulujem, vyhral si.")
        root.destroy()
    elif pocet_zadanych_pismenok >= max_pocet_neuhadnutych:
        print( "Prehral si." )
        root.destroy()

def ok_bttn():
    pism = pismenko.get()
    print( f"Ok button: Písmenko = {pism or 'Nic'}" )
    dlzka_pismenka = len( pism )
    if( dlzka_pismenka == 1  ):
      spracuj_pismenko( pism[0] )
    elif( dlzka_pismenka > 1 ):
       spracuj_pismenko( pism[dlzka_pismenka-1] )
    pism=""

def return_event(event):
    ok_bttn()

# program nam vyberie jedno z cisel z intervalu 1 a pocet slov v zozname
print("Pocet slov:", str(pocet_slov))
print("Zvolene cislo slova:", str(por_cis_slova))
print("Zvolene slovo je ", zvolene_slovo)
print("Dlzka slova je ", str(dlzka_slova))
print("Počet zadaných písmenok:", pocet_zadanych_pismenok )

root = tk.Tk()
root.title("Hangman")
root.geometry("800x340")

# pomocne premenne
pismenko = tk.StringVar()

main_frame = tk.Frame( root )
main_frame.pack( side="top", fill="both", expand=True )

label_1 = tk.Label( main_frame, text="HANGMAN", font=("Acme 40 "), background="yellow" )
label_1.pack(side="top", expand=False, fill="x", ipadx=10, ipady=10 )

can = tk.Canvas( main_frame, background="#96DED1", width=800, height=180)

for i in range(0, dlzka_slova ):
    can.create_rectangle(x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika),
                             y_zaciatok,
                             x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika,
                             y_zaciatok + vyska_obdlznika)
    #can.create_text( x_zaciatok + i * (medzera_medzi_obdlznikmi + sirka_obdlznika) + sirka_obdlznika / 2,
    #                         y_zaciatok + vyska_obdlznika / 2.25,  text=".", fill="blue", font=("Acme 28 "))

can.pack( side="top", expand=False, fill="x", ipadx=10, ipady=10  )

pism_label = tk.Label( root, text="Zadaj písmenko: " )
pism_label.pack( side="left", padx=10, pady=10, fill="x" )

pism_entry = ttk.Entry( root, width=1, textvariable=pismenko )
pism_entry.pack( side="left" )
pism_entry.focus()

root.bind( '<Return>', return_event )

bttn_quit = tk.Button( root, text="Quit", command=root.destroy )
bttn_quit.pack( side="right", padx=10, pady=10, fill="x", expand=False )

bttn_ok = tk.Button( root, text="Ok", command=ok_bttn )
bttn_ok.pack( side="right", padx=10, pady=10, fill="x", expand=False )

root.mainloop()







