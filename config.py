# LoL Custom Match Tracker — Configuración
# ==========================================

# ─── Live Client API ───────────────────────────────────────
LIVE_CLIENT_BASE_URL = "https://127.0.0.1:2999/liveclientdata"
SSL_VERIFY = False  # La Live Client API usa certificado autofirmado

# ─── Polling y Snapshots ──────────────────────────────────
POLLING_INTERVAL_SECONDS = 60  # 1 snapshot por minuto

# Minutos que se incluyen en el JSON final de salida.
# Se captura internamente 1 snapshot/min, pero solo estos se guardan.
# Usar None para guardar TODOS los minutos capturados.
SNAPSHOT_KEEP_MINUTES = [5, 10, 15, 20]

# ─── Almacenamiento ───────────────────────────────────────
OUTPUT_DIR = "./matches"

# ─── Versión ──────────────────────────────────────────────
COLLECTOR_VERSION = "1.0.0"
