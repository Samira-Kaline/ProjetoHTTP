from flask import Flask,request
from dados import clientes
import json
app = Flask(__name__)

#Listar
@app.route('/ListarClientes',methods=['GET'])
def ListarClientes():
    return {"data":clientes}

#Cadastrar
@app.route('/CadastrarCliente',methods=['POST'])
def CriarCliente():
    novo_cliente = json.loads(request.data)
    clientes.append(novo_cliente)
    return "Cadastrado com sucesso"

#Atualizar
# Ao colocar a URL coloque /id_do_cliente
@app.route('/AtualizarCliente/<int:id>',methods=['PUT'])
def AtualizarCliente(id:int):
    update_cliente = json.loads(request.data)
    clientes[id] = update_cliente
    return 'Atualização Completa'

#Deletar
# Ao colocar a URL coloque /id_do_cliente
@app.route('/DeletarCliente/<int:id>',methods=['DELETE'])
def DeletarCliente(id:int):
    del clientes[id]
    return 'Cliente Deletado'

app.run(debug=True)
