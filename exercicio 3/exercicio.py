class Funcionario:
    def __init__(self):
        self.__nome = None
        self.__idade = None
        self.__matricula = None
        self.__departamento = None

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome = nom

    def getIdade(self):
        return self.__idade

    def setIdade(self, ida):
        self.__idade = ida

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, mat):
        self.__matricula = mat

    def getDepartamento(self):
        return self.__departamento

    def setDepartamneto(self, dep):
        self.__departamento = dep

class Departamento:
    def __init__(self):
        self.__professores = []
        self.__horas = []
        self.__numero = None
        self.__nome = None
        self.__coordenador = None

    def getProfessores(self):
        return self.__professores

    def setProfessores(self, prof):
        self.__professores.append(prof)

    def getHoras(self):
        return self.__horas

    def setHoras(self, hor):
        self.__horas.append(hor)

    def getNumero(self):
        return self.__numero

    def setNumero(self, num):
        self.__numero = num

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome = nom

    def getCoordenador(self):
        return self.__coordenador

    def setCoordenador(self, coor):
        self.__coordenador = coor

class Centro:
    def __init__(self):
        self.__nome = None
        self.__chefe = None
        self.__telefone = None
        self.__departamento = []

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome = nom

    def getChefe(self):
        return self.__chefe

    def setChefe(self, che):
        self.__chefe = che

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, tel):
        self.__telefone = tel

    def getDepartamento(self):
        return self.__departamento

    def setDepartamento(self, dep):
        self.__departamento.append(dep)

class Professores:
    def __init__(self):
        self.__cargo = None
        self.__espPesquisa = None
        self.__projeto = []
        self.__horas = []
        self.__departamento = []

    def getCargo(self):
        return self.__cargo

    def setCargo(self, car):
        self.__cargo = car

    def getEspPesquisa(self):
        return self.__espPesquisa

    def setEspPesquisa(self, esp):
        self.__espPesquisa = esp

    def getProjeto(self):
        return self.__projeto

    def setProjeto(self, pro):
        self.__projeto.append(pro)

    def getHoras(self):
        return self.__horas

    def setHoras(self, hor):
        self.__horas.append(hor)

    def getDepartamento(self):
        return self.__departamento

    def setDepartamento(self, dep):
        self.__departamento.append(dep)

class Horas:
    def __init__(self):
        self.__quantidade = None

    def getQuantidade(self):
        return self.__quantidade

    def setQuantidade(self, quan):
        self.__quantidade = quan

class Projeto:
    def __init__(self):
        self.__professor = None
        self.__numero = None
        self.__orgFinanciador = None
        self.__dataInicio = None
        self.__dataFinal = None
        self.__orcamento = None
        self.__estudante = []

    def getProfessor(self):
        return self.__professor

    def setProfessor(self, professor):
        self.__professor = professor

    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = numero

    def getOrgFinanciador(self):
        return self.__orgFinanciador

    def setOrgFinanciador(self, orgFinanciador):
        self.__orgFinanciador = orgFinanciador

    def getDataInicio(self):
        return self.__dataInicio

    def setDataInicio(self, dataInicio):
        self.__dataInicio = dataInicio

    def getDataFinal(self):
        return self.__dataFinal

    def setDataFinal(self, dataFinal):
        self.__dataFinal = dataFinal

    def getOrcamento(self):
        return self.__orcamento

    def setOrcamento(self, orcamento):
        self.__orcamento = orcamento

    def getEstudante(self):
        return self.__estudante

    def setEstudante(self, est):
        self.__estudante.append(est)

class Estudantes:
    def __init__(self):
        self.__nome = None
        self.__idade = None
        self.__matricula = None
        self.__planoCurso = None
        self.__projeto = []
        self.__alunoPadrinho = None

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getPlanoCurso(self):
        return self.__planoCurso

    def setPlanoCurso(self, planoCurso):
        self.__planoCurso = planoCurso

    def getProjeto(self):
        return self.__projeto

    def setProjeto(self, projeto):
        self.__projeto.append(projeto)

    def getAlunoPadrinho(self):
        return self.__alunoPadrinho

    def setAlunoPadrinho(self, alunoPadrinho):
        self.__alunoPadrinho = alunoPadrinho

