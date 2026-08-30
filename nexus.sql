-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 30, 2026 at 07:26 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nexus`
--

-- --------------------------------------------------------

--
-- Table structure for table `banimento`
--

CREATE TABLE `banimento` (
  `veto` int(11) NOT NULL,
  `guilda_serv` int(11) NOT NULL,
  `apelido_banido` int(11) NOT NULL,
  `apelido_banidor` int(11) DEFAULT NULL,
  `motivo` varchar(255) DEFAULT NULL,
  `data_banimento` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `banimento`
--

INSERT INTO `banimento` (`veto`, `guilda_serv`, `apelido_banido`, `apelido_banidor`, `motivo`, `data_banimento`) VALUES
(1, 3, 2, 1, 'Teste', '2026-08-30 14:23:43');

-- --------------------------------------------------------

--
-- Table structure for table `canal`
--

CREATE TABLE `canal` (
  `sala` int(11) NOT NULL,
  `guilda_serv` int(11) NOT NULL,
  `secao_canal` int(11) DEFAULT NULL,
  `nome` varchar(50) NOT NULL,
  `tipo` enum('texto','voz') NOT NULL DEFAULT 'texto'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `canal`
--

INSERT INTO `canal` (`sala`, `guilda_serv`, `secao_canal`, `nome`, `tipo`) VALUES
(1, 3, 1, 'Teste', 'voz');

-- --------------------------------------------------------

--
-- Table structure for table `cargo`
--

CREATE TABLE `cargo` (
  `patente` int(11) NOT NULL,
  `guilda_serv` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `permissoes` bigint(20) UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cargo`
--

INSERT INTO `cargo` (`patente`, `guilda_serv`, `nome`, `permissoes`) VALUES
(1, 3, 'Teste', 1);

-- --------------------------------------------------------

--
-- Table structure for table `categoria_canal`
--

