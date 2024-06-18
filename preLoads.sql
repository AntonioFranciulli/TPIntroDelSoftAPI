START TRANSACTION;
-- REFUGIOS
INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `link_foto`, `lista_voluntarios`, `token`) VALUES
('Calle Solidaria',
 'Paseo Colon 850, San Telmo, Buenos Aires, 1063, Argentina',
 'Si no ppudiste terminar tus estudios nosotros te ayudamos',
 'Estudio',
 '1111-1111',
 'https://media.lacapital.com.ar/p/90db6f8482a928b1aa2fd723ea31f14f/adjuntos/203/imagenes/100/071/0100071190/1200x675/smart/image-13png.png',
 '[2222]',
 'hgfedba');

INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `link_foto`, `lista_voluntarios`, `token`) VALUES
('Universtory',
 'Cuenca 4347, Villa Pueyrredon, Buenos Aires, 1428, Argentina',
 'Hacemos revisiones clinicas a quienes menos tienen y mas lo necesitan',
 'VideoConsultas',
 '2222-2222',
 'https://www.zoorprendente.com/wp-content/uploads/2018/02/3000-2.jpg',
 '[5555]',
 'abcdefgh');

INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `link_foto`, `lista_voluntarios`, `token`) VALUES
('Donation+',
 'Pedro moran 3653, Villa Devoto, Buenos Aires, 1419, Argentina',
 'Somos un merendero con duchas',
 'ONGS',
 '3333-3333',
 'https://i.ytimg.com/vi/YX0q_2u1a8g/maxresdefault.jpg',
 '[3333, 4444]',
 '12345678');

INSERT INTO `refugios` (`nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `link_foto`, `token`) VALUES
('Orthix',
 'Av Libertador 6796, Belgrano, Buenos Aires, 1092, Argentina',
 'Si tuviste una lesion ultimamente veni que hacemos protesis a medida',
 'Ortesis', 
 '4444-4444',
 'https://i.ytimg.com/vi/YZ6esA40A_Q/maxresdefault.jpg',
 '87654321');


-- VOLUNTARIOS
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`, `token`) VALUES
(2222, 'asesor principal', '1123454', 'Lucas', 1, '5678efgh');
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`, `token`) VALUES
(3333, 'Desarrollador', '4565789', 'Agustin', 3, '5678abcd');
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`, `token`) VALUES
(4444, 'UX/UI', '9876543', 'Tobias', 3, 'efgh1234');
INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`,`link_foto`, `token`) VALUES
(5555, 'Desarrollador', '011245', 'Martin', 2, 'https://foto.haberler.com/haber/2021/02/13/dunyaca-unlu-sarkici-ricky-martin-in-son-goru-13924888_amp.jpg','abcd1234');

COMMIT;