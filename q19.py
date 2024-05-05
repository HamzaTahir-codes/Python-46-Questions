def bottle_of_beers(num_bottle):
    verse = []

    for i in range(num_bottle, 0, -1):
        if i == 1:
            verse.append(f"{i} bottles of beer on the wall,{i} bottles of beer.")
            verse.append(f"Take one down, pass it around,no more bottles of beer on the wall.")
        elif i == 2:
            verse.append(f"{i} bottles of beer on the wall,{i} bottles of beer.")
            verse.append(f"Take one down, pass it around,1 bottle of beer on the wall.")
        else:
            verse.append(f"{i} bottles of beer on the wall,{i} bottles of beer.")
            verse.append(f"Take one down, pass it around,{i - 1} bottles of beer.")
        verse.append("")
    verse.append("No more bottles of beer on the wall, no more bottles of beer.")
    verse.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return verse


numbers = int(input("Enter number of bottles:"))
for j in bottle_of_beers(numbers):
    print(j)
