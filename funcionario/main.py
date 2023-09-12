from cargo import Cargo
from funcionario import Funcionario

cargo_jr = Cargo(1000, 'Dev JR')
cargo_sr = Cargo(5000, 'Dev SR')

funcionarios = []

funcionario_1 = Funcionario('Funcionario 1', '123', cargo_sr)
funcionario_2 = Funcionario('Funcionario 2', '456', cargo_jr)
funcionario_3 = Funcionario('Funcionario 3', '789', cargo_jr)

funcionarios.append(funcionario_1)
funcionarios.append(funcionario_2)
funcionarios.append(funcionario_3)

funcionario_1.add_dependente('Dependente 1', '999')
funcionario_1.add_dependente('Dependente 2', '888')
funcionario_1.add_dependente('Dependente 3', '777')

funcionario_1.rem_dependente('777')

for funcionario in funcionarios:
    funcionario.mostra_dados()
    print('\n')
print('----------')
for dependente in funcionario_1.dependentes:
    dependente.mostra_dados()
