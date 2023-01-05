inputhours = input('enter hours :')
inputrates = input('enter rate :')

hours = int(inputhours)
rates = int(inputrates)

if hours > 40 :
	times = float(hours) - 40
else :
	times = 0
	
pay1 = 0.5 * float(rates) * times
pay2 = float(hours) * float(rates) + pay1

print(pay2)