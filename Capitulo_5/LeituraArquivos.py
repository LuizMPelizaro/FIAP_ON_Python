# -*- coding: utf-8 -*-
with open("ArquivosGerados/teste.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(f"Tipo de dado da variavel {type(conteudo)}\n"
      f"Conteúdo do arquivo:{conteudo}")

