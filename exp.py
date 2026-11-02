movies=["Bahubali","dhrishyam","premam","premalu","lucifer"]
ticket_price=(120,300,150,170,250,)

print("available movies:")

for i in range(len(movies)):
    print(movies[i], "- *",ticket_price[i])



movies=input("enter movie name:")
if movies in movies:
    index=movies.index(movies)
    ticket=int(input("enter number of tickets:"))
    total=ticket_price[index] * ticket

    print("movie:",movies.upper())
    print("total cost: *",total)

else:
    print("movie not available")


