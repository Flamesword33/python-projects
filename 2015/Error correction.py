def niceDiv(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Nice try, dividing by 0' + \
              ' is NOT allowed')
    except TypeError:
        print('Nice try, dividing with an' + \
              ' incorrect type')
    except NameError:
        print('Nice try, letters are NOT allowed')
    except SyntaxError:
        print('Nice try, symbols are NOT allowed')
