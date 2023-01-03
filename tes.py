# def isPalindrome(s):
#     return s == s[::-1]

# # Driver code
# s = input("Masukan kata yang akan di check!");
# ans = isPalindrome(s)

# if ans:
#     print("Ya")
# else:
#     print("Tidak")


def tambah(a,b):
    return (a+b)
def kurang(a,b):
    return (a-b)
def kali(a,b):
    return (a*b)
def bagi(a,b):
    return (a/b)

pilih=input()    
while pilih:
    a=(int(input))
    b=(int(input))

if pilih == 1:
    print(tambah(a, b))
elif pilih == 2:
    print(kurang(a, b))
elif pilih == 3:
    print(kali(a, b))
elif pilih == 4:
    print(bagi(a, b))
