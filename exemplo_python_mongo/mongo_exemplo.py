import pymongo

#Conectando ao servidor local do MongoDB
str_con = "mongodb+srv://admin:admin@projagil.t7xiqfu.mongodb.net/?retryWrites=true&w=majority"
client_con = pymongo.MongoClient(str_con)

#Selecionando o banco de dados e a collection
pacientes_coll = client_con.db_clinica.pacientes

#Filtra os dados
resultados = pacientes_coll.find()

lista_pacientes = list(resultados)
print('Todos os pacientes:')
print(lista_pacientes)

filter_ = {'idade': {'$gt': 30}}
projection_ = {'_id': 0, 'nome_paciente': 1, 'idade': 1}

resultados = pacientes_coll.find(filter_, projection_)
lista_pacientes = list(resultados)
print('Pacientes com idade maior que 30 anos:')
print(lista_pacientes)



