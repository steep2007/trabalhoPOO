class Pessoa:
    def __init__(self):
        self.__nome = None
        self.__sobrenome = None
        self.__email = None
        self.__endereco = None
        self.__telefone = None
        self.__tipo = []

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tip):
        self.__tipo.append(tip)

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome = nom

    def getSobrenome(self):
        return self.__sobrenome

    def setSobrenome(self, sob):
        self.__sobrenome = sob

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, end):
        self.__endereco = end

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, tel):
        self.__telefone = tel

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

class Cliente:
    def __init__(self):
        self.__dataAssociacao = None
        self.__emprestimo = []

    def getDataAssociacao(self):
        return  self.__dataAssociacao

    def setDataAssociacao(self, datA):
        self.__dataAssociacao = datA

    def getEmprestimo(self):
        return self.__emprestimo

    def setEmprestimo(self, emp):
        self.__emprestimo.append(emp)

class Funcionario:
    def __init__(self):
        self.__matricula = None

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, mat):
        self.__matricula = mat

class Emprestimo:
    def __init__(self):
        self.__nome = []
        self.__dataSaida = None
        self.__dataRetorno = None
        self.__valor = None
        self.__funcionario = []

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome.append(nom)

    def getDataSaida(self):
        return self.__dataSaida

    def setDataSaida(self, datS):
        self.__dataSaida = datS

    def getDataRetorno(self):
        return self.__dataRetorno

    def setDataRetorno(self, datR):
        self.__dataRetorno = datR

    def getValor(self):
        return self.__valor

    def setValor(self, val):
        self.__valor = val

    def getFuncionario(self):
        return self.__funcionario

    def setFuncionario(self, fun):
        self.__funcionario.append(fun)

class BlueRay:
    def __init__(self):
        self.__nome = []
        self.__codigoBarras = None
        self.__emprestimo = []

    def getCodigoBarras(self):
        return self.__codigoBarras

    def setCodigoBarras(self, codB):
        self.__codigoBarras = codB

    def getEmprestimo(self):
        return self.__emprestimo

    def setEmprestimo(self, empr):
        self.__emprestimo.append(empr)

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome.append(nom)

class Filme:
    def __init__(self):
        self.__nome = []
        self.__titulo = None
        self.__categoria = None
        self.__id = None
        self.__ano = None
        self.__ator = []
        self.__blueRay = []

    def getNomeF(self):
        return self.__nome

    def setNomeF(self, nom):
        self.__nome.append(nom)

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, tit):
        self.__titulo = tit

    def getCategoria(self):
        return self.__categoria

    def setCategoria(self, cat):
        self.__categoria = cat

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getAtor(self):
        return self.__ator

    def setAtor(self, ator):
        self.__ator.append(ator)

    def getBlueray(self):
        return self.__blueRay

    def setBlueray(self, blRy):
        self.__blueRay.append(blRy)

    def getFilmes(self):
        return self.__filmes

    def setFilmes(self, film):
        self.__filmes = film

class Ator:
    def __init__(self):
        self.__nome = None
        self.__dataNascimento = None
        self.__genero = None
        self.__filmes = []

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome = nom

    def getDataNascimento(self):
        return self.__dataNascimento

    def setDataNascimento(self, datN):
        self.__dataNascimento = datN

    def getGenero(self):
        return self.__genero

    def setGenero(self, gen):
        self.__genero = gen

    def getFilmes(self):
        return self.__filmes

    def setFilmes(self, film):
        self.__filmes.append(film)

pessoa = Pessoa()
pessoa.setNome('Step')
pessoa.setSobrenome('Borges')
pessoa.setEmail('step.borges@gmail.com')
pessoa.setEndereco('Rua das Lindezas, 888')
pessoa.setTelefone('11 111111-1111')
pessoa.setTipo('cliente')

print('Nome completo: ', pessoa.getNome(), pessoa.getSobrenome())
print('E-mail:', pessoa.getEmail())
print('Endereço:', pessoa.getEndereco())
print('Telefone:', pessoa.getTelefone())
print('Tipo:', pessoa.getTipo())


cliente = Cliente()
cliente.setDataAssociacao('01/01/2001')
print('Data de Associação:', cliente.getDataAssociacao())

funcionario = Funcionario()
funcionario.setMatricula('12345')
print('Matrícula:', funcionario.getMatricula())

emprestimo = Emprestimo()
emprestimo.setNome('Emprestimo 8')
emprestimo.setDataSaida('01/03/2023')
emprestimo.setDataRetorno('10/03/2023')
emprestimo.setValor(10.50)
emprestimo.setFuncionario('Bel')
print('Data de Saída:', emprestimo.getDataSaida())
print('Data de Retorno:', emprestimo.getDataRetorno())
print('Valor:', emprestimo.getValor())
print('Funcionário responsável:', emprestimo.getFuncionario())

blueray = BlueRay()
blueray.setNome('Blueray do Scooby Doo')
blueray.setCodigoBarras('1234567890')
blueray.setEmprestimo(emprestimo)
print('Código de Barras:', blueray.getCodigoBarras())
print('Empréstimo:', blueray.getEmprestimo()[0].getNome())

filme = Filme()
filme.setNomeF('Scooby Doo')
filme.setTitulo('Scooby Doo Mistérios S/A')
filme.setCategoria('Desenho')
filme.setId('001')
filme.setAno(2001)
filme.setAtor('Scooby')
filme.setBlueray(blueray)
print('Título:', filme.getTitulo())
print('Categoria:', filme.getCategoria())
print('ID:', filme.getId())
print('Ano:', filme.getAno())
print('Ator principal:', filme.getAtor())
print('Blu-ray:', filme.getBlueray()[0].getNome())

ator = Ator()
ator.setNome('Scooby')
ator.setDataNascimento('25/05/1989')
ator.setGenero('Masculino')
ator.setFilmes(filme)
print('Nome do ator:', ator.getNome())
print('Data de nascimento:', ator.getDataNascimento())
print('Gênero:', ator.getGenero())
print('Filmes em que atuou:', ator.getFilmes()[0].getNomeF())
