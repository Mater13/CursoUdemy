#!/usr/bin/env python3
import psycopg2

conexion = psycopg2.connect(
    user='matimedina',
    password='123456',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
