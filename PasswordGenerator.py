import random
import string

def gen():
    s1=string.ascii_letters
    s2=string.digits
    s3=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    random.shuffle(s)
    passLen=int(input("Enter the password length:\n"))
    pwd=("".join(s[0:passLen]))
    print(pwd)

gen()