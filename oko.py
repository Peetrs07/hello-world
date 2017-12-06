from random import randrange
x = randrange(2,11)

while x <=21:
    print("mas",x,)
    odp = input("chces dalsi kartu?(y/n)")
    if odp == "y":
        k = randrange (2,11)
        print("otocil jsi ", k)
        x = x + k
    elif odp == "n":
        break
    else:
        print("nerozumim")

if x == 21:
    print("gratuluji, vyhrals")
elif x > 21:
    print("prohrals,chacha")
else:
    print("chybelo ti jen ", 21 - x)
