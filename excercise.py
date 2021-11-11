import module


def calc():

    print("Hello, what would you like to do?")

    done = False

    while not done:

        choice = input(
            "Type 1 for sqaure footage. | Type 2 for circumference. | Type 3 to quit session. ")
        if choice == "1":
            length = float(input("Enter the length of the room: "))
            width = float(input("Enter the width of the room: "))
            l = (length)
            w = (width)
            sf = str(module.sq_ft_room(l, w))
            print("This room is " + sf + " sqaure feet.")

        elif choice == "2":
            diameter = float(input("Enter diameter of the circle: "))
            d = diameter
            cir = str(module.circumference(d))
            print("The circle's circumference is " + cir)

        elif choice == "3":
            confirm = input(
                'Are you sure you would like to end session? Y/N ').lower()
            if confirm == 'y':
                print("Have a good day!")
                done = True
            elif confirm == 'n':
                continue


calc()
