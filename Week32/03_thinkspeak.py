from machine import Pin
import dht
import network
import time
import urequests

# =========================
# WIFI
# =========================
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

# =========================
# THINGSPEAK
# =========================
WRITE_API_KEY = "YOUR_WRITE_API_KEY"

# =========================
# DHT22
# =========================
camBien_dht22 = dht.DHT22(Pin(4))


# Kết nối WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

print("Connecting WiFi...")

wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi.isconnected():
    time.sleep(0.5)

print("WiFi connected!")
print(wifi.ifconfig())


while True:

    cambien_dht22.measure() # Bật cảm biến

    nhietDo = camBien_dht22.temperature() # Lệnh lấy nhiệt độ
    doAm = camBien_dht22.humidity() # Lệnh lấy độ ẩm

    print("Nhiet do:", nhietDo, "C")
    print("Do am:", doAm, "%")

    # Gửi ThingSpeak
    url = (
        "https://api.thingspeak.com/update"
        "?api_key=" + WRITE_API_KEY +
        "&field1=" + str(temperature) +
        "&field2=" + str(humidity)
    )

    try:

        response = urequests.get(url)

        print("ThingSpeak response:")
        print(response.text)

        response.close()

    except Exception as e:
        print("ThingSpeak error:", e)

    # gửi lại sau 20 giây
    time.sleep(20)