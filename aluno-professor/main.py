from professor import Professor
from aluno import Aluno

mariani = Professor(456, 'Mariani', 'endereco', '48988888888')
davi = Aluno(123, 'Davi', 'endereco', mariani)

professores = []
alunos = []

professores.append(mariani)
alunos.append(davi)

print(professores, alunos)

professores.remove(mariani)
alunos.remove(davi)

print(professores, alunos)
