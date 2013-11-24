import string
base = string.ascii_lowercase + string.ascii_lowercase
for i in range(1, input()+1):
    s = ""
    for c in raw_input().replace("\n", ""):
        s += base[base.find(c)+3]
    print "Case #%s: %s" % (i, s)