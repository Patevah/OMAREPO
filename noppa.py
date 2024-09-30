import tkinter as tk
from random import randint

class NoppaSovellus:
    def __init__(self, ikkuna):
        self.ikkuna = ikkuna
        self.ikkuna.title("Noppasovellus")
        self.ikkuna.minsize(150,100)

        self.tulos_label = tk.Label(ikkuna, text="Tulos näkyy tässä")
        self.tulos_label.pack(pady=10)

        self.heitto_painike = tk.Button(ikkuna, text="Heitä noppaa", command=self.arvo_luku)
        self.heitto_painike.pack()

    def arvo_luku(self):
        tulos = randint(1, 6)
        self.tulos_label.config(text=f"Heitto: {tulos}")

if __name__ == "__main__":
    root = tk.Tk()
    sovellus = NoppaSovellus(root)
    root.mainloop()