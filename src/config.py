"""Rutas y constantes del proyecto."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_INTERIM = ROOT / "data" / "interim"
DATA_PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "reports" / "figures"
MODELS = ROOT / "models"

for _p in (DATA_INTERIM, DATA_PROCESSED, FIGURES, MODELS):
    _p.mkdir(parents=True, exist_ok=True)

# Columnas de fecha por tabla (según las bases del reto)
DATETIME_COLS = {
    "person": [],
    "visit_occurrence": ["visit_start_datetime", "visit_end_datetime"],
    "visit_detail": ["visit_detail_start_datetime", "visit_detail_end_datetime"],
    "condition_occurrence": ["condition_start_datetime"],
    "procedure_occurrence": ["procedure_datetime"],
    "measurement": ["measurement_datetime"],
}

# Conceptos OMOP estándar frecuentes (VERIFICAR con los datos reales)
VISIT_CONCEPTS = {
    9201: "Hospitalización",
    9202: "Ambulatoria",
    9203: "Urgencias",
    262: "Urgencias + Hospitalización",
}
GENDER_CONCEPTS = {8507: "Masculino", 8532: "Femenino"}

RANDOM_STATE = 42
