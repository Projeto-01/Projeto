# Como não sabemos como funciona o touch decidimos botar uma escolhas escritas para testar o código
import uuid
from datetime import date
from datetime import datetime
hj = date.today()
data = hj.weekday()
if data == 0:
    dia = "Segunda\n"
if data == 1:
    dia = "Terça\n"
if data == 2:
    dia = "Quarta\n"
if data == 4:
    dia = "Quinta\n"
if data == 3:
    dia = "Sexta\n"
if data == 5:
    dia = "Sabado\n"
if data == 6:
    dia = "Domingo\n"
professores = open("professores.txt", "r", encoding="utf8")
posicoes = professores.readlines()
professores.close()
alunos = open("alunos.txt", "r", encoding="utf8")
posicoes_a = alunos.readlines()
alunos.close()
codigos = open("codigo.txt", "r", encoding="utf8")
posicoes_c = codigos.readlines()
codigos.close()
alunos_a = open("alu.txt", "r", encoding="utf8")
posicoes_al = alunos_a.readlines()
alunos_a.close()
opcao_0 = ""
notificacao = 0
notificacao_prof = 0
notificacao_alu = 0
codigo_0 = 0
presenca = 0
b = 0
d = 0
a = 0
c = 0
n = 0
f = 0
y = 0
g = 0
h = 0
k = 0
m = 0
l = 0
w = 0
x = 0
s = 0
r = 0
mb = 0
po = 0
cm = 0
nm = 0
presentes = 0
codigo_aleatorio = ""
pessoa = ""
mensagem_prof = ""
chamadas = 0
mensagem_alu = ""
mensagens_re = ""
horario_p = []
horario_p_em_and = []
codigos_e_turmas_l = []
e = []
alunos_presentes = []
alunos_presenca = []
alunos = []
novo_horario = []
alunos = []
lista_turmas = []
aluno_presenca = []
print("LOGIN")
email = input("Digite seu e-mail: \n")  # E-mail que a cesar disponibilizará para os alunos e professores
senha = input("Digite a sua senha: \n")  # A senha é o CPF do aluno e do professor
email_verificacao = email + "\n"
senha_verificacao = senha + "\n"
if email_verificacao in posicoes:
    for i in posicoes:
        if c == 2:
            if senha_verificacao == i:
                pessoa = "Professor Verificado"
            c += 1
        if c == 1:
            c += 1
            nome = i
        if email_verificacao == i:
            c += 1
