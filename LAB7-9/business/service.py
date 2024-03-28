from domain.entities import Student, Disciplina, Nota, SefDTO
from utils.generatorutils import randomString


class ServiceStudenti:

    def __init__(self, validatorStudent, repoStudenti):
        self.__validatorStudent = validatorStudent
        self.__repoStudenti = repoStudenti

    def adaugaStudent(self, student):
        self.__validatorStudent.valideaza(student)
        self.__repoStudenti.store(student)

    def cautaStudent(self, idStudent):
        return self.__repoStudenti.cautaStudent(idStudent)

    def modificaStudent(self, idStudent, numeNouStudent):
        self.__repoStudenti.modificaStudent(idStudent, numeNouStudent)

    def getAll(self):
        return self.__repoStudenti.getAll()

    def size(self):
        return self.__repoStudenti.size()

    def generateStudent(self, nrOfGeneratedStudents):
        for i in range(0, int(nrOfGeneratedStudents)):
            studenti = self.__repoStudenti.getAll()
            if len(studenti) > 0:
                lastStudent = list(studenti)[-1]
                idStudent = lastStudent.getID() + 1
            else:
                idStudent = 1
            numeStudent = randomString(5)
            self.adaugaStudent(idStudent, numeStudent)


class ServiceDiscipline:

    def __init__(self, validatorDisc, repoDisc):
        self.__validatorDisc = validatorDisc
        self.__repoDisc = repoDisc

    def adaugaDisc(self, disciplina):
        self.__validatorDisc.valideaza(disciplina)
        self.__repoDisc.store(disciplina)

    def cautaDisciplina(self, idDisciplina):
        return self.__repoDisc.cautaDisciplina(idDisciplina)

    def modificaNumeDisc(self, idDisciplina, numeNouDisc):
        self.__repoDisc.modificaNumeDisciplina(idDisciplina, numeNouDisc)

    def modificaProfDisc(self, idDisciplina, profNouDisc):
        self.__repoDisc.modificaProfDisciplina(idDisciplina, profNouDisc)

    def getAll(self):
        return self.__repoDisc.getAll()

    def size(self):
        return self.__repoDisc.size()


class ServiceNote:

    def __init__(self, validatorNota, repoNote, repoStudenti, repoDisc):
        self.__validatorNota = validatorNota
        self.__repoNote = repoNote
        self.__repoStudenti = repoStudenti
        self.__repoDisc = repoDisc

    def AdaugaNota(self, nota):
        self.__validatorNota.valideaza(nota)
        self.__repoNote.store(nota)

    def cautaNota(self, idNota):
        return self.__repoNote.cautaNota(idNota)

    def StergeStudentSiNote(self, idStudent):
        note = self.__repoNote.getAll()
        noteStudent = [x for x in note if x.getIdStudent() == idStudent]
        for notaStudent in noteStudent:
            self.__repoNote.stergeNota(notaStudent.getID())
        self.__repoStudenti.stergeStudent(idStudent)

    def StergeDisciplinaSiNote(self, idDisciplina):
        note = self.__repoNote.getAll()
        noteDiscipline = [x for x in note if x.getIdDisc() == idDisciplina]
        for notaDisc in noteDiscipline:
            self.__repoNote.stergeNota(notaDisc.getID())
        self.__repoDisc.stergeDisc(idDisciplina)

    def StergeNota(self, idNota):
        self.__repoNote.stergeNota(idNota)

    def modificaNota(self, idNota, notaNoua):
        self.__repoNote.modificaNota(idNota, notaNoua)

    def getAllStudentiSiNote(self, idDisciplina):
        allNote = self.__repoNote.getAll()
        noteDisc = []
        for nota in allNote:
            if idDisciplina == "-":
                noteDisc.append(nota)
            elif nota.getIdDisc() == int(idDisciplina):
                noteDisc.append(nota)
        noteDisc.sort(key=lambda x: x.getNota(), reverse=True)
        situatieStudenti = {}
        for nota in noteDisc:
            student = self.__repoStudenti.cautaStudent(nota.getIdStudent())
            numeStudent = student.getName()
            if numeStudent not in situatieStudenti:
                situatieStudenti[numeStudent] = []
            situatieStudenti[numeStudent].append(nota.getNota())
        sortedSituatieStudenti = sorted(situatieStudenti.items(), key=lambda x: x[0])
        return sortedSituatieStudenti

    def getSefiDePromotie(self):
        allNote = self.__repoNote.getAll()
        situatieStudenti = {}
        for nota in allNote:
            idStudent = nota.getIdStudent()
            if idStudent not in situatieStudenti:
                situatieStudenti[idStudent] = []
            situatieStudenti[idStudent].append(nota.getNota())
        rez = []
        for idStudent in situatieStudenti:
            student = self.__repoStudenti.cautaStudent(idStudent)
            numeStudent = student.getName()
            medie = sum(situatieStudenti[idStudent])/len(situatieStudenti[idStudent])
            sef = SefDTO(idStudent, numeStudent, medie)
            rez.append(sef)
        rez.sort(key=lambda x: x.getMedie(), reverse=True)
        l = int(len(rez)/5)
        return rez[:l]

    def getWorstStudents(self, param):
        allNote = self.__repoNote.getAll()
        situatieStudenti = {}
        for nota in allNote:
            idStudent = nota.getIdStudent()
            if idStudent not in situatieStudenti:
                situatieStudenti[idStudent] = []
            situatieStudenti[idStudent].append(nota.getNota())
        rez = []
        for idStudent in situatieStudenti:
            student = self.__repoStudenti.cautaStudent(idStudent)
            numeStudent = student.getName()
            medie = sum(situatieStudenti[idStudent]) / len(situatieStudenti[idStudent])
            sef = SefDTO(idStudent, numeStudent, medie)
            rez.append(sef)
        rez.sort(key=lambda x: x.getMedie(), reverse=False)
        if param == "-":
            return rez[:]
        else:
            return rez[:int(param)]

    def getAll(self):
        return self.__repoNote.getAll()

    def size(self):
        return self.__repoNote.size()
