import unittest

from business.service import *
from domain.validators import *
from persistenta.filerepo import *
from utils.fileutils import clearFile


class TestCaseDomainStudenti(unittest.TestCase):
    def setUp(self):
        # code executed before every testMethod
        self.st1 = Student("1", "Robi")
        self.stGresit = Student("-1", "")
        self.val = ValidatorStudent()

    def tearDown(self):
        # cleanup code executed after every testMethod
        pass

    def testCreeaza(self):
        student = Student("2", "Alex")
        self.assertTrue(student.getID() == "2")
        self.assertTrue(student.getName() == "Alex")

    def testEgalStudent(self):
        st2 = Student("1", "Robi")
        self.assertEqual(self.st1, st2)

    def testSterge(self):
        self.st1.sterge()
        self.assertTrue(self.st1.getSters())

    # def testValidatorStudent(self):
    #     self.assertRaises(ValidError, self.val.valideaza(self.stGresit))


class TestCaseRepoStudenti(unittest.TestCase):
    def setUp(self) -> None:
        self.val = ValidatorStudent()
        fileName = "repoTestStudenti.txt"
        self.repo = StudentiRepositoryFile(fileName)
        self.st1 = Student(1, "Robi")
        clearFile(fileName)
        self.repo.store(self.st1)

    def tearDown(self) -> None:
        pass

    def testStore(self):
        self.assertTrue(self.repo.size() == 1)
        self.repo.store(Student(2, "Alex"))
        self.assertTrue(self.repo.size() == 2)

    def testCauta(self):
        self.assertEqual(self.repo.cautaStudent(1), self.st1)
        # self.assertRaises(RepoError, self.repo.cautaStudent(2))

    def testModifica(self):
        self.repo.modificaStudent(1, "Alex")
        self.assertTrue(self.repo.cautaStudent(1).getName() == "Alex")

    def testSterge(self):
        self.repo.stergeStudent(1)
        self.assertTrue(self.repo.size() == 0)


class TestCaseDomainDiscipline(unittest.TestCase):
    def setUp(self) -> None:
        self.disciplina1 = Disciplina(1, "fp", "istvan")
        self.disciplinaGresita = Disciplina(-3, "", "")
        self.val = ValidatorDisciplina()

    def tearDown(self) -> None:
        pass

    def testCreazaDisciplina(self):
        disciplina = Disciplina(2, "analiza", "berinde")
        self.assertEqual(disciplina.getID(), 2)
        self.assertEqual(disciplina.getName(), "analiza")
        self.assertEqual(disciplina.getProf(), "berinde")

    def testSterge(self):
        self.disciplina1.sterge()
        self.assertTrue(self.disciplina1.getSters())

    def testEgal(self):
        disciplina = Disciplina(1, "analiza", "berinde")
        self.assertEqual(self.disciplina1, disciplina)

    # def testValidator(self):
    #     self.assertRaises(ValidError, self.val.valideaza(self.disciplinaGresita))


class TestCaseDomainNote(unittest.TestCase):
    def setUp(self) -> None:
        self.val = ValidatorNota()
        self.nota1 = Nota(1, 1, 1, 9.5)
        self.notaGresita = Nota(-1, 1, 1, -1)

    def tearDown(self) -> None:
        pass

    def testCreazaNota(self):
        nota = Nota(2, 1, 1, 7.5)
        self.assertEqual(nota.getID(), 2)
        self.assertEqual(nota.getIdStudent(), 1)
        self.assertEqual(nota.getIdDisc(), 1)
        self.assertEqual(nota.getNota(), 7.5)

    def testStergeNota(self):
        self.nota1.sterge()
        self.assertTrue(self.nota1.getSters())

    def testEgalNota(self):
        nota2 = Nota(1, 1, 1, 9.5)
        self.assertEqual(self.nota1, nota2)

    # def testValidatorNota(self):
    #     self.assertRaises(ValidError, self.val.valideaza(self.notaGresita))


