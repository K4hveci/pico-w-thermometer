#bu kod bilgisayarda çalışacak, gelen veriyi dinleyip txt'ye kaydeder

from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_data():
    content = request.data.decode('utf-8')
    print("Gelen veri:", content)

    # txtye kaydetme kısmı
    with open("veriler.txt", "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{now} - {content}\n")

    return "Kayıt alındı", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # dinlenen port, duruma göre değiştirilebilir
