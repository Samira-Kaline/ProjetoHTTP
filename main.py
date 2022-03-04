from flask import Flask,jsonify,request
from dados import clientes
import json
app = Flask(__name__)

#Listar
@app.route('/ListarClientes',methods=['GET'])
def ListarClientes():
    return {"data":clientes}

#Criar
@app.route('/Cadastrar',methods=['POST'])
def CadastrarCliente():
    novo_cliente = json.loads(request.data)
    clientes.append(novo_cliente)
    return jsonify("Cadastrado com sucesso")

#Atualizar
@app.route('/todo/update',methods=['UPDATE'])
def AtualizarCliente():
    return 'Atualizar Dados do Cliente'

#Deletar
@app.route('/todo/delete',methods=['DELETE'])
def DeletarCliente():
    return 'Deletar Cliente'

app.run(debug=True)
