import re

class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass

def TestandoSenha(senha): #função que testa a força da senha
    if len(re.findall(r'\d', senha)) < 2: return True #verifica se senha tem 2 numeros ou mais
    elif len(re.findall(r'[a-z]', senha)) < 2: return True #verifica se senha tem 2 letras minusculas ou mais
    elif len(re.findall(r'[A-Z]', senha)) < 1: return True #verifica se senha tem uma letra maiuscula ou mais
    elif len(re.findall(r'[!,@,#,$,&,*]', senha)) < 1: return True #verifica se a função tem pelo menos um caractere especial
    elif len(senha) < 8: return True #verifica se senha tem 8 ou mais caracteres
    else: return False

def TestandoEmail(email):
    if (re.fullmatch(r'[\w_.+-]+@\w+.[A-Za-z]+', email)) == "": return True #verifica se email está no formato desejado
    if len((re.split(r'[@.]', email))[-1]) > 4 or len((re.split(r'[@.]', email))[-1]) < 2: return True #verifica se o dominio do email tem entre 2 e 4 caracteres
    else: return False

class Repositorio:
    def __init__(self):
        self.alunos = []
    
    #Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        for incluso in self.alunos:
            if aluno.ra == incluso.ra: #Se o RA do aluno for igual ao de algum já existente, RAInvalido
                raise RAInvalido()
                return
        if TestandoSenha(aluno.senha): raise SenhaFraca
        elif TestandoEmail(aluno.email): raise EmailInvalido
        else: self.alunos.append(aluno) #Se nenhuma das excessões acima for lançada, adiciona o aluno ao repositorio

    #Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):
        for incluso in self.alunos:
            if aluno.ra == incluso.ra: #Se achar RA, altera aluno, caso nao lançar nenhuma excessao   
                if TestandoSenha(aluno.senha): raise SenhaFraca
                elif TestandoEmail(aluno.email): raise EmailInvalido
                else: incluso = aluno
                return
        raise RAInvalido #caso nao achar, RAInvaido

    #Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):
        for incluso in self.alunos:
            if incluso.ra == ra: #Procura no repositorio o RA e retorna o objeto aluno
                return incluso
        raise RAInvalido #caso nao achar, RAInvalido

    #Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):
        for incluso in self.alunos:
            if incluso.ra == ra: #procura no repositorio, se achar, remove
                self.alunos.remove(incluso)
                return
        raise RAInvalido #Se nao achar, lança excessao

    #Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        self.alunos= []
