Perfecto, eso cambia una pieza **fundamental del modelo**: ya no estás calculando costo “histórico”, sino **costo basado en inventario disponible (valuation at hand)**.

Esto obliga a rediseñar tanto **la base de datos como la lógica de negocio** para que el sistema sea coherente y extensible.

Voy a rehacer todo con ese criterio.

---

# 1. Nuevo principio de negocio (core del sistema)

> El costo de una receta se calcula usando **el precio más alto entre los lotes actualmente disponibles (stock > 0)** de cada insumo.

### Implicaciones directas

* Necesitas **modelar inventario por lotes**, no solo cantidades agregadas.
* El concepto clave ya no es “compra histórica”, sino:

```text
LOTE DISPONIBLE
```

---

# 2. Arquitectura revisada (ligeramente más rica)

```text
[ UI (Flet) ]
        ↓
[ Application / Services ]
        ↓
[ Domain (entidades + reglas + estrategias) ]
        ↓
[ Infrastructure ]
    ├── Repositories
    └── SQLite
```

### Cambio clave respecto a antes

Ahora el dominio incluye explícitamente:

```text
Inventario / Lotes
```

---

# 3. Estructura de proyecto (ajustada al nuevo modelo)

```text
dulceria_costos/
│
├── app/
│   ├── main.py
│
│   ├── ui/
│   │   ├── ui.py
│   │   ├── views/
│   │   │   ├── materiales_view.py
│   │   │   ├── compras_view.py
│   │   │   ├── recetas_view.py
│   │   │   └── costos_view.py
│   │   └── components/
│
│   ├── services/
│   │   ├── cost_service.py
│   │   ├── inventory_service.py   # NUEVO
│   │   ├── recipe_service.py
│   │   ├── material_service.py
│   │   └── unit_service.py
│
│   ├── domain/
│   │   ├── models.py
│   │   ├── value_objects.py
│   │   ├── rules/
│   │   │   └── cost_strategies.py
│   │   └── exceptions.py
│
│   ├── infrastructure/
│   │   ├── db/
│   │   │   ├── db.py
│   │   │   ├── schema.sql
│   │   │   └── repositories/
│   │   │       ├── material_repo.py
│   │   │       ├── recipe_repo.py
│   │   │       ├── lot_repo.py        # NUEVO (clave)
│   │   │       └── movement_repo.py   # opcional futuro
│
│   └── config/
│       └── settings.py
│
└── tests/
```

---

# 4. Rediseño de base de datos (ahora orientado a inventario)

## 4.1 materia_prima

* id
* nombre_insumo
* unidad_medida_base
* unidad_medida_consumo

👉 Sin precios aquí

---

## 4.2 lotes (NÚCLEO DEL SISTEMA)

Representa compras activas con stock restante.

* id
* materia_prima_id (FK)
* cantidad_inicial
* cantidad_disponible   ← **clave**
* precio_unitario
* fecha_compra

---

## 4.3 receta

* id
* nombre_producto
* rendimiento

---

## 4.4 receta_ingrediente

* id
* receta_id
* materia_prima_id
* cantidad

---

## 4.5 (opcional futuro) movimientos_inventario

Para trazabilidad completa (ventas, mermas, etc.)

---

# 5. Modelo de dominio (actualizado)

## Entidades

* MateriaPrima
* Lote   ← **nuevo core**
* Receta
* IngredienteReceta

---

## Value Objects

* Cantidad (valor + unidad)
* Dinero
* UnidadMedida

---

## Nueva abstracción importante

```text
StockDisponible(materia_prima)
```

No es tabla → es **concepto de dominio**

---

# 6. Regla de negocio redefinida (formal)

Para cada ingrediente:

```text
1. Obtener todos los lotes con:
   cantidad_disponible > 0

2. Filtrar por materia_prima

3. Seleccionar:
   precio_maximo ENTRE esos lotes

4. Convertir unidades

5. Calcular costo
```

---

## Fórmula

```text
costo_total = Σ(
    cantidad_receta_normalizada * precio_max_lotes_disponibles
)

costo_unitario = costo_total / rendimiento
```

---

# 7. Capa de servicios (redefinida)

## cost_service (crítico)

Responsabilidad real:

```text
calcular_costo_receta(receta_id)
```

Pipeline:

```text
1. Obtener receta
2. Obtener ingredientes
3. Para cada ingrediente:
    a. obtener lotes disponibles
    b. validar que exista stock
    c. seleccionar precio máximo
    d. convertir unidades
4. sumar costos
5. dividir por rendimiento
```

---

## inventory_service (nuevo, clave)

Responsabilidades:

* registrar compra → crea lote
* consultar stock disponible
* validar disponibilidad

---

## unit_service

Sin cambios conceptuales, pero ahora es más crítico.

---

# 8. Repositorios (data access)

Ahora necesitas explícitamente:

### lot_repo

* obtener lotes por materia prima
* filtrar disponibles
* obtener precios

---

### Importante

El filtrado de “stock disponible” puede hacerse:

* en SQL (más eficiente)
* o en dominio (más flexible)

👉 Recomendación: **SQL + validación en dominio**

---

# 9. Estrategias de costo (ahora sí bien diseñadas)

Antes era histórico → ahora es inventario-aware

```text
CostStrategy

→ MaxPriceAvailableStockStrategy   ← ACTUAL
→ WeightedAverageStockStrategy     ← FUTURO
→ FIFO / LIFO                      ← FUTURO
```

---

## Beneficio

Tu sistema evoluciona hacia:

```text
motor de valoración de inventario
```

(no solo cálculo de recetas)

---

# 10. UI (impacto del cambio)

Ahora necesitas una vista adicional obligatoria:

### Registro de compras (lotes)

Porque:

* sin lotes → no hay costos

---

## Flujo real de uso

```text
1. Crear materia prima
2. Registrar compras (crear lotes)
3. Crear receta
4. Calcular costo
```

---

# 11. Validaciones críticas (más estrictas ahora)

* insumo sin stock disponible → ERROR (no warning)
* múltiples lotes → elegir el máximo
* unidades incompatibles → ERROR duro
* rendimiento <= 0 → inválido

---

# 12. Riesgos si ignoras este rediseño

Si no haces esto:

* usarás precios irrelevantes
* tendrás costos irreales
* no podrás evolucionar a inventario real
* romperás consistencia cuando agregues ventas

---

# 13. Diferencia conceptual clave (antes vs ahora)

| Antes                  | Ahora                           |
| ---------------------- | ------------------------------- |
| precio histórico       | precio de inventario disponible |
| compras como historial | lotes como estado               |
| sin inventario real    | inventario implícito            |
| simple pero incorrecto | correcto y extensible           |

---

# 14. Resumen arquitectónico

Tu sistema ahora es:

```text
Sistema de costeo basado en inventario por lotes
```

Con:

* separación de capas
* dominio explícito
* reglas intercambiables
* base lista para crecer a:

  * inventario real
  * ventas
  * márgenes
  * simulaciones de costo

---

# 15. Siguiente paso lógico

Ahora sí estamos en un punto serio.

Te recomiendo como siguiente iteración:

1. Definir contratos de servicios (inputs/outputs exactos)
2. Diseñar el `schema.sql` completo
3. Definir modelo de unidades (esto puede romper todo si se hace mal)

---

Si quieres, en el siguiente paso puedo:

* diseñarte el esquema SQL exacto listo para ejecutar
* definir interfaces tipo “arquitectura limpia”
* o modelar el flujo de cálculo paso a paso con pseudo-objetos

Elige profundidad.
