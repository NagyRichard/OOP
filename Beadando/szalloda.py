import datetime
datum=datetime.datetime.now()
class Szalloda:
    def __init__(self, name):
        self.name = name 
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def elerheto_szobak(self, szobatipus=None):
        if szobatipus:
            return [szoba for szoba in self.szobak if szoba.szobatipus == szobatipus and not szoba.fogalt]
        else:
            return [szoba for szoba in self.szobak if not szoba.fogalt]
        
    def make_reservation(self, foglalas):
        self.foglalasok.append(foglalas)

    def foglalas_torles(self, reservation_id):
        for foglalas in self.foglalasok:
            if foglalas.id == reservation_id:
                self.foglalasok.remove(foglalas)
                print(f"Foglalás (ID: {reservation_id}) sikeresen törölve.")
                return
        print(f"Nincs ilyen azonosítójú foglalás: {reservation_id}")

class szobak():
    def __init__(self, Szobaszam, szobatipus, ar):
        self.Szobaszam = Szobaszam
        self.szobatipus = szobatipus
        self.ar = ar
        self.fogalt = False

class bad_1(szobak):
    def __init__(self, Szobaszam, ar):
        super().__init__(Szobaszam, "EgyÁgyas", ar)

class bad_2(szobak):
    def __init__(self, Szobaszam, ar):
        super().__init__(Szobaszam, "KétÁgyas", ar)

class Foglalas:
    next_id = 1

    def __init__(self, vendeg_neve, Szobaszam, check_in_date, check_out_date):
        self.id = Foglalas.next_id
        Foglalas.next_id += 1
        self.vendeg_neve = vendeg_neve
        self.Szobaszam = Szobaszam
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def __str__(self):
        return f"Kedves {self.vendeg_neve}! A szobád: {self.Szobaszam}. A foglalásod dátuma {self.check_in_date}-tól {self.check_out_date}-ig. A fogalalás Azonosítója: {self.id}"

# Szálloda létrehozása
hotel = Szalloda('Platán')

# Szobák hozzáadása a szállodához
egyagyas_szoba = bad_1('101', 5000)
ketagyas_szoba1 = bad_2('201', 8000)
ketagyas_szoba2 = bad_2('202', 8000)

hotel.add_szoba(egyagyas_szoba)
hotel.add_szoba(ketagyas_szoba1)
hotel.add_szoba(ketagyas_szoba2)

# Példa foglalás létrehozására
foglalas1 = Foglalas('John Doe', '101', '2024-06-01', '2024-06-05')
foglalas2 = Foglalas('Jane Smith', '201', '2024-06-10', '2024-06-15')

#print(foglalas1)
#print(foglalas2)

# Elérhető szobák lekérdezése
#print("Elérhető szobák:")
#for szoba in available_rooms:
#available_rooms = hotel.elerheto_szobak()
# print(f"Szobaszám: {szoba.Szobaszam}, Típus: {szoba.szobatipus}, Ár: {szoba.ar} Ft")



while True:
        print("1. Elérhető szobák lekérdezése")
        print("2. Foglalás készítése")
        print("3. Foglalás lemondása")
        print("0. Kilépés")

        choice = input("Válassz egy opciót (0-3): ")

        if choice == '1':
            #szobatipus = input("Add meg a keresett szobatípust (Egyágyas/Kétágyas): ")
            available_rooms = hotel.elerheto_szobak()
            if available_rooms:
                print("\nElérhető szobák:")
                for szoba in available_rooms:
                    print(f"Szobaszám: {szoba.Szobaszam}, Típus: {szoba.szobatipus}, Ár: {szoba.ar} Ft")
            else:
                print("Nincsenek elérhető szobák a megadott típusban.")

        elif choice == '2':
            vendeg_neve = input("Add meg a vendég nevét: ")
            Szobaszam = input("Add meg a foglalni kívánt szobaszámot: ")
            Date=False
            while Date == False:
                if check_in_date<datum:
                    check_in_date = input("Add meg a check-in dátumot (YYYY-MM-DD formátumban): ")
                else: Date = True
            while Date == False:
                if check_out_date<=check_in_date:
                    check_out_date = input("Add meg a check-out dátumot (YYYY-MM-DD formátumban): ")
                else: Date=True
                
            foglalas = Foglalas(vendeg_neve, Szobaszam, check_in_date, check_out_date)
            print(f"Foglalás sikeresen létrehozva:\n{foglalas}")
        elif choice =='3':
            reservation_id = input("Add meg a lemondani kívánt foglalás ID-ját: ")
            hotel.foglalas_torles(int(reservation_id))
        


        elif choice == '0':
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérlek válassz újra.")