class TestCaseRepoNote(unittest.TestCase):
    def setUp(self) -> None:
        fileName = "repoTestNote.txt"
        self.repo = NoteRepositoryFile(fileName)
        self.nota1 = Nota(1, 1, 1, 9.5)
        clearFile(fileName)
        self.repo.store(self.nota1)

    def tearDown(self) -> None:
        pass

    def testStore(self):
        self.assertTrue(self.repo.size() == 1)
        self.repo.store(Nota(2, 1, 1, 7))
        self.assertTrue(self.repo.size() == 2)
        # self.assertRaises(RepoError, self.repo.store(Nota(1, 1, 1, 5)))

    def testCautaNota(self):
        self.assertEqual(self.repo.cautaNota(1), self.nota1)

    def testStergeNota(self):
        self.repo.stergeNota(1)
        self.assertEqual(self.repo.size(), 0)


class TestCaseRepositoryDiscipline(unittest.TestCase):
    def setUp(self) -> None:
        self.val = ValidatorDisciplina()
        self.disciplina1 = Disciplina(1, "fp", "istvan")
        fileName = "repoTestDiscipline.txt"
        self.repo = DisciplineRepositoryFile(fileName)
        clearFile(fileName)
        self.repo.store(self.disciplina1)

    def tearDown(self) -> None:
        pass

    def testStore(self):
        self.assertEqual(self.repo.size(), 1)
        self.repo.store(Disciplina(2, "analiza", "berinde"))
        self.assertEqual(self.repo.size(), 2)

    def testCautaDisciplina(self):
        self.assertEqual(self.repo.cautaDisciplina(1), self.disciplina1)

    def testStergeDisciplina(self):
        self.repo.stergeDisc(1)
        self.assertEqual(self.repo.size(), 0)


