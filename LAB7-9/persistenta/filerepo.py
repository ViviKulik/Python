from domain.entities import *
from persistenta.repository import *


class StudentiRepositoryFile(RepositoryStudenti):
    def __init__(self, fileName):
        RepositoryStudenti.__init__(self)
        self.__fileName = fileName

    def __readAllFromFile(self):
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            self._studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(" ")
                    idStudent = int(parts[0])
                    numeStudent = parts[1]
                    student = Student(idStudent, numeStudent)
                    self._studenti[idStudent] = student

    def __writeAllToFile(self):
        with open(self.__fileName, "w") as f:
            for student in self._studenti.values():
                if not student.getSters():
                    f.write(str(student)+"\n")

    def store(self, student):
        self.__readAllFromFile()
        RepositoryStudenti.store(self, student)
        self.__writeAllToFile()

    def modificaStudent(self, idStudent, numeNou):
        self.__readAllFromFile()
        RepositoryStudenti.modificaStudent(self, idStudent, numeNou)
        self.__writeAllToFile()

    def stergeStudent(self, idStudent):
        self.__readAllFromFile()
        RepositoryStudenti.stergeStudent(self, idStudent)
        self.__writeAllToFile()

    def cautaStudent(self, idStudent):
        self.__readAllFromFile()
        return RepositoryStudenti.cautaStudent(self, idStudent)

    def getAll(self):
        self.__readAllFromFile()
        return RepositoryStudenti.getAll(self)

    def size(self):
        self.__readAllFromFile()
        return RepositoryStudenti.size(self)


class DisciplineRepositoryFile(RepositoryDiscipline):
    def __init__(self, fileName):
        RepositoryDiscipline.__init__(self)
        self.__fileName = fileName

    def __readAllFromFile(self):
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            self._discipline.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(" ")
                    idDisciplina = int(parts[0])
                    numeDisciplina = parts[1]
                    profDisciplina = parts[2]
                    disciplina = Disciplina(idDisciplina, numeDisciplina, profDisciplina)
                    self._discipline[idDisciplina] = disciplina

    def __writeAllToFile(self):
        with open(self.__fileName, "w") as f:
            for disciplina in self._discipline.values():
                if not disciplina.getSters():
                    f.write(str(disciplina) + "\n")

    def store(self, disc):
        self.__readAllFromFile()
        RepositoryDiscipline.store(self, disc)
        self.__writeAllToFile()

    def modificaNumeDisciplina(self, idDisc, numeNou):
        self.__readAllFromFile()
        RepositoryDiscipline.modificaNumeDisciplina(self, idDisc, numeNou)
        self.__writeAllToFile()

    def modificaProfDisciplina(self, idDisc, profNou):
        self.__readAllFromFile()
        RepositoryDiscipline.modificaProfDisciplina(self, idDisc, profNou)
        self.__writeAllToFile()

    def stergeDisc(self, idDisc):
        self.__readAllFromFile()
        RepositoryDiscipline.stergeDisc(self, idDisc)
        self.__writeAllToFile()

    def cautaDisciplina(self, idDisc):
        self.__readAllFromFile()
        return RepositoryDiscipline.cautaDisciplina(self, idDisc)

    def getAll(self):
        self.__readAllFromFile()
        return RepositoryDiscipline.getAll(self)

    def size(self):
        self.__readAllFromFile()
        return RepositoryDiscipline.size(self)


class NoteRepositoryFile(RepositoryNote):
    def __init__(self, fileName):
        RepositoryNote.__init__(self)
        self.__fileName = fileName

    def __readAllFromFile(self):
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            self._note.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(" ")
                    idNota = int(parts[0])
                    idStudent = int(parts[1])
                    idDisc = int(parts[2])
                    valNota = float(parts[3])
                    nota = Nota(idNota, idStudent, idDisc, valNota)
                    self._note[idNota] = nota

    def __writeAllToFile(self):
        with open(self.__fileName, "w") as f:
            for nota in self._note.values():
                if not nota.getSters():
                    f.write(str(nota) + "\n")

    def store(self, nota):
        self.__readAllFromFile()
        RepositoryNote.store(self, nota)
        self.__writeAllToFile()

    def modificaNota(self, idNota, valNoua):
        self.__readAllFromFile()
        RepositoryNote.modificaNota(self, idNota, valNoua)
        self.__writeAllToFile()

    def stergeNota(self, idNota):
        self.__readAllFromFile()
        RepositoryNote.stergeNota(self, idNota)
        self.__writeAllToFile()

    def cautaNota(self, idNota):
        self.__readAllFromFile()
        return RepositoryNote.cautaNota(self, idNota)

    def getAll(self):
        self.__readAllFromFile()
        return RepositoryNote.getAll(self)

    def size(self):
        self.__readAllFromFile()
        return RepositoryNote.size(self)
