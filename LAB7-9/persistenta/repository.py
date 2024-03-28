from erori.repoError import RepoError


class RepositoryStudenti:
    def __init__(self):
        self._studenti = {}

    def store(self, student):
        if student.getID() in self._studenti:
            raise RepoError("Student deja existent!")
        self._studenti[student.getID()] = student

    def stergeStudent(self, idStudent):
        if idStudent not in self._studenti or self._studenti[idStudent].getSters == True:
            raise RepoError("Student inexistent!")
        self._studenti[idStudent].sterge()

    def cautaStudent(self, idStudent):
        if idStudent not in self._studenti:
            raise RepoError("Student inexistent!")
        return self._studenti[idStudent]

    def modificaStudent(self, idStudent, numeNou):
        if idStudent not in self._studenti:
            raise RepoError("Student inexistent!")
        self._studenti[idStudent].setName(numeNou)

    def size(self):
        return len(self._studenti)

    def getAll(self):
        l_studenti = []
        for idStudent in self._studenti:
            student = self._studenti[idStudent]
            if not student.getSters():
                l_studenti.append(student)
        return l_studenti


class RepositoryDiscipline:
    def __init__(self):
        self._discipline = {}

    def store(self, disc):
        if disc.getID() in self._discipline:
            raise RepoError("Discplina deja existenta!")
        self._discipline[disc.getID()] = disc

    def stergeDisc(self, idDisciplina):
        if idDisciplina not in self._discipline or self._discipline[idDisciplina].getSters == True:
            raise RepoError("Student inexistent!")
        self._discipline[idDisciplina].sterge()

    def cautaDisciplina(self, idDisc):
        if idDisc not in self._discipline:
            raise RepoError("Disciplina inexistenta!")
        return self._discipline[idDisc]

    def modificaNumeDisciplina(self, idDisciplina, numeNou):
        if idDisciplina not in self._discipline:
            raise RepoError("Student inexistent!")
        self._discipline[idDisciplina].setName(numeNou)

    def modificaProfDisciplina(self, idDisciplina, profNou):
        if idDisciplina not in self._discipline:
            raise RepoError("Student inexistent!")
        self._discipline[idDisciplina].setProf(profNou)

    def size(self):
        return len(self._discipline)

    def getAll(self):
        l_discipline = []
        for idDisciplina in self._discipline:
            if not self._discipline[idDisciplina].getSters():
                l_discipline.append(self._discipline[idDisciplina])
        return l_discipline


class RepositoryNote:
    def __init__(self):
        self._note = {}

    def store(self, nota):
        if nota.getID() in self._note:
            raise RepoError("Nota deja existenta!")
        self._note[nota.getID()] = nota

    def stergeNota(self, idNota):
        if idNota not in self._note or self._note[idNota].getSters() == True:
            raise RepoError("Nota inexistenta!")
        self._note[idNota].sterge()

    def cautaNota(self, idNota):
        if idNota not in self._note:
            raise RepoError("Nota inexistenta!")
        return self._note[idNota]

    def modificaNota(self, idNota, valNoua):
        if idNota not in self._note:
            raise RepoError("Nota inexistenta!")
        self._note[idNota].setNota(valNoua)

    def size(self):
        return len(self._note)

    def getAll(self):
        return list(self._note.values())
