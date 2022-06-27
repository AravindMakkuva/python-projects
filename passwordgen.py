import random

a=int(input("enter the length of the password: "))

s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()"

p="".join(random.sample(s,a))
print(p)