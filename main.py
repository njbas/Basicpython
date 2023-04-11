# import from package
# import all packages
import numberpackage as np
from numberpackage import *
from numberpackage import number as nb
from numberpackage import calculate as ca

print(numberpackage.number.factorial(5))
print(numberpackage.number.fibonacci(100))
print(np.number.fibonacci(100))
print(np.number.factorial(10))
print(np.calculate.plus(5, 5))
print(np.calculate.plus(5, 6))
