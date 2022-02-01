import random
z = int(input("Enter a number from 1-100"))



def numbersGame(y):
    x = random.randint(0, 10)
    if (x == y):
        print("yay")
    else:
        if x > y:
            print("nope too low")
        else:
            print("nope too high")


def evenOdd(w):
    if w>100 or w<1:
        print("number not in the range 1-100")
    else:
        g = w % 2
        prime = "This number is not prime"
        if g == 0:
            print("The number is even and", prime)
        else:
            print("The number is odd")
            for i in range(2,w-1):
                if (w % i) == 0:
                    prime = "This number is not prime"
                    break

                else:
                    prime = "The number is prime"
            print(prime)



numbersGame(z)

