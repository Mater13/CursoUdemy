def listarTerminos(**terminos):  # python utiliza el nombre KWARGS
    for llave, valor in terminos.items():  # KWARGS = kayword arguments
        print(f'{llave}: {valor}')


listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)  # llamo a la lista nombres
desplegarNombres('Carlos')  # str 'carlos'
desplegarNombres((8, 9))  # corre sobre la tupla (8, 9)
desplegarNombres([10, 9])  # corre sobre la lista
