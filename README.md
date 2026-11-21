# Data Challenge HUN 2026 — Flujo de pacientes del Hospital Universidad del Norte

> **Reto:** comprender, predecir y optimizar el flujo de pacientes, identificando cuellos de botella, patrones operacionales y oportunidades de mejora en los tiempos de atención.

## Enfoque

```
DIAGNÓSTICO           →  EXPLICACIÓN          →  PREDICCIÓN            →  ACCIÓN
Process mining +         Modelo LOS + SHAP       Pronóstico de            Simulación what-if
ocupación horaria        (factores de demora)    saturación + alerta      (impacto cuantificado)
```

Detalle completo en [`docs/01_posibles_soluciones.md`](docs/01_posibles_soluciones.md).

## Estructura

```
Data_Challenge_HUN_2026/
├── data/
│   ├── raw/          ← datos originales del reto (NO se suben a GitHub)
│   ├── sample/       ← datos sintéticos para pruebas (scripts/generar_datos_sinteticos.py)
│   ├── interim/      ← tablas intermedias (event log, features)
│   └── processed/    ← resultados y tablas para Power BI
├── docs/             ← bases, soluciones, plan, diccionario, hallazgos
├── notebooks/        ← análisis numerado 01 → 07
├── src/              ← funciones reutilizables
├── scripts/          ← utilidades
├── sql/              ← consultas para DBeaver
├── .env.example      ← plantilla de credenciales (copiar como .env, no se sube)
├── powerbi/          ← archivo .pbix y guía del dashboard
├── reports/figures/  ← gráficos para el documento
└── models/           ← modelos entrenados
```

| Notebook | Contenido |
|---|---|
| 01_calidad_datos | Volumen, fechas, nulos, huérfanos, conceptos a mapear |
| 02_flujo_process_mining | Event log, duración de etapas, esperas entre etapas, variantes, mapa pm4py |
| 03_congestion_ocupacion | Ocupación horaria, heatmaps, efecto de la congestión en la estancia |
| 04_modelo_estancia_shap | LightGBM (al ingreso / explicativo), estancia prolongada, SHAP |
| 05_pronostico_saturacion | Holt-Winters y LightGBM, alerta de saturación |
| 06_simulacion_what_if | SimPy calibrado con datos reales, escenarios de mejora |
| 07_export_powerbi | Modelo estrella en CSV para el dashboard |

## Cómo correr

```powershell
conda create -n hun python=3.11 -y
conda activate hun
pip install -r requirements.txt

# Probar con datos sintéticos (mientras llegan los reales)
python scripts/generar_datos_sinteticos.py --visitas 5000
# luego en los notebooks: SOURCE = "sample"
jupyter lab
```

### Con la base de datos del reto (FortiClient VPN + DBeaver)

1. Conectar **FortiClient VPN**.
2. Copiar `.env.example` como `.env` y llenarlo con los mismos datos de DBeaver.
3. Probar: `python -c "from src import db; db.test_connection(); print(db.row_counts())"`
4. Correr los notebooks en orden 01 → 07 (vienen con `SOURCE = "db"`).

Guía completa: [`docs/04_conexion_vpn_dbeaver.md`](docs/04_conexion_vpn_dbeaver.md). Consultas para explorar en DBeaver: [`sql/exploracion_dbeaver.sql`](sql/exploracion_dbeaver.sql).

Otras fuentes: `SOURCE = "sample"` (sintéticos) o `SOURCE = "raw"` (archivos exportados a `data/raw/`).

## Entregables

- [ ] Documentación del proyecto (`docs/`)
- [ ] Repositorio GitHub
- [ ] Dashboard Power BI (`powerbi/`)

## Equipo

| Integrante | Rol |
|---|---|
| | Datos y flujo |
| | Congestión y pronóstico |
| | Modelado explicable |
| | Power BI y documentación |
