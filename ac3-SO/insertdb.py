import random
from connectdb import insert_db
idadeRandom = random.randint(5,23)

filmeSelecionado = input("Filme que deseja ver: ")
faixaEtariaFilme = int(input("Faixa Etária do filme: "))

nome = input("Seu nome: ")
print("Sua idade :",idadeRandom)


if (idadeRandom < faixaEtariaFilme) :
    print("Filme não aconselhado para sua idade")
else :
    print("Tenha um bom filme")
    print(filmeSelecionado)
    
lista = [filmeSelecionado,faixaEtariaFilme,nome,idadeRandom]
insert_db(lista)