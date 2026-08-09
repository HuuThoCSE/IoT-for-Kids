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
sensor = dht.DHT22(Pin(4))


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

    # Đọc DHT22
    sensor.measure()

    temperature = sensor.temperature()
    humidity = sensor.humidity()

    print("-------------------")
    print("Temperature:", temperature, "C")
    print("Humidity:", humidity, "%")

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