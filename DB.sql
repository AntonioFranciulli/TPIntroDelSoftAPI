CREATE TABLE refugios (
    id_refugio INT NOT NULL AUTO_INCREMENT,
    nombre_refugio VARCHAR(50) NOT NULL,
    direccion VARCHAR(200)NOT NULL,
    descripcion VARCHAR(200)DEFAULT NULL,
    tipo_refugio VARCHAR(50),
    telefono VARCHAR(20),
    link_foto VARCHAR(10000) DEFAULT NULL,
    lista_voluntarios VARCHAR(2000)DEFAULT NULL,
    token VARCHAR(20) DEFAULT NULL,
    PRIMARY KEY(ID_refugio)
);

CREATE TABLE voluntarios (
cuil_voluntario INT NOT NULL,
puesto VARCHAR(50)NOT NULL,
telefono VARCHAR(50)NOT NULL,
nombre VARCHAR(50)NOT NULL,
id_refugio INT NOT NULL,
link_foto VARCHAR(10000) DEFAULT NULL,
token VARCHAR(20) DEFAULT NULL,
PRIMARY KEY (cuil_voluntario),
FOREIGN KEY (id_refugio) REFERENCES refugios(id_refugio)
);



