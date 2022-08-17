def tub(son):
    if son<1:
        False

    for i in range(2,son//2):
        if son%i==0:
            return False

    return True
