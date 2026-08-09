from machine import Pin
import dht
import time

camBien_dht22 = dht.DHT22(Pin(4))

while True:
    cambien_dht22.measure() # Bật cảm biến

    nhietDo = sensor.temperature() # Lệnh lấy nhiệt độ
    doAm = sensor.humidity() # Lệnh lấy độ ẩm

    print("Nhiet do:", nhietDo, "C")
    print("Do am:", doAm, "%")

    time.sleep(2)