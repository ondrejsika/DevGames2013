for i in range(1, input()+1):
    line = raw_input()
    for c in "lmnopqrstuvw":
        if c in line:
            line = " ".join(reversed(line.split()))
            break
    print "Case #%s: %s" % (i, line)