import copy

from domain.entities import *
from erori.repoError import RepoError
from erori.validationError import ValidError


class UI:

    def __init__(self, serviceStudenti, serviceDisc, serviceNote):
        self.__serviceStudenti = serviceStudenti
        self.__serviceNote = serviceNote
        self.__serviceDisc = serviceDisc
        self.__stack = []
        self.__inputs = {
            "adauga_student": self.__uiAdaugaStudent,
            "adauga_disciplina": self.__uiAdaugaDisc,
            "adauga_nota": self.__uiAdaugaNota,
            "print_studenti": self.__uiPrintStudenti,
            "print_discipline": self.__uiPrintDisc,
            "print_note": self.__uiPrintNote,
            "sterge_student": self.__uiStergeStudentSiNote,
            "sterge_disciplina": self.__uiStergeDisciplinaSiNote,
            "sterge_nota": self.__uiStergeNota,
            "cauta_student": self.__uiCautaStudentID,
            "cauta_disciplina": self.__uiCautaDisciplinaID,
            "cauta_nota": self.__uiCautaNotaID,
            "modifica_student": self.__uiModificaStudent,
            "modifica_nume_disciplina": self.__uiModificaNumeDisciplina,
            "modifica_prof_disciplina": self.__uiModificaProfDisciplina,
            "modifica_valoare_nota": self.__uiModificaNota,
            "print_studenti_si_note": self.__uiPrintAllStudentiSiNote,
            "print_sefi_promotie": self.__uiPrintSefiPromotie,
            "worst_students": self.__uiPrintWorstStudents,
            "genereaza_studenti": self.__uiGenerateStudent,
            "comenzi": self.__printMenu,
        }

    def __uiAdaugaStudent(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        idStudent = int(self.__params[0])
        numeStudent = self.__params[1]
        st = Student(idStudent, numeStudent)
        self.__serviceStudenti.adaugaStudent(st)
        print("Student adaugat cu succes!")

    def __uiAdaugaDisc(self):
        if len(self.__params) != 3:
            print("Numar parametri invalid!")
            return
        idDisc = int(self.__params[0])
        numeDisc = self.__params[1]
        profDisc = self.__params[2]
        disc = Disciplina(idDisc, numeDisc,  profDisc)
        self.__serviceDisc.adaugaDisc(disc)
        print("Disciplina adaugata cu succes!")

    def __uiAdaugaNota(self):
        if len(self.__params) != 4:
            print("Numar parametri invalid!")
            return
        idNota = int(self.__params[0])
        idStudent = int(self.__params[1])
        idDisciplina = int(self.__params[2])
        valNota = float(self.__params[3])
        nota = Nota(idNota, idStudent, idDisciplina, valNota)
        self.__serviceNote.AdaugaNota(nota)

    def __uiPrintDisc(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        discipline = self.__serviceDisc.getAll()
        if len(discipline) == 0:
            print("Nu exista discipline in aplicatie!")
            return
        for disciplina in discipline:
            print(disciplina)

    def __uiPrintStudenti(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        studenti = self.__serviceStudenti.getAll()
        if len(studenti) == 0:
            print("Nu exista studenti in aplicatie")
            return
        for student in studenti:
            print(student)

    def __uiPrintNote(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        note = self.__serviceNote.getAll()
        if len(note) == 0:
            print("Nu exista note in aplicatie")
            return
        for nota in note:
            print(nota)

    def __uiStergeStudentSiNote(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idStudent = int(self.__params[0])
        self.__serviceNote.StergeStudentSiNote(idStudent)
        print(f"Studentul cu id {idStudent} si notele lui au fost sterse cu succes!")

    def __uiStergeDisciplinaSiNote(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idDisc = int(self.__params[0])
        self.__serviceNote.StergeDisciplinaSiNote(idDisc)
        print(f"Disciplina cu id {idDisc} si notele asociate au fost sterse cu succes!")

    def __uiStergeNota(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idNota = int(self.__params[0])
        self.__serviceNote.StergeNota(idNota)
        print(f"Nota cu id {idNota} a fost stearsa cu succes!")

    def __uiCautaNotaID(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idNota = int(self.__params[0])
        print(self.__serviceNote.cautaNota(idNota))

    def __uiCautaStudentID(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idStudent = int(self.__params[0])
        print(self.__serviceStudenti.cautaStudent(idStudent))

    def __uiCautaDisciplinaID(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        idDisciplina = int(self.__params[0])
        print(self.__serviceDisc.cautaDisciplina(idDisciplina))

    def __uiModificaStudent(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        idStudent = int(self.__params[0])
        numeNouStudent = self.__params[1]
        self.__serviceStudenti.modificaStudent(idStudent, numeNouStudent)

    def __uiModificaNumeDisciplina(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        ifDisciplina = int(self.__params[0])
        numeNouDisc = self.__params[1]
        self.__serviceDisc.modificaNumeDisc(ifDisciplina, numeNouDisc)

    def __uiModificaProfDisciplina(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        ifDisciplina = int(self.__params[0])
        profNouDisc = self.__params[1]
        self.__serviceDisc.modificaProfDisc(ifDisciplina, profNouDisc)

    def __uiModificaNota(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        idNota = int(self.__params[0])
        notaNoua = self.__params[1]
        self.__serviceNote.modificaNota(idNota, notaNoua)

    def __uiPrintAllStudentiSiNote(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        studenti = self.__serviceNote.getAllStudentiSiNote(self.__params[0])
        for student in studenti:
            print(student)

    def __uiPrintSefiPromotie(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        studenti = self.__serviceNote.getSefiDePromotie()
        for student in studenti:
            print(student)

    def __uiPrintWorstStudents(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        studenti = self.__serviceNote.getWorstStudents(self.__params[0])
        for student in studenti:
            print(student)

    def __uiGenerateStudent(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        nrOfGeneratedStudents = self.__params[0]
        self.__serviceStudenti.generateStudent(nrOfGeneratedStudents)

    def __printMenu(self):
        print("Comenzi:")
        print("- adauga_student\n- adauga_disciplina\n- adauga_nota\n- print_studenti\n"
              "- print_discipline\n- print_note\n- sterge_student\n- sterge_disciplina\n"
              "- sterge_nota\n- cauta_student\n- cauta_disciplina\n- cauta_nota\n"
              "- modifica_student\n- modifica_nume_disciplina\n- modifica_prof_disciplina\n"
              "- modifica_valoare_nota\n- print_studenti_si_note\n- print_sefi_promotie\n"
              "- worst_students\n- genereaza_studenti\n- comenzi\n- exit")

    def run(self):
        print("[comenzi] pentru meniu comenzi")
        self.__printMenu()
        while True:
            input0 = input(">>>")
            input0 = input0.strip()
            if input0 == "":
                continue
            if input0 == "exit":
                return
            parti = input0.split()
            input1 = parti[0]
            self.__params = parti[1:]
            if input1 in self.__inputs:
                try:
                    self.__inputs[input1]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid!")
                except ValidError as ve:
                    print(f"Valid error:{ve}")
                except RepoError as re:
                    print(f"Repository error:{re}")
            else:
                print("Comanda invalida!")
