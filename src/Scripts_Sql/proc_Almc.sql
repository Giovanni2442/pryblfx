show databases;
use dbingbf;

show tables;
show databases;

			############ INSERT ###################
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
            VALUES (idCodPrdc,calibre,tolerancia);

		-- INSERTA AnchoBob_Tolr
		INSERT INTO AnchoBob_TolrExtr(idCodPrdc,anchoBob,tolerancia)
            VALUES (idCodPrdc,anchoBob,tolerancia);

		-- INSERTA AnchoCore_Tolr
		INSERT INTO AnchoCore_TolrExtr(idCodPrdc,anchoCore,tolerancia)
            VALUES (idCodPrdc,anchoCore,tolerancia);

		-- INSERTA DiametroBob_Tolr
		INSERT INTO DiametroBob_Tolr(idCodPrdc,diamBob,tolerancia)
            VALUES (idCodPrdc,diamBob,tolerancia);

		-- INSERTA Peso_Prom_Bob
		INSERT INTO Peso_Prom_Bob(idCodPrdc,pesoBob,tolerancia)
            VALUES (idCodPrdc,pesoBob,tolerancia);
        
		-- INSERTA Num_BobCama_CamTam
		INSERT INTO Num_BobCama_CamTam(idCodPrdc,num_Bob_Cama,camas_Tarima)
            VALUES (idCodPrdc,num_Bob_Cama,camas_Tarima);

		-- INSERTA la tabla Peso_prom_tarima
		INSERT INTO Peso_prom_tarimaExtr(idCodPrdc,peso_neto,tolerancia)
            VALUES (idCodPrdc,peso_neto,tolerancia);
        
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;

SHOW * FROM FICHATEC;
    # --- USO DEL PRODECIMIENTO ALMACENADO ---- # 
CALL InsertExtr(
	66666,                  -- idCodPrdc
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







			############ UPDATES ###################
# --- TRANSACCIÓN EXTRUCIÓN ---
 DROP PROCEDURE IF EXISTS UpdateExtrPru;
SET SQL_SAFE_UPDATES = 0;

SELECT * FROM EXTRUSION;
DELIMITER $$
	CREATE PROCEDURE UpdateExtr(
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

