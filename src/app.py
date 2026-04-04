from flask import Flask, request, jsonify, render_template
import os, time
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
SECRET_TOKEN = os.getenv("AUTH_TOKEN")

def security_log():
    # Ağır işlem simülasyonu (DoS riskini göstermek için)
    print("[SERVER LOG] Hassas veritabanı sorgusu işleniyor...")
    time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/vulnerable')
def vulnerable():
    security_log() # HATA: Önce ağır işlem, sonra yetki kontrolü!
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {SECRET_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"data": "Hassas Vize Notları"})

@app.route('/api/secure')
def secure():
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {SECRET_TOKEN}": # DOĞRU: Önce kontrol!
        return jsonify({"error": "Unauthorized"}), 401
    security_log()
    return jsonify({"data": "Hassas Vize Notları"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
