usuarios: dict = {"Chaves": ["Chaves Silva", "17/06/1975", "Recep_01", 100.00],
                  "Quico": ["Enrico Flores", "03/06/1976", "Raiox_02", 100.00],
                  "Quico": ["Enrico Flores", "04/06/1976", "Raiox_03", 100.00]}
# Outra forma de declarar um dicionario
usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01", 100.00]
usuarios["Florinda"] = ["Florinda Flores", "27/11/2017", "Recep_01", 100.00]

print(usuarios)
print("###########=========###########")
print(f'Dados: {usuarios.get("Chaves")}')

usuarios["Chaves"][3] *= 3
print(usuarios["Chaves"])
