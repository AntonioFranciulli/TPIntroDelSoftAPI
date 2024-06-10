-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 09-06-2024 a las 07:42:14
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `database`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `refugios`
--

CREATE TABLE `refugios` (
  `id_refugio` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_refugio` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `tipo_refugio` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `lista_voluntarios` varchar(2000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `refugios`
--

INSERT INTO `refugios` (`id_refugio`, `nombre_refugio`, `direccion`, `descripcion`, `tipo_refugio`, `telefono`, `lista_voluntarios`) VALUES
(2, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `voluntarios`
--

CREATE TABLE `voluntarios` (
  `cuil_voluntario` int(11) NOT NULL, 
  `puesto` varchar(50) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `id_refugio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `voluntarios`
--

INSERT INTO `voluntarios` (`cuil_voluntario`, `puesto`, `telefono`, `nombre`, `id_refugio`) VALUES
(2222, 'asesor principal', '1123454', 'Lucas', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `refugios`
--
ALTER TABLE `refugios`
  ADD PRIMARY KEY (`id_refugio`);

--
-- Indices de la tabla `voluntarios`
--
ALTER TABLE `voluntarios`
  ADD PRIMARY KEY (`cuil_voluntario`),
  ADD KEY `id_refugio` (`id_refugio`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `voluntarios`
--
ALTER TABLE `voluntarios`
  ADD CONSTRAINT `voluntarios_ibfk_1` FOREIGN KEY (`id_refugio`) REFERENCES `refugios` (`id_refugio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
