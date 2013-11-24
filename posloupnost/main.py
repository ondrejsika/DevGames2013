for k in range(1, input()+1):
    s = int(raw_input().split()[1])
    a = map(int, raw_input().split())
    x = 0
    res = []
    for i in range(len(a)):
        for j in range(1, len(a)+1):
            d = abs(i-j)
            ts = sum(a[i:j])
            if ts >= s:
                res.append(d)
    print "Case #%s: %s" % (k, min(res) if res else 0)