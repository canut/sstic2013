import smp

for o in smp.smp:
    if (o >> 7) == 0:
        print "A = 0x%x" % (o & 0x7f)
    elif (o >> 3) == 0x11:
        print "A = A & R%s" % (o & 7)
    elif (o >> 3) == 0x12:
        print "A = A | R%s" % (o & 7)
    elif (o >> 3) == 0x14:
        print "A = ~A"
    elif (o >> 3) == 0x15:
        print "A = R%s" % (o & 7)
    elif (o >> 3) == 0x16:
        print "R%s = A" % (o & 7)
    elif (o >> 3) == 0x17:
        print "jz R%s" % (o & 7)
    elif (o >> 3) == 0x18:
        print "[R%s] = A" % (o & 7)
    elif o == 0xc8:
        print "finished (return)"
    elif o == 0xd0:
        print "A = [A]"
    elif (o >> 3) == 0x1b:
        print "A = A << 1"
    elif (o >> 3) == 0x1c:
        print "A = 0x80 | A"
    else:
        print "A = 0"