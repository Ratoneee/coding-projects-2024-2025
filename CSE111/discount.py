import datetime

#gets input for the subtotal and sees what today is on the operating system
subtotal = float(input("What is your subtotal? "))
current_day = datetime.datetime.today().weekday()

#sees if subtotal is $50 or greater and checks the today is tuesday or wendsday
def apply_discount(subtotal):
    if subtotal >= 50 and (current_day == 1 or current_day == 2):
        discount = subtotal * 0.10
        subtotal -= discount
        print(f"Great! You qualify for a 10% discount of ${discount:.2f}.")
    else:
        print("You do not qualify for the 10% discount.")
    
    #addes a 6% sales tax to subtotal
    tax = subtotal * 0.06
    total_due = subtotal + tax
    
    #prints sales tax and total amount due with new sales tax added to the total
    print(f"Sales tax: ${tax:.2f}")
    print(f"Total amount due: ${total_due:.2f}")


apply_discount(subtotal)

#code written by Tony V