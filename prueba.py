from read_PAC import PAC3120
import time


PAC1 = PAC3120('/dev/ttyAMA0', 1, 9600)
PAC2 = PAC3120('/dev/ttyAMA0', 2, 9600)
PAC3 = PAC3120('/dev/ttyAMA0', 3, 9600)

def read_PAC(PAC):

	active_power_PAC = PAC.get_active_power()
	reactive_power_PAC = PAC.get_reactive_power()
	power_factor_PAC = PAC.get_power_factor()

	for x in range (0, 3):
		apparent_power_L = ((active_power_PAC[x]**2)+(reactive_power_PAC[x]**2))**0.5
		print("apparent_power_L" + str(x+1) + " "+str( apparent_power_L))
	time.sleep(0.1)


while True:
	try:
		PAC_ = [PAC1, PAC2, PAC3]
		for y in range (0, 3):
			read = read_PAC(PAC_[y])
	except Exception as e:
        	print(e)