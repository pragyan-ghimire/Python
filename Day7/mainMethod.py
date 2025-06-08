# if__name__ == __main__: (this script can be imported OR run standalone)
#                           Functions and classes in this module can be reused
#                           without the main block of code executing
# Good practice (code is modular
                # helps readability
                # leaves no global variables
                # avoid unintended execution)

def main():
    print("Not bad")

def favoriteFood():
    print("Momos")

print("mainMethod statement")
favoriteFood()

if __name__ == '__main__':
    main()