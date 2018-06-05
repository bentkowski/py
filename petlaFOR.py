import random

for x in range(0,100):
    y = (random.randint(0,10))
    if y>5:
        print('wieksze od 5')
    elif y<5:
        print ('mniejsze od 5')
    elif y=5:
        print ('zloty strzal')
    else:
        print ('konioec jesty blisko')

