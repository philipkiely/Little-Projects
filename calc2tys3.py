def func(a, b, c, d):
    exact = (a*b*c*d)
    ra = round(a) #round sometimes gives us weird things
    rb = round(b)
    rc = round(c)
    rd = round(d)
    rounded = (ra*rb*rc*rd)
    difference = exact - rounded
    print(difference)
    
