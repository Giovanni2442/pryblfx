def addFichTec(data,c):
    insertQuery = f"""
        INSERT INTO FichaTec(id_codProduct, cliente, fecha_Elav, fecha_Rev, producto)
        VALUES('{data[8][c]}', '{data[6][c]}', 'N/A', '{data[2][c]}', '{data[7][c]}')
    """
    return insertQuery    
