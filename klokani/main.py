for i in range(1, input()+1):
    a, b, c = sorted(map(int, raw_input().split()))
    print "Case #%s: %s" % (i, max(b-a, c-b)-1)