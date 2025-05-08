menu = {
    'Pizza':120,
    'Burger':80,
    'Sandwitch':70,
    'Momos':80,
    'Nuggets':80,
    'Coffee':40,
    'Popcorn':50,
}
print("Welcome to PYTHON Restarent")
print("Pizza : 120\nBurger : 80\nSandwitch : 70\nMomos : 80Nuggets : 80\nCoffee : 40\nPopcorn : 50")
total_order=0
iteam_1=input("Enter name of iteam you want=")
if iteam_1 in menu:
    total_order +=menu[iteam_1]
    print(f"Your iteam{iteam_1}has been added your order")
else:
    print(f"Ordered item{iteam_1}is not avaible yet")
anothe_order=input("Do you want add another iteam? (Yes/No)")
if anothe_order == "Yes":
    iteam_2=input("Enter the iteam two=")
    if iteam_2 in menu:
      total_order += menu[iteam_2]
      print(f"item 2{iteam_2}has been added your order")
    else:
        print(f"iteam two{iteam_2}is not avaible yet")
print(f"The total amout to pay {total_order}")          


