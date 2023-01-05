def computepay(hours=35,rate=9):
   pay1 = hours*rate
   pay2 =pay1 +5*1.5
if hours >= 45 :
    print(pay2)
else:
    print(pay1)
computepay(hours=45,rate=10)        