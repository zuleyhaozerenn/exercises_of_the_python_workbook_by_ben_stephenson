"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""

import math

a = int(input("Lütfen ilk sayınızı giriniz: "))
b = int(input("Lütfen ikinci sayınızı giriniz: "))

first_process = a + b
second_process = a - b
third_process = a * b
fourth_process = a / b
fifth_process = a % b
sixth_process = math.log(a,10)
seventh_process = math.pow(a,b)

print("""
The results:
The sum of a and b: {}
The difference when b is subtracted from a: {}
The product of a and b: {}
The quotient when a is divided by b: {}
The remainder when a is divided by b: {}
log10 a: {}
a^b: {}
""".format(first_process,second_process,third_process,fourth_process,fifth_process,sixth_process,seventh_process))
