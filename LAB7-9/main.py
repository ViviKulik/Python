from TestCases.tests import *
from business.service import *
from domain.validators import *
from persistenta.filerepo import *
from prezentare.ui import *
from testare.teste import Teste
import unittest

validatorStudent = ValidatorStudent()
validatorDisciplina = ValidatorDisciplina()
validatorNota = ValidatorNota()
repoStudenti = StudentiRepositoryFile("repoStudenti.txt")
repoDiscipline = DisciplineRepositoryFile("repoDiscipline.txt")
repoNote = NoteRepositoryFile("repoNote.txt")
serviceStudenti = ServiceStudenti(validatorStudent, repoStudenti)
serviceDiscipline = ServiceDiscipline(validatorDisciplina, repoDiscipline)
serviceNote = ServiceNote(validatorNota, repoNote, repoStudenti, repoDiscipline)
consola = UI(serviceStudenti, serviceDiscipline, serviceNote)

# TESTE
# teste = Teste()
# teste.runTests()

# testCaseDomainStudenti = TestCaseDomainStudenti()

# if __name__ == '__main__':
#     unittest.main()

consola.run()
