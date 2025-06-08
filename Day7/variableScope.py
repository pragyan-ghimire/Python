# variable scope = where a variable is visible and accessible
# scope resolution priority = (LEGB) Local > Enclosed > Global > Built-in

x = 4 # global variable
def func1():
    a = 2 # local to func1
    print (a)
    print(x)
func1()

# enclosed

def func2():
    a = 3 # enclosed variable for function 3
    def func3():
        print(a)
        print(x)
    func3()
func2()

from math import pi # built-in
print(pi)