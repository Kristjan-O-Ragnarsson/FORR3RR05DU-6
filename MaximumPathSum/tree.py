"""
Made By Kristjan O. Ragnarsson
github.com/Kristjan-O-Ragnarsson
"""
tree = []

n = 4


def my_gen():
    x = (3, 7, 4, 2, 4, 6, 8, 5, 9, 3)
    for i in range(10):
        yield x[i]


gen = my_gen()

for i in range(n):
    tree.append([next(gen) for i in range(i+1)])


old = 0
ind = 0
summ = 0
for i in range(n):
    summ += tree[i][ind]
    old = tree[i][ind]
    ind = tree[i].index(old)
    try:
        if tree[i+1][ind] < tree[i+1][ind+1]:
            ind += 1
    except IndexError:
        break

