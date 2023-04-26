select * from Cerveja where Pais = 'Mexico';
select distinct Fabricante, Pais from automoveis

select num, depnum from projeto


select nome, sobrenome from consumidores where cpf not in (select cpf from negocios)
select nome from empregado where ident not in (select identemp from dependente)

select ident, nome from empregado where endereco like 'São%'

select ident, nome from empregado where superident is null
select local from deploc union (select local from projeto)