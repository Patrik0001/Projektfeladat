import tkinter as tk
import datetime
import pm_modul


class PMKontakt:
    def __init__(self, nev, tel):
        self.nev = nev
        self.tel = tel

    def __str__(self):
        return f"{self.nev} - {self.tel}"


FAJL = "contacts.txt"

def mentes_fajlba(nev, tel):

    with open(FAJL, "a", encoding="utf-8") as f:
        f.write(f"{nev};{tel}\n")

def betoltes_fajlbol():

    try:
        with open(FAJL, "r", encoding="utf-8") as f:
            return [sor.strip().split(";") for sor in f if ";" in sor]
    except FileNotFoundError:
        return []


root = tk.Tk()
root.title("PM Névjegy-kezelő")

nev_entry = tk.Entry(root)
nev_entry.pack(pady=2)

tel_entry = tk.Entry(root)
tel_entry.pack(pady=2)

lista = tk.Listbox(root, width=40)
lista.pack(pady=5)


def hozzaadas():
    nev = nev_entry.get()
    tel = tel_entry.get()
    if nev and tel:
        kontakt = PMKontakt(nev, tel)
        lista.insert(tk.END, str(kontakt))
        mentes_fajlba(nev, tel)
        nev_entry.delete(0, tk.END)
        tel_entry.delete(0, tk.END)

gomb = tk.Button(root, text="Hozzáadás", command=hozzaadas)
gomb.pack(pady=2)

def betoltes():
    lista.delete(0, tk.END)
    adatok = betoltes_fajlbol()
    for nev, tel in adatok:
        lista.insert(tk.END, f"{nev} - {tel}")

betolt_gomb = tk.Button(root, text="Betöltés", command=betoltes)
betolt_gomb.pack(pady=2)


label = tk.Label(root, text=f"Dátum: {datetime.date.today()}")
label.pack(pady=5)


atlag_label = tk.Label(root, text=f"Átlag példa: {pm_modul.pm_szamolas([3, 6, 9])}")
atlag_label.pack(pady=5)

root.mainloop()

