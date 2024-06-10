START TRANSACTION;
-- REFUGIOS
INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`) VALUES
('Calle Solidaria', 'Paseo Colon 850', NULL, 'Estudio', '11111111');
INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`) VALUES
('Universtory', 'Av Libertador 6796', NULL, 'VideoConsultas', '222222');
INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`) VALUES
('Donation+', 'Av Libertador 6796', NULL, 'ONGS', '3333333');
INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`) VALUES
('Orthix', 'Av Libertador 6796', NULL, 'Ortesis', '444444');


-- VOLUNTARIOS
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`) VALUES
(2222, 'asesor principal', '1123454', 'Lucas', 1);
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`) VALUES
(3333, 'Desarrollador', '4565789', 'Agustin', 3);
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`) VALUES
(4444, 'UX/UI', '9876543', 'Tobias', 3);
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`) VALUES
(5555, 'Desarrollador', '011245', 'Martin', 2);

COMMIT;