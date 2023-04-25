#1
a=5
b=10
def swap(a, b):
    a, b = b, a
    return a, b
print(f'Before: a = {a}, b = {b},')
a, b = swap(a, b)
print(f'Past: a = {a}, b= {b}')

#2
s=input()
def count_vowels(s):
    k=0
    for i in s:
        if i=='a' or i=='o' or i=='e' or i=='i' or i=='u' or i=='y':
            k=k+1
    return k
print(count_vowels(s))

#3
lst=