if pessoa == "Professor Verificado":
    while b == 0:
        for i in posicoes:
            if i == nome:
                f += 1
            elif f == 1:
                if 1 <= d < 11:
                    horario_p.append(i)
                    d += 1
                elif i == dia:
                    d += 1
        posicoes_c_2 = []
        codigos_e_turmas_l = []
        codigos_2 = open("codigo.txt", "r", encoding="utf8")
        posicoes_c_2 = codigos_2.readlines()
        codigos_2.close()
        for i in posicoes_c_2:
            codigos_e_turmas_l.append(i)
        for i in horario_p:
            if i == "\n":
                continue
            elif i in codigos_e_turmas_l:
                horario_p_em_and.append(i)
        for i in horario_p:
            if i in horario_p_em_and:
                horario_p.remove(i)
        for i in horario_p:
            if i in horario_p_em_and:
                horario_p.remove(i)
        for i in horario_p:
            if i in horario_p_em_and:
                horario_p.remove(i)
        for i in horario_p_em_and:
            if i in codigos_e_turmas_l:
                continue
            else:
                horario_p_em_and.remove(i)
                horario_p.append(i)
        for i in horario_p_em_and:
            if i in codigos_e_turmas_l:
                continue
            else:
                horario_p_em_and.remove(i)
                horario_p.append(i)
        for i in horario_p_em_and:
            if i in codigos_e_turmas_l:
                continue
            else:
                horario_p_em_and.remove(i)
                horario_p.append(i)
        presencas = open("presenca.txt", "r", encoding="utf8")
        posicoes_pr = presencas.readlines()
        presencas.close()
        nome_p = nome.rstrip()
        print("\n\nOlá,", nome_p, "!\n\n")
        print("Chamadas em andamento:\n")
        for i in horario_p_em_and:
            print(i)
        print("Para hoje:\n")
        for i in horario_p:
            print(i)
        print("HISTÓRICO   AVISOS   HOME   MENSAGENS   PERFIL")
        opcao = input("")
        opcao_1 = opcao.title()
        opcao_01 = opcao_1.rstrip()
        opcao_02 = opcao_1 + "\n"
        opcao_00010 = opcao.upper()
        a = 0
        for i in horario_p:
            novo_hora = i.rstrip()
            novo_horario.append(novo_hora)

        if opcao_02 in horario_p_em_and:
            presenca = open("presenca.txt", "r", encoding="utf8")
            posicoes_q = presenca.readlines()
            presenca.close()
            for i in posicoes_q:
                if opcao_02 == i:
                    cm = 1
                elif i in posicoes:
                    cm = 0
                elif cm == 1:
                    print(i)
            opcao_007 = input("Escreva o nome do aluno que você quer retirar, ou escreva o nome do aluno que você "
                              "deseja adicionar na lista, ou escreva sim ou não para finalizar a chamada:")
            opcao_020 = opcao_007 + "\n"
            opcao_0070 = opcao_007.upper()
            opcao_00070 = opcao_007.title()
            opcao_0170 = opcao_00070 + "\n"
            if opcao_0070 == "HOME":
                continue
            elif opcao_0170 in posicoes_q:
                posicoes_q.remove(opcao_0170)
                manipulador = open("presenca.txt", "w", encoding="utf8")
                for i in posicoes_q:
                    manipulador.writelines(i)
                manipulador.close()
            elif opcao_0070 == "NÃO":
                continue
            elif opcao_0070 == "SIM":
                email_profe = email + "\n"
                turma = opcao_01 + "\n"
                for i in posicoes_q:
                    if i == turma:
                        r = 1
                    elif i in posicoes:
                        r = 0
                    elif r == 1:
                        alunos.append(i)
                historico = open("histórico.txt", "r", encoding="utf8")
                pos_h = historico.readlines()
                historico.close()
                pos_h.append(email_profe)
                now = datetime.now()
                hora = now.hour
                minuto = now.minute
                dia_c = now.day
                mes = now.month
                ano = now.year
                dt = str(dia_c) + "/" + str(mes) + "/" + str(ano) + " - "
                horario_a = dt + str(hora) + ":" + str(minuto) + "\n"
                pos_h.append(horario_a)
                pos_h.append(turma)
                for i in alunos:
                    pos_h.append(i)
                historico = open("histórico.txt", "w", encoding="utf8")
                for i in pos_h:
                    historico.writelines(i)
                historico.close()
                cod = open("codigo.txt", "w", encoding="utf8")
                cod.writelines("")
                cod.close()
                pre = open("presenca.txt", "w", encoding="utf8")
                for i in posicoes_q:
                    if i in alunos:
                        posicoes_q.remove(i)
                for i in posicoes_q:
                    if i in alunos:
                        posicoes_q.remove(i)
                for i in posicoes_q:
                    pre.writelines(i)
                pre.close()
            else:
                manipulador = open("presenca.txt", "w", encoding="utf8")
                for i in posicoes_q:
                    if i == opcao_02:
                        po = 1
                    elif po == 1:
                        pos = posicoes_q.index(i)
                        opcao_008 = opcao_00070.title()
                        opcao_08 = opcao_008 + "\n"
                        posicoes_q.insert(pos, opcao_08)
                        po = 0
                for i in posicoes_q:
                    manipulador.writelines(i)
                manipulador.close()
        elif opcao_01 in novo_horario:
            print("Você tem certeza de que quer fazer a chamada dessa turma?")
            opcao = input("")
            opcao_02 = opcao.upper()
            if opcao_02 == "HOME":
                continue
            horario = input("Qual o horário a chamada será automaticamente encerrada:")


            def my_random_string(string_length=10):
                random = str(uuid.uuid4())
                random = random.upper()
                random = random.replace("-", "")
                return random[0:string_length]


            codigo_aleatorio = my_random_string(6)
            opcao_0109 = opcao_01 + "\n"
            for i in horario_p:
                if opcao_0109 == i:
                    nm += 1
                elif nm == 1:
                    hr = i
                    nm = 0
            texto = opcao_0109 + hr + codigo_aleatorio + "\n" + horario + "\n"
            cod = open("codigo.txt", "a", encoding="utf8")
            cod.write(texto)
            cod.close()
            print("Seu código é:", codigo_aleatorio)
            # Como não sabiamos como colocar geolocalização, decidimos fazer apenas o código por enquanto
        elif opcao_00010 == "HISTÓRICO":
            historico = open("histórico.txt", "r", encoding="utf8")
            posicoes_h = historico.readlines()
            historico.close()
            email_e = email + "\n"
            for i in posicoes_h:
                if email_e == i:
                    mb = 1
                elif mb == 1:
                    hr_c = i
                    mb = 2
                elif mb == 2 and i in posicoes:
                    mb = 2
                    lista_turmas.append(i)
                    lista_turmas.append(hr_c)
                elif i in posicoes:
                    mb = 0
                elif mb == 2:
                    lista_turmas.append(i)
            for i in lista_turmas:
                print(i)
        elif opcao_00010 == "AVISOS":
            avisos = open("avisos.txt", "r", encoding="utf8")
            avisos_l = avisos.readlines()
            avisos.close()
            for i in avisos_l:
                print(i)
        elif opcao_00010 == "MENSAGENS":
            escolha = input("Você quer ver as mensagens recebidas(ver) ou mandar mensagem(mandar):")
            escolha_m = escolha.upper()
            if escolha_m == "VER":
                mens = open("mensagens.txt", "r", encoding="utf8")
                posicoes_m = mens.readlines()
                mens.close()
                email_e = email + "\n"
                for i in posicoes_m:
                    if i == email_e:
                        v = 1
                    elif v == 1:
                        email_aluno = i
                        email_aluno_e = email_aluno + "\n"
                        v = 2
                    elif v == 2:
                        mensagem_re = i
                        print(email_aluno_e)
                        print(mensagem_re)
                        v = 0
            if escolha_m == "MANDAR":
                mensagens = open("mensagens.txt", "a", encoding="utf8")
                escolha_de_a = input("Digite o email do aluno que você deseja manda a mensagem:")
                escolha_de_a_e = escolha_de_a + "\n"
                for i in posicoes_a:
                    if i == escolha_de_a_e:
                        while s == 0:
                            mensagem = input("Escreva a mensagem que você deseja enviar:")
                            email_e = email + "\n"
                            mensagem_e = mensagem + "\n"
                            mensagens.writelines(escolha_de_a_e)
                            mensagens.writelines(email_e)
                            mensagens.writelines(mensagem_e)
                            escolha_de_saida = input(
                                "Você deseja mandar outra mensagem para esse mesmo aluno(sim ou não)?")
                            escolha_de_saida_m = escolha_de_saida.upper()
                            if escolha_de_saida_m == "SIM":
                                s = 0
                            elif escolha_de_saida_m == "NÃO":
                                s = 1
                mensagens.close()
        elif opcao_00010 == "PERFIL":
            for i in posicoes:
                email_e = email + "\n"
                if email_e == i:
                    email_p = i
                    w += 1
                elif w == 1:
                    print(i)
                    print(email_p)
                    w += 1

