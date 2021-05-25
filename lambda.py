def run():
    palindromo = lambda test: test.lower() == test.lower()[::-1] #sin punto y coma al final
    print(palindromo('Pepito'))

if __name__ == '__main__':
    run()