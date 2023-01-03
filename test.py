import random

money = 1000000
while money>0:
    print("============HILO================")
    print("Saldo Anda Sekarang Adalah ", money)
    bet = int(input("Masukkan nominal bet anda: "))
    com = random.randint(1,100)
    print("Angka Musuh: ",com)
    pilih = str(input("High/Low/Equal: "))
    pilih = pilih.lower()
    player1 = random.randint(1,100)
    print("Angka Anda: ",player1)
    hasil = ""
    if (player1>com):
        hasil="high"
    elif(com>player1):
        hasil="low"
    elif(com==player1):
        hasil="equal"


    if pilih==hasil:
        print("W")
        money +=bet
    else:
        print("L")
        money -=bet
else:
    print("Uang anda tidak cukup")