import time
import digitalio
import board

# กำหนดขา PE0, PE1, PE2, PE3
led1 = digitalio.DigitalInOut(board.PE00)
led2 = digitalio.DigitalInOut(board.PE01)
led3 = digitalio.DigitalInOut(board.PE02)
led4 = digitalio.DigitalInOut(board.PE03)

# ตั้งค่าขาทั้งหมดเป็น OUTPUT
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT

while True:
    # เปิดไฟ LED ทีละดวง
    led1.value = True
    time.sleep(0.1)
    led1.value = False

    led2.value = True
    time.sleep(0.1)
    led2.value = False

    led3.value = True
    time.sleep(0.1)
    led3.value = False

    led4.value = True
    time.sleep(0.1)
    led4.value = False

