# the file where you import and use the module
# 22.1_module_use.py
# Using functions from 22_module_mymath module

import module_mymath as math_mod # Note: Python filenames can't start with numbers, so rename file to module_mymath.py or add prefix letters

x = 20
y = 4

print("Add:", math_mod.add(x, y))
print("Subtract:", math_mod.subtract(x, y))
print("Multiply:", math_mod.multiply(x, y))
print("Divide:", math_mod.divide(x, y))
print("Divide by zero:", math_mod.divide(x, 0))
