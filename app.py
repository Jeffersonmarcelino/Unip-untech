from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# Chave secreta necessária para gerenciar sessões (login)
app.secret_key = 'chave_secreta_unitech_2024'

# DICIONÁRIO SIMULANDO UM BANCO DE DADOS
# Usuários iniciais para teste
USERS = {
    'aluno@unitech.com': {'password': '123', 'profile': 'aluno'},
    'professor@unitech.com': {'password': '123', 'profile': 'professor'},
    'coord@unitech.com': {'password': '123', 'profile': 'coordenador'}
}

# ----------------------------------------------------
# ROTA 1: Tela de Seleção de Perfil (/)
# ----------------------------------------------------

@app.route('/')
def select_profile():
    return render_template('profile_selection.html') 

# ----------------------------------------------------
# ROTA 2: Exibe a Tela de Login/Registro (/auth_screen)
# ----------------------------------------------------

@app.route('/auth_screen', methods=['POST'])
def auth_screen():
    # Pega o perfil que foi escolhido na tela anterior
    profile = request.form.get('profile') 
    if profile:
        # Armazena o perfil escolhido temporariamente
        session['temp_profile'] = profile 
        # Renderiza a tela de login/registro
        return render_template('login_register.html', profile=profile)
    return redirect(url_for('select_profile'))

# ----------------------------------------------------
# ROTA 3: Processa o Login (/login_action)
# ----------------------------------------------------

@app.route('/login_action', methods=['POST'])
def login_action():
    email = request.form.get('email')
    password = request.form.get('password')
    temp_profile = session.get('temp_profile') # Perfil que o usuário escolheu

    # 1. Verifica se o e-mail existe
    if email in USERS:
        user_data = USERS[email]
        # 2. Verifica se a senha e o perfil correspondem
        if user_data['password'] == password and user_data['profile'] == temp_profile:
            
            # Login bem-sucedido!
            session['user_profile'] = temp_profile
            session.pop('temp_profile', None) # Limpa o perfil temporário
            
            # Redirecionamento para o dashboard correto
            if temp_profile == 'aluno':
                return redirect(url_for('student_dashboard'))
            elif temp_profile == 'professor':
                return redirect(url_for('teacher_dashboard'))
            elif temp_profile == 'coordenador':
                return redirect(url_for('coordinator_dashboard'))
            
    # Login falhou, volta para a tela de autenticação
    return render_template('login_register.html', profile=temp_profile, error='Credenciais inválidas ou perfil incorreto.')

# ----------------------------------------------------
# ROTA 4: Processa o Registro (/register_action)
# ----------------------------------------------------

@app.route('/register_action', methods=['POST'])
def register_action():
    email = request.form.get('email')
    password = request.form.get('password')
    temp_profile = session.get('temp_profile')

    if email in USERS:
        return render_template('login_register.html', profile=temp_profile, error='Este e-mail já está em uso.')
    
    # Adiciona o novo usuário ao dicionário (simulação de BD)
    USERS[email] = {'password': password, 'profile': temp_profile}
    
    # Redireciona para a tela de login com sucesso
    return render_template('login_register.html', profile=temp_profile, success='Registro realizado! Faça login com suas novas credenciais.')


# ----------------------------------------------------
# ROTAS DOS DASHBOARDS (Incluir as rotas aqui para funcionar)
# ----------------------------------------------------

@app.route('/aluno/dashboard')
def student_dashboard():
    if session.get('user_profile') == 'aluno':
        # Assuma que você tem aluno_dashboard.html
        return render_template('aluno_dashboard.html', user_name='João')
    return redirect(url_for('select_profile'))

@app.route('/professor/dashboard')
def teacher_dashboard():
    if session.get('user_profile') == 'professor':
        # Assuma que você tem professor_dashboard.html
        return render_template('professor_dashboard.html')
    return redirect(url_for('select_profile'))

@app.route('/coordenador/dashboard')
def coordinator_dashboard():
    if session.get('user_profile') == 'coordenador':
        # Assuma que você tem coordenador_dashboard.html
        return render_template('coordenador_dashboard.html')
    return redirect(url_for('select_profile'))


# Rota de Logout
@app.route('/logout')
def logout():
    session.pop('user_profile', None)
    session.pop('temp_profile', None)
    return redirect(url_for('select_profile'))

if __name__ == '__main__':
    app.run(debug=True)