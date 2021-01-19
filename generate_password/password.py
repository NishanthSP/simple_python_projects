import random
pass_len = int(input("Enter the length of password : "))
randoms = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(randoms, pass_len))
print(p)