CREATE TABLE refugios (
    id_refugio INT NOT NULL AUTO_INCREMENT,
    nombre_refugio VARCHAR(50) NOT NULL,
    direccion VARCHAR(50)NOT NULL,
    descripcion VARCHAR(50)DEFAULT NULL,
    tipo_refugio VARCHAR(50),
    telefono VARCHAR(20),
    lista_voluntarios VARCHAR(2000)DEFAULT NULL,
    PRIMARY KEY(ID_refugio)
);

CREATE TABLE voluntarios (
cuil_voluntario INT NOT NULL,
puesto VARCHAR(50)NOT NULL,
telefono VARCHAR(50)NOT NULL,
nombre VARCHAR(50)NOT NULL,
id_refugio INT NOT NULL,
PRIMARY KEY (cuil_voluntario),
FOREIGN KEY (id_refugio) REFERENCES refugios(id_refugio)
);



