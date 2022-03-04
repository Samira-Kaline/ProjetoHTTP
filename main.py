from flask import Flask,jsonify,render_template
from dados import clientes

app = Flask(__name__)

@app.route('/Inicio',methods=['GET'])
def Inicio():
    return render_template('main.html')

#Listar
@app.route('/ListarCliente',methods=['GET'])
def ListarClientes():
    return jsonify(clientes)

#Criar
@app.route('/todo/create',methods=['POST'])
def CriarCliente():
    return 'Criar novo Cliente'

#Atualizar
@app.route('/todo/update',methods=['UPDATE'])
def AtualizarCliente():
    return 'Atualizar Dados do Cliente'

#Deletar
@app.route('/todo/delete',methods=['DELETE'])
def DeletarCliente():
    return 'Deletar Cliente'

app.run(debug=True)
