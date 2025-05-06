pm = 0
pmn = 100000000000000000
for z in range (0, 5):
    p = int(input('Digite um peso: '))
    if p > pm:
        pm = p
    if p < pmn:
        pmn = p
print('o peso mario é {} e o peso menor é {}'.format(pm, pmn))
  


    