START TRANSACTION;
-- REFUGIOS
INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `link_foto`, `lista_voluntarios`, `token`) VALUES
('Calle Solidaria',
 'Paseo Colon 850',
 'Si no ppudiste terminar tus estudios nosotros te ayudamos',
 'Estudio',
 '1111-1111',
 'link_foto',
 '[2222]',
 'hgfedba');

INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `link_foto`, `lista_voluntarios`, `token`) VALUES
('Universtory',
 'Av Libertador 6796',
 'Hacemos revisiones clinicas a quienes menos tienen y mas lo necesitan',
 'VideoConsultas',
 '2222-2222',
 'LINK_FOTO',
 '[5555]',
 'abcdefgh');

INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `link_foto`, `lista_voluntarios`, `token`) VALUES
('Donation+',
 'Av Libertador 6796',
 'Somos un merendero con duchas',
 'ONGS',
 '3333-3333',
 'link',
 '[3333, 4444]',
 '12345678');

INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `link_foto`, `token`) VALUES
('Orthix',
 'Av Libertador 6796',
 'Si tuviste una lesion ultimamente veni que hacemos protesis a medida',
 'Ortesis', 
 '4444-4444',
 'link',
 '87654321');


-- VOLUNTARIOS
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`, `token`) VALUES
(2222, 'asesor principal', '1123454', 'Lucas', 1, '5678efgh');
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`, `token`) VALUES
(3333, 'Desarrollador', '4565789', 'Agustin', 3, '5678abcd');
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`, `token`) VALUES
(4444, 'UX/UI', '9876543', 'Tobias', 3, 'efgh1234');
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`, `token`) VALUES
(5555, 'Desarrollador', '011245', 'Martin', 2, 'abcd1234');

COMMIT;