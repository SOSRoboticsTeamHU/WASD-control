#! /bin/python

from gpiozero import OutputDevice
import time


class Motor:
	def __init__(self, fwpin, bwpin):
		self.fwpin = OutputDevice(fwpin)
		self.bwpin = OutputDevice(bwpin)
		self.stop()

	def forward(self):
		self.fwpin.on()
		self.bwpin.off()
	
	def backward(self):
		self.fwpin.off()
		self.bwpin.on()

	def stop(self):
		self.fwpin.off()
		self.bwpin.off()

class Movement:
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.stop()
	
	def forward(self):
		self.left.forward()
		self.right.forward()

	def backward(self):
		self.left.backward()
		self.right.backward()

	def turnLeft(self):
		self.left.backward()
		self.right.forward()

	def turnRight(self):
		self.left.forward()
		self.right.backward()

	def stop(self):
		self.left.stop()
		self.right.stop()


def test_motor(motor):
	motor.forward()
	time.sleep(1)
	motor.stop()
	time.sleep(1)
	motor.backward()
	time.sleep(1)
	motor.stop()

def test_motors(movement):
	test_motor(movement.left)
	time.sleep(1)
	test_motor(movement.right)

def test_movement(movement):
	movement.forward()
	time.sleep(1)
	movement.stop()
	time.sleep(1)
	movement.backward()
	time.sleep(1)
	movement.stop()
	time.sleep(1)
	movement.turnLeft()
	time.sleep(1)
	movement.stop()
	time.sleep(1)
	movement.turnRight()
	time.sleep(1)
	movement.stop()

def test_everything(movement):
	test_motors(movement)
	time.sleep(1)
	test_movement(movement)

if __name__ == "__main__":
	left_motor = Motor( 17, 27 )
	right_motor = Motor( 10, 22 )
	movement = Movement( left_motor, right_motor )
	test_everything( movement )
