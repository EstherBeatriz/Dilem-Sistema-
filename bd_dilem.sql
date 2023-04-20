-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Abr-2023 às 07:17
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bd_dilem`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `administrador`
--

CREATE TABLE `administrador` (
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `ocupacao` varchar(255) NOT NULL,
  `instituicao` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `chamados`
--

CREATE TABLE `chamados` (
  `id_chamado` int(11) NOT NULL,
  `area` varchar(10) DEFAULT NULL,
  `avaliacao` int(11) DEFAULT NULL,
  `situacao` varchar(11) DEFAULT NULL,
  `sub_ou_man` varchar(11) DEFAULT NULL,
  `pergunta1` text DEFAULT NULL,
  `pergunta2` text DEFAULT NULL,
  `pergunta3` text DEFAULT NULL,
  `pergunta4` text DEFAULT NULL,
  `pergunta5` text DEFAULT NULL,
  `pergunta6` text DEFAULT NULL,
  `data_form` date DEFAULT NULL,
  `objeto_afetado` varchar(30) DEFAULT NULL,
  `nome_numerosala` varchar(10) DEFAULT NULL,
  `bloco` char(1) DEFAULT NULL,
  `data_envio` date DEFAULT NULL,
  `hora_envio` time DEFAULT NULL,
  `fk_Usuario_email` varchar(30) DEFAULT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `chamados`
--

INSERT INTO `chamados` (`id_chamado`, `area`, `avaliacao`, `situacao`, `sub_ou_man`, `pergunta1`, `pergunta2`, `pergunta3`, `pergunta4`, `pergunta5`, `pergunta6`, `data_form`, `objeto_afetado`, `nome_numerosala`, `bloco`, `data_envio`, `hora_envio`, `fk_Usuario_email`, `descricao`) VALUES
(7, 'Técnico TI', NULL, 'Não resolvi', 'Manutenção', 'E falta de internet?: Nao', 'E problema de software?: não sei relatar', 'Sobre o problema: Está me impedindo de realizar o meu trabalho', 'E problema recorrente?: nao sei relatar', 'Ja teve manutencao: nao sei relatar', 'retirar esse objeto: Sim', '2023-04-05', 'Computador', 'Laboratóri', 'a', '0000-00-00', '20:49:21', '0000871809@senaimgaluno.com.br', 'O computador não quer mais ligar e meus arquivos importantes estão lá.'),
(8, 'Técnico TI', NULL, 'Não resolvi', 'Substituiçã', 'E falta de internet?: Nao', 'E problema de software?: não sei relatar', 'Sobre o problema: Está me impedindo de realizar o meu trabalho', 'E problema recorrente?: Sim', 'Ja teve manutencao: Sim', 'retirar esse objeto: Sim', '2023-04-06', 'Computador', 'Laboratóri', 'c', '0000-00-00', '01:54:59', '0000717122@senaimgaluno.com.br', 'O Computador liga e desliga e da tela Azul, e só depois de alguns momentos ele volta mas desliga de novo e não liga mais,');

-- --------------------------------------------------------

--
-- Estrutura da tabela `reserva`
--

CREATE TABLE `reserva` (
  `finalidade` varchar(1000) DEFAULT NULL,
  `data_reserva` date DEFAULT NULL,
  `horario_inicio` time DEFAULT NULL,
  `horario_fim` time DEFAULT NULL,
  `id_reserva` int(11) NOT NULL,
  `disciplina` varchar(20) DEFAULT NULL,
  `fk_Usuario_email` varchar(30) DEFAULT NULL,
  `fk_Sala_id_sala` int(11) DEFAULT NULL,
  `fk_Turma_id_turma` int(11) DEFAULT NULL,
  `status` varchar(100) NOT NULL DEFAULT 'Aguardando'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `reserva`
--

INSERT INTO `reserva` (`finalidade`, `data_reserva`, `horario_inicio`, `horario_fim`, `id_reserva`, `disciplina`, `fk_Usuario_email`, `fk_Sala_id_sala`, `fk_Turma_id_turma`, `status`) VALUES
('Prova Téorica', '2023-04-06', '08:00:00', '12:00:00', 9, 'Programação ', '0000871809@senaimgaluno.com.br', 57, 1, 'Aguardando'),
('Estudar para a prova.', '2023-04-07', '12:00:00', '16:00:00', 10, 'Matemática', '0000871809@senaimgaluno.com.br', 59, 5, 'Aguardando'),
('Leitura', '2023-04-28', '07:00:00', '12:00:00', 11, 'Literatura', '0000871809@senaimgaluno.com.br', 57, 6, 'Aguardando'),
('Apresentação dos Alunos', '2023-04-07', '12:00:00', '15:00:00', 12, 'Artes', '0000863801@senaimgaluno.com.br', 58, 4, 'Aguardando'),
('Aula Normal de Teoria', '2023-04-08', '19:00:00', '22:00:00', 13, 'Física', '0000717122@senaimgaluno.com.br', 57, 5, 'Aguardando');

-- --------------------------------------------------------

--
-- Estrutura da tabela `sala`
--

CREATE TABLE `sala` (
  `id_sala` int(11) NOT NULL,
  `bloco` char(1) DEFAULT NULL,
  `nome_ou_numerosala` varchar(30) DEFAULT NULL,
  `capacidade` int(11) DEFAULT NULL,
  `recursos` text DEFAULT NULL,
  `finalidade` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `sala`
--

INSERT INTO `sala` (`id_sala`, `bloco`, `nome_ou_numerosala`, `capacidade`, `recursos`, `finalidade`) VALUES
(51, 'b', 'Eletroeletrônica', 40, 'Máquinas;Equipamentos para manutenção;Quadro Branco;Mural de lembretes', 'Sala desenvolvida para aulas relacionadas e eletroeletrônica.'),
(52, 'b', 'Laboratório 103 B', 15, 'Máquinas ;Mesas duplas; Quadro', 'Laboratório de manutenção de máquinas e processos.'),
(53, 'b', 'Laboratório 102B', 30, 'Máquinas;Computadores;Quadro Branco;Mural de lembretes;Ventilador', 'Sala para aulas nas áreas de Redes e Eletroeletrônica.'),
(54, 'b', 'Laboratório CIM', 25, 'Computadores;Quadro;Mural e lembretes;Mesas duplas', 'Sala direcionada para aulas de Redes.'),
(55, 'b', 'Laboratório Robótica LEGO', 35, 'Lego;Mesas redondas - 6 pessoas;Mural de lembretes;Quadro;Ventilador', 'Laboratório direcionado para aulas para turmas do SESI sobre Robótica e Lego'),
(56, 'a', 'Sala 207A', 45, 'Televisão fixa;Quadro;Mural de lembretes;Ar Condicionado', 'Sala direcionada para aulas teóricas, atividades e aplicação de provas.'),
(57, 'b', 'Sala 201B', 40, 'Televisão fixa;Ar Condicionado;Retroprojetor;Quadro Branco', 'Sala para aulas nos computadores.'),
(58, 'b', ' Sala de Criatividade ', 50, 'Máquina de costura;Impressora 3D;Televisão não fixa;Quadro;3 Computadores;Mesas para 6 pessoas;Armários ;Mural de lembretes', 'Sala para apresentação de trabalhos, produção de protótipos e aulas diferenciadas.'),
(59, 'a', 'Sala 207A', 40, 'Televisão fixa;Quadro Branco;Mural de lembretes;Ar Condicionado;Retroprojetor', 'Sala direcionada para aulas teóricas, atividades e aplicação de provas.'),
(60, 'c', 'Laboratório 107C', 12, ' Impressora 3D;Mesas duplas;Lego;Máquinas', 'Laboratório para a área de robótica.'),
(61, 'c', 'Sala 207C', 40, 'Televisão não fixa;Ar Condicionado;Quadro Branco; Mural e lembretes', 'Sala para aulas nos computadores.'),
(62, 'c', 'Sala 229C', 40, 'Televisão não fixa;Ar Condicionado;Quadro', 'Sala De Aula '),
(63, 'c', 'Sala 220C', 40, 'Televisão não fixa;Ar Condicionado;Quadro', 'Sala de Aula'),
(64, 'c', 'Sala 207B', 40, 'Televisão não fixa;Ar Condicionado;Quadro', 'Sala de Aula');

-- --------------------------------------------------------

--
-- Estrutura da tabela `turma`
--

CREATE TABLE `turma` (
  `id_turma` int(11) NOT NULL,
  `nome_turma` varchar(30) DEFAULT NULL,
  `turno` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `turma`
--

INSERT INTO `turma` (`id_turma`, `nome_turma`, `turno`) VALUES
(1, 'Desenvolvimento de Sistema', 'Noite'),
(2, 'Mecânica', 'Manhã'),
(3, 'Manutenção Automotiva', 'Manhã'),
(4, '9ºB - Sesi', 'Manhã'),
(5, '8ºB - Sesi', 'Manhã'),
(6, '6ºA - Sesi', 'Manhã');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `ocupacao` varchar(255) NOT NULL,
  `instituicao` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `tipo_usuario` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`nome`, `email`, `ocupacao`, `instituicao`, `senha`, `tipo_usuario`) VALUES
('Isabella De Medeiros Duarte', '0000717122@senaimgaluno.com.br', 'Administrador', 'Sesi Senai - Betim', '123', 1),
('Maria Eduarda', '0000863801@senaimgaluno.com.br', 'Desenvolvedora', 'Sesi Senai - Betim', '86486211', 1),
('Esther Beatriz da Costa Oliveira', '0000871809@senaimgaluno.com.br', 'Administradora', 'Sesi Senai - Betim', '26112003', 1),
('Lorena Moreira Costa Xavier', '0000872568@senaimgaluno.com.br', 'Administrador', 'Sesi Senai - Betim', '1327', 0),
('Danyela Lisboa Cunha', 'Dany@gmail.com', 'Lider', 'Sesi Senai - Betim', '123', 1),
('Jhonatan Alves', 'jhonatanalves1998@gmail.com', 'Técnico ', 'Sesi Senai - Betim', '2525', 1),
('Rodrigo Lucas Santos', 'rls@fiemg.com', 'Professor', 'Sesi Senai - Betim', '2023', 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`email`);

--
-- Índices para tabela `chamados`
--
ALTER TABLE `chamados`
  ADD PRIMARY KEY (`id_chamado`);

--
-- Índices para tabela `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`id_reserva`),
  ADD KEY `fk_Sala_id_sala` (`fk_Sala_id_sala`);

--
-- Índices para tabela `sala`
--
ALTER TABLE `sala`
  ADD PRIMARY KEY (`id_sala`);

--
-- Índices para tabela `turma`
--
ALTER TABLE `turma`
  ADD PRIMARY KEY (`id_turma`);

--
-- Índices para tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `chamados`
--
ALTER TABLE `chamados`
  MODIFY `id_chamado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `reserva`
--
ALTER TABLE `reserva`
  MODIFY `id_reserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `sala`
--
ALTER TABLE `sala`
  MODIFY `id_sala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT de tabela `turma`
--
ALTER TABLE `turma`
  MODIFY `id_turma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `fk_Sala_id_sala` FOREIGN KEY (`fk_Sala_id_sala`) REFERENCES `sala` (`id_sala`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
