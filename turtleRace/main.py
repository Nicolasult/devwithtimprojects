import turtle

WIDTH, HEIGHT = 500, 500

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not a valid number.")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2 -10. Try again.")

racers = get_number_of_racers()

