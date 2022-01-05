maximo = int(input("Escreva ate qual numero da sequencia de fibonacci deseja ver"))
f1 = 0
f2 = 1
fn = 0
for numero in range(1,maximo,1):
    print(f'{numero} - {fn}')
    fn = f1 + f2
    f2 = f1
    f1 = fn

