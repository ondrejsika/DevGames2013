fib = [1, 1]
for j in xrange(2, 1000):
    fib.append(fib[j-2]+fib[j-1])
for i in range(1, input()+1):
    print "Case #%s: %s" % (i, fib[input()])