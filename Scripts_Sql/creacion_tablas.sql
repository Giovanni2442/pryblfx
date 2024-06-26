/*---CREAR TABLAS DE PREOCESOS*/


show databases;
use dbingbf;

/*--Drop tables--*/
drop table FichaTec;
drop table VENTAS;
drop table EXTRUSION;
	drop table CalibrePel_Tolr;
	drop table AnchoBob_Tolr;
    drop table AnchoCore_Tolr;
    drop table DiametroBob_Tolr;
    drop table Peso_Prom_Bob;
    drop table Num_BobCama_CamTam;
    drop table Peso_prom_tarima;
    drop table Peso_Prom_Bob;
    drop table Peso_Prom_Bob;
drop table FichaTec;
drop table FichaTec;drop table FichaTec;
drop table FichaTec;
drop table FichaTec;


	/*--crear bd--*/
create database dbIngBF;
use dbIngBF;

show tables;
/*tabalas*/

/*------------------------ficja encabezado------------------------------*/

INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2334','SS','SS','SS','SS');
INSERT INTO VENTAS(idCodPrdc,asesor,tipo_Empaque,product_Laminado,estruct_Product,empaca) VALUES ('E-2334','rr','rr','rr','rr','rr');

SELECT * FROM FichaTec;
SELECT * FROM VENTAS;

SELECT * FROM FichaTec;

DELETE FROM FichaTec WHERE id_codProduct = 'E-5234-A_R-1' ;

/*------------------------FICHA TECNICA------------------------------*/
CREATE TABLE FichaTec(
	id_codProduct VARCHAR(255) PRIMARY KEY NOT NULL,
    cliente VARCHAR(255) NOT NULL,
    fecha_Elav VARCHAR(255) NOT NULL,
    fecha_Rev VARCHAR(255) NOT NULL,
    producto VARCHAR(255) NOT NULL
);
/*------------------------VENTAS------------------------------*/
	CREATE TABLE VENTAS(
		id INT PRIMARY KEY auto_increment,
        idCodPrdc VARCHAR(255),
        asesor  VARCHAR(255) NOT NULL,
        tipo_Empaque VARCHAR(255) NOT NULL,
        product_Laminado VARCHAR(255) NOT NULL,
        estruct_Product VARCHAR(255) NOT NULL,
        empaca VARCHAR(255) NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
    );
    
/*------------------------EXTRUSION------------------------------*/
    CREATE TABLE EXTRUSION(
		id INT PRIMARY KEY auto_increment,
        idCodPrdc VARCHAR(255),         /*llave foranea*/
        tipo_Material VARCHAR(255) NOT NULL,
        dinaje VARCHAR(255) NOT NULL,
        formula VARCHAR(255) NOT NULL,
        pigmento_Pelicula VARCHAR(255) NOT NULL,
        tipo_Bobina VARCHAR(255) NOT NULL,
        tipo_Tratado VARCHAR(50) NOT NULL,
        max_Emplm INT NOT NULL,
        orient_Bob_Tarima VARCHAR(50) NOT NULL,
        Tipo_Empq_Bob VARCHAR(25) NOT NULL,
        pesar_Prdct VARCHAR(25) NOT NULL,
        etiquetado VARCHAR(25) NOT NULL,
        num_Bob_Tarima INT NOT NULL,
        tarima_Emplaye VARCHAR(25) NOT NULL,
        tarima_flejada VARCHAR(25) NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
    );
		/*Calibre de Pelicula y Tolerancia*/
		CREATE TABLE CalibrePel_Tolr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            calibre VARCHAR(50) NOT NULL,
            tolerancia VARCHAR(50) NOT NULL,
			FOREIGN KEY (idExtr) REFERENCES EXTRUSION(id) ON DELETE CASCADE
        );
        
        /*Ancho de Bobina y Tolerancia*/
        CREATE TABLE AnchoBob_Tolr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            anchoNonina float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idExtr) REFERENCES EXTRUSION(id) ON DELETE CASCADE
        );
        
        /*Ancho de Core y Tolerancia*/
        CREATE TABLE AnchoCore_Tolr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            anchoCore float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idExtr) REFERENCES EXTRUSION(id) ON DELETE CASCADE
        );
        
        /*Diametro de Bobina y Tolerancia*/
        CREATE TABLE DiametroBob_Tolr(
			id INT  PRIMARY KEY auto_increment,
            idExtr INT,
            anchoCore float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idExtr) REFERENCES EXTRUSION(id) ON DELETE CASCADE
        );
        
        /*Peso promedio por bobina*/
        CREATE TABLE Peso_Prom_Bob(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            peso float not null,
            tolerancia float not null,
			FOREIGN KEY (idExtr) REFERENCES EXTRUSION(id) ON DELETE CASCADE
        );
        
        /*Numero de bobinas por cama y camas por tarima*/
        CREATE TABLE Num_BobCama_CamTam(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            num_Bob_Cama int not null,
            camas_Tarima int not null,
			FOREIGN KEY (idExtr) REFERENCES EXTRUSION(id) ON DELETE CASCADE
        );
        
        /*peso neto promedio por tarima*/
        CREATE TABLE Peso_prom_tarima(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            peso_neto float not null,
            tolerancia float not null,
			FOREIGN KEY (idExtr) REFERENCES EXTRUSION(id) ON DELETE CASCADE
        );
        
