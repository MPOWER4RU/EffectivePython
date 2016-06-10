# Item 21 - Enforce Clarity with Keyword-Only Arguments


def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1, 10**500, True, False)
print(result)

result = safe_division(1, 0, False, True)
print(result)


def safe_division_b(number, divisor,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division_b(1, 10**500, ignore_overflow=True)
safe_division_b(1, 0, ignore_zero_division=True)

safe_division_b(1, 10**500, True, False)


def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# Won't work...
# safe_division_c(1, 10**500, True False)

safe_division_c(1, 0, ignore_zero_division=True)  # OK

try:
    safe_division_c(1, 0)
except ZeroDivisionError:
    pass  # Expected

# Python 2


def print_args(*args, **kwargs):
    print('Positional:', args)
    print('Keyword:   ', kwargs)

print_args(1, 2, foo='bar', stuff='meep')

# Python 2


def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)

    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_div:
            return float('inf')
        else:
            raise

safe_division_d(1.0, 10)
safe_division_d(1.0, 0, ignore_zero_division=True)
safe_division_d(1.0, 10**500, ignore_overflow=True)

# Won't work...
# safe_division_d(1.0, 0, False, True)

# Also won't work..
# safe_division_d(1.0, 0, unexpected=True)
