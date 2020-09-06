# This function verifies if the number is an integer number.
def readInt(num):
    try:
        n = int(input(num))
    except:
        print("ERROR!! Type a valid number.")
    else:
        return n


# This function sets dashed line
def dashedLine(size=42):
    return '-' * size


# This function set a headline - A centered text between to dashed lines.
def headLine(txt):
    print(dashedLine())
    print(f'{txt}'.center(42))
    print(dashedLine())


# This function sets up enumeration on menu
def option(opt):
    count = 1
    for x in opt:
        print(f'{count} - {x}')
        count += 1
    print(dashedLine())
    opt = readInt("Type an option: ")
    print(dashedLine())
    return opt
