from flask import Flask, jsonify, render_template, url_for , request, flash, session, redirect, url_for
import urllib.request
import json
import re #Este módulo fornece operações para correspondência de expressões regulares semelhantes às encontradas em Perl
# from bancodedados import cadastro_usuario
from config import mysql, init_app
import mysql.connector
from datetime import datetime, date

from config import DATABASE


import smtplib
import email.message


bd = mysql.connector.connect(
    host=DATABASE['host'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    database=DATABASE['db']
)
print('HAHAHAHAHA')
print(bd)
app = Flask(__name__)#AQUI DEFINE NORMALMENTE
app.secret_key = 'asfdwqewrawrEFF23eea'
init_app(app)

app.config['SECRET_KEY'] = "random string" #NECESSARIO PRO FLASH FUNCIONAR ("alerta de mensagens")

#SUPORTE EMAIL DA TELA INICIAL---------------------

#------------------------------------------------------
# CADASTRO DE PESSOAS----------------------------------


@app.route('/cadastraradm')
def adicionaradm():
    if session.get('logged') == True and session.get('nivel')==1:
        session['rota_anterior'] = request.path
        return render_template("cadastroAdministrador.html")
    else:
        return render_template('login.html')

    


# NAVEGA ATÉ A TELA ADICIONAR
@app.route('/cadastrarUsu')
def adicionar():
    if session.get('logged') == True:
        session['rota_anterior'] = request.path
        return render_template('cadastroUsuario.html')
    else:
        return render_template('login.html')
    
    
# LOGIN-------------------------------------------------------

@app.route('/perifl')
def perfil(): # verifica se o usuário já está logado na sessão, comparando o valor armazenado na variável de sessão 'logged' com True.
    if session.get('logged') == True:
        #TESTANDO COM BASE.HTML
        return render_template('perfil.html', nivel=session['nivel'])
    else: 
        return render_template('login.html')
@app.route('/login')
def login(): # verifica se o usuário já está logado na sessão, comparando o valor armazenado na variável de sessão 'logged' com True.
    if session.get('logged') == True:
        #TESTANDO COM BASE.HTML
        return render_template('base.html', nivel=session['nivel'])
    else: 
        return render_template('login.html')

@app.route('/logar', methods=['POST'])
def logar():
    print('AQUI 00')
    if session.get('logged') == True:
        print('AQUI 01')
        return render_template('inicio.html')
    else:
        email = request.form['email']
        senha = request.form['password']

        conn = bd
        conn.reconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        

        usuario = cursor.fetchall()
        print(usuario)
        if usuario:
            if senha == usuario[0][4] and email == usuario[0][1]:
                session['logged'] = True
                session['username'] = usuario[0][0]
                session['email'] = usuario[0][1]
                session['nivel'] = usuario[0][5]
                session['ocupacao'] = usuario[0][2]
                session['instituicao'] = usuario[0][3]
                session['pass'] = usuario[0][4]
                
                print('AQUI 1')
                # VOU PASSAR NO NIVEL DO USUARIO PARA HOME(BASE.HTML)
                return render_template('inicio.html', nivel=session['nivel'])
            else:
                flash('Usuário ou senha incorreto!')
                print('AQUI 2')
                return render_template('login.html')
        else:
            print('AQUI 3')
            flash('Usuário ou senha incorreto!')
            return render_template('login.html')


@app.route('/logout') #Essa rota remove as informações da sessão do usuário e redireciona-o para a página de login.
def logout():
    session.pop('logged', False)
    session.pop('username', None)
    session.pop('email', None)
    session.pop('nivel', None)
    session.pop('ocupacao', None)
    session.pop('instituicao', None)
    session.pop('pass', None)
    return render_template('login.html')

# CADASTRAR USU E ADM----------------------
@app.route('/adicionar', methods=['POST'])
def cadastrarUsu():
    if session.get('logged') == True:
        nome = request.form['nome']
        email = request.form['email']
        ocupacao = request.form['ocupacao']
        instituicao = request.form['instituicao']
        senha = request.form['senha']
        senha2 = request.form['senha2']
        page_name = ''
        print("if adicionar acaba page_name")
    
        if senha != senha2:
            flash('As senhas não estão iguais. Tente novamente.') 
            print("quando as senhas não são iguais retorna para a mesma url")
            #recupera a rota anterior
            #rota_anterior = session.get('rota_anterior')
            previous_url = request.referrer
            return redirect(previous_url)
        else:
            
            if 'tipo_usuario' in request.form and request.form['tipo_usuario'] and session['nivel']==1:
                tipoUsuario = request.form['tipo_usuario']
                query = 'insert into usuarios(nome, email, ocupacao, instituicao, senha, tipo_usuario) values (%s, %s, %s, %s, %s, %s)'
                fieldsValue = (nome, email, ocupacao,
                           instituicao, senha, tipoUsuario)
                page_name = 'cadastroAdministrador.html'
                print("primeiro if rota adicionar deu certo usuárioo adm ")
            else:
                query = 'insert into usuarios(nome, email, ocupacao, instituicao, senha) values (%s, %s, %s, %s, %s)'
                fieldsValue = (nome, email, ocupacao, instituicao, senha)
                page_name = 'cadastroUsuario.html'
                print("primeiro if rota adicionar deu certo usuárioo normal ")

            if bd.is_connected():
                comando = query
                cursor = bd.cursor()
                valores = fieldsValue
                cursor.execute(comando, valores)
                bd.commit()

                flash("CADASTO FEITO COM SUCESSO")
                print("PRIMEIRO FLASH")
                return render_template('opcoes.html')
                # print("conecta o bd e dá um comit ")
                
    else:
        return render_template('login.html')
    
    # ERRADO TEM QUE ESTAR NO IF DE CIMA render_template('opcoes.html')
    
    
    
#CADASTRAR SALA-------------------------------------------------------------------------

# @app.route('/cadastrarsala', methods=['POST'])
# def cadastrarSala():     
#             #aqui começa o paranaue
#             if session.get('logged') == True:
#                 if session.get('nivel')==1: #não sei se vai precisar ser adm, se não for depois você tira este if
#                     #vai precisar sim, só pode adicionar o adm
#                     conn = bd
#                     conn.reconnect()
#                     cursor = conn.cursor()
#                     cursor.execute("SELECT * FROM sala")
                

#                     salas = cursor.fetchall()
#                     print("SALAS AQUI")    
#                     print(salas)    
                    
#                     return render_template('cadastrarSala.html', mensagem="", salas=salas, nivel= session.get('nivel'))  
            
#                 else:           
#                     return render_template('base.html')
#             else:
#                 return render_template('login.html')
    

#ROTAS --------------------- #ROTAS----------------------- #ROTAS


@app.route('/') 
def bases():
    if session.get('logged') == True:
        return render_template("inicio.html", nivel=session['nivel'])
    else:
        return render_template('login.html')

#ESQUECEU A SENHA ------------------------------------------------------------------
@app.route('/Esqueceuasenha')
def esqueceuasenhas():
    return render_template("esqueceusenha.html")


# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USERNAME'] = 'seu-email@gmail.com'
# app.config['MAIL_PASSWORD'] = 'sua-senha'

# mail = Mail(app)

# @app.route('/esqueceu-a-senha', methods=['GET', 'POST'])
# def esqueceu_a_senha():
  #   if request.method == 'POST':
   #      email = request.form['email']
   #      # Verificar se o email existe no banco de dados e obter o usuário correspondente
   #      user = User.query.filter_by(email=email).first()
   #      if user:
    #         # Gerar um token de redefinição de senha com uma validade de 1 hora
    #         token = user.generate_reset_token()
    #        # Enviar um email de redefinição de senha com o link para a página de redefinição de senha
     #        msg = Message('Redefinição de senha', sender='seu-email@gmail.com', recipients=[email])
    #         msg.body = f"Para redefinir a sua senha, acesse o seguinte link: {url_for('reset_senha', token=token, _external=True)}"
    #         mail.send(msg)
    #         flash('Um email de redefinição de senha foi enviado para o seu endereço de email.')
    #     else:
    #         flash('O email fornecido não está cadastrado no nosso sistema.')
    #     return redirect(url_for('login'))
   #  return render_template('esqueceu_a_senha.html')
#-------------------------------------------------------------------------------------
@app.route('/home') #AO CLICAR NA BASE
def inicios():
    if session.get('logged') == True:
        return render_template("inicio.html",nivel=session['nivel'])
    else:
        return render_template('login.html')
    
@app.route('/opcao')
def opcao():
    if( session.get('nivel')==1):
        return render_template("opcoes.html", nivel=session['nivel'])
    else:
        return render_template("base.html", nivel=session['nivel'])
    
@app.route('/saida')
def saindo():
    return render_template("login.html")

@app.route('/contatosuporte')
def obrigada():
    if session.get('logged') == True:
        return render_template("obrigada.html")
    else:
        return render_template('login.html')
    


@app.route('/SalasOcupadas')
def ocupadas():
    if session.get('logged') == True:
        return render_template("salas_ocup.html", nivel=session['nivel'])
    else:
        return render_template('login.html')

@app.route('/HistoricoSalas')
def historicos():
    if session.get('logged') == True:
        return listarHistoricoSalas()
    #TEM QUE CHAMAR A FUNÇÃO QUE LISTA, PARA ASSIM QUE CARREGAR A PÁGINA A LISTA SER CARREGADAN
    else:
        return render_template('login.html')

        
@app.route('/recuperarsenha')
def recuperar():
    if session.get('logged') == True:
        return render_template("esqueceusenha.html", nivel=session['nivel'])
    else:
        return render_template('login.html')
    

@app.route('/Chamados')
def Chamados():
    if session.get('logged') == True:
        return render_template("chamados.html", nivel=session['nivel'])
    else:
        return render_template('login.html')
   
   
#Manutenção em TI-------------------------------------------------     
@app.route('/ManutençãoTi')
def ti():
    if session.get('logged') == True:
        conn = bd
        conn.reconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sala")
        

        salasdbRetorno = cursor.fetchall() 
        #return salasdbRetorno
        print("MANUTENÇÃOOOOOO")
        return render_template("pedir_ti.html", nivel=session['nivel'], salas = salasdbRetorno)
    else:
        return render_template('login.html')
    

@app.route('/relatarProblema', methods=['POST'])
def relatarProblema():
    if session.get('logged') == True:
        area = "Técnico TI"
        situacao = request.form['status-situacao']
        sub_man = request.form['tipo-chamado']
        pergunta1 = request.form['no-net']
        pergunta2 = request.form['problem-soft']
        pergunta3 = request.form['about-problem']
        pergunta4 = request.form['occurrence']
        pergunta5 = request.form['recurrence']
        pergunta6 = request.form['remove']
        data = request.form['data-solicitacao']
        objeto = request.form['objeto']
        sala = request.form['salas']
        bloco = request.form['bloco']
        dataenvio = date.today().strftime("%d/%m/%Y")
        horaenvio = datetime.now().strftime("%H:%M:%S")
        emailUser = session.get('email')
        descProblema = request.form['desc-problem']
        
        query = 'insert into chamados(area, situacao, sub_ou_man, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, data_form, objeto_afetado, nome_numerosala, bloco, data_envio, hora_envio, fk_Usuario_email, descricao) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        fieldsValue = (area, situacao, sub_man, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, data, objeto, sala, bloco, dataenvio, horaenvio, emailUser, descProblema)

        if bd.is_connected():
            comando = query
            cursor = bd.cursor()
            valores = fieldsValue
            cursor.execute(comando, valores)
            bd.commit()
            
        return render_template("chamados.html", nivel=session['nivel'], mensagem="Chamado aberto com sucesso!")

   
# @app.route('pedirTi', methods=['POST'])
# def pedindoTi():
#     if session.get('logged') == True:
#         blocos = request.form['blocos']
#         salas = request.form['salas']
        
    
#-----------------------------------------------------------------    

@app.route('/ManutençãoPredial')
def predial():
    if session.get('logged') == True:
        return render_template("pedir_predial.html", nivel=session['nivel'])
    else:
        return render_template('login.html')
   

@app.route('/ManutençãoMecanica')
def mecanica():
    if session.get('logged') == True:
        return render_template("pedir_mecanica.html", nivel=session['nivel'])
    else:
        return render_template('login.html')
    
@app.route('/Limpeza')
def limpeza():
    if session.get('logged') == True:
        return render_template("pedir_limpeza.html", nivel=session['nivel'])
    else:
        return render_template('login.html')

@app.route('/ManutencaoEletrotecnica')
def eletrotecnico():
    if session.get('logged') == True:
        return render_template("pedir_manutencao.html", nivel=session['nivel'])
    else:
        return render_template('login.html')
    

@app.route('/VerAndamento')
def verAndamento():
    if session.get('logged') == True:
        return render_template("VerAndamento.html", nivel=session['nivel'])
    else:
        return render_template('login.html')

@app.route('/HistoricoManutencoes')
def histoManuts():
    if session.get('logged') == True:
        return listarChamados()
    else:
        return render_template('login.html')

@app.route('/eventos')
def eventos():
    if session.get('logged') == True:
        return render_template("eventos.html", nivel=session['nivel'])
    else:
        return render_template('login.html')

    

@app.route('/Notificacoes')
def notificacoes():
    if session.get('logged') == True:
        notificar()
        return notificar()
    else:
        return render_template('login.html')
  

@app.route('/editarReserva')
def editarReserva():
    if session.get('logged') == True:
        return render_template("editar_reserva.html", nivel=session['nivel'], salas ="")
    else:
        return render_template('login.html')
   

@app.route('/editarManutencao')
def editar():
    if session.get('logged') == True:
        return render_template("editar_manu.html", nivel=session['nivel'])
    else:
        return render_template('login.html')
   
@app.route('/ReservarSala')
def reservando():
    return render_template("Reservar_sala.html")   
   
#-------------------------------------------------------------------------- 
#ESTA ROTA + DEF É RESPONSAVEL POR ABRIR A TELA DE CADASTRO QUANDO CLICAR NO MENU CADASTRAR SALA
#DENTRO DELA EU CHAMO LISTASALAS PARA QUE AO MESMO TEMPO QUE CHAMO A TELA CADASTRARSALA O PY RETORNAR COM AS SALAS ATUALIZADAS NA TELA



@app.route('/CadastrarSala')
def cadastros():
    #SE O USUARIO FOR NIVEL 1(ADM)
    #DEPOS VIM PRA CÁ, PARA QUE TODA VEZ QUE CLICAR NO MENU CADASTRAR SALAS ELE CHAMAR A FUNÇÃO LISTARSALAS, E TRAZER A PÁGINA COM TODAS AS SALAS CADASTRADAS
    #DUVIDA NESTA PARTE?
    #a VONTEDE PRA PERGUNTAR
    #OK, PODE PROSSEGUIR
    if( session.get('nivel')==1):
        #listarSalas()
        #ELE CONSEGUIRAR ACESSAR A ROTA CADASTRARSALA PELA URL
        return listarSalas("")
    else:

        return render_template("base.html", nivel=session['nivel'])
    
    

    
@app.route('/cadastrasala', methods=['POST'])
def cadastrasala():
    if session.get('logged') == True:
        blocos = request.form['blocos']
        capacidade = request.form['capacidade']
        #numerodasala = request.form['numerodasala']
        nomeNumeroSala = request.form['nomeNumeroSala']
        finalidade = request.form['finalidade']
        recurso = request.form['inputListaTarefas']
        
        if session['nivel']==1:
            query = 'insert into sala(bloco, nome_ou_numerosala, capacidade, recursos, finalidade) values (%s, %s, %s, %s, %s)'
            fieldsValue = (blocos,nomeNumeroSala, capacidade, recurso, finalidade)

            if bd.is_connected():
                    comando = query
                    cursor = bd.cursor()
                    valores = fieldsValue
                    cursor.execute(comando, valores)
                    bd.commit()
            #TEM QUE AJUSTAR ESTA MENSAGEM DE SUCESSO
            return listarSalas("Cadastrada com sucesso")
        else:           
            return render_template('base.html')
    else:
        return render_template('login.html')
   
#VOU CRIAR UMA DEF SEPARADO PRA FAZER O SELECT DAS SALAS, PORQUE VOU PRECISAR DELA SEMPRE QUE UMA NOVA SALA FOR INSERIDA TBM

#CRIEI ESTA DEF LISTARSALAS PRA FAZER UM SELECT E TRAZER TODAS AS SALAS PRA GENTE
#ATE AQUI SEM NOVIDADES, CERTO??, PRA MIM É TUDO NOVIDADE, CORRETO, PODE PROSSEGUIR KKKK
#FALO NESTA PARTE ABAIXO. FOI A MESMA COISA QUE FIZEMOS COM LOGIN, A DIFERENÇA É QUE O SELECT NÃO TEM WHERE, ENNTENDI SIM

#POR ULTIMO ESTA, ELA VAI NO BANCO E TRAS TODAS AS SALAS CADASTRADAS E PASSA A VARIAVEL DESTE RETORNO PARA O HTML EXIBIR USANDO O "FOR"
#eu coloquei este parametro mensagem, para que quando cadastrarmos uma sala nova, ela já apareça na tela de salas, testar na pratica agora!
def listarSalas(mensagem):
    if session.get('logged') == True:
        if session.get('nivel')==1: #não sei se vai precisar ser adm, se não for depois você tira este if
            #vai precisar sim, só pode adicionar o adm
            conn = bd
            conn.reconnect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sala")
        

            salasdbRetorno = cursor.fetchall() #ESTA LINHA SIMPLESMENTE PEGA O RETORNO DO BANCO E JOGA NESTA VARIAVEL SALAS, NO RENDER_TEMPLATE QUE EU PASSO SALAS PARA O HTML
            #print("SALAS AQUI")    
            #print(salas)    
            # NOTA QUE ESTOU PASSANDO UMA VARIAVEL "salasdbRetorno" PARA A PAGINA CADASTRARSALAS SÓ TO BUGADA NUMA PARTE O CADASTRAR, CALMA LA, KKK TO LERDA PRA APRENDER HJ KK
            #voce fez aquela dunção de cadastrar sala, e o banco recebe essas informações apartir dessa fun, essa da lista trás pra gente meio que "ao vivo" kkkk
            #organizar aqui pera ai
            return render_template('cadastrarSala.html', mensagem="", salas=salasdbRetorno, nivel= session['nivel'])  
    else: 
        return render_template('login.html')
    
    
#-----------------------VERFICAR RESERVA DE SALA-----------------------


@app.route('/reserva')
def reservas():
    if session.get('logged') == True:
        return render_template("reserva.html")
    else:
        return render_template('login.html')



# @app.route('/VerificarRserva', methods=['POST'])
# def verificarReserva(id_reserva, data_reserva, horario_inicio, horario_fim):
   
#  # Conexão com o banco de dados
#     conn = bd
#     conn.reconnect()
#     cursor = conn.cursor()
#     total_reservas=""
#     # Consulta SQL para verificar se já existe uma reserva para a sala na data e intervalo de horário desejados
#     consulta = """
#         SELECT COUNT(*) as total_reservas
#         FROM reserva
#         WHERE fk_Sala_id_sala = %s
#         AND data_reserva = %s
#         AND (
#             (horario_inicio >= %s AND horario_inicio < %s) OR
#             (horario_fim > %s AND horario_fim <= %s) OR
#             (horario_inicio < %s AND horario_fim > %s)
#         );
#     """
#     parametros = (id_reserva, data_reserva, horario_inicio, horario_fim)
#     cursor.execute(consulta, parametros)
#     resultado = cursor.fetchone() #recupera a próxima linha de um conjunto de resultados de consulta e retorna uma única sequência ou None se não houver mais linhas disponíveis.
#     if resultado is not None:
#         total_reservas = resultado['total_reservas']
#     else:
#         total_reservas = 0

#     # Encerrando a conexão com o banco de dados
#     cursor.close()

#     # Verificando se já existe uma reserva para a sala na data e intervalo de horário desejados
#     if total_reservas == 0:
#         return True
#     else:
#         return False
    
#-------------------------------------------------------------------------------------------------------------------------------  


@app.route('/filtrarSalas', methods=['POST'])
def filtrarSalas():

    bloco =  request.form['bloco']
    #turno =  request.form['turno']
    data_reserva =  request.form['data_desejada']
    horario_inicio =  request.form['hora_i']
    horario_fim =  request.form['hora_f']
    recursos_str =  request.form['recursos_selecionados']
    capacidade = int(request.form["capacidade"])

    # bloco =  'c'
    # data_reserva =  '2023-04-15'
    # horario_inicio = '18:00:00'
    # horario_fim = '22:00:00'
    # recursos_str =  "Quadro Branco;Projetor"
    # capacidade = 1

    recursos = recursos_str.split(';')
    condicao_recursos = " OR ".join([f"s.recursos LIKE '%{r}%'" for r in recursos])


    conn = bd
    conn.reconnect()
    cursor = conn.cursor()

    consulta = f"""
        SELECT s.*
        FROM sala s
        WHERE s.bloco = %s
            AND s.capacidade >= %s
            AND NOT EXISTS (
                SELECT 1
                FROM reserva r
                WHERE r.fk_Sala_id_sala = s.id_sala
                    AND r.data_reserva = %s
                    AND r.horario_fim > %s
                    AND r.horario_inicio < %s
            )
            AND ({condicao_recursos})
    """

    cursor.execute(consulta, (bloco, capacidade, data_reserva, horario_inicio, horario_fim))

    salas = cursor.fetchall()

    #print(salas)
    turmas = buscarTurmas()
    return render_template("reserva.html", nivel=session['nivel'], salas= salas, horario_i = horario_inicio, horario_f = horario_fim, data = data_reserva, turmas = turmas)

@app.route('/reservar' , methods=['POST'])
def reservar():
    conn = bd
    conn.reconnect()
    cursor = conn.cursor()
    finalidade= request.form['finalidade']
    data_reserva= request.form['data']
    horario_i= request.form['hora_i']
    horario_f= request.form['hora_f']
    disciplina= request.form['Disciplina']
    sala_id = int(request.form["fk_sala_id"])
    turma_id = request.form["Turma"]
    email_user = session.get('email')

    if session.get('logged') == True:
    
        if session['nivel']==1:
            query = 'insert into reserva(finalidade, data_reserva, horario_inicio, horario_fim, disciplina, fk_Usuario_email, fk_Sala_id_sala, fk_Turma_id_turma) values (%s, %s, %s, %s, %s, %s, %s, %s)'
            fieldsValue = (finalidade,data_reserva, horario_i, horario_f, disciplina, email_user, sala_id, turma_id)

            if bd.is_connected():
                    comando = query
                    cursor = bd.cursor()
                    valores = fieldsValue
                    cursor.execute(comando, valores)
                    bd.commit()
            #TEM QUE AJUSTAR ESTA MENSAGEM DE SUCESSO
            return render_template("reserva.html", nivel=session['nivel'], salas= "", horario_i = "", horario_f = "", data = "", mensagem = "Solicitação de reserva realizada com sucesso, em breve um administrador entrará em contato!")
        else:           
            return render_template('base.html')
    else:
        return render_template('login.html')


@app.route('/notificar')   
def notificar():
    if session.get('logged') == True:
        if session['nivel']==1:
            conn = bd
            conn.reconnect()
            cursor = conn.cursor()
            cursor.execute("SELECT reserva.fk_Sala_id_sala, reserva.finalidade, reserva.data_reserva, reserva.horario_inicio, reserva.horario_fim, reserva.id_reserva, reserva.fk_Usuario_email, sala.id_sala, sala.nome_ou_numerosala, usuarios.email, usuarios.nome, usuarios.ocupacao, sala.bloco, reserva.status FROM sala INNER JOIN reserva ON sala.id_sala = reserva.fk_Sala_id_sala INNER JOIN usuarios ON usuarios.email = reserva.fk_Usuario_email WHERE reserva.status = 'Aguardando'")
        
            rows = cursor.fetchall()
            result = []

            # Converte cada objeto timedelta em uma string
            for row in rows:
                row = list(row)
                row[3] = str(row[3])
                row[4] = str(row[4])
                result.append(row)

            #print(result)
            
            return render_template('notificacoes.html', nivel=session['nivel'], results = result)
        else:           
            return render_template('base.html')
    else:

        return render_template('login.html')

#LISTAR CHAMADOS ------------------------------------------------------
def listarChamados():
    if session.get('logged') == True:
        conn = bd
        conn.reconnect()
        cursor = conn.cursor()
        email_logado = session['email']
        cursor.execute("SELECT usuarios.nome, chamados.id_chamado, chamados.area, chamados.sub_ou_man, chamados.data_form, chamados.bloco, chamados.nome_numerosala, chamados.data_envio, chamados.fk_Usuario_email, chamados.hora_envio, chamados.descricao  FROM chamados INNER JOIN usuarios ON chamados.fk_Usuario_email = usuarios.email WHERE usuarios.email= %s;",(email_logado,))
        
        rows = cursor.fetchall()
        resultSingleuser = []

        # Converte cada objeto timedelta em uma string
        for row in rows:
            row = list(row)
            row[3] = str(row[3])
            row[4] = str(row[4])
            resultSingleuser.append(row)

            
        if session['nivel']==1:
            #exemplo pra exibir
            cursor.execute("SELECT usuarios.nome, chamados.id_chamado, chamados.area, chamados.sub_ou_man, chamados.data_form, chamados.bloco, chamados.nome_numerosala, chamados.data_envio, chamados.fk_Usuario_email, chamados.hora_envio, chamados.descricao FROM chamados INNER JOIN usuarios ON chamados.fk_Usuario_email = usuarios.email;")
        
            rows = cursor.fetchall()
            resultsAll = []

            # Converte cada objeto timedelta em uma string
            for row in rows:
                row = list(row)
                row[3] = str(row[3])
                row[4] = str(row[4])
                resultsAll.append(row)

            #print(result)
            
            return render_template('historico_manut.html', nivel=session['nivel'], resultsAll = resultsAll, results = resultSingleuser)
        else:           
            
            #print(result)
            
            return render_template('historico_manut.html', nivel=session['nivel'], results = resultSingleuser)
    else:

        return render_template('login.html')


#LISTAR RESERVAS DE SALA------------------------------------------------

def listarHistoricoSalas():
    if session.get('logged') == True:
        conn = bd
        conn.reconnect()
        cursor = conn.cursor()
        email_logado = session['email']
        cursor.execute("SELECT usuarios.nome, reserva.id_reserva, reserva.finalidade, reserva.data_reserva, reserva.horario_inicio, reserva.horario_fim, reserva.disciplina, reserva.fk_Usuario_email, reserva.fk_Sala_id_sala, reserva.fk_Turma_id_turma, reserva.status FROM reserva INNER JOIN usuarios ON reserva.fk_Usuario_email = usuarios.email WHERE usuarios.email= %s;",(email_logado,))
        
        rows = cursor.fetchall()
        resultSingleuser = []

        # Converte cada objeto timedelta em uma string
        for row in rows:
            row = list(row)
            row[3] = str(row[3])
            row[4] = str(row[4])
            resultSingleuser.append(row)

            
        if session['nivel']==1:
            #exemplo pra exibir
            cursor.execute("SELECT usuarios.nome, reserva.id_reserva, reserva.disciplina,reserva.data_reserva,  reserva.finalidade, reserva.horario_inicio, reserva.horario_fim,  reserva.fk_Usuario_email, reserva.fk_Sala_id_sala, reserva.fk_Turma_id_turma, reserva.status FROM reserva INNER JOIN usuarios ON reserva.fk_Usuario_email = usuarios.email;")

            rows = cursor.fetchall()
            resultsAll = []

            # Converte cada objeto timedelta em uma string
            for row in rows:
                row = list(row)
                row[3] = str(row[3])
                row[4] = str(row[4])
                resultsAll.append(row)

            #print(result)
            
            return render_template('Salas_historico.html', nivel=session['nivel'], resultsAll = resultsAll, results = resultSingleuser)
        else:           
            
            #print(result)
            
            return render_template('Salas_historico.html', nivel=session['nivel'], results = resultSingleuser)
    else:

        return render_template('login.html')    
    

#exemplo de update
@app.route('/atualizarReserva', methods=['POST'])
def atualizarReservas():
    if session.get('logged') == True:
        if session['nivel']==1:
            conn = bd
            conn.reconnect()
            cursor = conn.cursor()
            opcao = request.form['opcao']
            id_reserva = int(request.form['id_reserva'])

            print(opcao)
            print(id_reserva)

            cursor.execute('UPDATE reserva SET status = %s WHERE id_reserva = %s', (opcao, id_reserva))
            conn.commit()

            #turmas = cursor.fetchall()
            return notificar()
        else:           
            return render_template('base.html')
    else:

        return render_template('login.html')
    
@app.route('/alterarDados', methods=['POST'])
def alterarDados():
    if session.get('logged') == True:
        email = session['email']
        ocupacao = request.form['ocupacao']
        instituicao = request.form['instituicao']
        senha = request.form['pass']
        conf_senha = request.form['pass-conf']
        conn = bd
        conn.reconnect()
        cursor = conn.cursor()

        if senha == conf_senha and senha != '':
            
            cursor.execute('UPDATE usuarios SET ocupacao = %s, instituicao = %s, senha = %s WHERE email = %s', (ocupacao, instituicao, senha, email))
            conn.commit()

            #turmas = cursor.fetchall()
            session.pop('logged', False)
            session.pop('username', None)
            session.pop('email', None)
            session.pop('nivel', None)
            session.pop('ocupacao', None)
            session.pop('instituicao', None)
            session.pop('pass', None)
            flash('Dados atualizados, faça login novamente!')
            return render_template('login.html')
        else:
            return render_template('perfil.html')
    else:

        return render_template('login.html')

#exemplo de delete       
@app.route('/deletarChamado', methods=['POST'])
def deletarChamado():
    if session.get('logged') == True:
        conn = bd
        conn.reconnect()
        cursor = conn.cursor()

        if session['nivel']==1:
            
            id_chamado = request.form["id_chamado"]

            cursor.execute("DELETE FROM chamados WHERE id_chamado = %s",(id_chamado,))

            conn.commit()

            return listarChamados()
        else:   
            id_chamado = request.form["id_chamado"]
            email = session['email']
            
            cursor.execute("DELETE FROM chamados WHERE id_chamado = %s AND fk_Usuario_email = %s",(id_chamado, email))

            conn.commit()

            return listarChamados()     
    else:
        return render_template('login.html')
    
def buscarTurmas():
    if session.get('logged') == True:

        conn = bd
        conn.reconnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM turma")
        

        turmas = cursor.fetchall()
        return turmas
    else:

        return render_template('login.html')
        

if __name__=="__main__":
    app.run(debug=True) 

    
    
