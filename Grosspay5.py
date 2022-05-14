# Gross pay w/ or w/out overtime
# Hours input
while True:
    try:
        hrs = float(input('Enter hours: '))
    except ValueError:
        print('Numerics only')
        continue
    else:
        break
# Rate input
while True:
    try:
        rte = float(input('Enter Rate: '))
    except ValueError:
        print('Numerics only')
        continue
    else:
        break
# Calculations
if hrs > 40 :
    othour = hrs - 40
    otrate = rte * 1.5
    print('Your pay is:', (40 * rte) + othour * otrate)
else:
    pay = hrs * rte
    print('Your pay is:', '$',pay)
