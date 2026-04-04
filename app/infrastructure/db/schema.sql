PRAGMA foreign_keys = ON;

-- =========================
-- TABLA: materia_prima
-- =========================
CREATE TABLE IF NOT EXISTS materia_prima (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_insumo TEXT NOT NULL UNIQUE,
    unidad_base TEXT NOT NULL,
    unidad_consumo TEXT NOT NULL,
    factor_conversion REAL NOT NULL CHECK (factor_conversion > 0)
);

-- =========================
-- TABLA: lotes
-- =========================
CREATE TABLE IF NOT EXISTS lotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    materia_prima_id INTEGER NOT NULL,

    cantidad_inicial REAL NOT NULL CHECK (cantidad_inicial > 0),
    cantidad_disponible REAL NOT NULL CHECK (
        cantidad_disponible >= 0 AND cantidad_disponible <= cantidad_inicial
    ),

    precio_unitario REAL NOT NULL CHECK (precio_unitario > 0),
    fecha_compra TEXT NOT NULL,

    FOREIGN KEY (materia_prima_id) REFERENCES materia_prima(id)
);

-- Índices clave para performance
CREATE INDEX IF NOT EXISTS idx_lotes_materia
ON lotes (materia_prima_id);

CREATE INDEX IF NOT EXISTS idx_lotes_disponible
ON lotes (cantidad_disponible);

-- =========================
-- TABLA: receta
-- =========================
CREATE TABLE IF NOT EXISTS receta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_producto TEXT NOT NULL UNIQUE,
    rendimiento REAL NOT NULL CHECK (rendimiento > 0)
);

-- =========================
-- TABLA: receta_ingrediente
-- =========================
CREATE TABLE IF NOT EXISTS receta_ingrediente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    receta_id INTEGER NOT NULL,
    materia_prima_id INTEGER NOT NULL,
    cantidad REAL NOT NULL CHECK (cantidad > 0),

    FOREIGN KEY (receta_id) REFERENCES receta(id),
    FOREIGN KEY (materia_prima_id) REFERENCES materia_prima(id),

    UNIQUE (receta_id, materia_prima_id)
);