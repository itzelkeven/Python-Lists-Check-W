foods = ["pizza", "burgers", "steak", "ice cream", "posole", "menudo", "tamales", "tortas"]
print("Third element of list: ", foods[2])
foods.append("tacos")
print("Size of list: ", len(foods))
print("The whole list: ", foods)
print()
print()
print()

petname = []
user = input("What is your pets name?")
while user != 'q':
    petname.append(user)
    user = input("Or type 'q' to quit")

petname.sort()
print("Your entered names: ", petname)

