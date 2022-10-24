import random
import main


def test_main():

    strval = 'Python Programming'
    mygen = main.consonant(strval)
    resultlst = list(mygen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert len(resultlst) == 14, "Wrong number of elements"
    assert resultlst[0] == 'P', "Invalid value "
    assert resultlst[1] == 'y', "Invalid value "
    assert resultlst[2] == 't', "Invalid value "
    assert resultlst[3] == 'h', "Invalid value "
    assert resultlst[4] == 'n', "Invalid value "
    assert resultlst[5] == ' ', "Invalid value "


def test_fibo2():

    strval = 'PAYETIHONU'
    mygen = main.consonant(strval)
    resultlst = list(mygen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert len(resultlst) == 5, "Wrong number of elements"
    assert resultlst[0] == 'P', "Invalid value "
    assert resultlst[1] == 'Y', "Invalid value "
    assert resultlst[2] == 'T', "Invalid value "
    assert resultlst[3] == 'H', "Invalid value "
    assert resultlst[4] == 'N', "Invalid value "