opcao_0 = ""
notificacao = 0
notificacao_prof = 0
notificacao_alu = 0
codigo_0 = 0
presenca = 0
b = 0
d = 0
a = 0
c = 0
n = 0
f = 0
y = 0
g = 0
h = 0
k = 0
m = 0
l = 0
w = 0
x = 0
v = 0
s = 0
p = 0
u = 0
nome_prof = ""
presentes = 0
codigo_aleatorio = ""
pessoa = ""
mensagem_prof = ""
chamadas = 0
mensagem_alu = ""
horario_a = []
horario_a_em_and = []
mensagens = []
codigos_e_turmas_l = []
e = []
notas_l = []
alunos_presentes = []
alunos_presenca = []
novo_horario = []
alunos = []
aluno_presenca = []
email_verificacao = email + "\n"
senha_verificacao = senha + "\n"
if email_verificacao in posicoes_a:
    for i in posicoes_a:
        if c == 2:
            if senha_verificacao == i:
                pessoa = "Aluno Verificado"
            c += 1
        if c == 1:
            c += 1
            nome = i
        if email_verificacao == i:
            c += 1
if pessoa == "Aluno Verificado":
    while b == 0:
        for i in posicoes_a:
            if i == nome:
                f += 1
            if f == 1:
                if 1 <= d < 11:
                    horario_a.append(i)
                    d += 1
                if i == dia:
                    d += 1
        posicoes_c_2 = []
        codigos_2 = open("codigo.txt", "r", encoding="utf8")
        posicoes_c_2 = codigos_2.readlines()
        codigos_2.close()
        for i in posicoes_c_2:
            codigos_e_turmas_l.append(i)
        for i in horario_a:
            if i in codigos_e_turmas_l:
                horario_a_em_and.append(i)
                horario_a.remove(i)
        for i in horario_a:
            if i in codigos_e_turmas_l:
                horario_a_em_and.append(i)
                horario_a.remove(i)
        for i in horario_a:
            if i in codigos_e_turmas_l:
                horario_a_em_and.append(i)
                horario_a.remove(i)
        for i in horario_a:
            if i in codigos_e_turmas_l:
                horario_a_em_and.append(i)
                horario_a.remove(i)
        nome_a = nome.rstrip()
        print("\n\nOlá,", nome_a, "!\n\n")
        print("Aula em andamento:\n")
        for i in horario_a_em_and:
            print(i)
        print("Aulas de hoje:\n")
        for i in horario_a:
            print(i)
        print("AVISOS   NOTAS   HOME   MENSAGENS   PERFIL")
        opcao = input("")
        opcao_1 = opcao.title()
        opcao_h = opcao_1 + "\n"
        opcao_01 = opcao_1.rstrip()
        opcao_0100 = opcao.upper()
        a = 0
        if opcao_h in horario_a_em_and:
            codigo = input("Insira o código fornecido pelo seu professor:")
            for i in posicoes_c:
                if opcao_h == i:
                    p = 1
                elif p == 1:
                    p = 2
                elif p == 2:
                    codigo_c = i
                    codigo_c_e = codigo_c.rstrip()
                    p = 0
            if codigo == codigo_c_e:
                print("OK! Sua presença foi marcada, boa aula!")
                presenca_r = open("presenca.txt", "r", encoding="utf8")
                posicoes_n = presenca_r.readlines()
                presenca_r.close()
                nome_pre = nome_a + "\n"
                print(opcao_h)
                print(posicoes_n)
                for i in posicoes_n:
                    if opcao_h == i and u == 0:
                        u = 1
                    elif u == 1:
                        posicao_p = posicoes_n.index(i)
                        u = 2
                        posicoes_n.insert(posicao_p, nome_pre)
                presenca = open("presenca.txt", "w", encoding="utf8")
                for i in posicoes_n:
                    presenca.writelines(i)
                presenca.close()
        elif opcao_h in horario_a:
            print("Essa turma ainda não esta disponivel para marcar presença, tente novamente mais tarde")
        if opcao_0100 == "AVISOS":
            avisos = open("avisos.txt", "r", encoding="utf8")
            avisos_l = avisos.readlines()
            avisos.close()
            for i in avisos_l:
                print(i)
        elif opcao_0100 == "NOTAS":
            notas = open("notas.txt", "r", encoding="utf8")
            posicoes_n = notas.readlines()
            notas.close()
            for i in posicoes_n:
                notas_sem = i.rstrip()
                notas_l.append(notas_sem)
            for i in notas_l:
                if email == i:
                    q = 1
                elif i in posicoes_al:
                    q = 0
                elif q == 1:
                    print(i)
                    q = 2
                elif q == 2:
                    novo_i = i.replace("-", " ")
                    novo_i_ = novo_i.split()
                    nota1 = novo_i_[0]
                    nota2 = novo_i_[1]
                    nota3 = novo_i_[2]
                    media = (float(nota1) + float(nota2) + float(nota3)) / 3
                    media_a = str(media) + "\n"
                    print(media_a)
                    q = 1
        elif opcao_0100 == "MENSAGENS":
            escolha = input("Você quer ver as mensagens recebidas(ver) ou mandar mensagem(mandar):")
            escolha_m = escolha.upper()
            if escolha_m == "VER":
                mens = open("mensagens.txt", "r", encoding="utf8")
                posicoes_m = mens.readlines()
                mens.close()
                email_e = email + "\n"
                for i in posicoes_m:
                    if i == email_e:
                        v = 1
                    elif v == 1:
                        email_pro = i
                        email_pro_e = email_pro + "\n"
                        v = 2
                        for g in posicoes:
                            if g == email_pro_e:
                                x = 1
                            elif x == 1:
                                nome_prof = i
                                x = 0
                    elif v == 2:
                        mensagem_re = i
                        print(nome_prof)
                        print(mensagem_re)
                        v = 0
            if escolha_m == "MANDAR":
                mensagens = open("mensagens.txt", "a", encoding="utf8")
                escolha_de_p = input("Digite o email do professor que você deseja mandar a mensagem: ")
                escolha_de_p_e = escolha_de_p + "\n"
                for i in posicoes:
                    if i == escolha_de_p_e:
                        while s == 0:
                            mensagem = input("Escreva a mensagem que você deseja enviar:")
                            escolha_de_p_e = escolha_de_p + "\n"
                            email_e = email + "\n"
                            mensagem_e = mensagem + "\n"
                            mensagens.writelines(escolha_de_p_e)
                            mensagens.writelines(email_e)
                            mensagens.writelines(mensagem_e)
                            escolha_de_saida = input(
                                "Você deseja mandar outra mensagem para esse mesmo professor(sim ou não)")
                            escolha_de_saida_m = escolha_de_saida.upper()
                            if escolha_de_saida_m == "SIM":
                                s = 0
                            elif escolha_de_saida_m == "NÃO":
                                s = 1
                mensagens.close()
        elif opcao_0100 == "PERFIL":
            email_e = email + "\n"
            for i in posicoes_a:
                if email_e == i:
                    email_a = i
                    w += 1
                elif w == 1:
                    print(i)
                    print(email_a)
                    w += 1
