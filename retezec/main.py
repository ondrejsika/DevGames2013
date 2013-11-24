for i in range(1, input()+1):
    s = raw_input()
    while True:
        next = 0
        if s.find("yx") != -1:
            s = s.replace("yx", "xy", 1)
            next += 1
        if s.find("xy") != -1:
            s = s.replace("xy", "", 1)
            next += 1
        if not next:
            print "Case #%s: %s" % (i, s)
            break