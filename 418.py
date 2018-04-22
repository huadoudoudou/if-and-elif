height = float(input('height :'))
weight = float(input('weight :'))
BMI = weight/(height*height)
if BMI <= 18.5:
    print('U are too thin')
elif BMI > 18.5 and BMI <= 25:
    print('U are normal')
elif BMI > 25 and BMI <= 28:
    print('U are overweight')
elif BMI > 28 and BMI <= 32:
    print('U should lose  your weight ')
else:
    print('U really should lose your weight')