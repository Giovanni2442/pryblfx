show variables like "max_connections";
set global max_connections = 250;
/*---CREAR TABLAS DE PREOCESOS*/
show databases;
use dbingbf;
create database dbingbf;

show tables;
show databases;

DROP DATABASE dbingbf;

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

drop table impresion;



	/*--crear bd--*/
create database dbIngBF;
use dbIngBF;

show tables;
/*tabalas*/

/*------------------------ficja encabezado------------------------------*/

						/*------ INSERCIÓNES A LA BASE DE DATOS ----------*/
                        
/*--------FichaTec--------*/
select * from FichaTec WHERE id_codProduct = "232321";
select * from VENTAS WHERE idCodPrdc = "14141414";

UPDATE FichaTec SET
	cliente="HOLA",
	fecha_Elav="RERERER",
	fecha_Rev="IJIJI",
	producto="HOLA"
WHERE id_codProduct = "454545";

INSERT INTO VENTAS(idCodPrdc,asesor,tipo_Empaque,product_Laminado,estruct_Product,empaca) VALUES ('E-2334','rr','rr','rr','rr','rr');

UPDATE VENTAS SET
	asesor="HOLA",
	tipo_Empaque="HOLA",
	product_Laminado="HOLA",
	estruct_Product="HOLA",
    empaca="HOLA"
WHERE idCodPrdc = '14141414';

select * from FichaTec;
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('2323','Reyma','Envaces desechables','03/07/2024','03/07/2024');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2335','Fresno','granos','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2336','Waltmart','herramientas','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2337','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2338','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2339','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2340','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2341','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2342','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2343','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2344','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2345','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2346','pounch','comina','03/07/2024','SS');

/*--------VENTAS--------*/
INSERT INTO VENTAS(idCodPrdc,asesor,tipo_Empaque,product_Laminado,estruct_Product,empaca) VALUES ('E-2334','rr','rr','rr','rr','rr');

/*--------EXTRUSIÓN--------*/
INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada) VALUES ('E-2334','rr','rr','rr','rr','rr','qe',10,'qe','qe','qe','qe',88,'qe','qe');

INSERT INTO CalibrePel_Tolr(idCodPrdc,calibre,tolerancia) VALUES  ('E-2334',30,40);

INSERT INTO AnchoBob_Tolr(idCodPrdc,anchoBob,tolerancia) VALUES ('E-2334',30,40);

INSERT INTO AnchoCore_Tolr(idCodPrdc,anchoCore,tolerancia) VALUES ('E-2334',30,40);

INSERT INTO DiametroBob_Tolr(idCodPrdc,diamBob,tolerancia) VALUES ('E-2334',30,40);

INSERT INTO Peso_Prom_Bob(idCodPrdc,pesoBob,tolerancia) VALUES ('E-2334',30,40);

INSERT INTO Num_BobCama_CamTam(idCodPrdc,num_Bob_Cama,camas_Tarima) VALUES ('E-2334',30,40);

INSERT INTO Peso_prom_tarima(idCodPrdc,peso_neto,tolerancia) VALUES ('E-2334',30,40);

/*--------IMPRESIÓN--------*/
INSERT INTO IMPRESION (idCodPrdc,material_Imprimir,dinaje,grosor_Core,desarrolloImpr,rep_Eje,rep_Dessr,cant_TintasImpr,tipoImpr,tipoTintas_Utilizar,tipo_Barniz,figEmbob_Impr,maxEmpalmes,tipoEmpaqBob,orientBob_Tarima,pesarProduct, etiquetado,Num_bob_tarima,tarima_Emplaye,tarima_Flejada)
 VALUES ('E-2335','Papel','300g',0.5,5,3,2,4,'Offset','Tinta UV','Barniz Brillante',1,2,'Caja','Vertical','Peso Neto','Etiqueta A',20,'Envuelta','Flejada');

INSERT INTO vldClr(idCodPrdc,color,tolDelts) VALUES ('E-2121','EW','EW');

INSERT INTO Peso_prom_tarimaImpr(idCodPrdc,pesoNto,tolerancia) VALUES ('E-2335',0,0);

INSERT INTO LAMINADO(idCodPrdc, estructProduct, tipoTratado, maxEmpalmesBob, orientBobRack, tipoEmpaqBob, etiquetado, pesarProduct) 
VALUES (
    'E-2335',          -- idCodPrdc: Debe existir en la tabla FichaTec
    'Estructura A',  -- estructProduct: Valor no nulo
    'Tratado X',     -- tipoTratado: Valor no nulo
    '5',             -- maxEmpalmesBob: Valor no nulo
    'Vertical',      -- orientBobRack: Valor no nulo
    'Empaque A',     -- tipoEmpaqBob: Valor no nulo
    'Etiqueta B',    -- etiquetado: Valor no nulo
    'Pesado Y'       -- pesarProduct: Valor no nulo
);

