import time
    def timing(f, n, a):
        print f.__name__,
        r = range(n)
        t1 = time.clock()
        for i in r:
            f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a)
        t2 = time.clock()
        print round(t2-t1, 3)