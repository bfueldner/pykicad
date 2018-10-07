import decimal

class flt(float):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return '!'+str(self.val)

if __name__ == '__main__':
    print("XXX")
    lst = [100.0, 0.0, 5.0, 0.5, flt(0.001), 0.0000001]

    for i in lst:
        print('{:f}'.format(i))
    print()

    dir(float)

    ctx = decimal.Context()
    ctx.prec = 20

    for i in lst:
    #    print('{:f}'.format(i))
        print(repr(i))
    #    format(ctx.create_decimal(repr(f)), 'f')
    print()
