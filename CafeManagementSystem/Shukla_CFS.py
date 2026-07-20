#define the name of dishes
from tkinter import Menu


Menu={
    'Pizza':50,
    'Pasta':40,
    'Burger':70,
    'Salad':30,
    'Coffee':90

}
print(Menu)
#Greetings
print("Welcome to SHUKLA Cafe!Where Dishes Meets with your Choice")
print("Pizza:Rs.50\nPasta:Rs.40\nBurger:Rs.70\nSalad:Rs.30\nCoffee:Rs.90")
orderTotal=0
item_1=input("Enter your Choice: ")
if item_1 in Menu:
    orderTotal+=Menu[item_1]
    print(f"your dish {item_1} confirm Successfully Please wait for Serve")
else:
    print(f"Oh!Sorry, Currently {item_1} is not available:)")
otherOrder=input("Do You want to choose another Dish? (Yes/No)")
if otherOrder=="Yes":
    item_2=input("Enter your Second choice=")
    if item_2 in Menu:
        orderTotal+=Menu[item_2]
        print(f"Successful!{item_2} is Confirmed")
    else:
        print(f"Oh!Sorry, Currently {item_2} is not available:)")
    
    print(f"Your Total Payment: {orderTotal}")
    print("Thanks for Visit SHUKLA Cafe See you next time")