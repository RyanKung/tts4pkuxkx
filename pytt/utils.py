def split(a, b, i=0):
    assert i in (0, 1)
    return a.split(b)[i]


def cmd(a):
    print('cmd %s' % a)


def show(a):
    print('cmd #showme %s' % a)
