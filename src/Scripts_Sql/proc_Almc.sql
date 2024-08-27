show databases;
use dbingbf;

show tables;
show databases;

SELECT * FROM FICHATEC;
SELECT * FROM VENTAS;
SELECT * FROM EXTRUSION;
SELECT * FROM IMPRESION;

DELETE FROM FichaTec WHERE id_codProduct = "2323";

select * from impresion;
select * from extrusion;
SELECT COUNT(*) FROM INFORMATION_SCHEMA.PROCESSLIST
SHOW PROCESSLIST;
KILL 2310;

SELECT CONCAT('KILL ', id, ';') 
FROM information_schema.processlist 
WHERE user = 'root' 
AND id <> 210;

KILL CONNECTION 1559;

			############## GET ###################

DROP PROCEDURE IF EXISTS getExtrs;

			-- *** EXTRUSIÓN ***
SELECT * FROM extrusion;
DELETE FROM FichaTec WHERE id_codProduct = "232323";

DELIMITER $$
	CREATE PROCEDURE getExtrs(
		IN id_idCodPrdct VARCHAR(255)
	)
	BEGIN 
		-- Iniciar la transacción
		START TRANSACTION;

		SELECT * FROM  extr
	        INNER JOIN CalibrePel_Tolr cltr ON extr.idCodPrdc = cltr.idCodPrdc
            INNER JOIN AnchoBob_TolrExtr anchBob ON extr.idCodPrdc = anchBob.idCodPrdc
            INNER JOIN AnchoCore_TolrExtr anchCor ON extr.idCodPrdc = anchCor.idCodPrdc
            INNER JOIN DiametroBob_Tolr didmBob ON extr.idCodPrdc = didmBob.idCodPrdc
            INNER JOIN Peso_Prom_Bob psPrmBob ON extr.idCodPrdc = psPrmBob.idCodPrdc
            INNER JOIN Num_BobCama_CamTam numBobCam ON extr.idCodPrdc = numBobCam.idCodPrdc
            INNER JOIN Peso_prom_tarimaExtr psPrmTrm ON extr.idCodPrdc = psPrmTrm.idCodPrdc
        WHERE extr.idCodPrdc = id_idCodPrdct;

		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;
    
CALL getExtrs(
	'3333'
)
SELECT * FROM FICHATEC;
			-- *** IMPRESIÓN ***
SELECT * FROM extrusion;
DROP PROCEDURE IF EXISTS getImprs;
select * from impresion;
CALL getImprs(
	'4444'
)
DELIMITER $$
	CREATE PROCEDURE getImprs(
		IN id_idCodPrdct VARCHAR(255)
	)
	BEGIN 
		-- Iniciar la transacción
		START TRANSACTION;

		SELECT * FROM IMPRESION imprs
	        INNER JOIN vldClr vlcl ON imprs.idCodPrdc = vlcl.idCodPrdc
            INNER JOIN CalMater_Tolr clMtr ON imprs.idCodPrdc = clMtr.idCodPrdc
            INNER JOIN AnchoBobImpr_Tolr anchBob ON imprs.idCodPrdc = anchBob.idCodPrdc
            INNER JOIN AnchoCore_TolrImpr anchCr ON imprs.idCodPrdc = anchCr.idCodPrdc
            INNER JOIN DiamBob_Tolr dmBob ON imprs.idCodPrdc = dmBob.idCodPrdc
            INNER JOIN PesoPromBob psPrmB ON imprs.idCodPrdc = psPrmB.idCodPrdc
            INNER JOIN Num_BobCama_CamaTarima numCm ON imprs.idCodPrdc = numCm.idCodPrdc
			INNER JOIN Peso_prom_tarimaImpr psPrmT ON imprs.idCodPrdc = psPrmT.idCodPrdc
		WHERE imprs.idCodPrdc = id_idCodPrdct;

		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;


			-- ############## INSERT ###################

DELETE FROM FichaTec WHERE id_codProduct = '2424';
select * from fichatec;
SELECT * FROM extrusion;
SELECT * FROM impresion;
SELECT * FROM ventas;
DROP PROCEDURE IF EXISTS InsertExtr;

	-- *** FICHA / VENTAS ***
    
