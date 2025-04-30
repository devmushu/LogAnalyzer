# LogAnalyzer
# Analizador de Logs de Backend

Esta aplicación permite analizar archivos de logs generados por un backend de e-commerce u otra API, identificando el rendimiento de las solicitudes según su método, endpoint, y latencia.

## Funcionalidades principales

- ✅ **Filtrado por fecha**: analiza los logs según una fecha específica.
- ✅ **Filtrado por método HTTP**: GET, POST, PUT, DELETE, etc.
- ✅ **Clasificación de latencia**: los tiempos de respuesta son clasificados como `SALUDABLE`, `MODERADO` o `LENTO`.
- ✅ **Detección de endpoints más lentos**: identifica solicitudes con tiempos superiores a 500ms.
- ✅ **Lectura dinámica de rutas**: puedes ingresar manualmente la ruta del archivo `.log`.

## Requisitos

- Python 3.x
- Pandas

Instalación de dependencias:
```bash
pip install pandas
