# 📊 LoL Custom Match Tracker

Recopilador de datos de partidas personalizadas de League of Legends usando la **Live Client Data API**. Genera un JSON estructurado compatible con la API de Riot para ser procesado por un bot de Discord.

## 🚀 Instalación

### 1. Requisitos previos
- **Python 3.10+** instalado
- **League of Legends** instalado
- **Riot API Key** (gratuita) → [developer.riotgames.com](https://developer.riotgames.com/)

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar API Key

Copia el archivo de ejemplo y añade tu API Key:

```bash
copy .env.example .env
```

Edita `.env` y pega tu API Key:
```
RIOT_API_KEY=RGAPI-tu-api-key-real
RIOT_REGION=europe
```

## ▶️ Uso

### 1. Lanza el script
```bash
python collector.py
```

### 2. Abre LoL y entra en una partida personalizada

El script detectará automáticamente cuando empiece la partida.

### 3. Juega normalmente

El script captura un snapshot por minuto en segundo plano.

### 4. Al terminar la partida

El script genera automáticamente un archivo `matches/match_FECHA_HORA.json`.

### 5. Sube el JSON a Discord

Usa tu comando del bot de Discord para procesar el archivo.

## ⚙️ Configuración

Edita `config.py` para ajustar:

| Parámetro | Default | Descripción |
|---|---|---|
| `POLLING_INTERVAL_SECONDS` | `60` | Intervalo de captura (segundos) |
| `SNAPSHOT_KEEP_MINUTES` | `[5, 10, 15, 20]` | Minutos a incluir en el JSON. `None` = todos |
| `OUTPUT_DIR` | `./matches` | Carpeta de salida |

## 📁 Estructura del JSON de salida

```
{
  match_id, game_mode, game_duration_seconds, game_version,
  teams: { blue: { win, objectives }, red: { win, objectives } },
  participants: [
    { puuid, riotId, championName, role,
      snapshots: { t5, t10, t15, t20, final },
      final_stats: { kills, deaths, assists, kda, kp_percent, ... }
    }
  ],
  events_timeline: [ ... ]
}
```

## ⚠️ Notas importantes

- La **Riot API Key gratuita** caduca cada **24 horas**. Renuévala en el portal de Riot.
- El script **no es baneable** — usa la API oficial de Riot expuesta localmente.
- El certificado SSL es autofirmado, el script lo maneja automáticamente.
