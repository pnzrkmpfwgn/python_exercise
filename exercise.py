from decimal import Decimal


Distance =float(input('Enter the amount of your jumping distance:'))

Remaining_Distance = 8.85 - Distance

if Remaining_Distance < 0 :
    print('You broke the world record!\n New Record' + str(Distance))

else:
    print('You need to jump:'+"%.2f" % Remaining_Distance + ' additional meters to improve the world record')
    print('Meters: ' + "%.0f" % Remaining_Distance)
    Decimeters = Remaining_Distance * 10
    Decimeters = Decimeters % 10
    print('Decimeters: ' + str(round(Decimeters)))
    Cantimeter = Decimeters * 10
    Cantimeter = Cantimeter % 10
    print('Cantimeters:' + str(round(Cantimeter)))