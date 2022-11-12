colors=["Green", "Blue", "Red", "Black", "White"]
cars=["TATA", "Alto", "Nano"]
players=("Dhoni", "Messi", "Dravid")

colors.insert(2,"Indigo")
colors.append("BMW")
colors.extend(cars)
colors.extend(players)
colors.remove("Red")
colors.pop(3)
print(colors)