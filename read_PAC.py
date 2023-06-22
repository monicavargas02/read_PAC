import time, datetime
import minimalmodbus
import RPi.GPIO as io


class PAC3120:

	def __init__(self, port_rs, id_slave, baudrate):
		self.port = port_rs
		self.id_slave = id_slave
		self.baudrate = baudrate

	def read_instrument(self, registeraddress, len_register, funct):
		try:
			io.setwarnings(False)
			io.setmode(io.BOARD)
			io.setup(16, io.OUT)
			io.output(16,True)
			instrument = minimalmodbus.Instrument(self.port, self.id_slave)  # port name, slave address (in decimal)
			instrument.serial.timeout  = 1
			instrument.debug = True
			instrument.close_port_after_each_call = True
			instrument.serial.baudrate = self.baudrate
			resp = instrument.read_float(registeraddress, funct, len_register)
			io.output(16,False)
			return resp
		except:
			print("Failed to read from instrument")
			

	def get_active_power(self):
		
		active_power = []
		for x in range (25, 30, 2):
			active_power.append(self.read_instrument(x, 2, 4))
		return active_power

	def get_reactive_power(self):

		reactive_power = []
		for x in range (31, 36, 2):
			reactive_power.append(self.read_instrument(x, 2, 4))
		return reactive_power

	def get_power_factor(self):

		power_factor = []
		for x in range (37, 42, 2):
			power_factor.append(self.read_instrument(x, 2, 4))
		return power_factor