DELIMITER $$
	CREATE PROCEDURE InsertFichaVentas(
		IN id_idCodPrdct VARCHAR(255),
		IN cliente VARCHAR(255),
		IN producto VARCHAR(255),
		IN fecha_Elav VARCHAR(255),
		IN fecha_Rev VARCHAR(255),
		IN asesor VARCHAR(255),
		IN tipo_Empaque VARCHAR(255),
		IN product_Laminado VARCHAR(255),
		IN estruct_Product VARCHAR(255),
		IN empaca VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
			# INSER FICHA
			INSERT INTO FichaTec(id_codProduct,cliente,fecha_Elav,fecha_Rev,producto) VALUES (id_idCodPrdct,cliente,fecha_Elav,fecha_Rev,producto);
            # INSERT VENTAS
            INSERT INTO VENTAS(idCodPrdc,asesor,tipo_Empaque,product_Laminado,estruct_Product,empaca) VALUES (id_idCodPrdct,asesor,tipo_Empaque,product_Laminado,estruct_Product,empaca);
		COMMIT;
	END$$
	DELIMITER ;
    
	-- *** EXTRUCIÓN ***	
DELIMITER $$
	CREATE PROCEDURE InsertExtr(
		IN idCodPrdc INT,
		IN tipo_Material VARCHAR(255),				/*EXTRUCIÓN*/
		IN dinaje VARCHAR(255),
		IN formula VARCHAR(255),
		IN pigmento_Pelicula VARCHAR(255),
		IN tipo_Bobina VARCHAR(255),
		IN tipo_Tratado VARCHAR(255),
		IN max_Emplm INT,
		IN orient_Bob_Tarima VARCHAR(255),
		IN Tipo_Empq_Bob VARCHAR(255),
		IN pesar_Prdct VARCHAR(255),
		IN etiquetado VARCHAR(255),
		IN num_Bob_Tarima INT,
		IN tarima_Emplaye VARCHAR(255),
		IN tarima_flejada VARCHAR(255),
		IN calibre DECIMAL(10,2),
		IN tol_calibre DECIMAL(10,2),
		IN anchoBob DECIMAL(10,2),
		IN tol_anchoBob DECIMAL(10,2),
		IN anchoCore DECIMAL(10,2),
		IN tol_anchoCore DECIMAL(10,2),
		IN diamBob DECIMAL(10,2),
		IN tol_diamBob DECIMAL(10,2),
		IN pesoBob DECIMAL(10,2),
		IN tol_pesoBob DECIMAL(10,2),
		IN num_Bob_Cama INT,
		IN camas_Tarima INT,
		IN peso_neto DECIMAL(10,2),
		IN tol_peso_neto DECIMAL(10,2)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;

		-- INSERTA EXTRUSION
		INSERT INTO EXTRUSION(idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada)
            VALUES (idCodPrdc,tipo_Material,dinaje,formula,pigmento_Pelicula,tipo_Bobina,tipo_Tratado,max_Emplm,orient_Bob_Tarima,Tipo_Empq_Bob,pesar_Prdct,etiquetado,num_Bob_Tarima,tarima_Emplaye,tarima_flejada);

		-- INSERTA CalibrePel_Tolr
		INSERT INTO CalibrePel_Tolr(idCodPrdc,calibre,tolerancia)
            VALUES (idCodPrdc,calibre,tol_calibre);

		-- INSERTA AnchoBob_Tolr
		INSERT INTO AnchoBob_TolrExtr(idCodPrdc,anchoBob,tolerancia)
            VALUES (idCodPrdc,anchoBob,tol_anchoBob);

		-- INSERTA AnchoCore_Tolr
		INSERT INTO AnchoCore_TolrExtr(idCodPrdc,anchoCore,tolerancia)
            VALUES (idCodPrdc,anchoCore,tol_anchoCore);

		-- INSERTA DiametroBob_Tolr
		INSERT INTO DiametroBob_Tolr(idCodPrdc,diamBob,tolerancia)
            VALUES (idCodPrdc,diamBob,tol_diamBob);

		-- INSERTA Peso_Prom_Bob
		INSERT INTO Peso_Prom_Bob(idCodPrdc,pesoBob,tolerancia)
            VALUES (idCodPrdc,pesoBob,tol_pesoBob);
        
		-- INSERTA Num_BobCama_CamTam
		INSERT INTO Num_BobCama_CamTam(idCodPrdc,num_Bob_Cama,camas_Tarima)
            VALUES (idCodPrdc,num_Bob_Cama,camas_Tarima);

		-- INSERTA la tabla Peso_prom_tarima
		INSERT INTO Peso_prom_tarimaExtr(idCodPrdc,peso_neto,tolerancia)
            VALUES (idCodPrdc,peso_neto,tol_peso_neto);
        
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;

    # --- USO DEL PRODECIMIENTO ALMACENADO ---- # 
CALL InsertExtr(

	2323,                  -- idCodPrdc
    'PPPPPPPPP',          -- tipo_Material
    'DinajeY',            -- dinaje
    'FormulaZ',           -- formula
    'PigmentoA',          -- pigmento_Pelicula
    'BobinaB',            -- tipo_Bobina
    'TratadoC',           -- tipo_Tratado
    10,                   -- max_Emplm
    'OrientacionD',       -- orient_Bob_Tarima
    'EmpaqueE',           -- Tipo_Empq_Bob
    'Si',                 -- pesar_Prdct
    'EtiquetaF',          -- etiquetado
    5,                    -- num_Bob_Tarima
    'EmplayeG',           -- tarima_Emplaye
    'FlejadaH',           -- tarima_flejada
    0.45,                 -- calibre
    0.05,                 -- tol_calibre
    120.5,                -- anchoBob
    0.5,                  -- tol_anchoBob
    5.5,                  -- anchoCore
    0.2,                  -- tol_anchoCore
    30.5,                 -- diamBob
    0.3,                  -- tol_diamBob
    200.0,                -- pesoBob
    10.0,                 -- tol_pesoBob
    20,                   -- num_Bob_Cama
    3,                    -- camas_Tarima
    500.0,                -- peso_neto
    15.0                 -- tol_peso_neto
);
		        
	-- **** IMPRESIÓN ****

 DROP PROCEDURE IF EXISTS InsertImprs;
 SELECT * FROM IMPRESION;
DELIMITER $$
	CREATE PROCEDURE InsertImprs(
		IN idCodPrdc INT,
		IN material_Imprimir VARCHAR(255),				/*EXTRUCIÓN*/
		IN dinaje VARCHAR(255),
		IN grosor_Core DECIMAL(10,2),
		IN desarrolloImpr INT,
		IN rep_Eje INT,
		IN rep_Dessr INT,
		IN cant_TintasImpr INT,
		IN tipoImpr VARCHAR(255),
		IN tipoTintas_Utilizar VARCHAR(255),
		IN tipo_Barniz VARCHAR(255),
		IN figEmbob_Impr INT,
		IN maxEmpalmes INT,
		IN tipoEmpaqBob VARCHAR(255),
		IN orientBob_Tarima VARCHAR(255),
		IN pesarProduct VARCHAR(255),
		IN etiquetado VARCHAR(255),
		IN Num_bob_tarima INT,
		IN tarima_Emplaye VARCHAR(255),
		IN tarima_Flejada VARCHAR(255),
		IN color VARCHAR(255),
		IN tolDelts VARCHAR(255),
		IN calibre VARCHAR(255),
		IN tol_cal VARCHAR(255),
		IN ancho VARCHAR(255),
		IN tol_ancho VARCHAR(255),
		IN ancho_Core VARCHAR(255),
		IN tol_anchCore VARCHAR(255),
		IN diametro VARCHAR(255),
		IN tol_dim VARCHAR(255),
		IN peso VARCHAR(255),
		IN tol_pso VARCHAR(255),
		IN numBobCama VARCHAR(255),
		IN camaTam VARCHAR(255),
		IN pesoNto VARCHAR(255),
		IN tol_psoNto VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;

		-- INSERTA EXTRUSION
		INSERT INTO IMPRESION (idCodPrdc,material_Imprimir,dinaje,grosor_Core,desarrolloImpr,rep_Eje,rep_Dessr,cant_TintasImpr,tipoImpr,tipoTintas_Utilizar,tipo_Barniz,figEmbob_Impr,maxEmpalmes,tipoEmpaqBob,orientBob_Tarima,pesarProduct, etiquetado,Num_bob_tarima,tarima_Emplaye,tarima_Flejada)
                VALUES (idCodPrdc,material_Imprimir,dinaje,grosor_Core,desarrolloImpr,rep_Eje,rep_Dessr,cant_TintasImpr,tipoImpr,tipoTintas_Utilizar,tipo_Barniz,figEmbob_Impr,maxEmpalmes,tipoEmpaqBob,orientBob_Tarima,pesarProduct,etiquetado,Num_bob_tarima,tarima_Emplaye,tarima_Flejada);

		-- INSERTA VALIDAR COLOR
		INSERT INTO vldClr(idCodPrdc,color,tolDelts)
                VALUES (idCodPrdc,color,tolDelts);

		-- INSERTA CALIBRE_MATERIAL_TOL
		INSERT INTO CalMater_Tolr(idCodPrdc,calibre,tolerancia)
                VALUES (idCodPrdc,calibre,tol_cal);

		-- INSERTA ANCHOBOB_TOL
		INSERT INTO AnchoBobImpr_Tolr(idCodPrdc,ancho,tolerancia)
                VALUES (idCodPrdc,ancho,tol_ancho);

		-- INSERTA ANCHO_CORE_TOL
		INSERT INTO AnchoCore_TolrImpr(idCodPrdc,ancho_Core,tolerancia)
                VALUES (idCodPrdc,ancho_Core,tol_anchCore);

		-- INSERTA Peso_Prom_Bob
		INSERT INTO DiamBob_Tolr(idCodPrdc,diametro,tolerancia)
                VALUES (idCodPrdc,diametro,tol_dim);
        
		-- INSERTA Num_BobCama_CamTam
		INSERT INTO PesoPromBob(idCodPrdc,peso,tolerancia)
                VALUES (idCodPrdc,peso,tol_pso);

		-- INSERTA la tabla Peso_prom_tarima
		INSERT INTO Num_BobCama_CamaTarima(idCodPrdc,numBobCama,camaTam)
                VALUES (idCodPrdc,numBobCama,camaTam);

		-- INSERTA PESO_PROM_TARIMAimpr
		INSERT INTO Peso_prom_tarimaImpr(idCodPrdc,pesoNto,tolerancia)
                VALUES (idCodPrdc,pesoNto,tol_psoNto);
        
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;

			
			############ UPDATES ###################
            
            
# --- UPDATE FICHA / VENTAS ---

DELIMITER $$
	CREATE PROCEDURE UpdateFichaVentas(
		IN cliente VARCHAR(255),
		IN producto VARCHAR(255),
		IN fecha_Elav VARCHAR(255),
		IN fecha_Rev VARCHAR(255),
		IN asesor VARCHAR(255),
		IN tipo_Empaque VARCHAR(255),
		IN product_Laminado VARCHAR(255),
		IN estruct_Product VARCHAR(255),
		IN empaca VARCHAR(255),
        IN id_idCodPrdct VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
        
			# UPDATE FICHA
			UPDATE FichaTec SET
                cliente=cliente,
                fecha_Elav=fecha_Elav,
                fecha_Rev=fecha_Rev,
                producto=producto
            WHERE id_codProduct = id_idCodPrdct;
            
            # UPDATE VENTAS
            UPDATE VENTAS SET
                asesor=asesor,
                tipo_Empaque=tipo_Empaque,
                product_Laminado=product_Laminado,
                estruct_Product=estruct_Product,
                empaca=empaca
            WHERE idCodPrdc = id_idCodPrdct;
		COMMIT;
	END$$
	DELIMITER ;        
            
# --- TRANSACCIÓN EXTRUCIÓN ---
 DROP PROCEDURE IF EXISTS UpdateEtrs;
SET SQL_SAFE_UPDATES = 0;

SELECT * FROM EXTRUSION;
DELIMITER $$
	CREATE PROCEDURE UpdateEtrs(
		IN tipo_Material VARCHAR(255),				/*EXTRUCIÓN*/
		IN dinaje VARCHAR(255),
		IN formula VARCHAR(255),
		IN pigmento_Pelicula VARCHAR(255),
		IN tipo_Bobina VARCHAR(255),
		IN tipo_Tratado VARCHAR(255),
		IN max_Emplm INT,
		IN orient_Bob_Tarima VARCHAR(255),
		IN Tipo_Empq_Bob VARCHAR(255),
		IN pesar_Prdct VARCHAR(255),
		IN etiquetado VARCHAR(255),
		IN num_Bob_Tarima INT,
		IN tarima_Emplaye VARCHAR(255),
		IN tarima_flejada VARCHAR(255),
		IN calibre DECIMAL(10,2),
		IN tol_calibre DECIMAL(10,2),
		IN anchoBob DECIMAL(10,2),
		IN tol_anchoBob DECIMAL(10,2),
		IN anchoCore DECIMAL(10,2),
		IN tol_anchoCore DECIMAL(10,2),
		IN diamBob DECIMAL(10,2),
		IN tol_diamBob DECIMAL(10,2),
		IN pesoBob DECIMAL(10,2),
		IN tol_pesoBob DECIMAL(10,2),
		IN num_Bob_Cama INT,
		IN camas_Tarima INT,
		IN peso_neto DECIMAL(10,2),
		IN tol_peso_neto DECIMAL(10,2),
		IN id_idCodPrdc INT
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;

		-- Actualizar la tabla EXTRUSION
		UPDATE EXTRUSION
		SET tipo_Material = tipo_Material,
			dinaje = dinaje,
			formula = formula,
			pigmento_Pelicula = pigmento_Pelicula,
			tipo_Bobina = tipo_Bobina,
			tipo_Tratado = tipo_Tratado,
			max_Emplm = max_Emplm,
			orient_Bob_Tarima = orient_Bob_Tarima,
			Tipo_Empq_Bob = Tipo_Empq_Bob,
			pesar_Prdct = pesar_Prdct,
			etiquetado = etiquetado,
			num_Bob_Tarima = num_Bob_Tarima,
			tarima_Emplaye = tarima_Emplaye,
			tarima_flejada = tarima_flejada
		WHERE idCodPrdc = id_idCodPrdc;

		-- Actualizar la tabla CalibrePel_Tolr
		UPDATE CalibrePel_Tolr
		SET calibre = calibre,
			tolerancia = tol_calibre
		WHERE idCodPrdc = id_idCodPrdc;

		-- Actualizar la tabla AnchoBob_Tolr
		UPDATE AnchoBob_TolrExtr
		SET anchoBob = anchoBob,
			tolerancia = tol_anchoBob
		WHERE idCodPrdc = id_idCodPrdc;

		-- Actualizar la tabla AnchoCore_Tolr
		UPDATE AnchoCore_TolrExtr
		SET anchoCore = anchoCore,
			tolerancia = tol_anchoCore
		WHERE idCodPrdc = id_idCodPrdc;

		-- Actualizar la tabla DiametroBob_Tolr
		UPDATE DiametroBob_Tolr
		SET diamBob = diamBob,
			tolerancia = tol_diamBob
		WHERE idCodPrdc = id_idCodPrdc;

		-- Actualizar la tabla Peso_Prom_Bob
		UPDATE Peso_Prom_Bob
		SET pesoBob = pesoBob,
			tolerancia = tol_pesoBob
		WHERE idCodPrdc = id_idCodPrdc;
        
		-- Actualizar la tabla Num_BobCama_CamTam
		UPDATE Num_BobCama_CamTam
		SET num_Bob_Cama = num_Bob_Cama,
			camas_Tarima = camas_Tarima
		WHERE idCodPrdc = id_idCodPrdc;

		-- Actualizar la tabla Peso_prom_tarima
		UPDATE Peso_prom_tarimaExtr
		SET peso_neto = peso_neto,
			tolerancia = tol_peso_neto
		WHERE idCodPrdc = id_idCodPrdc;
        
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;

		-- **** IMPRESIÓN ****

DELIMITER $$
	CREATE PROCEDURE UpdateImpr(
		IN material_Imprimir VARCHAR(255),				/*EXTRUCIÓN*/
		IN dinaje VARCHAR(255),
		IN grosor_Core DECIMAL(10,2),
		IN desarrolloImpr INT,
		IN rep_Eje INT,
		IN rep_Dessr INT,
		IN cant_TintasImpr INT,
		IN tipoImpr VARCHAR(255),
		IN tipoTintas_Utilizar VARCHAR(255),
		IN tipo_Barniz VARCHAR(255),
		IN figEmbob_Impr INT,
		IN maxEmpalmes INT,
		IN tipoEmpaqBob VARCHAR(255),
		IN orientBob_Tarima VARCHAR(255),
		IN pesarProduct VARCHAR(255),
		IN etiquetado VARCHAR(255),
		IN Num_bob_tarima INT,
		IN tarima_Emplaye VARCHAR(255),
		IN tarima_Flejada VARCHAR(255),
		IN color VARCHAR(255),
		IN tolDelts VARCHAR(255),
		IN calibre VARCHAR(255),
		IN tol_cal VARCHAR(255),
		IN ancho VARCHAR(255),
		IN tol_ancho VARCHAR(255),
		IN ancho_Core VARCHAR(255),
		IN tol_anchCore VARCHAR(255),
		IN diametro VARCHAR(255),
		IN tol_dim VARCHAR(255),
		IN peso VARCHAR(255),
		IN tol_pso VARCHAR(255),
		IN numBobCama VARCHAR(255),
		IN camaTam VARCHAR(255),
		IN pesoNto VARCHAR(255),
		IN tol_psoNto VARCHAR(255),
		IN id_idCodPrdc INT
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;

		-- ACTUALIZA EXTRUSION
		-- Actualizar la tabla EXTRUSION
		UPDATE IMPRESION
		SET material_Imprimir = material_Imprimir,
			dinaje = dinaje,
			grosor_Core = grosor_Core,
			desarrolloImpr = desarrolloImpr,
			rep_Eje = rep_Eje,
			rep_Dessr = rep_Dessr,
			cant_TintasImpr = cant_TintasImpr,
			tipoImpr = tipoImpr,
			tipoTintas_Utilizar = tipoTintas_Utilizar,
			tipo_Barniz = tipo_Barniz,
			figEmbob_Impr = figEmbob_Impr,
			maxEmpalmes = maxEmpalmes,
			tipoEmpaqBob = tipoEmpaqBob,
			orientBob_Tarima = orientBob_Tarima,
			pesarProduct = pesarProduct,
			etiquetado = etiquetado,
			Num_bob_tarima = Num_bob_tarima,
			tarima_Emplaye = tarima_Emplaye,
			tarima_Flejada = tarima_Flejada
		WHERE id_idCodPrdc = id_idCodPrdc;

		-- ACTUALIZA VALIDAR COLOR
		UPDATE vldClr
		SET color = color,
			tolDelts = tolDelts
		WHERE id_idCodPrdc = id_idCodPrdc;
        

		-- ACTUALIZA CALIBRE_MATERIAL_TOL
		UPDATE CalMater_Tolr
		SET calibre = calibre,
			tolerancia = tol_cal
		WHERE id_idCodPrdc = id_idCodPrdc;

		-- ACTUALIZA ANCHOBOB_TOL
		UPDATE AnchoBobImpr_Tolr
		SET ancho = ancho,
			tolerancia = tol_ancho
		WHERE id_idCodPrdc = id_idCodPrdc;

		-- ACTUALIZA ANCHO_CORE_TOL
		UPDATE AnchoCore_TolrImpr
		SET ancho_Core = ancho_Core,
			tolerancia = tol_anchCore
		WHERE id_idCodPrdc = id_idCodPrdc;

		-- ACTUALIZA DIAMETRO_BOB_TOL
		UPDATE DiamBob_Tolr
		SET diametro = diametro,
			tolerancia = tol_dim
		WHERE id_idCodPrdc = id_idCodPrdc;
        
		-- ACTUALIZA PESO_PROM_BOB
		UPDATE PesoPromBob
		SET peso = peso,
			tolerancia = tol_pso
		WHERE id_idCodPrdc = id_idCodPrdc;

		-- ACTUALIZA NUM_BOB_CAMATAM
		UPDATE Num_BobCama_CamaTarima
		SET numBobCama = numBobCama,
			camaTam = camaTam
		WHERE id_idCodPrdc = id_idCodPrdc;

		-- ACTUALIZA PESO_PROM_TARIMAimpr
		UPDATE Peso_prom_tarimaImpr
		SET pesoNto = pesoNto,
			tolerancia = tol_psoNto
		WHERE id_idCodPrdc = id_idCodPrdc;
        
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;