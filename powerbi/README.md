# Dashboard Power BI

Guardar aquí el archivo `dashboard_HUN.pbix`. Las tablas se generan con `notebooks/07_export_powerbi.ipynb` en `data/processed/powerbi/`.

## Modelo de datos (estrella)

```
dim_fecha (fecha) ──1:N── fact_visita (fecha, visit_occurrence_id) ──1:N── fact_etapa (visit_occurrence_id)

Tablas sueltas (sin relación): transiciones, duracion_etapas, ocupacion_horaria,
importancia_shap, pronostico_ocupacion, alerta_saturacion, simulacion_escenarios
```

## Páginas

1. **Resumen ejecutivo** — tarjetas KPI, tendencia semanal de visitas y LOS, filtro por tipo de visita.
2. **Flujo y cuellos de botella** — ranking de esperas por transición (`transiciones`), duración por etapa, heatmap hora × día (matriz con formato condicional sobre `fact_visita`). Para el Sankey: visual personalizado "Sankey Chart" de AppSource con `etapa_anterior` → `etapa`, valor = `n`.
3. **Factores de demora** — barras de `importancia_shap`, LOS por franja/edad/tipo, % estancia prolongada por segmento.
4. **Predicción y alerta** — línea real vs. pronóstico (`pronostico_ocupacion`), semáforo con `alerta_saturacion`.
5. **Recomendaciones** — tabla de `simulacion_escenarios` con reducción % y textos de acción.

## Medidas DAX base

```DAX
Visitas = DISTINCTCOUNT ( fact_visita[visit_occurrence_id] )

LOS mediana (h) = MEDIAN ( fact_visita[los_h] )

LOS P90 (h) = PERCENTILEX.INC ( fact_visita, fact_visita[los_h], 0.9 )

% Estancia prolongada = DIVIDE ( SUM ( fact_visita[estancia_prolongada] ), [Visitas] )

Espera media entre etapas (h) =
    AVERAGEX ( FILTER ( fact_etapa, fact_etapa[orden] > 1 ), fact_etapa[espera_previa_h] )

Ocupación pico = MAX ( ocupacion_horaria[ocupacion] )

Riesgo saturación =
VAR p = MAX ( alerta_saturacion[prob_saturacion] )
RETURN SWITCH ( TRUE (), p >= 0.7, "Alto", p >= 0.4, "Medio", "Bajo" )
```

## Publicar

Publicar en Power BI Service (cuenta Uninorte) → "Publicar en la web" o compartir enlace, según lo que pidan los organizadores. Verificar que el enlace abra sin iniciar sesión antes de entregar.
