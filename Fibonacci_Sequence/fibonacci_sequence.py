parents, babies = (1, 1)

while babies < 100:
    print "This generation has %s babies" % babies
    parents, babies = (babies, parents + babies)