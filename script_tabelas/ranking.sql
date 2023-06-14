create database jogo;
use jogo;

select * from cadastro;CREATE DATABASE IF NOT EXISTS jogo;
use jogo;

CREATE TABLE IF NOT EXISTS cadastro(nome TEXT, email varchar(50), senha TEXT,
primary key(email));

INSERT INTO cadastro VALUES ("teste", "teste@teste.com", "teste");

CREATE TABLE IF NOT EXISTS Ranking(Nome varchar(30),
Tempo_Total varchar(30),
pontos int,
email varchar (50),
FOREIGN KEY (email) REFERENCES cadastro (email) ON DELETE CASCADE ON UPDATE CASCADE);


INSERT INTO Ranking(Tempo_Total, email) VALUES ("teste", "teste@teste.com");

describe ranking;

drop table ranking;

drop table cadastro;

select * from Ranking;

select * from perguntas;

INSERT INTO Ranking (Tempo_Total, email) VALUES ("234234234", "teste@teste.com");