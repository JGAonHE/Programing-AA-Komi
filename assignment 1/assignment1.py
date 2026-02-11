"""
The task is to create a program for a retailer that creates an invoice aftger a dialog with the customer.
Name:Komi
Date: 2026-02-5
"""
import storeinforatmion as store
print("Welcome to Komi figure store!")
print("Please tell us your name, phone number and post code")

customer_name = input("Name: ")
customer_phone = input("Phone number: ")
customer_postcode = input("Post code: ")

print(f"First we have {store.product1_name} for ${store.product1_price}")
qty1 = int(input(f"How many {store.product1_name} would you like to buy?(0-10) "))
while qty1 < 0 or qty1 > 10:
    print("Invalid input. Please enter a number between 0 and 10.")
    qty1 = int(input(f"How many {store.product1_name} would you like to buy?(0-10) "))
print(f"Second we have {store.product2_name} for ${store.product2_price}")
qty2 = int(input(f"How many {store.product2_name} would you like to buy?(0-10) "))
while qty2 < 0 or qty2 > 10:
    print("Invalid input. Please enter a number between 0 and 10.")
    qty2 = int(input(f"How many {store.product2_name} would you like to buy?(0-10) "))

print(f"Third we have {store.product3_name} for ${store.product3_price}")
qty3 = int(input(f"How many {store.product3_name} would you like to buy?(0-10) "))
while qty3 < 0 or qty3 > 10:
    print("Invalid input. Please enter a number between 0 and 10.")
    qty3 = int(input(f"How many {store.product3_name} would you like to buy?(0-10) "))

print(f"Fourth we have {store.product4_name} for ${store.product4_price}")
qty4 = int(input(f"How many {store.product4_name} would you like to buy?(0-10) "))
while qty4 < 0 or qty4 > 10:
    print("Invalid input. Please enter a number between 0 and 10.")
    qty4 = int(input(f"How many {store.product4_name} would you like to buy?(0-10) "))

print(f"Fifth we have {store.product5_name} for ${store.product5_price}")
qty5 = int(input(f"How many {store.product5_name} would you like to buy?(0-10) "))
while qty5 < 0 or qty5 > 10:
    print("Invalid input. Please enter a number between 0 and 10.")
    qty5 = int(input(f"How many {store.product5_name} would you like to buy?(0-10) "))

discount_precentage = float(input("What is your discount percentage? (0-100): "))
while discount_precentage < 0 or discount_precentage > 100:
    print("Invalid input. Please enter a number between 0 and 100.")
    discount_precentage = float(input("What is your discount percentage? (0-100): "))



