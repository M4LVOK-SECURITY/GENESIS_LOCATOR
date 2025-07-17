# 🚨 GENESIS – Proyecto ético y educativo de rastreo web

**GENESIS** es una herramienta de concientización y demostración educativa que permite evidenciar cómo un simple enlace compartido puede capturar información sensible del visitante. Esta aplicación ha sido diseñada **solo con fines éticos, educativos y de investigación**, para ser utilizada en entornos controlados como conferencias, talleres o laboratorios de ciberseguridad.

---

## 🧠 Objetivo del Proyecto

> Demostrar el funcionamiento básico de técnicas de rastreo web y fingerprinting a través de la interacción con un enlace disfrazado. La finalidad es educar sobre los riesgos del uso no consciente de enlaces en redes sociales, mensajería instantánea y páginas web.
Aunque esta versión utiliza Ngrok como túnel público para facilitar pruebas educativas, la herramienta puede ser mejorada o adaptada fácilmente para utilizar otros servicios de redirección o camuflaje más avanzados (como Replit, Cloudflare Tunnel, Glitch, Fly.io o servidores personalizados), con el fin de aumentar el realismo, persistencia y el nivel de disfraz del enlace generado.

---

## ⚙️ Funcionalidades

- ✅ Solicitud manual de una URL destino (imagen, publicación, sitio web)
- ✅ Generación de un servidor Flask con enlace personalizado
- ✅ Captura de:
  - Dirección IP pública (incluyendo ubicación, ciudad, país, ISP)
  - Coordenadas GPS con precisión si el usuario lo permite
  - Nivel de batería, navegador, sistema operativo, idioma, resolución de pantalla
- ✅ Redirección automática al enlace original
- ✅ Registro completo de datos en un archivo `datos.txt`
- ✅ Compatible con `ngrok` para compartir públicamente


---

## 🧱 Estructura del Proyecto

```
GENESIS_LOCATOR/
├── app.py               # Código principal de la aplicación
├── datos.txt            # Archivo donde se almacenan los registros
├── static/
│   └── script.js        # Script de rastreo en el navegador
└── templates/
    └── index.html       # Página de carga del rastreo
```

---

## 🚀 Instrucciones de uso

### 1. Clona o descarga el proyecto

```bash
git clone https://github.com/M4LVOK-SECURITY/GENESIS_LOCATOR.git
cd genesis
```

### 2. Ejecuta el script principal

```bash
python app.py
```

- El sistema comprobará si tienes las dependencias necesarias (`flask`, `requests`) y las instalará si no están.
- Te pedirá ingresar la URL destino para camuflarla.

### 🪟 Windows

1. Instala Python 3 desde [python.org](https://python.org)
2. Instala Flask y Requests:
```bash
pip install flask requests
```
3. Ejecuta `app.py`
4. Abre Ngrok:
```bash
ngrok http 5000
```

### 🐧 Kali Linux

1. Ya incluye Python. Solo instala Flask y Requests:
```bash
sudo pip3 install flask requests
```
2. Corre como en Windows:
```bash
python3 app.py
```

---

## 💻 Ejemplo de ejecución

```
🔗 Ingresa la URL que deseas camuflar y rastrear: https://facebook.com/algunpost
```

---

### 3. Usa Ngrok para exponer el servidor

> (De no tenerlo, descargar y configurar, para poder ejecutar el comando siguiente:)

```bash
ngrok http 5000
```

- Copia el enlace generado por ngrok (por ejemplo: `https://abc123.ngrok.io`)
- Compártelo con fines demostrativos
- Ngrok está disponible para Linux y Windows. Si necesitas ayuda, revisa algún tutorial o contáctame en TikTok o YouTube.

---

## 🛡️ Aviso Legal

> Este software ha sido creado exclusivamente con fines **educativos y de concientización**. Cualquier uso indebido, sin consentimiento del usuario o con fines maliciosos, **podría constituir un delito** conforme a la legislación local e internacional. El autor **no se hace responsable por usos no autorizados** de esta herramienta.

---

## ✨ Autor

**M4LVOK_SECURITY**  
Proyecto GENESIS_LOCATOR – Desarrollado en el marco de concientización de seguridad informática.

---

## 📌 Licencia

MIT License – Uso libre para fines educativos. Prohibido para prácticas maliciosas.
