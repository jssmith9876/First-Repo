def alhpabatize(sentance):
    words = sentance.split()
    words.sort()
    result = ' '.join(words)
    return result

def main():
    while(True):
        usr = str(input("Enter a sentance: "))
        if (usr == ''):
            break
        else:
            print(alhpabatize(usr))

main()
