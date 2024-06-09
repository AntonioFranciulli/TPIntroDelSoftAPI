START TRANSACTION;

INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`) VALUES
('Calle Solidaria', 'Paseo Colon 850', NULL, 'Estudio', '11111111');

INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`) VALUES
(2222, 'asesor principal', '1123454', 'Lucas', 1);

COMMIT;