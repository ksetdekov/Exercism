def convert(n):
    result = ''
    if (n % 3) == 0:
        result = result + 'Pling'
    if (n % 5) == 0:
        result = result + 'Plang'
    if (n % 7) == 0:
        result = result + 'Plong'
    else:
        result = str(n)
    return result
