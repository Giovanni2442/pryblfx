from src.conectDataBase.testConectDb import db

class appFichVent():
    def __init__(self):
        self.connect = db()

    # --- Tabla Ficha Tecnica TABLA PADRE ----

    # --- METHOD GET ----
    # Show all products
    def get_row_Table(self):
        query = 'SELECT * FROM FichaTec;'
        cursor = self.connect.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    # SHOW WITH ID
    def get_row_Id(self,id):
        query = 'SELECT * FROM FichaTec WHERE id_codProduct = %s;'
        cursor = self.connect.cursor()
        cursor.execute(query,(id,))
        result = cursor.fetchall()
        return result
    # ----------------------------
        
    
    # --- METHOD POST ----
    # Insert in table FichaTecnica 
    def post_data(self,*args):
        # INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2335','Fresno','granos','03/07/2024','SS');
        query = 'INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES (%s,%s,%s,%s,%s);'
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"
    # -----------------------

    
    # --- METHOD PUT -------
    # edit any product select in the row
    def putFichaTec(self,id,*args):
        query = '''
            UPDATE FichaTec SET
                cliente=%s,
                fecha_Elav=%s,
                fecha_Rev=%s,
                producto=%s
            WHERE id_codProduct = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query,(id,))
        self.connect.commit()
        return "Update Ok!"

    # ----------------------

    
    # --- METHOD DELETE ----
    # Delete any product select in the row
    def delete_row_Table(self,id):
        query = 'DELETE FROM FichaTec WHERE id_codProduct = %s'
        cursor = self.connect.cursor()
        cursor.execute(query,(id,))
        self.connect.commit()
        return "Delete Ok!"
    # ----------------------
    
    
    
    # --- Tabla Ventas ---
    
    # --- METHOD GET -------
    # edit any product select in the row
    def put_row_Table(self):
        pass

    # ----------------------

    # --- METHOD POST -------
    # Test Insert in table FichaTecnica 
    def post_dataVentas(self,*args):
        # INSERT INTO VENTAS(idCodPrdc,asesor,tipo_Empaque,product_Laminado,estruct_Product,empaca) VALUES ('E-2334','rr','rr','rr','rr','rr');
        query = 'INSERT INTO VENTAS(idCodPrdc,asesor,tipo_Empaque,product_Laminado,estruct_Product,empaca) VALUES (%s,%s,%s,%s,%s,%s);'
        cursor = self.connect.cursor()
        #cursor.execute(query,(id,cln,fch1,fch2,prdct,))
        cursor.execute(query,args)
        self.connect.commit()
        return "Insert Ok!"

    # ----------------------

    # --- METHOD PUT -------
    # edit any product select in the row
    def put_row_Table(self):
        pass

    # ----------------------

    # --- METHOD DELETE -------
    # edit any product select in the row
    def put_row_Table(self):
        pass

    # ----------------------
    
    
    #### QUERY´S DE PRUEBA ####

    def getFichaVentas(self):
        query = '''
            SELECT 
                FichaTec.id_codProduct,
                FichaTec.cliente,
                FichaTec.producto,
                FichaTec.fecha_Elav,
                FichaTec.fecha_Rev,
                VENTAS.asesor,
                VENTAS.tipo_Empaque,
                VENTAS.product_Laminado,
                VENTAS.estruct_Product,
                VENTAS.empaca
            FROM 
                FichaTec
            INNER JOIN 
                VENTAS ON FichaTec.id_codProduct = VENTAS.idCodPrdc
            WHERE 
                FichaTec.id_codProduct = %s;
        '''
        cursor = self.connect.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    ###################################
    
#pr = Controllers()
#print(pr.delete_row_Table("E-2335"))
#print(pr.get_row_Table())
