# Wojciech Fuśnik gr15

def add(x1, x2):
    return int(x1)+int(x2)

def subtract(x1, x2):
    return int(x1)-int(x2)

def multiplication(x1,x2):
    return int(x1)*int(x2)

def division(x1,x2):
    return int(x1)/int(x2)


def main():
    print("a-add,s-subtract,m-multiplication,d-division")
    o = input("chose operation: ")
    a = input("first variable: ")
    b = input("secound variable: ")
    int(a)
    int(b)
    if o == "a":
        print(add(a,b))
    elif o== "s":
        print(subtract(a,b))
    elif o=="m":
        print(multiplication(a,b))
    elif o=="d":
        print(division(a,b))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