class TestCaseService(unittest.TestCase):
    def setUp(self) -> None:
        self.st1 = Student(1, "Robi")
        self.disc1 = Disciplina(1, "fp", "istvan")
        self.nota1 = Nota(1, 1, 1, 9.5)
        self.valSt = ValidatorStudent()
        self.valDisc = ValidatorDisciplina()
        self.valNota = ValidatorNota()
        fileNameSt = "repoTestStudenti.txt"
        fileNameDisc = "repoTestDisc.txt"
        fileNameNote = "repoTestNote.txt"
        self.repoSt = StudentiRepositoryFile(fileNameSt)
        self.repoDisc = DisciplineRepositoryFile(fileNameDisc)
        self.repoNote = NoteRepositoryFile(fileNameNote)
        self.srvSt = ServiceStudenti(self.valSt, self.repoSt)
        self.srvDisc = ServiceDiscipline(self.valDisc, self.repoDisc)
        self.srvNote = ServiceNote(self.valNota, self.repoNote, self.repoSt, self.repoDisc)
        clearFile(fileNameSt)
        clearFile(fileNameDisc)
        clearFile(fileNameNote)
        self.srvSt.adaugaStudent(self.st1)
        self.srvDisc.adaugaDisc(self.disc1)
        self.srvNote.AdaugaNota(self.nota1)

    def tearDown(self) -> None:
        pass

    def testStergeStudentSiNote(self):
        self.srvNote.StergeStudentSiNote(1)
        self.assertEqual(self.srvNote.size(), 0)
        self.assertEqual(self.srvSt.size(), 0)

    def testStergeDisciplinaSiNote(self):
        self.srvNote.StergeDisciplinaSiNote(1)
        self.assertEqual(self.srvNote.size(), 0)
        self.assertEqual(self.srvDisc.size(), 0)

    def testModificaNota(self):
        self.srvNote.modificaNota(1, 7.8)
        self.assertEqual(self.srvNote.cautaNota(1).getNota(), 7.8)

    def testGetAllStudentiSiNote(self):
        st2 = Student(2, "Raluca")
        self.srvSt.adaugaStudent(st2)
        st3 = Student(3, "Marian")
        self.srvSt.adaugaStudent(st3)
        disc2 = Disciplina(2, "analiza", "berinde")
        self.srvDisc.adaugaDisc(disc2)
        nota2 = Nota(2, 1, 2, 7.5)
        self.srvNote.AdaugaNota(nota2)
        nota3 = Nota(3, 2, 1, 10)
        self.srvNote.AdaugaNota(nota3)
        nota4 = Nota(4, 2, 2, 9)
        self.srvNote.AdaugaNota(nota4)
        nota5 = Nota(5, 3, 1, 6)
        self.srvNote.AdaugaNota(nota5)
        nota6 = Nota(6, 3, 2, 9.5)
        self.srvNote.AdaugaNota(nota6)
        self.assertTrue(self.srvNote.getAllStudentiSiNote(2) == [('Marian', [9.5]), ('Raluca', [9.0]), ('Robi', [7.5])])
        self.assertTrue(self.srvNote.getAllStudentiSiNote(1) == [('Marian', [6.0]), ('Raluca', [10.0]), ('Robi', [9.5])])

    def testGetSefiDePromotie(self):
        st2 = Student(2, "Raluca")
        self.srvSt.adaugaStudent(st2)
        st3 = Student(3, "Marian")
        self.srvSt.adaugaStudent(st3)
        st4 = Student(4, "Andreea")
        self.srvSt.adaugaStudent(st4)
        st5 = Student(5, "Cristian")
        self.srvSt.adaugaStudent(st5)
        disc2 = Disciplina(2, "analiza", "berinde")
        self.srvDisc.adaugaDisc(disc2)
        nota2 = Nota(2, 1, 2, 7.5)
        self.srvNote.AdaugaNota(nota2)
        nota3 = Nota(3, 2, 1, 10)
        self.srvNote.AdaugaNota(nota3)
        nota4 = Nota(4, 2, 2, 9)
        self.srvNote.AdaugaNota(nota4)
        nota5 = Nota(5, 3, 1, 6)
        self.srvNote.AdaugaNota(nota5)
        nota6 = Nota(6, 3, 2, 9.5)
        self.srvNote.AdaugaNota(nota6)
        nota7 = Nota(7, 4, 1, 10)
        self.srvNote.AdaugaNota(nota7)
        nota8 = Nota(8, 4, 2, 9.5)
        self.srvNote.AdaugaNota(nota8)
        nota9 = Nota(9, 5, 1, 7)
        self.srvNote.AdaugaNota(nota9)
        nota10 = Nota(10, 5, 2, 8)
        self.srvNote.AdaugaNota(nota10)
        self.assertEqual(self.srvNote.getSefiDePromotie()[0], st4)

    def testWorstStudents(self):
        st2 = Student(2, "Raluca")
        self.srvSt.adaugaStudent(st2)
        st3 = Student(3, "Marian")
        self.srvSt.adaugaStudent(st3)
        disc2 = Disciplina(2, "analiza", "berinde")
        self.srvDisc.adaugaDisc(disc2)
        nota2 = Nota(2, 1, 2, 7.5)
        self.srvNote.AdaugaNota(nota2)
        nota3 = Nota(3, 2, 1, 10)
        self.srvNote.AdaugaNota(nota3)
        nota4 = Nota(4, 2, 2, 9)
        self.srvNote.AdaugaNota(nota4)
        nota5 = Nota(5, 3, 1, 6)
        self.srvNote.AdaugaNota(nota5)
        nota6 = Nota(6, 3, 2, 9.5)
        self.srvNote.AdaugaNota(nota6)
        self.assertEqual(self.srvNote.getWorstStudents("-")[0], st3)
        self.assertEqual(self.srvNote.getWorstStudents("-")[1], self.st1)
        self.assertEqual(self.srvNote.getWorstStudents("-")[2], st2)
