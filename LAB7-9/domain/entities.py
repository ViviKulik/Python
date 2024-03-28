class Student:
    def __init__(self, idStudent, numeStudent):
        self.__id = idStudent
        self.__name = numeStudent
        self.__sters = False

    def sterge(self):
        self.__sters = True

    def getSters(self):
        return self.__sters

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def setName(self, numeNou):
        self.__name = numeNou

    def __eq__(self, other):
        return self.getID() == other.getID()

    def __str__(self):
        return f"{int(self.__id)} {self.__name}"


class Disciplina:
    def __init__(self, idDisciplina, numeDisciplina, profDisciplina):
        self.__id = idDisciplina
        self.__name = numeDisciplina
        self.__prof = profDisciplina
        self.__sters = False

    def sterge(self):
        self.__sters = True

    def getID(self):
        return self.__id

    def getSters(self):
        return self.__sters

    def getName(self):
        return self.__name

    def setName(self, numeNou):
        self.__name = numeNou

    def setProf(self, profNou):
        self.__prof = profNou

    def getProf(self):
        return self.__prof

    def __eq__(self, other):
        return self.getID() == other.getID()

    def __str__(self):
        return f"{self.__id} {self.__name} {self.__prof}"


class Nota:
    def __init__(self, idNota, idStudent, idDisciplina, valNota):
        self.__id = idNota
        self.__idStudent = idStudent
        self.__idDisciplina = idDisciplina
        self.__valNota = float(valNota)
        self.__sters = False

    def sterge(self):
        self.__sters = True

    def getSters(self):
        return self.__sters

    def getID(self):
        return self.__id

    def getIdStudent(self):
        return self.__idStudent

    def getIdDisc(self):
        return self.__idDisciplina

    def getNota(self):
        return self.__valNota

    def setNota(self, notaNoua):
        self.__valNota = notaNoua

    def __eq__(self, other):
        return self.getID() == other.getID()

    def __str__(self):
        return f"{self.__id} {self.__idStudent} {self.__idDisciplina} {self.__valNota}"


class SefDTO:
    def __init__(self, idStudent, numeStudent, medie):
        self.__id = idStudent
        self.__name = numeStudent
        self.__medie = medie

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getMedie(self):
        return self.__medie

    def __eq__(self, other):
        return self.getID() == other.getID()

    def __str__(self):
        return f"{self.__id} {self.__name} {self.__medie}"
