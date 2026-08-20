"""
5. Movie Ticket Booking System
"""

class Ticket:
    def __init__(self,name,mvi_nm,ttl_seats,):
        self.name=name
        self.mvi_nm=mvi_nm
        self.seats=[]
        self.ttl_seats=ttl_seats
        self.price=[]
    def book(self):
        n=int(input("Enter the no. of seats you want to book: "))
        v=0
        while v<n:
          sts=int(input(f"Enter the {v+1} seat you want to book: "))
          if 0 < sts <= self.ttl_seats:
            print("VALID SEAT NO.")
            if sts in self.seats:
              print("Seat already booked")

            else:
              self.seats.append(sts)
              v+=1
              if 0<sts<=40:             #)
                prce=300                  #)
              elif 40<sts<=80:          #)
                prce=600                 #----> Automatic tiering price
              else:                     #)
                prce=900                  #)
              self.price.append(prce)   #)

              #y=int(input(f"Enter the price of the seat: "))
              #self.price.append(y)
          else:
            print(f"INVALID SEAT NO. (Must be in range 1 to {self.ttl_seats})")
        print(f"\nCustomer : {self.name}\n")
        print(f"Movie Name : {self.mvi_nm}")
        print("Your final booked seats are :\n")
        for i in range(len(self.seats)):
          print(f"{self.seats[i]} : Rs {self.price[i]}")
        print(f"Your total bill is : {sum(self.price)}")

nm=input("Enter your name: ")
mvi=input("Enter the name of the movie: ")
tl_seat=100

tk=Ticket(nm,mvi,tl_seat)
tk.book()
