import re

class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass

def TestandoSenha(senha):
    if len(re.findall(r'\d', senha)) < 2: return True
    elif len(re.findall(r'[a-z]', senha)) < 2: return True
    elif len(re.findall(r'[A-Z]', senha)) < 1: return True
    elif len(re.findall(r'[!,@,#,$,&,*]', senha)) < 1: return True
    elif len(senha) < 8: return True
    else: return False

def TestandoEmail(email):
    if (re.fullmatch(r'[\w_.+-]+@\w+.[A-Za-z]+', email)) == "": return True
    if len((re.split(r'[@.]', email))[-1]) > 4 or len((re.split(r'[@.]', email))[-1]) < 2: return True
    else: return False

class Repositorio:
    def __init__(self):
        self.alunos = []
    
    #Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        for incluso in self.alunos:
            if aluno.ra == incluso.ra:
                raise RAInvalido()
                return
        if TestandoSenha(aluno.senha): raise SenhaFraca
        elif TestandoEmail(aluno.email): raise EmailInvalido
        else: self.alunos.append(aluno)

    #Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):  
        for incluso in self.alunos:
            if aluno.ra == incluso.ra:        
                if TestandoSenha(aluno.senha): raise SenhaFraca
                elif TestandoEmail(aluno.email): raise EmailInvalido
                else: incluso = aluno
                return
        raise RAInvalido

    #Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):
        for incluso in self.alunos:
            if incluso.ra == ra:
                return incluso
        raise RAInvalido

    #Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):
        for incluso in self.alunos:
            if incluso.ra == ra:
                self.alunos.remove(incluso)
        raise RAInvalido

    #Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        pass #print("#",self.alunos)
