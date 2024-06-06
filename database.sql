CREATE TABLE IF NOT EXISTS refugios (
    ID_refugio INT,
    nombre_refugio VARCHAR(50),
    direccion VARCHAR(50),
    descripcion VARCHAR(50),
    tipo_refugio VARCHAR(50),
    telefono VARCHAR(20),
    lista_voluntarios VARCHAR(2000),
    PRIMARY KEY(ID_refugio)

);

CREATE TABLE if not EXISTS voluntarios (
CUIL_voluntario INT,
puesto VARCHAR(50),
telefono VARCHAR(50),
Nombre VARCHAR(50),
ID_refugio INT,
PRIMARY KEY (CUIL_voluntario),
FOREIGN KEY (ID_refugio) REFERENCES refugios(ID_refugio)
);




