import mysql.connector

def insert_db(filmes):
    try:  
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "vit221bRomans8.0",
            database = "dbVerificacaoFilme"
        )

        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)

            mycursor = mydb.cursor() 

            sql_query = "INSERT INTO tbVerFilme(nomeFilme,faixaEtariaFilme,nomeUsuario,idadeUsuario) VALUES (%s, %s, %s, %s)"

            mycursor.execute(sql_query, filmes)
            
            mydb.commit()

            print(mycursor.rowcount, "registro inserido")
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")