/*------------------------IMPRESION------------------------------*/
	 CREATE TABLE IMPRESION(
		id INT PRIMARY KEY auto_increment,
		idCodPrdc VARCHAR(255), #llave foranea
        material_Imprimir VARCHAR(255) NOT NULL,
        dinaje VARCHAR(255) NOT NULL,
        grosor_Core float NOT NULL,
        desarrolloImpr int NOT NULL,
        rep_Eje int NOT NULL,
        rep_Dessr int NOT NULL,
        cant_TintasImpr int NOT NULL,
        tipoImpr VARCHAR(50) NOT NULL,
        tipoTintas_Utilizar VARCHAR(50) NOT NULL,
        tipo_Barniz VARCHAR(50) NOT NULL,
        figEmbob_Impr int NOT NULL,
        maxEmpalmes int NOT NULL,
        tipoEmpaqBob VARCHAR(50) NOT NULL,
        orientBob_Tarima VARCHAR(50) NOT NULL,
        pesarProduct VARCHAR(50) NOT NULL,
        etiquetado VARCHAR(50) NOT NULL,
        Num_bob_tarima int NOT NULL,
        validacion VARCHAR(50) not null,
        tarima_Emplaye VARCHAR(50) NOT NULL,
        tarima_Flejada VARCHAR(50) NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
    
		/*Calibre del material y Tolerancia*/
        CREATE TABLE CalMater_Tolr(
			id INT PRIMARY KEY auto_increment,
            idImpr INT,
            calibre float not null,
            tolerancia float not null,
			FOREIGN KEY (idImpr) REFERENCES IMPRESION(id) ON DELETE CASCADE
        );
        
         /*Ancho de bobina a imprimir y tolerancia*/
        CREATE TABLE AnchoBobImpr_Tolr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            ancho float not null,
            tolerancia float not null,
			FOREIGN KEY (idExtr) REFERENCES IMPRESION(id) ON DELETE CASCADE
        );
        
        /*Ancho de core y tolerancia*/
        CREATE TABLE AnchoCore_Tolr_Extr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            ancho_Core float not null,
            tolerancia float not null,
			FOREIGN KEY (idExtr) REFERENCES IMPRESION(id) ON DELETE CASCADE
        );
            
        /*Diametro de bobina y Tolerancia*/
        CREATE TABLE DiamBob_Tolr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            diametro float not null,
            tolerancia float not null,
			FOREIGN KEY (idExtr) REFERENCES IMPRESION(id) ON DELETE CASCADE
        );
        
        /*Peso neto promedio de bobina*/
        CREATE TABLE PesoPromBob(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            peso float not null,
            tolerancia float not null,
			FOREIGN KEY (idExtr) REFERENCES IMPRESION(id) ON DELETE CASCADE
        );
        
        /*Numero de bobinas por cama y camas por tarima*/
        CREATE TABLE Num_BobCama_CamTam_Extr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            num_Bob_Cama int not null,
            camas_Tarima int not null,
			FOREIGN KEY (idExtr) REFERENCES IMPRESION(id) ON DELETE CASCADE
        );
        
        /*Numero de bobinas por cama y camas por tarima*/
        CREATE TABLE Peso_prom_tarima_Extr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            numBobCama VARCHAR(10) not null,
            camaTam int not null,
			FOREIGN KEY (idExtr) REFERENCES IMPRESION(id) ON DELETE CASCADE
        );

        /*Peso neto promedio por tarima y tolerancia*/
        CREATE TABLE Peso_prom_tarima_Extr(
			id INT PRIMARY KEY auto_increment,
            idExtr INT,
            pesoNto int not null,
            tolerancia int not null,
			FOREIGN KEY (idExtr) REFERENCES IMPRESION(id) ON DELETE CASCADE
        );
        
