#Bu kod pico w için

import network
import time
import urequests
from machine import Pin
import dht

# WiFi bilgileri, kendi WiFi adın ve şifresini giri
SSID = 'WiFi_ADIN'
PASSWORD = 'WiFi_SIFRE'

# DHT sensör (DHT22 veya DHT11)
sensor = dht.DHT11(Pin(1))  # DHT11 kullanıyorsan DHT11 olarak değiştir, 1. pine sensörü tak, eğer sensörün pini değişirse bunu da değiştir

# WiFi bağlantısı
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("WiFi'ye bağlanılıyor...")
        time.sleep(1)
    print("WiFi bağlantısı tamamlandı!", wlan.ifconfig())

connect_wifi()

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        mesaj = f"Oda no: 1, Termometre no: 1, Sıcaklık: {temp:.1f} derece, Nem: %{hum:.1f}"  # Gönderilen mesaj, duruma göre değiştirin
        print("Gönderilen:", mesaj)

        response = urequests.post("http://192.168.0.31:5000/log", data=mesaj) # Verinin gönderileceği bilgisayarın ip adresi ve portu burayı kendi cihazına göre değiş (port logger kodundaki port ile aynı olmalı)
        print("Sunucu yanıtı:", response.status_code)
        response.close()
    except Exception as e:
        print("Hata:", e)

    time.sleep(10) # 10 saniye bekler bu yüzden 10 saniyede 1 veriyi gönderir, eğer daha sık veya daha  seyrek isterseniz süreyi değiştirin
