# This game was written by me
# John
print("Welcome to Adventure Game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

# Variable
peva = "Please Enter Valid Answer."

# Permission to play game (OLD ENOUGH OR NOT) 1
if age >= 18:
    print("You are old enough to Play!")

    # Asking player to play 1
    want_to_play = input("Do you want to play? (yes/no) ").lower()
    if want_to_play == "yes":
        print("Let's Play!")

        # Asking player wanna go left or right 1
        left_or_right = input("Do you want to go left or right? (left/right) ").lower()
        if left_or_right == "left":

            # Asking player wanna go tracks or woods 1
            train_track_or_woods = input("You saw train tracks and woods... Which one you choose? (track/woods) ").lower()
            if train_track_or_woods == "track":
                x1 = input("You go along that train tracks it takes 1 hour walk... (Press Enter to continue)")

                # Asking player wanna go bridge or lake 1
                bridge_or_lake = input("You saw bridge and lake.. Which one you choose? (bridge/lake) ").lower()
                if bridge_or_lake == "lake":

                    # Asking player wanna swim or go around 1
                    left_lake = input("Do you want to swim or go around? (swim/around) ").lower()
                    if left_lake == "around":
                        print("To be Continue...")

                    # Asking Player wanna swim or go around 2    
                    elif left_lake == "swim":
                        print("You drown and DIE!!!")
                    else:
                        print(peva)

                # Asking player wanna go bridge or lake 2
                elif bridge_or_lake == "bridge":
                    print("You got hit by a train in the bridge and DIE!!!")       
                else:
                    print(peva)

            # Asking player wanna go tracks or woods 2        
            elif train_track_or_woods == "woods":
                x7 = input("You went into deep woods. Suddenly, you came across abandon bus. (Press Enter to continue)")
                x8 = input("The bus looks so old. It's look like from 90s (Press Enter to continue)")
                x9 = input("Suddenly, You felt the water drop on your skin. Before you could react. (Press Enter to continue) ")
                x10 = input("The rain pouring so heavily... (Press Enter to continue)")

                # Asking player wanna go inside the bus or stay 1
                bus_stay = input("Which one choose? (bus/stay) ")
                if bus_stay == "bus":
                    print("To Be Continue...")

                # Asking player wanna go inside the bus or stay 2
                elif bus_stay == "stay":
                    print("You got eaten by wolf pack in the woods...DIE!!!")
                else:
                    print(peva)

            # Asking player wanna go tracks or woods 3    
            else:
                print(peva)

        # Asking player wanna go left or right 2            
        elif left_or_right == "right":

            # Asking player swim or around 1
            right_lake = input("You saw a lake.. You swim or go around? (swim/around) ").lower()
            if right_lake == "around":

                # Asking player house or barn 1
                x2 = input("You go around and saw house and barn. (Press Enter to continue)")
                house_barn = input("Which one you choose? (house/barn)")
                if house_barn == "barn":
                    x3 = input("You arrived at the barn at night. (Press Enter to continue)")
                    x4 = input("You was looking around and you found a path to the woods. (Press Enter to continue)")

                    # Asking player wanna stay at the barn or not 1
                    stay_woods_1 = input("Which one you choose? (stay/woods) ").lower()
                    if stay_woods_1 == "stay":

                        # Asking player wanna stay or woods 1
                        x5 =input("You woke up early and saw path to the woods very clearly. (Press Enter to continue)")
                        stay_woods_2 = input("Which one you choose? (stay/woods) ").lower()
                        if stay_woods_2 == "woods":
                            x6 = input("You've been walking an hour into the woods. (Press Enter to continue)")

                            # Asking player wanna go inside or stay 1
                            inside_stay = input("Then you found abandon house. You wanna go inside or stay away from it? (inside/stay) ")
                            if inside_stay == "inside":
                                print("To Be Continue...")

                            # Asking player wanna go inside or stay 2
                            elif inside_stay == "stay":
                                print("You got eaten by wolf pack in the woods...DIE!!!")
                            else:
                                print(peva)

                        # Asking player wanna stay or woods 2
                        elif stay_woods_2 == "stay":
                            print("You got killed by crazy man...DIE!!!")
                        else:
                            print(peva)

                    # Asking player wanna stay at the barn or not 2
                    elif stay_woods_1 == "woods":
                        print("You got eaten by wolf pack in the woods...DIE!!!")
                    else:
                        print(peva)

                # Asking player house or barn 2
                elif house_barn == "house":
                    print("You got killed by crazy man... DIE!!!")
                else:
                    print(peva)

            # Asking player swim or around 2
            elif right_lake == "swim":
                print("You drown and DIE!!!")
            else:
                print(peva)

        # Asking player wanna go left or right 3
        else:
            print(peva)

    # Asking player to play 2
    elif want_to_play == "no":
        print("Shutdown!!!")
    else:
        print(peva)

# Permission to play game (OLD ENOUGH OR NOT) 2
else:
    print("You are not old enough to Play!")
