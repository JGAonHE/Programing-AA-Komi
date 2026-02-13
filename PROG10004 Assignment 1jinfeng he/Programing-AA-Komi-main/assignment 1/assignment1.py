"""
The task is to create a program for a retailer that creates an invoice aftger a dialog with the customer.
Name:Komi
Date: 2026-02-5
"""
import storeinforatmion as store

#Ask the user for their name, phone number and post code
print("Welcome to Komi figure store!")
print("Please tell us your name, phone number and post code")

customer_name = input("Name: ")
customer_phone = input("Phone number: ")
customer_postcode = input("Post code: ")

#ask the user how many of each product they want to buy and validate the input
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

#line total
line_total1 = qty1 * store.product1_price
line_total2 = qty2 * store.product2_price
line_total3 = qty3 * store.product3_price 
line_total4 = qty4 * store.product4_price
line_total5 = qty5 * store.product5_price
subtotal = line_total1 + line_total2 + line_total3 + line_total4 + line_total5

tax_rate_amount = subtotal * store.tax_rate
total_with_tax = subtotal + tax_rate_amount

#discount
discount_rate = discount_precentage / 100
discount_amount = total_with_tax * discount_rate

final_price = total_with_tax - discount_amount

print("\n" + "=" * 55)
print("Receipt / Invoicei")
print("=" * 55)

#Customer and store information line
print("Store information")
print(" Store: "+ store.store_name)
print(" Address: "+ store.store_address)
print(" Phone: "+ store.store_phone)
print("_" * 55)
print("Customer information") 
print(" name: "+ customer_name) 
print(" phone number: "+ customer_phone) 
print(" post code: "+ customer_postcode)

#print the invoice with the product name, quantity, price and line total for each product, then print the subtotal, tax amount, total with tax, discount amount and final price. Format the output to look like a receipt.
print("-" * 55)
print(f"{'Product':<25}{'Qty':>5}{'Price':>10}{'Line Total':>15}")
print("-" * 55)


print(f"{store.product1_name:<25}{qty1:>5}{store.product1_price:>10.2f}{line_total1:>12.2f}")
print(f"{store.product2_name:<25}{qty2:>5}{store.product2_price:>10.2f}{line_total2:>12.2f}")
print(f"{store.product3_name:<25}{qty3:>5}{store.product3_price:>10.2f}{line_total3:>12.2f}")
print(f"{store.product4_name:<25}{qty4:>5}{store.product4_price:>10.2f}{line_total4:>12.2f}")
print(f"{store.product5_name:<25}{qty5:>5}{store.product5_price:>10.2f}{line_total5:>12.2f}")

print("-" * 55)
print(f"{'Subtotal':<35}${subtotal:>10.2f}")
print(f"{'Tax':<35}${tax_rate_amount:>10.2f}")
print(f"{'Total with tax':<35}${total_with_tax:>10.2f}")
print(f"{'Discount':<35}${discount_amount:>10.2f}")
print("=" * 55)
print(f"{'Final price':<35}${final_price:>10.2f}")
print("=" * 55)

print("Thank you for shopping with us!")