class Financiador:
    def __init__(self):
        self.__projetos = []
        self.__nome = None
        self.__cnpj = None
        self.__endereco = None
        self.__telefone = None

    def getProjetos(self):
        return self.__projetos

    def setProjetos(self, projetos):
        self.__projetos.append(projetos)

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCnpj(self):
        return self.__cnpj

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, telefone):
        self.__telefone = telefone


func1 = Funcionario()
func1.setNome("Victor Gabriel")
func1.setIdade(35)
func1.setMatricula(123456)
func1.setDepartamneto("TI")

print("Nome do funcionário:", func1.getNome())
print("Idade do funcionário:", func1.getIdade())
print("Matrícula do funcionário:", func1.getMatricula())
print("Departamento do funcionário:", func1.getDepartamento())


dep1 = Departamento()
dep1.setNome("Departamento de Ciência da Computação")
dep1.setNumero(123)
dep1.setCoordenador("Julinha Furacão")
dep1.setProfessores("Bruna Soares")
dep1.setProfessores("Brenda Souza")
dep1.setHoras(40)
dep1.setHoras(20)

print("Nome do departamento:", dep1.getNome())
print("Número do departamento:", dep1.getNumero())
print("Coordenador do departamento:", dep1.getCoordenador())
print("Professores do departamento:", dep1.getProfessores())
print("Horas do departamento:", dep1.getHoras())

centro1 = Centro()
centro1.setNome("Centro de Tecnologia da Informação")
centro1.setChefe("Carlos Alberto")
centro1.setTelefone("1234567890")
centro1.setDepartamento(dep1)

print("Nome do centro:", centro1.getNome())
print("Chefe do centro:", centro1.getChefe())
print("Telefone do centro:", centro1.getTelefone())
print("Departamento do centro:", centro1.getDepartamento()[0].getNome())

prof1 = Professores()
prof1.setCargo("Professor Doutor")
prof1.setEspPesquisa("Redes de Computadores")
prof1.setDepartamento(dep1)
prof1.setHoras(20)
prof1.setProjeto("Arduino")
prof1.setProjeto("Investimento")

print("Cargo do professor:", prof1.getCargo())
print("Especialidade de pesquisa do professor:", prof1.getEspPesquisa())
print("Departamento do professor:", prof1.getDepartamento()[0].getNome())
print("Horas do professor:", prof1.getHoras())
print("Projetos do professor:", prof1.getProjeto())


horas1 = Horas()
horas1.setQuantidade(40)
print("Quantidade de horas:", horas1.getQuantidade())

projeto1 = Projeto()
projeto1.setProfessor("Andre Quintiliano")
projeto1.setNumero(1)
projeto1.setOrgFinanciador("CNPq")
projeto1.setDataInicio("01/01/2023")
projeto1.setDataFinal("01/07/2023")
projeto1.setOrcamento(50000.00)

print("Professor:", projeto1.getProfessor())
print("Número:", projeto1.getNumero())
print("Organização financiadora:", projeto1.getOrgFinanciador())
print("Data de início:", projeto1.getDataInicio())
print("Data final:", projeto1.getDataFinal())
print("Orçamento:", projeto1.getOrcamento())

estudante1 = Estudantes()
estudante1.setNome("Taylor Swift")
estudante1.setIdade(15)
estudante1.setMatricula(1234)
estudante1.setPlanoCurso("Bacharelado em Ciência da Computação")
estudante1.setAlunoPadrinho("Lana")
estudante1.setProjeto(projeto1)

print("Nome do estudante: ", estudante1.getNome())
print("Idade do estudante: ", estudante1.getIdade())
print("Matrícula do estudante: ", estudante1.getMatricula())
print("Plano de curso do estudante: ", estudante1.getPlanoCurso())
print("Aluno padrinho do estudante: ", estudante1.getAlunoPadrinho())
print("Projeto do estudante: ", estudante1.getProjeto()[0].getNumero())

financiador1 = Financiador()
financiador1.setNome("CNPq")
financiador1.setCnpj("12345678901234")
financiador1.setEndereco("Rua S, 123")
financiador1.setTelefone("55 11 1234-5678")
financiador1.setProjetos(projeto1)

print("Nome do financiador:", financiador1.getNome())
print("CNPJ do financiador:", financiador1.getCnpj())
print("Endereço do financiador:", financiador1.getEndereco())
print("Telefone do financiador:", financiador1.getTelefone())