SELECT * FROM FichaTec;
SELECT * FROM VENTAS;
	# -- TABLA EXTRUSION -- #
SELECT * FROM EXTRUSION;
	SELECT * FROM CalibrePel_Tolr;
	SELECT * FROM AnchoBob_Tolr;
	SELECT * FROM AnchoCore_TolrExtr;
	SELECT * FROM DiametroBob_Tolr;
	SELECT * FROM Peso_Prom_Bob;
	SELECT * FROM Peso_prom_tarima;
	
    # -- TABLA IMPRESIÓN -- #
SELECT * FROM IMPRESION;
	SELECT * FROM vldClr;
    SELECT * FROM CalMater_Tolr;
    SELECT * FROM AnchoBobImpr_Tolr;
    SELECT * FROM AnchoCore_TolrImpr;
    SELECT * FROM DiamBob_Tolr;
    SELECT * FROM PesoPromBob;
    SELECT * FROM Num_BobCama_CamaTarima;
    SELECT * FROM Peso_prom_tarimaImpr;
    
       # -- TABLA IMPRESIÓN -- #
SELECT * FROM LAMINADO;

/*
SELECT 
	FichaTec.id_codProduct,
    EXTRUSION.tipo_Material,
    EXTRUSION.dinaje,
    EXTRUSION.formula,
    EXTRUSION.pigmento_Pelicula,
    EXTRUSION.tipo_Bobina,
    EXTRUSION.tipo_Tratado,
    EXTRUSION.max_Emplm,
    EXTRUSION.orient_Bob_Tarima,
    EXTRUSION.Tipo_Empq_Bob,
    EXTRUSION.pesar_Prdct,
    EXTRUSION.etiquetado,
    EXTRUSION.num_Bob_Tarima,
	CalibrePel_Tolr.calibre,
	CalibrePel_Tolr.tolerancia,
	AnchoBob_Tolr.anchoBob,
	AnchoBob_Tolr.tolerancia,
	DiametroBob_Tolr.diamBob,
	DiametroBob_Tolr.tolerancia,
	Peso_Prom_Bob.pesoBob,
	Peso_Prom_Bob.tolerancia,
	Num_BobCama_CamTam.num_Bob_Cama,
    Num_BobCama_CamTam.camas_Tarima,
    Peso_prom_tarima.peso_neto,
    Peso_prom_tarima.tolerancia
FROM 
	EXTRUSION
INNER JOIN 
	CalibrePel_Tolr,Peso_prom_tarima ON FichaTec.id_codProduct = VENTAS.idCodPrdc
WHERE 
	FichaTec.id_codProduct = %s; */

/*--------------------------------------------------------------------------------------------------------------------------------------*/
show tables;

/*-----------------------------PRINTD CARD--------------------------------------*/
select * from PrindCard;
drop table PrindCard;
CREATE TABLE PrindCard(
        idCodPrdc VARCHAR(255),
		prindCrdPdf LONGBLOB NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
);

/*------------------------FICHA TECNICA------------------------------*/
CREATE TABLE FichaTec(
	id_codProduct VARCHAR(255) PRIMARY KEY NOT NULL,
    cliente VARCHAR(255) NOT NULL,
	producto VARCHAR(255) NOT NULL,
    fecha_Elav VARCHAR(255) NOT NULL,
    fecha_Rev VARCHAR(255) NOT NULL
);
/*------------------------VENTAS------------------------------*/
	CREATE TABLE VENTAS(
        idCodPrdc VARCHAR(255),
        asesor  VARCHAR(255) NOT NULL,
        tipo_Empaque VARCHAR(255) NOT NULL,
        product_Laminado VARCHAR(255) NOT NULL,
        estruct_Product VARCHAR(255) NOT NULL,
        empaca VARCHAR(255) NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
    );
    