CREATE TABLE `categoria_canal` (
  `secao` int(11) NOT NULL,
  `guilda_serv` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categoria_canal`
--

INSERT INTO `categoria_canal` (`secao`, `guilda_serv`, `nome`) VALUES
(1, 3, 'Teste');

-- --------------------------------------------------------

--
-- Table structure for table `convite`
--

CREATE TABLE `convite` (
  `passe` int(11) NOT NULL,
  `guilda_serv` int(11) NOT NULL,
  `sala_canal` int(11) DEFAULT NULL,
  `apelido_criador` int(11) NOT NULL,
  `codigo` varchar(16) NOT NULL,
  `usos_max` int(11) DEFAULT NULL,
  `usos_atual` int(11) NOT NULL DEFAULT 0,
  `data_expiracao` datetime DEFAULT NULL,
  `data_criacao` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `convite`
--

INSERT INTO `convite` (`passe`, `guilda_serv`, `sala_canal`, `apelido_criador`, `codigo`, `usos_max`, `usos_atual`, `data_expiracao`, `data_criacao`) VALUES
(1, 3, 1, 1, 'T3ST3', NULL, 0, NULL, '2026-08-30 14:07:25');

-- --------------------------------------------------------

--
-- Table structure for table `membro`
--

CREATE TABLE `membro` (
  `cracha` int(11) NOT NULL,
  `apelido_usuario` int(11) NOT NULL,
  `guilda_serv` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `apelido_no_servidor` varchar(50) NOT NULL,
  `data_entrada` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `membro`
--

INSERT INTO `membro` (`cracha`, `apelido_usuario`, `guilda_serv`, `nome`, `apelido_no_servidor`, `data_entrada`) VALUES
(3, 1, 3, 'Teste', 'Testando', '2026-08-30 08:59:06');

-- --------------------------------------------------------

--
-- Table structure for table `servidor`
--

CREATE TABLE `servidor` (
  `guilda` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `apelido_dono` int(11) NOT NULL,
  `data_criacao` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `servidor`
--

INSERT INTO `servidor` (`guilda`, `nome`, `apelido_dono`, `data_criacao`) VALUES
(3, 'Servidor Teste 1', 1, '2026-08-29 15:06:29');

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `apelido` int(11) NOT NULL,
  `nome_usuario` varchar(45) NOT NULL,
  `email` varchar(200) NOT NULL,
  `senha` varchar(200) NOT NULL,
  `status_serv` enum('Online','Não Perturbe','AFK','Offline') NOT NULL DEFAULT 'Offline',
  `data_criacao` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`apelido`, `nome_usuario`, `email`, `senha`, `status_serv`, `data_criacao`) VALUES
(1, 'Teste 1', 'teste@teste1.com', '123456', 'Online', '2026-08-29 13:17:00'),
(2, 'Teste 2', 'teste@teste2.com', '123456', 'Online', '2026-08-30 14:18:05');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `banimento`
--
ALTER TABLE `banimento`
  ADD PRIMARY KEY (`veto`),
  ADD KEY `fk_banimento_servidor` (`guilda_serv`),
  ADD KEY `fk_banimento_banido` (`apelido_banido`),
  ADD KEY `fk_banimento_banidor` (`apelido_banidor`);

--
-- Indexes for table `canal`
--
ALTER TABLE `canal`
  ADD PRIMARY KEY (`sala`),
  ADD KEY `fk_canal_servidor` (`guilda_serv`),
  ADD KEY `fk_canal_categoria` (`secao_canal`);

--
-- Indexes for table `cargo`
--
ALTER TABLE `cargo`
  ADD PRIMARY KEY (`patente`),
  ADD UNIQUE KEY `uq_cargo_nome_servidor` (`guilda_serv`,`nome`);

--
-- Indexes for table `categoria_canal`
--
ALTER TABLE `categoria_canal`
  ADD PRIMARY KEY (`secao`),
  ADD KEY `fk_categoria_servidor` (`guilda_serv`);

--
-- Indexes for table `convite`
--
ALTER TABLE `convite`
  ADD PRIMARY KEY (`passe`),
  ADD KEY `fk_convite_servidor` (`guilda_serv`),
  ADD KEY `fk_convite_canal` (`sala_canal`),
  ADD KEY `fk_convite_criador` (`apelido_criador`);

--
-- Indexes for table `membro`
--
ALTER TABLE `membro`
  ADD PRIMARY KEY (`cracha`),
  ADD UNIQUE KEY `uq_membro_ususario_servidor` (`apelido_usuario`,`guilda_serv`),
  ADD KEY `fk_membro_servidor` (`guilda_serv`);

--
-- Indexes for table `servidor`
--
ALTER TABLE `servidor`
  ADD PRIMARY KEY (`guilda`),
  ADD KEY `fk_servidor_dono` (`apelido_dono`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`apelido`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `banimento`
--
ALTER TABLE `banimento`
  MODIFY `veto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `canal`
--
ALTER TABLE `canal`
  MODIFY `sala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cargo`
--
ALTER TABLE `cargo`
  MODIFY `patente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `categoria_canal`
--
ALTER TABLE `categoria_canal`
  MODIFY `secao` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `convite`
--
ALTER TABLE `convite`
  MODIFY `passe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `membro`
--
ALTER TABLE `membro`
  MODIFY `cracha` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `servidor`
--
ALTER TABLE `servidor`
  MODIFY `guilda` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `apelido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `banimento`
--
ALTER TABLE `banimento`
  ADD CONSTRAINT `fk_banimento_banido` FOREIGN KEY (`apelido_banido`) REFERENCES `usuario` (`apelido`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_banimento_banidor` FOREIGN KEY (`apelido_banidor`) REFERENCES `usuario` (`apelido`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_banimento_servidor` FOREIGN KEY (`guilda_serv`) REFERENCES `servidor` (`guilda`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `canal`
--
ALTER TABLE `canal`
  ADD CONSTRAINT `fk_canal_categoria` FOREIGN KEY (`secao_canal`) REFERENCES `categoria_canal` (`secao`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_canal_servidor` FOREIGN KEY (`guilda_serv`) REFERENCES `servidor` (`guilda`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `cargo`
--
ALTER TABLE `cargo`
  ADD CONSTRAINT `fk_cargo_servidor` FOREIGN KEY (`guilda_serv`) REFERENCES `servidor` (`guilda`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `categoria_canal`
--
ALTER TABLE `categoria_canal`
  ADD CONSTRAINT `fk_categoria_servidor` FOREIGN KEY (`guilda_serv`) REFERENCES `servidor` (`guilda`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `convite`
--
ALTER TABLE `convite`
  ADD CONSTRAINT `fk_convite_canal` FOREIGN KEY (`sala_canal`) REFERENCES `canal` (`sala`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_convite_criador` FOREIGN KEY (`apelido_criador`) REFERENCES `usuario` (`apelido`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_convite_servidor` FOREIGN KEY (`guilda_serv`) REFERENCES `servidor` (`guilda`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `membro`
--
ALTER TABLE `membro`
  ADD CONSTRAINT `fk_membro_servidor` FOREIGN KEY (`guilda_serv`) REFERENCES `servidor` (`guilda`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_membro_ususario` FOREIGN KEY (`apelido_usuario`) REFERENCES `usuario` (`apelido`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `servidor`
--
ALTER TABLE `servidor`
  ADD CONSTRAINT `fk_servidor_dono` FOREIGN KEY (`apelido_dono`) REFERENCES `usuario` (`apelido`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
