class Airticket:
    def __init__(self):
        self.bookings = []
        self.routes = {
            ("Dhaka", "Chittagong"): 4500,
            ("Dhaka", "Sylhet"): 5000,
            ("Dhaka", "Cox Bazaar"): 8000,
            ("Chittagong", "Sylhet"): 5500
        }


    def get_cost(self, src, dest):
        if (src, dest)in self.routes:
            return self.routes[(src, dest)]
        elif (dest, src) in self.routes:
            return self.routes[(dest, src)]
        else:
            return None
        
    def book_ticket(self):
        name = input("Passenger Name: ")
        src = input("From: ")
        dest = input("To: ")

        cost = self.get_cost(src, dest)

        if cost is None:
            print("❌ Route not available!\n")
            return
        

        ticket = {
            "name": name,
            "From": src,
            "To": dest,
            "cost": cost
        }
        
        self.bookings.append(ticket)
        print(f"✅ Ticket Booked successfully! Cost: {cost} BDT\n")


    def view_tickets(self):
        if not self.bookings:
            print("❌ No bookings found!\n")
            return
        

        for i, t in enumerate(self.bookings, 1):
           print(f"{i}. {t['name']} | {t['from']} → {t['to']} | Cost: {t['cost']} BDT")
           print()

        
    def compare_cost(self):
        src = input("From: ")
        dest = input("To: ")

        cost = self.get_cost(src, dest)
        if cost:
            print(f"💰 Ticket cost from {src} to {dest}: {cost} BDT\n")
        else:
            print("❌ Route not available!\n")



    def menu(self):
        while True:
            print("✈️ Air Ticket Booking System")
            print("1. Book Tickets")
            print("2. View Tickets ")
            print("3. Compare costs")
            print("4. Exit") 

            choice = input("Choose option: ")


            if choice == "1":
                self.book_ticket()
            elif choice == "2":
                self.view_tickets()
            elif choice == "3":
                self.compare_cost()
            elif choice == "4":
                print("Thank you! 👋")
                break
            else:
                print("Invalid option!\n")


system = Airticket()
system.menu() 