/*------------------------LAMINADO------------------------------*/
        
	CREATE TABLE LAMINADO(
		id INT PRIMARY KEY auto_increment,
		idCodPrdc VARCHAR(255),
		estructProduct VARCHAR(255) NOT NULL,
        tipoTratado VARCHAR(100) NOT NULL,
        maxEmpalmesBob VARCHAR(50) NOT NULL,
        orientBobRack VARCHAR(50) NOT NULL,
        tipoEmpaqBob VARCHAR(50) NOT NULL,
        etiquetado VARCHAR(50) NOT NULL,
        pesarProduct VARCHAR(50) NOT NULL,
		FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
		 /*Material Impreso*/
        CREATE TABLE Material_Impreso(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            tipoTratado VARCHAR(50) NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        );
			/*Calibre de pelicula y Tolerancia*/
			CREATE TABLE CalibrePelic_Tolr(
				id INT PRIMARY KEY auto_increment,
				idMtrlIm INT,
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrlIm) REFERENCES Material_Impreso(id) ON DELETE CASCADE
			);
        
			/*Ancho de Bobina y Tolerancia*/
			CREATE TABLE AnchoBob_TolrMtrl(
				id INT PRIMARY KEY auto_increment,
				idMtrlIm INT,
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrlIm) REFERENCES Material_Impreso(id) ON DELETE CASCADE
			);
            
		 /*Laminación 1*/
        
        /*Laminación 1*/
        CREATE TABLE Material_Laminar_1(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            Material = VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
            tipoLamin VARCHAR(50) NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        );
        
			/*Ancho de Bobina y Tolerancia Laminación 1*/
			CREATE TABLE CalibrePelic_TolrLam1(
				id INT PRIMARY KEY auto_increment,
				idMtrLam1 INT,  /*foreign key*/
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrLam1) REFERENCES Material_Laminar_1(id) ON DELETE CASCADE
			);
            
            /*Ancho de Bobina y Tolerancia Laminación 1*/
			CREATE TABLE AnchoBob_TolrLam1(
				id INT PRIMARY KEY auto_increment,
				idMtrLam1 INT,  /*foreign key*/
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrLam1) REFERENCES Material_Laminar_1(id) ON DELETE CASCADE
			);
           
		/*Laminación 2*/
		 CREATE TABLE Material_Laminar_2(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            Material = VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
            tipoLamin VARCHAR(50) NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        );
        
			/*Ancho de Bobina y Tolerancia Laminación 2*/
			CREATE TABLE CalibrePelic_TolrLam2(
				id INT PRIMARY KEY auto_increment,
				idMtrLam1 INT,  /*foreign key*/
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrLam1) REFERENCES Material_Laminar_2(id) ON DELETE CASCADE
			);
            
             /*Ancho de Bobina y Tolerancia Laminación 1*/
			CREATE TABLE AnchoBob_TolrLam2(
				id INT PRIMARY KEY auto_increment,
				idMtrLam1 INT,  /*foreign key*/
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrLam1) REFERENCES Material_Laminar_2(id) ON DELETE CASCADE
			);
            
		/*Laminación 3*/
		 CREATE TABLE Material_Laminar_3(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            Material = VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
            tipoLamin VARCHAR(50) NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        );
        
			/*Ancho de Bobina y Tolerancia Laminación 2*/
			CREATE TABLE CalibrePelic_TolrLam3(
				id INT PRIMARY KEY auto_increment,
				idMtrLam1 INT,  /*foreign key*/
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrLam1) REFERENCES Material_Laminar_3(id) ON DELETE CASCADE
			);
            
             /*Ancho de Bobina y Tolerancia Laminación 1*/
			CREATE TABLE AnchoBob_TolrLam3(
				id INT PRIMARY KEY auto_increment,
				idMtrLam1 INT,  /*foreign key*/
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrLam1) REFERENCES Material_Laminar_3(id) ON DELETE CASCADE
			);
            
		/*Laminación 4*/
		 CREATE TABLE Material_Laminar_4(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            Material = VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
            tipoLamin VARCHAR(50) NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        );
        
			/*Ancho de Bobina y Tolerancia Laminación 2*/
			CREATE TABLE CalibrePelic_TolrLam4(
				id INT PRIMARY KEY auto_increment,
				idMtrLam1 INT,  /*foreign key*/
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrLam1) REFERENCES Material_Laminar_4(id) ON DELETE CASCADE
			);
            
             /*Ancho de Bobina y Tolerancia Laminación 1*/
			CREATE TABLE AnchoBob_TolrLam4(
				id INT PRIMARY KEY auto_increment,
				idMtrLam1 INT,  /*foreign key*/
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idMtrLam1) REFERENCES Material_Laminar_4(id) ON DELETE CASCADE
			);
            
		/*Medida de la manga para la Transferencia*/
		CREATE TABLE MedidManga(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            medidaManga float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
		);
        
        /*Ancho de core y Tolerancia*/
        CREATE TABLE AnchoCore_TolrLam(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            anchoCore float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        );
        
        /*Diametro y Grosor de core*/
        CREATE TABLE Diametro_GrosCore(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            diametro float NOT NULL,
            grosorCore float NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        );

        /*Diametro de bobina y Tolerancia*/
        CREATE TABLE Diametro_Bob_Tolr(
			id INT PRIMARY KEY auto_increment,
            idLam INT,
            diametroBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        );

        /*Peso promedio por bobina y Tolerancia*/
        CREATE TABLE Peso_Prom_Bob(
            id INT PRIMARY KEY auto_increment,
            idLam INT,
            pesoPromBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idLam) REFERENCES LAMINADO(id) ON DELETE CASCADE
        )
        
