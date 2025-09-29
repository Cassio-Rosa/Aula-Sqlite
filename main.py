#Importar a biblioteca sqlite3
import sqlite3

#Cria uma conexão com o banco de dados chamado "escola.db"

conexao = sqlite3.connect("escola.db")

#Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()

#Criar uma tabela no banco de dados
cursor.execute("""

CREATE TABLE IF NOT EXISTS alunos (
               
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
                
    )
""")


# #inserir um aluno no banco de dados
# nome = input("Digite o nome do aluno que desejar cadastrar: ")
# cursor.execute(f"""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?,?,?)
# """, (nome, 20, 'Medicina'))


# #Podemos cadastrar varias informações no banco de dados
# alunos = [
#     ('Enzo', 22, 'Direito'),
#     ('Murilo', 33, 'Computação'),
#     ('Eduardo', 41, 'Computação'),
# ]

# # Executemany permite inserir múltiplas linhas de uma vez só
# cursor.executemany("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?,?,?)
# """, alunos)


# #Precisamos confirmar as alterações no banco de dados
# conexao.commit()

#Atualizar os dados no banco de dados
# cursor.execute("""
# UPDATE alunos
# SET idade = ?, curso = ?
# WHERE id = ?
# """,(27,"ADS",2))
# conexao.commit()
# print("Dados atualizados com sucesso!")

# #Consultar os dados no banco de dados
# cursor.execute("SELECT * FROM alunos")
# #fetchall traz todas as linhas da tabela
# for linha in cursor.fetchall():
#     print(f"ID: {linha[0]}| Nome: {linha[1]}| Idade: {linha[2]}| Curso: {linha[3]}")

# cursor.execute("SELECT * FROM alunos WHERE curso = ?", ("Computação",))
# for linha in cursor.fetchall():
#     print(f"ID: {linha[0]}| Nome: {linha[1]}| Idade: {linha[2]}| Curso: {linha[3]}")


#Deletando dados no banco

def deletar_aluno():
    try:
        conexao = sqlite3.connect("escola.db")
        cursor = conexao.cursor()

        id_aluno = int(input("Digite o ID do aluno que deseja deletar: "))

        cursor.execute("DELETE FROM alunos WHERE id=?", (id_aluno,))
        conexao.commit()
        #Verificar se o item foi deletado
        if cursor.rowcount > 0:
            print("Aluno removido com sucesso")
        else:
            print("Nenhum aluno cadastrado com o ID fornecido")
    except Exception as erro:
        print(f"Errp ap tentar excluir o aluno. Erro = {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()
       
deletar_aluno()

