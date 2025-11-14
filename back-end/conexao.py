import psycopg2
from dotenv import load_dotenv
import os 


load_dotenv()

def conector():
    try:
        conexao = psycopg2.connect(
            database=os.getenv("DB_NAME", "estoque"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "dev1t@24"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432")
        )
        cursor = conexao.cursor()
        print("Conexão estabelecida")
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexão")
        return None, None
    
