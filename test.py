def improve(update,close,guess=1):
    print("improve()")
    while not close(guess):
        guess=update(guess)
    return guess

def approx_eq(x,y,tolerance=1e-15):
    print("approx_eq()")
    return abs(x-y)<tolerance

def golden_update(guess):
    print("golden_update()")
    return 1/guess+1

def square_close_to_successor(guess):
    print("square_close_to_successor()")
    return approx_eq(guess*guess,guess+1)

def myprint(pr1, pr2):
    print("myprint")
    print(pr1(1),pr2(2))