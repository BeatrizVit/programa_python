create database dbVerificacaoFilme;
use dbVerificacaoFilme;

create table tbVerFilme(
	idVerFilme int primary key auto_increment,
    nomeFilme varchar(45) not null,
    faixaEtariaFilme int not null,
    nomeUsuario varchar(45) not null,
    idadeUsuario int not null
);

select * from tbVerFilme;