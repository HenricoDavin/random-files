#butuh modul random
import random
import timeit

#generate list terurut berukuran n
def generate_list(n):
    batas_atas = n * 100
    randomlist = random.sample(range(0, batas_atas), n)
    randomlist.sort()
    return randomlist

def cari_pasangan(data, target):
    for i in range(0, len(data)-1):
        for j in range(i, len(data)):
            if data[i] + data[j] == target:
                print(data[i], '+', data[j], '=', target)
                return True
    return False

n = 5000
data = generate_list(n)

start = timeit.default_timer()
hasil = cari_pasangan(data, target)
print(hasil)

end = timeit.default_timer()
print(target, n, '=', end-start)
