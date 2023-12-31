# -*- coding: utf-8 -*-
"""AIRLINE_RESERVATION_SYSTEM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RoN5fZsGZtu5cUptx-AtS3wPRqU4yTWi
"""

class Passenger:
    account={}
    def __init__(self,name,dob,nationality,contact,email,password):
        self.__name= name
        self.__dob=dob
        self.__natonality=nationality
        self.__contact=contact
        self.__email=email
        self.__pass=password
        Passenger.account[self.__email]=self.__pass

    def setName(self,name):
        self.__name= name
    def getName(self):
        return self.__name
    def setDob(self,dob):
        self.__dob=dob
    def getDob(self):
        return self.__dob
    def setNationality(self,nationality):
        self.__nationality=nationality
    def getNationality(self):
        return self.__nationality
    def setContact(self,con):
        self.__contact=con
    def getContact(self):
        return self.__contact
    def setEmail(self,em):
        self.__email=em
    def getEmail(self):
        return self.__email
    def setPassword(self,pas):
        self.__pass=pas
    def getPassword(self):
        return self.__pass

    @classmethod
    def signup(cls,name,dob,nat,con,em,pas):
        name=name
        dob=dob
        nationality=nat
        contact=con
        email=em
        password=pas
        obj=cls(name,dob,nationality,contact,email,password)
        return obj

    @staticmethod
    def check_if_mail_in_use_during_signup(em):
        email= em
        if email not in Passenger.account:
            return False
        else:
            return True

    @staticmethod
    def check_if_mail_in_use_during_login(em,ps):
        email= em
        pas=ps
        if email not in Passenger.account and pas not in Passenger.account:
                return False
        else:
            return True

class Reservation:
    def __init__(self,type1,way,date,fro,to,num,code):
        self.type_of_flight=type1
        self.way=way
        self.date=date
        self.source=fro
        self.dest=to
        self.num_of_seats=num
        self.code=code

    @staticmethod
    def confirmation(con):
        obj = con
        if obj == '1':
            return True
        else:
            return False

    def reservationCost(self,a):
        if a=='1':
            if self.way=='oneway':
                price=3000*self.num_of_seats
            elif self.way=='round':
                price=3000*2*self.num_of_seats

        else:
            if self.way=='oneway':
                price=80000*self.num_of_seats
            elif self.way=='round':
                price=80000*2*self.num_of_seats
        return price

class Flight(Reservation):
    def __init__(self):
        self.dc01seats=50
        self.dc02seats=50
        self.cd01seats=50
        self.cd02seats=50
        self.bc01seats=100
        self.cb01seats=100
        self.bu01seats=100
        self.ub01seats=100
    def info(self,f):
        self.f=f
        if self.f=='1':
            for i in range(17,23,1):
                print('#####AVAILABLE DOMESTIC FLIGHTS DURING THIS WEEK#####')
                print(f"DATE: {i}/04/23")
                print('FLIGHT #DC01 | DHK-->CTG :')
                print(f"DEPARTURE: 13:00 BST \\ AVAILABLE SEATS: {self.dc01seats}")
                print('FLIGHT #DC02 | DHK-->CTG :')
                print(f"DEPARTURE: 15:00 BST \\ AVAILABLE SEATS: {self.dc02seats}")
                print('FLIGHT #CD01 | CTG-->DHK :')
                print(f"DEPARTURE: 14:00 BST \\ AVAILABLE SEATS: {self.cd01seats}")
                print('FLIGHT #CD02 | CTG-->DHK :')
                print(f"DEPARTURE: 16:00 BST \\ AVAILABLE SEATS: {self.cd02seats}")
                print('-------------------------------------------------------------------')
        elif self.f=='2':
            for i in range(17,23,1):
                print('#####AVAILABLE INTERNATIONAL FLIGHTS THIS WEEK#####')
                print(f"DATE: {i}/04/23")
                print('FLIGHT #BC01 | BAN-->CAD :')
                print(f"DEPARTURE: 1:00 BST \\ AVAILABLE SEATS: {self.bc01seats}")
                print('FLIGHT #CB01 | CAD-->BAN :')
                print(f"DEPARTURE: 2:00 BST \\ AVAILABLE SEATS: {self.cb01seats}")
                print('FLIGHT #BU01 | BAN-->USA :')
                print(f"DEPARTURE: 4:00 BST \\ AVAILABLE SEATS: {self.bu01seats}")
                print('FLIGHT #UB01 | USA-->BAN :')
                print(f"DEPARTURE: 6:00 BST \\ AVAILABLE SEATS: {self.ub01seats}")
                print('---------------------------------------------------------------------')

class Ticket(Reservation):
     def __init__(self,type1,way,date,fro,to,num,code):
        super().__init__(type1,way,date,fro,to,num,code)

     def details(self,price):
       if  self.num_of_seats>50:
           print('Sorry. There are not suffecient seats in this aircraft')

       else:
         self.price=price
         if len(self.date)==1:
             print('------------------------------------------------------------')
             print('Flight Date:',self.date[0])
             print(f"From {self.source}")
             print(f"To {self.dest}")
         elif len(self.date)==2:
             print('------------------------------------------------------------')
             print(f"Departure Date:{self.date[0]} \nFrom {self.source} To {self.dest}")
             print(f"Arrival Date:{self.date[1]} \nFrom {self.dest} To {self.source}")
         print(f"Ticket Price: {self.price}")
         print('------------------------------------------------------------')