/*------------------------REFILADO------------------------------*/

	CREATE TABLE REFILADO(
		id INT PRIMARY KEY auto_increment,
		idCodPrdc VARCHAR(255),  #foreign key
		proceso VARCHAR(50) NOT NULL,
        acabadoBob VARCHAR(50) NOT NULL,
        grosorCore VARCHAR(50) NOT NULL,
        figEmbob_impr VARCHAR(50) NOT NULL,
        bobinaRefilar VARCHAR(50) NOT NULL,
        maximo_Empal int NOT NULL,
        señalEmpl VARCHAR(50) NOT NULL,
        orient_Bob_Tarima VARCHAR(50) NOT NULL,
        tipo_Empaque VARCHAR(50) NOT NULL,
        pesar_Prdct VARCHAR(50) NOT NULL,
        etiquetado VARCHAR(50) NOT NULL,
        tarima_emplaye VARCHAR(50) NOT NULL,
        tarima_flejada VARCHAR(50) NOT NULL,
		FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
		/*Ancho final de bobina al refilarse/Doblarse y Tolerancia*/
		CREATE TABLE AnchoFinalBob_Tolr(
			id INT PRIMARY KEY auto_increment,
            idRef INT,
			anchoFinalBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idRef) REFERENCES REFILADO(id) ON DELETE CASCADE
        );
        /*Ancho de core y Tolerancia*/
        CREATE TABLE AnchoFinalBob_TolrRefil(
			id INT PRIMARY KEY auto_increment,
            idRef INT,
			anchoCore float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idRef) REFERENCES REFILADO(id) ON DELETE CASCADE
        );
        
        /*Metros por bobina al refilarse/doblarse y tolerancia*/
        CREATE TABLE MetrosBobRefil_Tolr(
			id INT PRIMARY KEY auto_increment,
            idRef INT,
			metros float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idRef) REFERENCES REFILADO(id) ON DELETE CASCADE
        );
        
        /*Diametro de bobina al refilarse/doblarse y tolerancia*/
        CREATE TABLE DiamBobRefil_Tolr(
			id INT PRIMARY KEY auto_increment,
            idRef INT,
			diametro float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idRef) REFERENCES REFILADO(id) ON DELETE CASCADE
        );
        
         /*Peso neto promedio por bobina */
        CREATE TABLE PesoNet_Prom_Bob(
			id INT PRIMARY KEY auto_increment,
            idRef INT,
			peso float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idRef) REFERENCES REFILADO(id) ON DELETE CASCADE
        );
        
		/*Numero de bobinas por cama y camas por tarima*/
        CREATE TABLE Num_BobCama_CamTamRefil(
			id INT PRIMARY KEY auto_increment,
            idRef INT,
			num_Bob_Cama float NOT NULL,
            camas_Tarima float NOT NULL,
			FOREIGN KEY (idRef) REFERENCES REFILADO(id) ON DELETE CASCADE
        );
        
        /*Peso neto promedio por tarima*/
        CREATE TABLE Peso_prom_tarimaRefil(
			id INT PRIMARY KEY auto_increment,
            idRef INT,
			pesoNeto float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idRef) REFERENCES REFILADO(id) ON DELETE CASCADE
        );
        
