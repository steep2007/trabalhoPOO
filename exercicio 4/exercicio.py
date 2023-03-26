class Empregados:
    def __init__(self):
        self.__codigo = None
        self.__matricula = None
        self.__nome = None
        self.__tipo = []

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        self.__tipo.append(tipo)

class Frequencia:
    def __init__(self, empregado, turno, dia):
        self.__empregado = empregado
        self.__turno = turno
        self.__dia = dia
        self.__tipo = []

    def getEmpregado(self):
        return self.__empregado

    def getTurno(self):
        return self.__turno

    def getDia(self):
        return self.__dia

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tip):
        self.__tipo.append(tip)

class diaDaSemana:
    def __init__(self):
        self.__codigo = None
        self.__nomeCurto = None
        self.__nome = None

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, cod):
        self.__codigo = cod

    def getNomeCurto(self):
        return self.__nomeCurto

    def setNomeCurto(self, nomC):
        self.__nomeCurto = nomC

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome = nom

class Turno:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__id = None

    def getInicio(self):
        return self.__inicio

    def setInicio(self, inicio):
        self.__inicio = inicio

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getFim(self):
        return self.__fim

    def setFim(self, fim):
        self.__fim = fim

empregado = Empregados()
empregado.setCodigo(111)
empregado.setMatricula(12345)
empregado.setNome('Andre')
empregado.setTipo('Professor')

print('Informações do empregado:')
print('Código:', empregado.getCodigo())
print('Matrícula:', empregado.getMatricula())
print('Nome:', empregado.getNome())
print('Tipo:', empregado.getTipo())

dia = diaDaSemana()
dia.setCodigo(1)
dia.setNomeCurto('S')
dia.setNome('Segunda-feira')

print('Informações do dia da semana:')
print('Código:', dia.getCodigo())
print('Nome curto:', dia.getNomeCurto())
print('Nome:', dia.getNome())

turno = Turno()
turno.setInicio('07:00')
turno.setFim('11:00')
turno.setId(1)

print('Informações do turno:')
print('ID:', turno.getId())
print('Início:', turno.getInicio())
print('Fim:', turno.getFim())

frequencia = Frequencia(empregado, turno, dia)

print('Frequência:')
print(frequencia.getEmpregado().getNome())
print(frequencia.getDia().getNome())
print(frequencia.getTurno().getInicio())
