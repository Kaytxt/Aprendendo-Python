mi = 0
mii = 0
for v in range(0, 10):
    i = int(input('Digite uma idade: '))
    if i >= 21:
        mi += 1
    else:
        mii += 1

print('{} pessoas atingiram a maior idade e {} pessoas não atingiram'.format(mi, mii))