CREATE TABLE IF NOT EXISTS refugios (
    id_refugio INT,
    nombre_refugio VARCHAR(50),
    direccion VARCHAR(50),
    descripcion VARCHAR(50),
    tipo_refugio VARCHAR(50),
    telefono VARCHAR(20),
    lista_voluntarios VARCHAR(2000),
    PRIMARY KEY(ID_refugio)

);

CREATE TABLE if not EXISTS voluntarios (
cuil_voluntario INT,
puesto VARCHAR(50),
telefono VARCHAR(50),
nombre VARCHAR(50),
id_refugio INT,
PRIMARY KEY (cuil_voluntario),
FOREIGN KEY (id_refugio) REFERENCES refugios(id_refugio)
);
