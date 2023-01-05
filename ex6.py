Hours = input()
Rate = 10
try :
    Hour = int(Hours)
except :
    Hour = -1
    print('Error')

if Hour < 40 :
    result = Hour * Rate
    print(result)
if Hour > 40 :
    result = (Hour - 40) * (15) + 400
    print(result)
