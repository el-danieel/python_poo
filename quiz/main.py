from quiz import *


if __name__ == '__main__':
    q1 = Quiz(5, 1)
    q2 = Quiz2A(5, 1)
    q3 = Quiz3A(5, 1)
    lista_quiz = [q1, q2, q3]
    a1 = Aluno(1, "Daniel", lista_quiz)
    a2 = Aluno(2, "Giovanna", lista_quiz)
    a3 = Aluno(3, "Erika", lista_quiz)
    a4 = Aluno(4, "Marcos", lista_quiz)
    d1 = Disciplina("POO", "Ferauche", 2, 2)
    d2 = Disciplina("Circuitos Digitais", "Moreira", 2 , 2)
    d1.add_aluno(a1)
    d1.add_aluno(a2)
    d2.add_aluno(a3)
    print(d1)
    print(d2)
