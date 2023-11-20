
def start():
    print("Welcome to Santa's list!")
    name = input("Please enter your name to see if you are on the nice list: ")
    print("How nice are you on a scale of 1-10?")
    nice = int(input("Nice: "))
    if nice >= 5:
        print(name, "you're on the nice list!")
    else:
        print(name, "you're on the naughty list!")

start()