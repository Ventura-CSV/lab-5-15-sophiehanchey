
def consonant(strval):
   # define vowels
   vowels = ["a", "e", "i", "o", "u"]
   
   # split string into individual characters
   listStr = [*strval]
   
   # use loop to check character
   for i in listStr:
       if i.isalpha():
           if not i in vowels:
               yield i

def main():
    strval = 'Python Programming'
    mygen = consonant(strval)

    rlst = list(mygen)
    print(len(rlst))
    for v in rlst:
        print(v, end=' ')
    print()


if __name__ == '__main__':
    main()
