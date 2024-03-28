import unittest

import erori
from domain.entities import *
from erori.repoError import RepoError
from erori.validationError import ValidError
from domain.validators import *
from persistenta.filerepo import *
from utils.fileutils import clearFile


class Teste:

    def runTests(self):
        self.__runStudentiRepoTests()
        self.__runDisciplineRepoTests()
        self.__runNoteRepoTests()
        self.__testCreazaStudent()
        self.__testEgalStudent()
        self.__testValidatorStudent()
        self.__testCreazaDisciplina()
        self.__testEgalDisciplina()
        self.__testValidatorDisciplina()
        self.__testCreazaNota()
        self.__testEgalNota()
        self.__testValidatorNota()

    def __runStudentiRepoTests(self):
        fileName = "repoTestStudenti.txt"
        clearFile(fileName)
        repo = StudentiRepositoryFile(fileName)
        assert repo.size() == 0
        student = Student("1", "Alex")
        assert repo.size() == 0
        repo.store(student)
        assert repo.size() == 1
        student2 = Student("2", "Iarina")
        repo.store(student2)
        assert repo.size() == 2
        clearFile(fileName)
        student = Student(5, "Alex")
        repo.store(student)
        assert repo.cautaStudent(5) == student
        try:
            repo.cautaStudent("3")
            assert False
        except RepoError:
            pass
        clearFile(fileName)
        student = Student(7, "Alex")
        repo.store(student)
        repo.modificaStudent(7, "Tudor")
        student = repo.cautaStudent(7)
        assert student.getName() == "Tudor"
        clearFile(fileName)
        student = Student("10", "Alex")
        repo.store(student)
        repo.stergeStudent(10)
        assert repo.size() == 0

    def __runDisciplineRepoTests(self):
        fileName = "repoTestDiscipline.txt"
        clearFile(fileName)
        repo = DisciplineRepositoryFile(fileName)
        disc = Disciplina(1, "FP", "Czibula")
        assert repo.size() == 0
        repo.store(disc)
        assert repo.size() == 1
        disc2 = Disciplina(2, "ASC", "Vancea")
        repo.store(disc2)
        assert repo.size() == 2
        disc3 = Disciplina(2, "LC", "Pop")
        try:
            repo.store(disc3)
            assert False
        except RepoError:
            pass
        clearFile(fileName)
        disc = Disciplina(1, "FP", "Czibula")
        repo.store(disc)
        assert repo.cautaDisciplina(1) == disc
        try:
            repo.cautaDisciplina(3)
            assert False
        except RepoError:
            pass
        disc = Disciplina(8, "FP", "Czibula")
        repo.store(disc)
        repo.modificaNumeDisciplina(8, "ASC")
        repo.modificaProfDisciplina(8, "Vancea")
        disc = repo.cautaDisciplina(8)
        assert disc.getName() == "ASC"
        assert disc.getProf() == "Vancea"
        clearFile(fileName)
        disc = Disciplina(10, "FP", "Czibula")
        repo.store(disc)
        repo.stergeDisc(10)
        assert repo.size() == 0

    def __runNoteRepoTests(self):
        fileName = "repoTestNote.txt"
        repo = NoteRepositoryFile(fileName)
        assert repo.size() == 15
        nota = Nota(13, 2, 3, 10)
        try:
            repo.store(nota)
            assert False
        except RepoError:
            pass
        repo.stergeNota(15)
        nota1 = Nota(15, 1, 1, 6)
        repo.store(nota1)
        nota2 = repo.cautaNota(15)
        assert nota1 == nota2
        repo.stergeNota(15)
        nota = Nota(15, 1, 1, 6)
        repo.store(nota)
        repo.modificaNota(15, 8)
        nota = repo.cautaNota(15)
        assert nota.getNota() - 8 < 0.0001

    def __testCreazaStudent(self):
        student = Student("1", "Alex")
        assert student.getID() == "1"
        assert student.getName() == "Alex"

    def __testEgalStudent(self):
        student1 = Student("1", "Alex")
        student2 = Student("1", "Alex")
        assert student1 == student2

    def __testCreazaDisciplina(self):
        disciplina = Disciplina("1", "FP", "Czibula")
        assert disciplina.getID() == "1"
        assert disciplina.getName() == "FP"
        assert disciplina.getProf() == "Czibula"

    def __testEgalDisciplina(self):
        d1 = Disciplina("1", "FP", "Czibula")
        d2 = Disciplina("1", "FP", "Czibula")
        assert d1 == d2

    def __testCreazaNota(self):
        nota = Nota("1", 1, 1, 10.0)
        assert nota.getID() == "1"
        assert nota.getIdStudent() == 1
        assert nota.getIdDisc() == 1
        assert nota.getNota() == 10.0

    def __testEgalNota(self):
        nota1 = Nota("1", 1, 1, 10.0)
        nota2 = Nota("1", 1, 2, 10.0)
        assert nota1 == nota2

    def __testValidatorStudent(self):
        student = Student("-3", "")
        vs = ValidatorStudent()
        try:
            vs.valideaza(student)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID student invalid!\nNume student invalid!\n"

    def __testValidatorDisciplina(self):
        disciplina = Disciplina("-5", "", "")
        vd = ValidatorDisciplina()
        try:
            vd.valideaza(disciplina)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID disciplina invalid!\nNume disciplina invalid!\nNume profesor invalid!\n"

    def __testValidatorNota(self):
        nota = Nota("-1", 1, 1, -5)
        vn = ValidatorNota()
        try:
            vn.valideaza(nota)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID nota invalid!\nValoare nota invalida!\n"
