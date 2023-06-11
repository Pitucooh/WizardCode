create database cadastro;
use cadastro;

CREATE TABLE IF NOT EXISTS cadastro
                 (nome TEXT, email TEXT, senha TEXT);
                 
INSERT INTO cadastro VALUES (?, ?, ?);

SELECT * FROM cadastro WHERE email=? AND senha=?;

describe cadastro;

select * from cadastro;