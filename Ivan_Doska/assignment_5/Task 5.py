import numpy as n

a = n.arange(21) #[0; 21)
b = a[a % 2 == 0] #0 % any num == 0
c = a[a % 3 == 0]

print("Initial array:", a)
print("Even numbers:", b)
print("Divisible by 3:", c)