class Pessoa:
    def __init__(self):
        self._nome = None
        self._idade = None

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getIdade(self):
        return self._idade

    def setIdade(self, idade):
        self._idade = idade


class Treinador(Pessoa):
    def __init__(self, idade=None, nome=None):
        super().__init__(nome, idade)
        self.__modalidade = None

    def getModalidade(self):
        return self.__modalidade

    def setModalidade(self, modalidade):
        self.__modalidade = modalidade

class Jogador(Pessoa):
    def __init__(self, idade=None, nome=None):
        super().__init__(nome, idade)
        self.__codTurma = None
        self.__posicao = None

    def getCodTurma(self):
        return self.__codTurma

    def setCodTurma(self, codTurma):
        self.__codTurma = codTurma

    def getPosicao(self):
        return self.__posicao

    def setPosicao(self, posicao):
        self.__posicao = posicao

class Modalidade:
    def __init__(self):
        self.__tipo = None
        self.__quantJogador = None
        self.__genero = None

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getQuantJogador(self):
        return self.__quantJogador

    def setQuantJogador(self, quant):
        self.__quantJogador = quant

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero


class Equipe:
    def __init__(self):
        self.__jogador = []
        self.__periodo = None
        self.__cor = None
        self.__modalidade = None

    def getJogador(self):
        return self.__jogador

    def setJogador(self, jogador):
        self.__periodo.append(jogador)

    def getPeriodo(self):
        return self.__periodo

    def setPeriodo(self, periodo):
        self.__periodo = periodo

    def getCor(self):
        return self.__cor

    def setCor(self, cor):
        self.__cor = cor

    def getModalidade(self):
        return self.__modalidade

    def setModalidade(self, mod):
        self.__modalidade = mod

class Horario:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def getInicio(self):
        return self.__inicio

    def setInicio(self, inicio):
        self.__inicio = inicio

    def getFim(self):
        return self.__fim

    def setFim(self, fim):
        self.__fim = fim

class Local:
    def __init__(self):
        self.__endereco = None

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco = endereco

class Ranking:
    def __init__(self):
        self.__pontos = None
        self.__equipe = []

    def getPontos(self):
        return self.__pontos

    def setPontos(self, pontos):
        self.__pontos = pontos

    def getEquipe(self):
        return self.__equipe

    def setEquipe(self, equipe):
        self.__equipe.append(equipe)

class Jogo:
    def __init__(self):
        self.__placar = None
        self.__equipe = []
        self.__local = None
        self.__horario = None
        self.__ranking = None

    def getPlacar(self):
        return self.__placar

    def setPlacar(self, placar):
        self.__placar = placar

    def getEquipe(self):
        return self.__equipe

    def setEquipe(self, equipe):
        self.__equipe.append(equipe)

    def getLocal(self):
        return self.__local

    def setLocal(self, local):
        self.__local = local

    def getHorario(self):
        return self.__horario

    def setHorario(self, horario):
        self.__horario = horario

    def getRanking(self):
        return self.__ranking

    def setRanking(self, ranking):
        self.__ranking = ranking


class Arquivos:
   def lerArquivo(self):
        with open("teste.txt ", "r") as arquivo:
            conteudo = arquivo.read()
            return conteudo
        for linha in conteudo:
            print(linha.strip())

   def escreverArquivo(self):
       with open("arquivo.txt ", "w") as arquivo:
           arquivo.write("")


# Instâncias dos objetos Treinador
treinador1 = Treinador()
treinador1.setNome("Josué")
treinador1.setIdade(25)
treinador1.setModalidade("Futebol")

treinador2 = Treinador()
treinador2.setNome("Loi")
treinador2.setIdade(32)
treinador2.setModalidade("Futebol")

# Instâncias dos objetos Jogador
jogador1 = Jogador()
jogador1.setNome("João")
jogador1.setIdade(28)
jogador1.setPosicao("Atacante")
jogador1.setCodTurma(2022)

jogador2 = Jogador()
jogador2.setNome("Anton")
jogador2.setIdade(25)
jogador2.setPosicao("Goleiro")
jogador2.setCodTurma(2022)

jogador3 = Jogador()
jogador3.setNome("Eric")
jogador3.setIdade(27)
jogador3.setPosicao("Ala")
jogador3.setCodTurma(2022)

jogador4 = Jogador()
jogador4.setNome("Davi")
jogador4.setIdade(20)
jogador4.setPosicao("Pivô")
jogador4.setCodTurma(2022)

jogador5 = Jogador()
jogador5.setNome("Miguel")
jogador5.setIdade(23)
jogador5.setPosicao("Meio-campista")
jogador5.setCodTurma(2022)

jogador6 = Jogador()
jogador6.setNome("André")
jogador6.setIdade(65)
jogador6.setPosicao("Zagueiro")
jogador6.setCodTurma(2022)

jogador7 = Jogador()
jogador7.setNome("Rodrigo")
jogador7.setIdade(28)
jogador7.setPosicao("Armador")
jogador7.setCodTurma(2023)

jogador8 = Jogador()
jogador8.setNome("Guilherme")
jogador8.setIdade(19)
jogador8.setPosicao("Ponta")
jogador8.setCodTurma(2023)

jogador9 = Jogador()
jogador9.setNome("Juliano")
jogador9.setIdade(18)
jogador9.setPosicao("Lateral")
jogador9.setCodTurma(2023)

jogador10 = Jogador()
jogador10.setNome("Eduardo")
jogador10.setIdade(21)
jogador10.setPosicao("Centroavante")
jogador10.setCodTurma(2023)

jogador11 = Jogador()
jogador11.setNome("Flinn")
jogador11.setIdade(25)
jogador11.setPosicao("Levantador")
jogador11.setCodTurma(2023)

jogador12 = Jogador()
jogador12.setNome("Pedro")
jogador12.setIdade(25)
jogador12.setPosicao("Oposto")
jogador12.setCodTurma(2023)

# Instâncias dos objetos Modalidade
modalidade1 = Modalidade()
modalidade1.setTipo("Futebol")
modalidade1.setQuantJogador(6)
modalidade1.setGenero("Masculino")

# Instâncias das Equipes
equipe1 = Equipe()
equipe1.setPeriodo("3° período")
equipe1.setCor("Preto")
equipe1.setModalidade(modalidade1.setTipo())
equipe1.setJogador([jogador1, jogador2, jogador3, jogador4, jogador5, jogador6])
equipe1.setJogador(treinador1)

equipe2 = Equipe()
equipe2.setPeriodo("1° período")
equipe2.setCor("Azul")
equipe2.setModalidade(modalidade1.setTipo())
equipe2.setJogador([jogador7, jogador8, jogador9, jogador10, jogador11, jogador12])
equipe2.setJogador(treinador2)

horario1 = Horario()
horario1.setInicio("09:00")
horario1.setFim("11:00")

local1 = Local()
local1.setEndereco("R. Projetada, 854-922 - Vila Morena")

ranking1 = Ranking()
ranking1.setPontos(10)
ranking1.setEquipe(equipe1)

jogo1 = Jogo()
jogo1.setPlacar("2-1")
jogo1.setEquipe(equipe1)
jogo1.setLocal(local1)
jogo1.setHorario(horario1)
jogo1.setRanking(ranking1)

arquivo = Arquivos()
arquivo.escreverArquivo()
arquivo.lerArquivo()