/*------------------------EXTRUSION------------------------------*/
	show tables;
     drop table EXTRUSION;
    CREATE TABLE EXTRUSION(
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
            idCodPrdc VARCHAR(255),
            calibre VARCHAR(50) NOT NULL,
            tolerancia VARCHAR(50) NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
        
        /*Ancho de Bobina y Tolerancia*/
        CREATE TABLE AnchoBob_TolrExtr(
			idCodPrdc VARCHAR(255),
            anchoBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
  
        /*Ancho de Core y Tolerancia*/
        drop table AnchoCore_TolrExtr;
        CREATE TABLE AnchoCore_TolrExtr(
			idCodPrdc VARCHAR(255),
            anchoCore float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
        
        /*Diametro de Bobina y Tolerancia*/
        CREATE TABLE DiametroBob_Tolr(
            idCodPrdc VARCHAR(255),
            diamBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
		
        /*Peso promedio por bobina*/
        CREATE TABLE Peso_Prom_Bob(
            idCodPrdc VARCHAR(255),
            pesoBob float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );

		
        /*Numero de bobinas por cama y camas por tarima*/
        CREATE TABLE Num_BobCama_CamTam(
            idCodPrdc VARCHAR(255),
            num_Bob_Cama int not null,
            camas_Tarima int not null,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
        
        /*peso neto promedio por tarima*/
        CREATE TABLE Peso_prom_tarimaExtr(
            idCodPrdc VARCHAR(255),
            peso_neto float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
        
        /*peso neto promedio por tarima*/
        select * from Peso_prom_tarima;
        drop table Peso_prom_tarimaExtr;
 
/*------------------------IMPRESION------------------------------*/
	 CREATE TABLE IMPRESION(
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
        tarima_Emplaye VARCHAR(50) NOT NULL,
        tarima_Flejada VARCHAR(50) NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
    
		/*Validación de color*/
        CREATE TABLE vldClr(
            idCodPrdc VARCHAR(255),
            color VARCHAR(255) not null,
            tolDelts VARCHAR(255) not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
    
		/*Calibre del material y Tolerancia*/
        CREATE TABLE CalMater_Tolr(
            idCodPrdc VARCHAR(255),
            calibre float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
         /*Ancho de bobina a imprimir y tolerancia*/
        CREATE TABLE AnchoBobImpr_Tolr(
			idCodPrdc VARCHAR(255),
            ancho float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
        drop table AnchoCore_Tolr;
        
        select * from AnchoCore_TolrImpr;
        /*Ancho de core y tolerancia*/
        CREATE TABLE AnchoCore_TolrImpr(
			idCodPrdc VARCHAR(255),
            ancho_Core float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
            
        /*Diametro de bobina y Tolerancia*/
        CREATE TABLE DiamBob_Tolr(
			idCodPrdc VARCHAR(255),
            diametro float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
        /*Peso neto promedio de bobina*/
        CREATE TABLE PesoPromBob(
			idCodPrdc VARCHAR(255),
            peso float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
                
        /*Numero de bobinas por cama y camas por tarima*/
        CREATE TABLE Num_BobCama_CamaTarima(
			idCodPrdc VARCHAR(255),
            numBobCama VARCHAR(10) not null,
            camaTam int not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
        
		drop table Peso_prom_tarimaImpr;
        /*Peso neto promedio por tarima y tolerancia*/
        CREATE TABLE Peso_prom_tarimaImpr(
			idCodPrdc VARCHAR(255),
            pesoNto int not null,
            tolerancia int not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
/*------------------------LAMINADO------------------------------*/

	show tables;

	drop table LAMINADO;
    SELECT * FROM LAMINADO;
    
    INSERT INTO LAMINADO(idCodPrdc, estructProduct, maxEmpalmesBob, orientBobRack, tipoEmpaqBob, etiquetado, pesarProduct,psoNtoBob)
		VALUES (
			'lñlñ',          -- idCodPrdc: Debe existir en la tabla FichaTec
			'Estructura A',  -- estructProduct: Valor no nulo
			'5',             -- maxEmpalmesBob: Valor no nulo
			'Vertical',      -- orientBobRack: Valor no nulo
			'Empaque A',     -- tipoEmpaqBob: Valor no nulo
			'Etiqueta B',    -- etiquetado: Valor no nulo
			'Pesado Y',       -- pesarProduct: Valor no nulo
            'Pesado Y'       -- pesarProduct: Valor no nulo
		);
	
    drop Table LAMINADO;
    SELECT * FROM LAMINADO;
	CREATE TABLE LAMINADO(
		idCodPrdc VARCHAR(255),
		estructProduct VARCHAR(255) NOT NULL,
        maxEmpalmesBob int NOT NULL,
        orientBobRack VARCHAR(50) NOT NULL,
        tipoEmpaqBob VARCHAR(50) NOT NULL,
        etiquetado VARCHAR(50) NOT NULL,
        pesarProduct VARCHAR(50) NOT NULL,
        psoNtoBob  VARCHAR(50) NOT NULL,
		FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
  

		drop table Material_Impreso;
		 /*Material Impreso*/
        CREATE TABLE Material_Impreso(
            idCodPrdc VARCHAR(255),
            tipoTratado VARCHAR(50) NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );
			/*Calibre de pelicula y Tolerancia*/
			CREATE TABLE CalibrePelic_Tolr(
				idCodPrdc VARCHAR(255),
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Impreso(idCodPrdc) ON DELETE CASCADE
			);
        
			/*Ancho de Bobina y Tolerancia*/
/*---CREAR TABLAS DE PREOCESOS*/
show databases;
use dbingbf;
create database dbingbf;

show databases;

DROP DATABASE dbingbf;

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

drop table impresion;



	/*--crear bd--*/
create database dbIngBF;
use dbIngBF;

show tables;
/*tabalas*/

/*------------------------ficja encabezado------------------------------*/

						/*------ INSERCIÓNES A LA BASE DE DATOS ----------*/
                        
/*--------FichaTec--------*/
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2334','Reyma','Envaces desechables','03/07/2024','03/07/2024');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2335','Fresno','granos','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2336','Waltmart','herramientas','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2337','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2338','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2339','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2340','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2341','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2342','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2343','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2344','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2345','pounch','comina','03/07/2024','SS');
INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES ('E-2346','pounch','comina','03/07/2024','SS');

/*--------VENTAS--------*/
INSERT INTO VENTAS(idCodPrdc,asesor,tipo_Empaque,product_Laminado,estruct_Product,empaca) VALUES ('E-2334','rr','rr','rr','rr','rr');

/*--------EXTRUSIÓN--------*/
select * from EXTRUSION;
INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada,numBobTam)
 VALUES ('E-2334','rr','rr','rr','rr','rr','qe',10,'qe','qe','qe','qe',88,'qe','qe',0);

INSERT INTO CalibrePel_Tolr(idCodPrdc,calibre,tolerancia) VALUES  ('E-2334',30,40);

INSERT INTO AnchoBob_Tolr(idCodPrdc,anchoBob,tolerancia) VALUES ('E-2334',30,40);

INSERT INTO AnchoCore_Tolr(idCodPrdc,anchoCore,tolerancia) VALUES ('E-2334',30,40);

INSERT INTO DiametroBob_Tolr(idCodPrdc,diamBob,tolerancia) VALUES ('E-2334',30,40);

INSERT INTO Peso_Prom_Bob(idCodPrdc,pesoBob,tolerancia) VALUES ('E-2334',30,40);

INSERT INTO Num_BobCama_CamTam(idCodPrdc,num_Bob_Cama,camas_Tarima) VALUES ('E-2334',30,40);

INSERT INTO Peso_prom_tarima(idCodPrdc,peso_neto,tolerancia) VALUES ('E-2334',30,40);

/*--------IMPRESIÓN--------*/
INSERT INTO IMPRESION (idCodPrdc,material_Imprimir,dinaje,grosor_Core,desarrolloImpr,rep_Eje,rep_Dessr,cant_TintasImpr,tipoImpr,tipoTintas_Utilizar,tipo_Barniz,figEmbob_Impr,maxEmpalmes,tipoEmpaqBob,orientBob_Tarima,pesarProduct, etiquetado,Num_bob_tarima,tarima_Emplaye,tarima_Flejada)
 VALUES ('E-2335','Papel','300g',0.5,5,3,2,4,'Offset','Tinta UV','Barniz Brillante',1,2,'Caja','Vertical','Peso Neto','Etiqueta A',20,'Envuelta','Flejada');

INSERT INTO vldClr(idCodPrdc,color,tolDelts) VALUES ('E-2121','EW','EW');

INSERT INTO Peso_prom_tarimaImpr(idCodPrdc,pesoNto,tolerancia) VALUES ('E-2335',0,0);

INSERT INTO LAMINADO(idCodPrdc, estructProduct, maxEmpalmesBob, orientBobRack, tipoEmpaqBob, etiquetado, pesarProduct) 
VALUES (
    'qwqw',          -- idCodPrdc: Debe existir en la tabla FichaTec
    'Estructura A',  -- estructProduct: Valor no nulo
    '5',             -- maxEmpalmesBob: Valor no nulo
    'Vertical',      -- orientBobRack: Valor no nulo
    'Empaque A',     -- tipoEmpaqBob: Valor no nulo
    'Etiqueta B',    -- etiquetado: Valor no nulo
    'Pesado Y'       -- pesarProduct: Valor no nulo
);

SELECT * FROM FichaTec;
SELECT * FROM VENTAS;
	# -- TABLA EXTRUSION -- #
SELECT * FROM EXTRUSION;
	SELECT * FROM CalibrePel_Tolr;
	SELECT * FROM AnchoBob_Tolr;
	SELECT * FROM AnchoCore_Tolr;
	SELECT * FROM DiametroBob_Tolr;
	SELECT * FROM Peso_Prom_Bob;
	SELECT * FROM Peso_prom_tarima;
	
    # -- TABLA IMPRESIÓN -- #
SELECT * FROM IMPRESION;
	SELECT * FROM vldClr;
    SELECT * FROM CalMater_Tolr;
    SELECT * FROM AnchoBobImpr_Tolr;
    SELECT * FROM AnchoCore_TolrImpr;
    SELECT * FROM DiamBob_Tolr;
    SELECT * FROM PesoPromBob;
    SELECT * FROM Num_BobCama_CamaTarima;
    SELECT * FROM Peso_prom_tarimaImpr;
    
       # -- TABLA IMPRESIÓN -- #
SELECT * FROM LAMINADO;

/*
SELECT 
	FichaTec.id_codProduct,
    EXTRUSION.tipo_Material,
    EXTRUSION.dinaje,
    EXTRUSION.formula,
    EXTRUSION.pigmento_Pelicula,
    EXTRUSION.tipo_Bobina,
    EXTRUSION.tipo_Tratado,
    EXTRUSION.max_Emplm,
    EXTRUSION.orient_Bob_Tarima,
    EXTRUSION.Tipo_Empq_Bob,
    EXTRUSION.pesar_Prdct,
    EXTRUSION.etiquetado,
    EXTRUSION.num_Bob_Tarima,
	CalibrePel_Tolr.calibre,
	CalibrePel_Tolr.tolerancia,
	AnchoBob_Tolr.anchoBob,
	AnchoBob_Tolr.tolerancia,
	DiametroBob_Tolr.diamBob,
	DiametroBob_Tolr.tolerancia,
	Peso_Prom_Bob.pesoBob,
	Peso_Prom_Bob.tolerancia,
	Num_BobCama_CamTam.num_Bob_Cama,
    Num_BobCama_CamTam.camas_Tarima,
    Peso_prom_tarima.peso_neto,
    Peso_prom_tarima.tolerancia
FROM 
	EXTRUSION
INNER JOIN 
	CalibrePel_Tolr,Peso_prom_tarima ON FichaTec.id_codProduct = VENTAS.idCodPrdc
WHERE 
	FichaTec.id_codProduct = %s; */

/*--------------------------------------------------------------------------------------------------------------------------------------*/
show tables;

/*-----------------------------PRINTD CARD--------------------------------------*/
CREATE TABLE PrindCard(
        idCodPrdc VARCHAR(255),
		prindCrdPdf BLOB NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
    );
    
/*------------------------------------------------------------------------------*/



/*------------------------FICHA TECNICA------------------------------*/
CREATE TABLE FichaTec(
	id_codProduct VARCHAR(255) PRIMARY KEY NOT NULL,
    cliente VARCHAR(255) NOT NULL,
	producto VARCHAR(255) NOT NULL,
    fecha_Elav VARCHAR(255) NOT NULL,
    fecha_Rev VARCHAR(255) NOT NULL
);
/*------------------------VENTAS------------------------------*/
	CREATE TABLE VENTAS(
        idCodPrdc VARCHAR(255),
        asesor  VARCHAR(255) NOT NULL,
        tipo_Empaque VARCHAR(255) NOT NULL,
        product_Laminado VARCHAR(255) NOT NULL,
        estruct_Product VARCHAR(255) NOT NULL,
        empaca VARCHAR(255) NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
    );
    
/*------------------------EXTRUSION------------------------------*/

	select * from EXTRUSION;
    #drop table EXTRUSION; 
    CREATE TABLE EXTRUSION(
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
            idCodPrdc VARCHAR(255),
            calibre VARCHAR(50) NOT NULL,
            tolerancia VARCHAR(50) NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
         
        /*Ancho de Bobina y Tolerancia*/
        drop table AnchoBob_TolrExtr;
        CREATE TABLE AnchoBob_TolrExtr(
            idCodPrdc VARCHAR(255),
            anchoBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
         
        /*Ancho de Core y Tolerancia*/
        drop table AnchoCore_TolrExtr;
        CREATE TABLE AnchoCore_TolrExtr(
			idCodPrdc VARCHAR(255),
            anchoCore float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
		
        /*Diametro de Bobina y Tolerancia*/
        CREATE TABLE DiametroBob_Tolr(
            idCodPrdc VARCHAR(255),
            diamBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
		
        /*Peso promedio por bobina*/
        CREATE TABLE Peso_Prom_Bob(
            idCodPrdc VARCHAR(255),
            pesoBob float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );

        /*Numero de bobinas por cama y camas por tarima*/
        CREATE TABLE Num_BobCama_CamTam(
            idCodPrdc VARCHAR(255),
            num_Bob_Cama int not null,
            camas_Tarima int not null,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
        select * from Peso_prom_tarima;
        drop table Peso_prom_tarimaExtr;
        /*peso neto promedio por tarima*/
        CREATE TABLE Peso_prom_tarimaExtr(
            idCodPrdc VARCHAR(255),
            peso_neto float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES EXTRUSION(idCodPrdc) ON DELETE CASCADE
        );
        
/*------------------------IMPRESION------------------------------*/
	 CREATE TABLE IMPRESION(
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
        tarima_Emplaye VARCHAR(50) NOT NULL,
        tarima_Flejada VARCHAR(50) NOT NULL,
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
    
		/*Validación de color*/
        CREATE TABLE vldClr(
            idCodPrdc VARCHAR(255),
            color VARCHAR(255) not null,
            tolDelts VARCHAR(255) not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
    
		/*Calibre del material y Tolerancia*/
        CREATE TABLE CalMater_Tolr(
            idCodPrdc VARCHAR(255),
            calibre float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
         /*Ancho de bobina a imprimir y tolerancia*/
        CREATE TABLE AnchoBobImpr_Tolr(
			idCodPrdc VARCHAR(255),
            ancho float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
        drop table AnchoCore_Tolr;
        
        /*Ancho de core y tolerancia*/
        CREATE TABLE AnchoCore_TolrImpr(
			idCodPrdc VARCHAR(255),
            ancho_Core float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
            
        /*Diametro de bobina y Tolerancia*/
        CREATE TABLE DiamBob_Tolr(
			idCodPrdc VARCHAR(255),
            diametro float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
        /*Peso neto promedio de bobina*/
        CREATE TABLE PesoPromBob(
			idCodPrdc VARCHAR(255),
            peso float not null,
            tolerancia float not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
          
          drop table Num_BobCama_CamaTarima;
        /*Numero de bobinas por cama y camas por tarima*/
        CREATE TABLE Num_BobCama_CamaTarima(
			idCodPrdc VARCHAR(255),
            numBobCama int not null,
            camaTam int not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
        
		drop table Peso_prom_tarimaImpr;
        /*Peso neto promedio por tarima y tolerancia*/
        CREATE TABLE Peso_prom_tarimaImpr(
			idCodPrdc VARCHAR(255),
            pesoNto int not null,
            tolerancia int not null,
			FOREIGN KEY (idCodPrdc) REFERENCES IMPRESION(idCodPrdc) ON DELETE CASCADE
        );
        
/*------------------------LAMINADO------------------------------*/

	show tables;
	drop table LAMINADO;
    SELECT * FROM LAMINADO;
    
    INSERT INTO LAMINADO(idCodPrdc, estructProduct, maxEmpalmesBob, orientBobRack, tipoEmpaqBob, etiquetado, pesarProduct,psoNtoBob) 
		VALUES (
			'E-2335',          -- idCodPrdc: Debe existir en la tabla FichaTec
			'Estructura A',  -- estructProduct: Valor no nulo
			'5',             -- maxEmpalmesBob: Valor no nulo
			'Vertical',      -- orientBobRack: Valor no nulo
			'Empaque A',     -- tipoEmpaqBob: Valor no nulo
			'Etiqueta B',    -- etiquetado: Valor no nulo
			'Pesado Y',       -- pesarProduct: Valor no nulo
            'Pesado Y'       -- pesarProduct: Valor no nulo
		);
    
	CREATE TABLE LAMINADO(
		idCodPrdc VARCHAR(255),
		estructProduct VARCHAR(255) NOT NULL,
        maxEmpalmesBob int NOT NULL,
        orientBobRack VARCHAR(50) NOT NULL,
        tipoEmpaqBob VARCHAR(50) NOT NULL,
        etiquetado VARCHAR(50) NOT NULL,
        pesarProduct VARCHAR(50) NOT NULL,
        psoNtoBob  VARCHAR(50) NOT NULL,
		FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
    
		drop table Material_Impreso;
		 /*Material Impreso*/
         SELECT * FROM Material_Impreso;

        CREATE TABLE Material_Impreso(
            idCodPrdc VARCHAR(255),
            mtrlImprs VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );
			 SELECT * FROM CalibrePelic_Tolr;
                                             	drop table Material_Laminar_1;

			/*Calibre de pelicula y Tolerancia*/
			CREATE TABLE CalibrePelic_Tolr(
				idCodPrdc VARCHAR(255),
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Impreso(idCodPrdc) ON DELETE CASCADE
			);
			
			SELECT * FROM AnchoBob_TolrMtrl;
			/*Ancho de Bobina y Tolerancia*/
			CREATE TABLE AnchoBob_TolrMtrl(
				idCodPrdc VARCHAR(255),
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Impreso(idCodPrdc) ON DELETE CASCADE
			);
            
        /*Laminación 1*/
        SELECT * FROM Material_Laminar_1;
        CREATE TABLE Material_Laminar_1(
			idCodPrdc VARCHAR(255),
            Material VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
            tipoLamin VARCHAR(50) NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );
        
			/*Ancho de Bobina y Tolerancia Laminación 1*/
			CREATE TABLE CalibrePelic_TolrLam1(
				idCodPrdc VARCHAR(255),
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Laminar_1(idCodPrdc) ON DELETE CASCADE
			);

            
            #SELECT * FROM AnchoBob_TolrLam1;
            /*Ancho de Bobina y Tolerancia Laminación 1*/
			CREATE TABLE AnchoBob_TolrLam1(
				idCodPrdc VARCHAR(255),
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Laminar_1(idCodPrdc) ON DELETE CASCADE
			);
           
		SELECT * FROM Material_Laminar_2;
		/*Laminación 2*/
		 CREATE TABLE Material_Laminar_2(
			idCodPrdc VARCHAR(255),
            Material VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
            tipoLamin VARCHAR(50) NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );
        
			#SELECT * FROM CalibrePelic_TolrLam2;
			/*Ancho de Bobina y Tolerancia Laminación 2*/
			CREATE TABLE CalibrePelic_TolrLam2(
				idCodPrdc VARCHAR(255),
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Laminar_2(idCodPrdc) ON DELETE CASCADE
			);
            
            #SELECT * FROM AnchoBob_TolrLam2;
             /*Ancho de Bobina y Tolerancia Laminación 1*/

			CREATE TABLE AnchoBob_TolrLam2(
				idCodPrdc VARCHAR(255),
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Laminar_2(idCodPrdc) ON DELETE CASCADE
			);
            
		SELECT * FROM Material_Laminar_3;
		/*Laminación 3*/
        drop table Material_Laminar_3;
		 CREATE TABLE Material_Laminar_3(
			idCodPrdc VARCHAR(255),
            Material VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
            tipoLamin VARCHAR(50) NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );
        
			/*Ancho de Bobina y Tolerancia Laminación 2*/
			drop table CalibrePelic_TolrLam3;
			CREATE TABLE CalibrePelic_TolrLam3(
				idCodPrdc VARCHAR(255),
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Laminar_3(idCodPrdc) ON DELETE CASCADE
			);
            
            SELECT * FROM AnchoBob_TolrLam3;
             /*Ancho de Bobina y Tolerancia Laminación 1*/
             drop table AnchoBob_TolrLam3;
			CREATE TABLE AnchoBob_TolrLam3(
				idCodPrdc VARCHAR(255),
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Laminar_3(idCodPrdc) ON DELETE CASCADE
			);
            
		/*Laminación 4*/
		 CREATE TABLE Material_Laminar_4(
			idCodPrdc VARCHAR(255),
            Material VARCHAR(50) NOT NULL,
            tipoTratado VARCHAR(50) NOT NULL,
            tipoLamin VARCHAR(50) NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );
			/*Ancho de Bobina y Tolerancia Laminación 2*/
            select * from CalibrePelic_TolrLam4;
			CREATE TABLE CalibrePelic_TolrLam4(
				idCodPrdc VARCHAR(255),
				calibre float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Laminar_4(idCodPrdc) ON DELETE CASCADE
			);
            
             /*Ancho de Bobina y Tolerancia Laminación 1*/
			CREATE TABLE AnchoBob_TolrLam4(
				idCodPrdc VARCHAR(255),
				anchoBob float NOT NULL,
                tolerancia float NOT NULL,
				FOREIGN KEY (idCodPrdc) REFERENCES Material_Laminar_4(idCodPrdc) ON DELETE CASCADE
			);
            
            	
		/*Medida de la manga para la Transferencia*/
        SELECT * FROM MedidManga;
		CREATE TABLE MedidManga(
            idCodPrdc VARCHAR(255),
            medidaManga float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
		);
        
        /*Ancho de core y Tolerancia*/
        CREATE TABLE AnchoCore_TolrLam(
            idCodPrdc VARCHAR(255),
            anchoCore float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );
        
        /*Diametro y Grosor de core*/
        CREATE TABLE Diametro_GrosCore(
            idCodPrdc VARCHAR(255),
            diametro float NOT NULL,
            grosorCore float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );
	
		SELECT * FROM Diametro_Bob_Tolr;
        /*Diametro de bobina y Tolerancia*/
        CREATE TABLE Diametro_Bob_Tolr(
            idCodPrdc VARCHAR(255),
            diametroBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES LAMINADO(idCodPrdc) ON DELETE CASCADE
        );

/*------------------------REFILADO------------------------------*/


	INSERT INTO REFILADO (idCodPrdc, proceso, acabadoBob, grosorCore, figEmbob_impr, bobinaRefilar, maximo_Empal, señalEmpl, orient_Bob_Tarima, tipo_Empaque, pesar_Prdct, etiquetado, tarima_emplaye, tarima_flejada, numBobTam)
    VALUES ('2323', 'Proceso X', 'Acabado Y', 'Grosor Z', 'Figura A', 'Bobina B', 10, 'Señal C', 'Orientación D', 'Tipo E', 'Sí', 'Etiqueta F', 'Emplaye G', 'Flejada H',24);

	drop table REFILADO;
    show tables;
    select * from REFILADO;
	CREATE TABLE REFILADO(
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
        numBobTam int NOT NULL,
		FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
	);
		/*Ancho final de bobina al refilarse/Doblarse y Tolerancia*/
        select * from AnchoFinalBob_TolrRef;  

		CREATE TABLE AnchoFinalBob_TolrRef( 
            idCodPrdc VARCHAR(255),
			anchoFinalBob float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES REFILADO(idCodPrdc) ON DELETE CASCADE
        );
        
        show tables;
        /*Metros por bobina al refilarse/doblarse y tolerancia*/ 
        CREATE TABLE MetrosBobRefil_Tolr(
			idCodPrdc VARCHAR(255),
			metros float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES REFILADO(idCodPrdc) ON DELETE CASCADE
        );

        /*Diametro de bobina al refilarse/doblarse y tolerancia*/ 
        CREATE TABLE DiamBobRefil_Tolr( 
			idCodPrdc VARCHAR(255),
			diametro float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES REFILADO(idCodPrdc) ON DELETE CASCADE
        );

         /*Peso neto promedio por bobina */ 
        CREATE TABLE PesoNet_Prom_Bob(
			idCodPrdc VARCHAR(255),
			peso float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES REFILADO(idCodPrdc) ON DELETE CASCADE
        );

		/*Numero de bobinas por cama y camas por tarima*/ 
        CREATE TABLE Num_BobCama_CamTamRefil(
			idCodPrdc VARCHAR(255),
			num_Bob_Cama float NOT NULL,
            camas_Tarima float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES REFILADO(idCodPrdc) ON DELETE CASCADE
        );

	
        /*Peso neto promedio por tarima*/
        CREATE TABLE Peso_prom_tarimaRefil(
			idCodPrdc VARCHAR(255),
			pesoNeto float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES REFILADO(idCodPrdc) ON DELETE CASCADE
        );
        
        # Ancho de Core y Tolerancia
        CREATE TABLE anchCre_TolRefil(
			idCodPrdc VARCHAR(255),
			core float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES REFILADO(idCodPrdc) ON DELETE CASCADE
        );
        

	
        
/*------------------------CONVERSION------------------------------*/
	
    select * from CONVERSION;
    drop table CONVERSION;
	CREATE TABLE CONVERSION(
		idCodPrdc VARCHAR(255),  #foreign key
		tipo_Empaque VARCHAR(100) NOT NULL,
        tipoSello VARCHAR(50) NOT NULL,
        tipoAcabado VARCHAR(50) NOT NULL,
        prdctPerf VARCHAR(50) NOT NULL,
        cntPerf int NOT NULL,
        prdctSuaje VARCHAR(50) NOT NULL,
        tipSuaje VARCHAR(50) NOT NULL,
        empcdPrdct VARCHAR(50) NOT NULL,
        cantPzsPacq float NOT NULL,
        tipEmblj VARCHAR(50) NOT NULL,
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
			idCodPrdc VARCHAR(255),
			ancho float NOT NULL,
            alto float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES CONVERSION(idCodPrdc) ON DELETE CASCADE
        );
         select * from NumBlts_CajsCmas_CmasTarim;
         
        /*Numero de bultos o cajas por camas y camas por tarima*/         
        CREATE TABLE NumBlts_CajsCmas_CmasTarim(
			idCodPrdc VARCHAR(255),
			cajasCama float NOT NULL,  
            camasTarima float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES CONVERSION(idCodPrdc) ON DELETE CASCADE
        );
        
        /*Numero de bultos o cajas por camas y camas por tarima*/
        drop table NumBlts_CajsTarim;
        select * from NumBlts_CajsTarim;
        CREATE TABLE NumBlts_CajsTarim(
			idCodPrdc VARCHAR(255),
			num float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES CONVERSION(idCodPrdc) ON DELETE CASCADE
        );
			
		select * from psPromTam;
         CREATE TABLE psPromTam(
			idCodPrdc VARCHAR(255),
			peso float NOT NULL,
            tolerancia float NOT NULL,
			FOREIGN KEY (idCodPrdc) REFERENCES CONVERSION(idCodPrdc) ON DELETE CASCADE
        );