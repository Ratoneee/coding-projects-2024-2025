import csv
import os
from datetime import datetime

def read_dictionary(filename, key_column_index):
    product_dict = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                key = row[key_column_index]
                product_dict[key] = row
    except FileNotFoundError:
        print(f"error: the file {filename} was not found.")
        exit()
    return product_dict

def main():
    print("Inkom Emporium")
    
    products_dict = read_dictionary('products.csv', 0)
    
    current_time = datetime.now().strftime("%A %I:%M %p")
    
    print(f"Date & Time: {current_time}")
    
    total_items = 0
    subtotal = 0.0
    try:
        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            print("\nRequested Items:")
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                
                try:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    price = float(product_info[2])
                    
                    total_items += quantity
                    item_total = quantity * price
                    subtotal += item_total
                    
                    print(f"{product_name}: {quantity} @ {price:.2f} = {item_total:.2f}")
                except KeyError:
                    print(f"error: product number {product_number} not found.")
        
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        
        print(f"\nTotal Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax (6%): {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        
        print("\nThank you for shopping with us!")
        
        print("\nReminder: Our New Year's Sale begins on January 1st!")
        
    except FileNotFoundError:
        print("error: the file request.csv was not found.")
        exit()

if __name__ == "__main__":
    main()
