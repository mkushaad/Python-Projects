#Project NUMBER 01
# Monte Hall || BMW is the prize, goats are in the other doors
import random
doors = [0]*3   # total numbers of doors
goatDoors = [0]*2   # doors without the prize
swap_wins = 0
no_swap_wins = 0
j = 0
while j < 10:
    x = random.randint(0,2) # choosing a door for the prize
    doors[x] = "BMW"
    #print("Door in ", x)
    for i in range(0, 3):
        if x == i:
            continue
        else:
            doors[i] = "GOAT"
            goatDoors.append(i)  # inputting indexes where door is goat
    choice = int(input("Enter your choice:"))
    door_open = random.choice(goatDoors)    # opening a door other than BMW one (in index form)
    while door_open == choice:      # making sure that we don't open a door tha tis choice
        door_open = random.choice(goatDoors)
    print("Door ", door_open, " doesnt have the prize.")
    ch = input("Do you want to swap your choice? Y/N")
    if ch == 'Y' or ch == 'y':
        if choice == x:
            print("You Lost!!")
        else:
            print("!!!!!!!!!!You Won")
            swap_wins += 1
    else:
        if choice == x:
            print("You Won!")
            no_swap_wins += 1
        else:
            print("You Lost!!!!!!!!!!!!!!")
    j += 1
print("Swap Wins = ", swap_wins,
      "Non-Sawp Wins = ", no_swap_wins)