/*------------------------CONVERSION------------------------------*/
	
	CREATE TABLE CONVERSION(
		id INT PRIMARY KEY auto_increment,
		idCodPrdc VARCHAR(255),  #foreign key
		tipo_Empaque VARCHAR(100) NOT NULL,
        tipoSello VARCHAR(50) NOT NULL,
        tipoAcabado VARCHAR(50) NOT NULL,
        perf int NOT NULL,
        llevaSuaj VARCHAR(50) NOT NULL,
        suaje VARCHAR(50) NOT NULL,
        empcProd VARCHAR(50) NOT NULL,
        cantPzsPacq float NOT NULL,
        embalaje VARCHAR(50) NOT NULL,
        medidEmblj int NOT NULL,
        pesarProd VARCHAR(50) NOT NULL,
        pesoProm float NOT NULL,
        etiquetado VARCHAR(50) NOT NULL,
        tarima_Emplaye VARCHAR(50) NOT NULL,
        tarima_Flejada VARCHAR(50) NOT NULL,
		FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
    
		/*Medida del empaque Ancho/Alto*/
        CREATE TABLE MedidEmpq(
			id INT PRIMARY KEY auto_increment,
            idCnvrs INT,		#foreign key
			ancho float NOT NULL,
            alto float NOT NULL,
			FOREIGN KEY (idCnvrs) REFERENCES CONVERSION(id) ON DELETE CASCADE
        );
        
        /*Numero de bultos o cajas por camas y camas por tarima*/
        CREATE TABLE NumBlts_CajsCmas_CmasTarim(
			id INT PRIMARY KEY auto_increment,
            idCnvrs INT,		#foreign key
			cajasCama float NOT NULL,  
            camasTarima float NOT NULL,
			FOREIGN KEY (idCnvrs) REFERENCES CONVERSION(id) ON DELETE CASCADE
        );
        
        /*Numero de bultos o cajas por camas y camas por tarima*/
        CREATE TABLE NumBlts_CajsTarim(
			id INT PRIMARY KEY auto_increment,
            idCnvrs INT,		#foreign key
			peso float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCnvrs) REFERENCES CONVERSION(id) ON DELETE CASCADE
        );
        
        
    
		
        
        

		
            
		
            
		
            
            
        
			
            
            
        
			
			
		
        
	
        
        
        
        
        
		
        
        
        
        
        
        
    
    