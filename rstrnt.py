food=["dosa","biriyani","soup","burger","pizza"]
price=(120,180,400,300,789)


print("restaurant menu")


for i in range(len(food)):
    print(food[i], "* ",price[i])

choice=input("enter food items:")

if choice in food:
    index=food.index(choice)
    quantity=int(input("enter quantity:" ))


    total=price[index]*quantity
    print("food:",choice)
    print("total price: *",total)

    if total>500:
        print("order amount is above $500")
    else:
        print("order amount is $500 or below")
else:
    print("food item  not avaialable")