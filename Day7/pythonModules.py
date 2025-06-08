# module = a file containing code you want to include in your program use 'import'
# to include a module(built-in or your own)
# useful to break up a large program reusable separate files

# print(help("modules"))

# import math (recommended)
# import math as m # giving alias
# print(m.pi)

# from math import pi # can use pi directly(not recommended as conflict can occur)
# print(pi)

# user module

import module1

r1 = module1.add(2,3)
r2 = module1.sub(2,3)
r3 = module1.mul(2,3)
r4 = module1.div(2,3)

print(r1, r2, r3, r4, sep=" ")