class Payment(Reservation):
    def __init__(self,type1,way,date,fro,to,num,code,cost):
        super().__init__(type1,way,date,fro,to,num,code)
        self.price=cost
        self.og=cost

    def paymentMethod(self,a):
        if a=='1':
            self.method='Card'
        elif a=='2':
            self.method='Mobile Banking'
        return self.method

    def check_discount(self,a):
        op=a
        if self.method=='Card':
            if op=='1':
                print('####CONGRATULATIONS! You are a City AMEX Card Holder. You will enjoy 10% discount on your total cost.####')
                self.discount= (self.price*(10/100))
                self.price= self.price-self.discount
            else:
                print('We do not have any discount for the following operator. Please proceed')
                self.discount=0
        else:
            if op=='1':
                print('####CONGRATULATIONS! You are a Bkash user. You will enjoy 10% discount on your total cost.#####')
                self.discount= (self.price*(10/100))
                self.price= self.price-self.discount
            else:
                print('We do not have any discount for the following operator. Please proceed')
                self.discount=0

    def finalInvoice(self,a):
        way=a
        if self.type_of_flight==1:
            print('Flight Type: Domestic')
        else:
            print('Flight Type: International')
        print(f"Trip Type: {way}")
        print(f"Flight No.: {self.code}")
        if way=='oneway':
            print('Flight Date:',self.date[0])
            print(f"From {self.source}")
            print(f"To {self.dest}")
        else:
             print(f"Departure Date:{self.date[0]} \nFrom {self.source} To {self.dest}")
             print(f"Arrival Date:{self.date[1]} \nFrom {self.dest} To {self.source}")
        print('Original Ticket Price:',self.og,'BDT')
        print(f"Total Discount: {self.discount} BDT")
        print(f"Final Price:{self.price} BDT")

print('Welcome!')
flag1=True
flag2= True
while flag2==True:
    ans= input('Enter 1 to signup and 2 to login:')
    if ans=='1':
        print('Your Signup Procedure Starts!')
        name=input('Enter name:')
        dob=input('Enter date of birth(DD/MM/YY):')
        nat=input('Enter Nationality:')
        con=input("Enter contact number:")
        email1=input('Enter Email:')
        password1=input('Enter Password:')
        Passenger.signup(name,dob,nat,con,email1,password1)
        flag1= Passenger.check_if_mail_in_use_during_signup(email1)
        if flag1==False:
            print('This mail is already in use. Please login or try another')
        else:
            print("Signup Successful! Please login again!")
    elif ans=='2':
        print('Your Login Procedure Starts')
        attempts=0
        while attempts<3:
            email2=input('Enter Email:')
            password2=input('Enter Password:')
            attempts+=1
            flag1= Passenger.check_if_mail_in_use_during_login(email2,password2)
            if flag1== True:
                print('Login Successful!')
                flag2= False
                break
            else:
                print('Invalid mail. Please try again')
        if flag2== True:
            print('Your email does not exist. Please try signing up.')
print('You are verified! Please Proceed.')
type1=input("What type of flight do you want to avail? Press 1 for Domestic and 2 for International:")
f1=Flight()
f1.info(type1)
while True:
    way=input('What kind of trip will it be? Press 1 for one-way trip and Press 2 for a round trip:')
    if way=='1':
        triptype='oneway'
        date1=input('Select date to travel(DD/MM/YY):')
        date=[date1]
    else:
        triptype='round'
        date1=input('Select date of Departure(DD/MM/YY):')
        date2=input('Select date of Arrival(DD/MM/YY):')
        date=[date1,date2]
    source=input('Select Source(eg.-DHK,CTG,CAD,USA):')
    #source= source.lower()
    dest=input('Select Destination(eg.-DHK,CTG,CAD,USA):')
    #dest= dest.lower()
    number=int(input('How many tickets do you want to book?'))
    code=input('Kindly enter the flight code of your desired flight(eg.- CD02,UB01):')
    break


r=Reservation(type1,triptype,date,source,dest,number,code)
cost= r.reservationCost(type1)
#print(cost)
flag3= True
con=input(f"Do you want to confirm your reservation?Press 1 to confirm, 2 to discard(WARNING: You will lose all your progress if you discard)")
flag3=r.confirmation(con)
while flag3==True:
    if flag3==True:
        print('Your Reservation Has Been Confirmed! Please proceed to see the ticket price')
        price=Ticket(type1,triptype,date,source,dest,number,code)
        price.details(cost)
        ques=input('Do you want to proceed with the payment? Press 1 to book your reservation, Press 2 to cancel your reservation:')
        if ques=='1':
            pay=Payment(type1,triptype,date,source,dest,number,code,cost)
            m=input('Please choose a payment method. Press 1 for Card Payment,2 for Mobile Banking: ')
            method=pay.paymentMethod(m)
            if method=='Card':
                print('Choose Your designated bank from the following:')
                bank=input('For City Bank press 1, For Brac bank press 2, For UCB Bank press 3, For Bank Asia press 4')
                pay.check_discount(bank)
            else:
                print('Choose the following mobile banking:')
                mob=input('For Bkash press 1,For Nagad press 2, For Rocket press 3, for Upay press 4')
                pay.check_discount(mob)
            print('========================================================')
            print('YOUR BOOKING HAS BEEN COMPLETED SUCCESSFULLY!')
            print(f"Name:{name}")
            print(pay.finalInvoice(triptype))
            print('========================================================')
            print('THANK YOU FOR BOOKING YOUR FLIGHT WITH US! FLY SAFE')
            break
        else:
            print('Your Reservation has been cancelled. You will be redirected to login page')
            flag3= False
    else:
        print('Your Reservation Has Been Cancelled! You will be redirected to the login page')
        break

