import datetime

datum = datetime.datetime.now().strftime('%Y-%m-%d')

class Szalloda:
    def __init__(self, name):
        self.name = name
        self.szobak = []
        self.foglalasok = []
#szoba hozzáadása
    def add_szoba(self, szoba):
        self.szobak.append(szoba)
#szobák lekérdezése
    def elerheto_szobak(self, szobatipus=None):
        if szobatipus:
            return [szoba for szoba in self.szobak if szoba.szobatipus == szobatipus and not szoba.foglalt]
        else:
            return [szoba for szoba in self.szobak if not szoba.foglalt]
#szobafoglalás
    def make_reservation(self, foglalas):
        self.foglalasok.append(foglalas)
        for szoba in self.szobak:
            if szoba.Szobaszam == foglalas.Szobaszam:
                szoba.foglalt = True
                break
#Foglalások törlése
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
    def __init__(self, Szobaszam, szobatipus, ar):
        self.Szobaszam = Szobaszam
        self.szobatipus = szobatipus
        self.ar = ar
        self.foglalt = False
    alap_ar = 10000  # Szobák alap ára
 #    def set_ar(self):
 #       if self.szobatipus == "KétÁgyas":
 #           return int(szobak.alap_ar * 1.2)
 #      return szobak.alap_ar
 #szoba osztályok
class bad_1(szobak):
    def __init__(self, Szobaszam,):
        super().__init__(Szobaszam, "EgyÁgyas", "10000" )
        


class bad_2(szobak):
    def __init__(self, Szobaszam,):
        super().__init__(Szobaszam, "KétÁgyas", "12000" )

#foglalási azonosító
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
        return (f"Kedves {self.vendeg_neve}! A foglalásod sikeres volt. "
            f"A szobád: {self.Szobaszam}. "
            f"A foglalásod dátuma {self.check_in_date.strftime('%Y-%m-%d')}-tól {self.check_out_date.strftime('%Y-%m-%d')}-ig. "
            f"A foglalás Azonosítója: {self.id}. "
            f"A foglalás ára: {self.ar} Ft.")
# Szálloda létrehozása
hotel = Szalloda('Platán')

# Szobák hozzáadása a szállodához
egyagyas_szoba = bad_1('101')
ketagyas_szoba1 = bad_2('201')
ketagyas_szoba2 = bad_2('202')

hotel.add_szoba(egyagyas_szoba)
hotel.add_szoba(ketagyas_szoba1)
hotel.add_szoba(ketagyas_szoba2)

# Példa foglalás létrehozására
foglalas1 = Foglalas('John Doe', '101', datetime.datetime.strptime('2024-06-01', '%Y-%m-%d'), datetime.datetime.strptime('2024-06-05', '%Y-%m-%d'))
foglalas2 = Foglalas('Jane Smith', '201', datetime.datetime.strptime('2024-06-10', '%Y-%m-%d'), datetime.datetime.strptime('2024-06-15', '%Y-%m-%d'))

#Konzol Felület
while True:
    print("1. Elérhető szobák lekérdezése")
    print("2. Foglalás készítése")
    print("3. Foglalás lemondása")
    print("0. Kilépés")

    choice = input("Válassz egy opciót (0-3): ")
# Elérhető szobák
    if choice == '1':
        available_rooms = hotel.elerheto_szobak()
        if available_rooms:
            print("\nElérhető szobák:")
            for szoba in available_rooms:
                print(f"Szobaszám: {szoba.Szobaszam}, Típus: {szoba.szobatipus}, Ár: {szoba.ar} Ft")
        else:
            print("Nincsenek elérhető szobák a megadott típusban.")

# Foglalás dátum ellenörzéssel
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
                    foglalas = Foglalas(vendeg_neve, Szobaszam, check_in_date, check_out_date)
                    hotel.make_reservation(foglalas)
                    print("Foglalás sikeresen létrehozva:\n{foglalas}")
            except ValueError:
                print("Hibás dátumformátum. Kérlek, próbáld újra.")

#Foglalás törlése
    elif choice == '3':
        reservation_id = input("Add meg a lemondani kívánt foglalás ID-ját: ")
        hotel.foglalas_torles(int(reservation_id))

    elif choice == '0':
        print("Kilépés...")
        break

    else:
        print("Érvénytelen választás. Kérlek válassz újra.")