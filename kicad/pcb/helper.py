import decimal

ctx = decimal.Context()
ctx.prec = 12

def quote_str(value):
    if not isinstance(value, str):
        raise TypeError('value is not instance of str')

    if all(ord(char) > 127 for char in value):
        raise ValueError('Only ASCII 7bit allowed!')

    return "\"{}\"".format(value.replace('"', '""'))

def float_to_str(value):
    if not isinstance(value, float):
        raise TypeError('value is not instance of float')

    return format(ctx.create_decimal(repr(value)), 'f')
