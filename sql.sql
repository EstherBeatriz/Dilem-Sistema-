create database bd_dilem;

use bd_dilem;

CREATE TABLE usuarios (
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL PRIMARY KEY,
  ocupacao VARCHAR(255) NOT NULL,
  instituicao VARCHAR(255) NOT NULL,
  senha VARCHAR(255) NOT NULL,
  tipo_usuario INT(1) NOT NULL DEFAULT 0
);

