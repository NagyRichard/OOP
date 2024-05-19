import datetime

datum = datetime.datetime.now().strftime('%Y-%m-%d')

class Szalloda:
    def __init__(self, name):
        self.name = name
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def elerheto_szobak(self, szobatipus=None):
        if szobatipus:
            return [szoba for szoba in self.szobak if szoba.szobatipus == szobatipus and not szoba.foglalt]
        else:
            return [szoba for szoba in self.szobak if not szoba.foglalt]

    def make_reservation(self, foglalas):
        self.foglalasok.append(foglalas)
        for szoba in self.szobak:
            if szoba.Szobaszam == foglalas.Szobaszam:
                szoba.foglalt = True
                break

    def foglalas_torles(self, reservation_id):
        for foglalas in self.foglalasok:
            if foglalas.id == reservation_id:
                self.foglalasok.remove(foglalas)
                for szoba in self.szobak:
                    if szoba.Szobaszam == foglalas.Szobaszam:
                        szoba.foglalt = False
                        break
                print(f"Foglalás (ID: {reservation_id}) sikeresen törölve.")
                return
        print(f"Nincs ilyen azonosítójú foglalás: {reservation_id}")

class szobak:
    alap_ar = 10000  # Alap ár egyágyas szobára

    def __init__(self, Szobaszam, szobatipus):
        self.Szobaszam = Szobaszam
        self.szobatipus = szobatipus
        self.ar = self.set_ar()
        self.foglalt = False

    def set_ar(self):
        if self.szobatipus == "KétÁgyas":
            return int(szobak.alap_ar * 1.2)
        return szobak.alap_ar

class bad_1(szobak):
    def __init__(self, Szobaszam):
        super().__init__(Szobaszam, "EgyÁgyas")

class bad_2(szobak):
    def __init__(self, Szobaszam):
        super().__init__(Szobaszam, "KétÁgyas")

class Foglalas:
    next_id = 1

    def __init__(self, vendeg_neve, Szobaszam, check_in_date, check_out_date, ar_per_night):
        self.id = Foglalas.next_id
        Foglalas.next_id += 1
        self.vendeg_neve = vendeg_neve
        self.Szobaszam = Szobaszam
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.ar_per_night = ar_per_night
        self.total_ar = self.calculate_total_ar()
        self.foglalt = True

    def calculate_total_ar(self):
        num_nights = (self.check_out_date - self.check_in_date).days
        return self.ar_per_night * num_nights

    def __str__(self):
     return (f"Kedves {self.vendeg_neve}! A foglalásod sikeres volt. \n"
            f"A szobád: {self.Szobaszam}. \n"
            f"A foglalásod dátuma {self.check_in_date.strftime('%Y-%m-%d')}-tól {self.check_out_date.strftime('%Y-%m-%d')}-ig. \n"
            f"A foglalás Azonosítója: {self.id}. \n"
            f"A foglalás ára: {self.total_ar} Ft.\n")
# Szálloda létrehozása
hotel = Szalloda('Platán')

# Szobák hozzáadása a szállodához
Szoba_101 = bad_1('101')
Szoba_102 = bad_1('102')
Szoba_103 = bad_1('103')
Szoba_201 = bad_2('201')
Szoba_202 = bad_2('202')
Szoba_203 = bad_2('203')
Szoba_204 = bad_1('204')

hotel.add_szoba(Szoba_101)
hotel.add_szoba(Szoba_102)
hotel.add_szoba(Szoba_103)
hotel.add_szoba(Szoba_201)
hotel.add_szoba(Szoba_202)
hotel.add_szoba(Szoba_203)
hotel.add_szoba(Szoba_204)

# Példa foglalás létrehozására
foglalas1 = Foglalas('John Doe', '101', datetime.datetime.strptime('2024-06-01', '%Y-%m-%d'), datetime.datetime.strptime('2024-06-05', '%Y-%m-%d'), Szoba_101.ar)
foglalas3 = Foglalas('Teszt User', '102', datetime.datetime.strptime('2024-06-02', '%Y-%m-%d'), datetime.datetime.strptime('2024-06-03', '%Y-%m-%d'), Szoba_102.ar)
foglalas2 = Foglalas('Jane Smith', '201', datetime.datetime.strptime('2024-06-10', '%Y-%m-%d'), datetime.datetime.strptime('2024-06-15', '%Y-%m-%d'), Szoba_201.ar,)
hotel.make_reservation(foglalas1)
hotel.make_reservation(foglalas2)

#Kezelői felület:
while True:
    print("1. Elérhető szobák lekérdezése")
    print("2. Foglalás készítése")
    print("3. Foglalás lemondása")
    print("0. Kilépés")

    choice = input("Válassz egy opciót (0-3): ")
#szoobák lekérdezése
    if choice == '1':
        available_rooms = hotel.elerheto_szobak()
        if available_rooms:
            print("\nElérhető szobák:")
            for szoba in available_rooms:
                print(f"Szobaszám: {szoba.Szobaszam}, Típus: {szoba.szobatipus}, Ár: {szoba.ar} Ft")
        else:
            print("Nincsenek elérhető szobák a megadott típusban.")
#Új foglalás /dátum ellenörzés
    elif choice == '2':
        vendeg_neve = input("Add meg a vendég nevét: ")
        Szobaszam = input("Add meg a foglalni kívánt szobaszámot: ")

        Date = False
        while Date == False:
            check_in_date = input("Add meg a check-in dátumot (YYYY-MM-DD formátumban): ")
            try:
                check_in_date = datetime.datetime.strptime(check_in_date, '%Y-%m-%d')
                if check_in_date < datetime.datetime.strptime(datum, '%Y-%m-%d'):
                    print("A bejelentkezési dátum nem lehet korábbi, mint a mai dátum.")
                else:
                    Date = True
            except ValueError:
                print("Hibás dátumformátum. Kérlek, próbáld újra.")

        Date = False
        while Date == False:
            check_out_date = input("Add meg a check-out dátumot (YYYY-MM-DD formátumban): ")
            try:
                check_out_date = datetime.datetime.strptime(check_out_date, '%Y-%m-%d')
                if check_out_date <= check_in_date:
                    print("A kijelentkezési dátum nem lehet korábbi vagy azonos a bejelentkezési dátummal.")
                else:
                    Date = True
                    # Keressük meg a szoba árát
                    ar_per_night = None
                    for szoba in hotel.szobak:
                        if szoba.Szobaszam == Szobaszam:
                            ar_per_night = szoba.ar
                            break
                    if ar_per_night is None:
                        print("Nincs ilyen szobaszám. Kérlek, próbáld újra.")
                        continue

                    foglalas = Foglalas(vendeg_neve, Szobaszam, check_in_date, check_out_date, ar_per_night)
                    hotel.make_reservation(foglalas)
                    print(f"Foglalás sikeresen létrehozva:\n{foglalas}")
            except ValueError:
                print("Hibás dátumformátum. Kérlek, próbáld újra.")
#foglalás törlés
    elif choice == '3':
        reservation_id = input("Add meg a lemondani kívánt foglalás ID-ját: ")
        hotel.foglalas_torles(int(reservation_id))

    elif choice == '0':
        print("Kilépés...")
        break

    else:
        print("Érvénytelen választás. Kérlek válassz újra.")