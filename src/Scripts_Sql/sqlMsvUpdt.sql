	/* --- ACTUALIZACIÓNES MASIVAS --- */
use dbingbf;

SELECT DISTINCT marca
FROM productos;

SELECT * FROM FichaTec;

SET SQL_SAFE_UPDATES = 0;

/* ---------------------------- IMPRECIÓNES DE LAS TABLAS -----------------------------*/
select * from fichatec;
select * from extrusion;

SELECT DISTINCT cliente
FROM FichaTec;

#########################################################################################


/* --- GET TABLE --- */

CALL getExtrs(
	'5656'
);

/* --- ##############  ACTUALIZACIÓN MASIVA DE CADA PROCESO ############################################ ---*/
-- NOTAS : Cada transacción se hace referencia al atribito "CLIENTE", de la tabla padre "FichaTec", para poder hacer el WHERE en cada tabla

-- /////////////////////////// FICHA / VENTAS ///////////////////////////////////////////////////////////////////////////////////////////

select * from fichatec;
select * from ventas;
SET SQL_SAFE_UPDATES = 0;

select * from fichatec;

-- PRUEBAS
CALL UpdtMsvFichaVentas_PRU(
    'Asi nomas',      -- producto (se actualiza)
    'N/A',        -- fecha_Elav (se actualiza)
    'QUEDO',        -- fecha_Rev (se actualiza)
    'N/A',       -- asesor (se actualiza)
    'N/A',    -- tipo_Empaque (se actualiza)
    'N/A',-- product_Laminado (se actualiza)
    'JBANDA',     -- estruct_Product (se actualiza)
    'N/A',       -- empaca (se actualiza)
    '2222,3333'            -- ID (id a actualizar)
);


DROP PROCEDURE IF EXISTS UpdtMsvFichaVentas_PRU;


/* ---- ACTUALIZACIÓN MASIVA, PRUEBAS ----- */
 

DELIMITER $$
CREATE PROCEDURE UpdtMsvFichaVentas(
    IN producto VARCHAR(255),
    IN fecha_Elav VARCHAR(255),
    IN fecha_Rev VARCHAR(255),
    IN asesor VARCHAR(255),
    IN tipo_Empaque VARCHAR(255),
    IN product_Laminado VARCHAR(255),
    IN estruct_Product VARCHAR(255),
    IN empaca VARCHAR(255),
    
    IN cliente VARCHAR(255)
)
BEGIN
    -- Iniciar la transacción
    START TRANSACTION;
    
    -- UPDATE FichaTec usando la clave primaria
    UPDATE FichaTec
    SET fecha_Elav = CASE WHEN fecha_Elav <> 'N/A' THEN fecha_Elav ELSE fecha_Elav END,
        fecha_Rev = CASE WHEN fecha_Rev <> 'N/A' THEN fecha_Rev ELSE fecha_Rev END,
        producto = CASE WHEN producto <> 'N/A' THEN producto ELSE producto END
    WHERE cliente = cliente;
    
    -- UPDATE VENTAS con JOIN usando la clave primaria de FichaTec
    UPDATE VENTAS vnts
    INNER JOIN FichaTec ft ON vnts.idCodPrdc = ft.id_codProduct
    SET asesor = CASE WHEN asesor <> 'N/A' THEN asesor ELSE asesor END,
        tipo_Empaque = CASE WHEN tipo_Empaque <> 'N/A' THEN tipo_Empaque ELSE tipo_Empaque END,
        product_Laminado = CASE WHEN product_Laminado <> 'N/A' THEN product_Laminado ELSE product_Laminado END,
        estruct_Product = CASE WHEN estruct_Product <> 'N/A' THEN estruct_Product ELSE estruct_Product END,
        empaca = CASE WHEN empaca <> 'N/A' THEN empaca ELSE empaca END
    WHERE ft.cliente = cliente;
    
    -- Si todo fue exitoso, hacer commit
    COMMIT;
END$$
 DELIMITER ;
 

-- //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

-- /////////////////////////// EXTRUSIÓN ///////////////////////////////////////////////////////////////////////////////////////////

-- INSERCIÓNES DE PRUEBA

-- PRUEBAS
CALL prMsvExtrs(
    'N/A',        -- new_tipo_Material (se actualiza)
    'N/A',                -- new_dinaje (no se actualiza)
    'RE-78',          -- new_formula (se actualiza)
    'N/A',      -- new_pigmento_Pelicula (se actualiza)
    'N/A',      -- new_tipo_Bobina (se actualiza)
    'N/A',         -- new_tipo_Tratado (se actualiza)
	0,                  -- new_max_Emplm (se actualiza)
    'N/A',  -- new_orient_Bob_Tarima (se actualiza)
    'N/A',     -- new_Tipo_Empq_Bob (se actualiza)
    'N/A',                -- new_pesar_Prdct (no se actualiza)
    'N/A',     -- new_etiquetado (se actualiza)
    0,                   -- new_num_Bob_Tarima (se actualiza)
    'N/A',    -- new_tarima_Emplaye (se actualiza)
    'N/A',      -- new_tarima_flejada (se actualiza)
    0.0,
    0.0,
    0.0,
    45.45,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    
    'REYMA'               -- Updt_Cliente (cliente a actualizar)
);

DROP PROCEDURE IF EXISTS UpdtMsvExtrs;

DELIMITER $$
	CREATE PROCEDURE UpdtMsvExtrs(
		IN new_tipo_Material VARCHAR(255),				/*EXTRUCIÓN*/
		IN new_dinaje VARCHAR(255),
		IN new_formula VARCHAR(255),
		IN new_pigmento_Pelicula VARCHAR(255),
		IN new_tipo_Bobina VARCHAR(255),
		IN new_tipo_Tratado VARCHAR(255),
		IN new_max_Emplm INT,
		IN new_orient_Bob_Tarima VARCHAR(255),
		IN new_Tipo_Empq_Bob VARCHAR(255),
		IN new_pesar_Prdct VARCHAR(255),
		IN new_etiquetado VARCHAR(255),
		IN new_num_Bob_Tarima INT,
		IN new_tarima_Emplaye VARCHAR(255),		
		IN new_tarima_flejada VARCHAR(255),		
		
		IN new_calibre 	DECIMAL(10,2),			#	DECIMAL(10,2)
		IN new_tol_calibre 	DECIMAL(10,2),		#	DECIMAL(10,2)
		IN new_anchoBob 	DECIMAL(10,2),			#	DECIMAL(10,2)
		IN new_tol_anchoBob 	DECIMAL(10,2),		#	DECIMAL(10,2)
		IN new_anchoCore 	DECIMAL(10,2),			#	DECIMAL(10,2)
		IN new_tol_anchoCore 	DECIMAL(10,2),		
		IN new_diamBob 	DECIMAL(10,2),
		IN new_tol_diamBob 	DECIMAL(10,2),
		IN new_pesoBob 	DECIMAL(10,2),
		IN new_tol_pesoBob 	DECIMAL(10,2),
		IN new_num_Bob_Cama INT,
		IN new_camas_Tarima INT,
		IN new_peso_neto 	DECIMAL(10,2),
		IN new_tol_peso_neto 	DECIMAL(10,2),

		IN Updt_Cliente VARCHAR(255)			# Nombre del cliente
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
			
		-- Actualizar la tabla EXTRUSION
		UPDATE EXTRUSION extrs   	
		INNER JOIN fichatec ft on extrs.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET tipo_Material = CASE WHEN new_tipo_Material <> 'N/A' THEN new_tipo_Material ELSE tipo_Material END,
			dinaje = CASE WHEN new_dinaje <> 'N/A' THEN new_dinaje ELSE dinaje END,
			formula = CASE WHEN new_formula <> 'N/A' THEN new_formula ELSE formula END,
			pigmento_Pelicula =  CASE WHEN new_pigmento_Pelicula <> 'N/A' THEN new_pigmento_Pelicula ELSE pigmento_Pelicula END,
			tipo_Bobina = CASE WHEN new_tipo_Bobina <> 'N/A' THEN new_tipo_Bobina ELSE tipo_Bobina END,
			tipo_Tratado = CASE WHEN new_tipo_Tratado <> 'N/A' THEN new_tipo_Tratado ELSE tipo_Tratado END,
			max_Emplm = CASE WHEN new_max_Emplm <> 0 THEN new_max_Emplm ELSE max_Emplm END,
			orient_Bob_Tarima = CASE WHEN new_orient_Bob_Tarima <> 'N/A' THEN new_orient_Bob_Tarima ELSE orient_Bob_Tarima END,
			Tipo_Empq_Bob = CASE WHEN new_Tipo_Empq_Bob <> 'N/A' THEN new_Tipo_Empq_Bob ELSE Tipo_Empq_Bob END,
			pesar_Prdct = CASE WHEN new_pesar_Prdct <> 'N/A' THEN new_pesar_Prdct ELSE pesar_Prdct END,
			etiquetado = CASE WHEN new_etiquetado <> 'N/A' THEN new_etiquetado ELSE etiquetado END,
			num_Bob_Tarima = CASE WHEN new_num_Bob_Tarima <> 0 THEN new_num_Bob_Tarima ELSE num_Bob_Tarima END,
			tarima_Emplaye = CASE WHEN new_tarima_Emplaye <> 'N/A' THEN new_tarima_Emplaye ELSE tarima_Emplaye END,
			tarima_flejada = CASE WHEN tarima_flejada <> 'N/A' THEN tarima_flejada ELSE tarima_flejada END
		WHERE ft.cliente = Updt_Cliente;

		-- Actualizar la tabla CalibrePel_Tolr
		UPDATE CalibrePel_Tolr clbPl   	
		INNER JOIN fichatec ft on clbPl.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET calibre = CASE WHEN new_calibre <> 0.0 THEN new_calibre ELSE calibre END,
			tolerancia = CASE WHEN new_tol_calibre <> 0.0 THEN new_tol_calibre ELSE tolerancia END
		WHERE ft.cliente = Updt_Cliente;

		-- Actualizar la tabla AnchoBob_Tolr
		UPDATE AnchoBob_TolrExtr anchBob   	
		INNER JOIN fichatec ft on anchBob.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET anchoBob = CASE WHEN new_anchoBob <> 0.0 THEN new_anchoBob ELSE anchoBob END,
			tolerancia = CASE WHEN new_tol_anchoBob <> 0.0 THEN new_tol_anchoBob ELSE tolerancia END
		WHERE ft.cliente = Updt_Cliente;

		-- Actualizar la tabla AnchoCore_Tolr
		UPDATE AnchoCore_TolrExtr anchCr   	
		INNER JOIN fichatec ft on anchCr.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET anchoCore = CASE WHEN new_anchoCore <> 0.0 THEN new_anchoCore ELSE anchoCore END,
			tolerancia = CASE WHEN new_tol_anchoCore <> 0.0 THEN new_tol_anchoCore ELSE tolerancia END
		WHERE ft.cliente = Updt_Cliente;

		-- Actualizar la tabla DiametroBob_Tolr
		UPDATE DiametroBob_Tolr dmBob   	
		INNER JOIN fichatec ft on dmBob.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET diamBob = CASE WHEN new_diamBob <> 0.0 THEN new_diamBob ELSE diamBob END,
			tolerancia = CASE WHEN new_tol_diamBob <> 0.0 THEN new_tol_diamBob ELSE tolerancia END
		WHERE ft.cliente = Updt_Cliente;

		-- Actualizar la tabla Peso_Prom_Bob
		UPDATE Peso_Prom_Bob psPrmBob   	
		INNER JOIN fichatec ft on psPrmBob.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET pesoBob = CASE WHEN new_pesoBob <> 0.0 THEN new_pesoBob ELSE pesoBob END,
			tolerancia = CASE WHEN new_tol_pesoBob <> 0.0 THEN new_tol_pesoBob ELSE tolerancia END
		WHERE ft.cliente = Updt_Cliente;

		-- Actualizar la tabla Num_BobCama_CamTam
		UPDATE Num_BobCama_CamTam nmBobCm   	
		INNER JOIN fichatec ft on nmBobCm.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET num_Bob_Cama = CASE WHEN new_num_Bob_Cama <> 0.0 THEN new_num_Bob_Cama ELSE num_Bob_Cama END,
			camas_Tarima = CASE WHEN new_camas_Tarima <> 0.0 THEN new_camas_Tarima ELSE camas_Tarima END
		WHERE ft.cliente = Updt_Cliente;

		-- Actualizar la tabla Peso_prom_tarima
		UPDATE Peso_prom_tarimaExtr psPrmTam   	
		INNER JOIN fichatec ft on psPrmTam.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET peso_neto = CASE WHEN new_peso_neto <> 0.0 THEN new_peso_neto ELSE peso_neto END,
			tolerancia = CASE WHEN new_tol_peso_neto <> 0.0 THEN new_tol_peso_neto ELSE tolerancia END
		WHERE ft.cliente = Updt_Cliente;

		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
DELIMITER ;
-- //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


-- /////////////////////////// IMPRESION ///////////////////////////////////////////////////////////////////////////////////////////
select * from fichatec;

-- OBSERVAR TABLAS
CALL getImprs(
	'3333'
);

-- PRUEBAS
CALL UpdtMsvImprs(
    'Material para Imprimir',  -- material_Imprimir
    'PP',                  -- dinaje
    0.0,                      -- grosor_Core
    0,                       -- desarrolloImpr
    0,                         -- rep_Eje
    0,                         -- rep_Dessr
    0,                         -- cant_TintasImpr
    'N/A',          -- tipoImpr
    'N/A',                -- tipoTintas_Utilizar
    'N/A',              -- tipo_Barniz
    0,                         -- figEmbob_Impr
    0,                         -- maxEmpalmes
    'N/A',           -- tipoEmpaqBob
    'N/A',               -- orientBob_Tarima
    'N/A',                       -- pesarProduct
    'N/A',        -- etiquetado
    0,                         -- Num_bob_tarima
    'N/A',     -- tarima_Emplaye
    'N/A',           -- tarima_Flejada
    'N/A',                     -- color
    'N/A',                      -- tolDelts
    0.0,               -- calibre
    0.0,                    -- tol_cal
    0.0,                      -- ancho
    0.0,                     -- tol_ancho
    0.0,               -- ancho_Core
    0.0,                     -- tol_anchCore
    0.0,                    -- diametro
    0.0,                    -- tol_dim
    0.0,                   -- peso
    0.0,                    -- tol_pso
    0,                         -- numBobCama
    0,                          -- camaTam
    0,                   -- pesoNto
    0,                   -- tol_psoNto
    'REYMA'                -- Updt_Cliente (nombre del cliente a actualizar)
);


DROP PROCEDURE IF EXISTS UpdtMsvImprs;
DELIMITER $$
	CREATE PROCEDURE UpdtMsvImprs(
		IN material_Imprimir VARCHAR(255),				/*EXTRUCIÓN*/
		IN dinaje VARCHAR(255),
		IN grosor_Core 	DECIMAL(10,2),
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
		IN calibre DECIMAL(10,2),
		IN tol_cal DECIMAL(10,2),
		IN ancho DECIMAL(10,2),
		IN tol_ancho DECIMAL(10,2),
		IN ancho_Core DECIMAL(10,2),
		IN tol_anchCore DECIMAL(10,2),
		IN diametro DECIMAL(10,2),
		IN tol_dim DECIMAL(10,2),
		IN peso DECIMAL(10,2),
		IN tol_pso DECIMAL(10,2),
		IN numBobCama INT,
		IN camaTam INT,
		IN pesoNto INT,
		IN tol_psoNto INT,
        
		IN Updt_Cliente VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;

		-- ACTUALIZA EXTRUSION
		UPDATE IMPRESION imprs   	
		INNER JOIN fichatec ft on imprs.idCodPrdc = ft.id_codProduct
		SET material_Imprimir=CASE WHEN material_Imprimir <> 'N/A' THEN material_Imprimir ELSE material_Imprimir END,
			dinaje = CASE WHEN dinaje <> 'N/A' THEN dinaje ELSE dinaje END,
			grosor_Core = CASE WHEN grosor_Core <> 0.0 THEN grosor_Core ELSE grosor_Core END,
			desarrolloImpr = CASE WHEN desarrolloImpr <> 0 THEN desarrolloImpr ELSE desarrolloImpr END,
			rep_Eje = CASE WHEN rep_Eje <> 0 THEN rep_Eje ELSE rep_Eje END,
			rep_Dessr = CASE WHEN rep_Dessr <> 0 THEN rep_Dessr ELSE rep_Dessr END,
			cant_TintasImpr = CASE WHEN cant_TintasImpr <> 0 THEN cant_TintasImpr ELSE cant_TintasImpr END,
			tipoImpr = CASE WHEN tipoImpr <> 'N/A' THEN tipoImpr ELSE tipoImpr END,
			tipoTintas_Utilizar = CASE WHEN tipoTintas_Utilizar <> 'N/A' THEN tipoTintas_Utilizar ELSE tipoTintas_Utilizar END,
			tipo_Barniz = CASE WHEN tipo_Barniz <> 'N/A' THEN tipo_Barniz ELSE tipo_Barniz END,
			figEmbob_Impr = CASE WHEN figEmbob_Impr <> 0 THEN figEmbob_Impr ELSE figEmbob_Impr END,
			maxEmpalmes = CASE WHEN maxEmpalmes <> 0 THEN maxEmpalmes ELSE maxEmpalmes END,
			tipoEmpaqBob = CASE WHEN tipoEmpaqBob <> 'N/A' THEN tipoEmpaqBob ELSE tipoEmpaqBob END,
			orientBob_Tarima = CASE WHEN orientBob_Tarima <> 'N/A' THEN orientBob_Tarima ELSE orientBob_Tarima END,
			pesarProduct =  CASE WHEN pesarProduct <> 'N/A' THEN pesarProduct ELSE pesarProduct END,
			etiquetado = CASE WHEN etiquetado <> 'N/A' THEN etiquetado ELSE etiquetado END,
			Num_bob_tarima = CASE WHEN Num_bob_tarima <> 0 THEN Num_bob_tarima ELSE Num_bob_tarima END,
			tarima_Emplaye = CASE WHEN tarima_Emplaye <> 'N/A' THEN tarima_Emplaye ELSE tarima_Emplaye END,
			tarima_Flejada = CASE WHEN tarima_Flejada <> 'N/A' THEN tarima_Flejada ELSE tarima_Flejada END
		WHERE ft.cliente = Updt_Cliente;

		-- ACTUALIZA VALIDAR COLOR
		UPDATE vldClr vlc   	
		INNER JOIN fichatec ft on vlc.idCodPrdc = ft.id_codProduct		# TRAEMOS EL ATRIBUTO DE LA CLASE PADRE Y LO REFERENCIAMOS
		SET color = CASE WHEN color <> 'N/A' THEN color ELSE color END,
			tolDelts = CASE WHEN tolDelts <> 'N/A' THEN tolDelts ELSE tolDelts END
		WHERE ft.cliente = Updt_Cliente;
        
		-- ACTUALIZA CALIBRE_MATERIAL_TOL
		UPDATE CalMater_Tolr clm   	
		INNER JOIN fichatec ft on clm.idCodPrdc = ft.id_codProduct	
		SET calibre = CASE WHEN calibre <> 0.0 THEN calibre ELSE calibre END,
			tolerancia = CASE WHEN tol_cal <> 0.0 THEN tol_cal ELSE tol_cal END
		WHERE ft.cliente = Updt_Cliente;

		-- ACTUALIZA ANCHOBOB_TOL
		UPDATE AnchoBobImpr_Tolr anchBobImpr   	
		INNER JOIN fichatec ft on anchBobImpr.idCodPrdc = ft.id_codProduct	
		SET ancho = CASE WHEN ancho <> 0.0 THEN ancho ELSE ancho END,
			tolerancia = CASE WHEN tol_ancho <> 0.0 THEN tol_ancho ELSE tol_ancho END
		WHERE ft.cliente = Updt_Cliente;

		-- ACTUALIZA ANCHO_CORE_TOL
		UPDATE AnchoCore_TolrImpr anchCre   	
		INNER JOIN fichatec ft on anchCre.idCodPrdc = ft.id_codProduct
		SET ancho_Core = CASE WHEN ancho_Core <> 0.0 THEN ancho_Core ELSE ancho_Core END,
			tolerancia = CASE WHEN tol_anchCore <> 0.0 THEN tol_anchCore ELSE tol_anchCore END
		WHERE ft.cliente = Updt_Cliente;

		-- ACTUALIZA DIAMETRO_BOB_TOL

		UPDATE DiamBob_Tolr anchCre   	
		INNER JOIN fichatec ft on anchCre.idCodPrdc = ft.id_codProduct
		SET diametro = CASE WHEN diametro <> 0.0 THEN diametro ELSE diametro END,
			tolerancia = CASE WHEN tol_dim <> 0.0 THEN tol_dim ELSE tol_dim END
		WHERE ft.cliente = Updt_Cliente;
        
		-- ACTUALIZA PESO_PROM_BOB
		UPDATE PesoPromBob psPrmBob   	
		INNER JOIN fichatec ft on psPrmBob.idCodPrdc = ft.id_codProduct
		SET peso = CASE WHEN peso <> 0.0 THEN peso ELSE peso END,
			tolerancia = CASE WHEN tol_pso <> 0.0 THEN tol_pso ELSE tol_pso END
		WHERE ft.cliente = Updt_Cliente;

		-- ACTUALIZA NUM_BOB_CAMATAM
		UPDATE Num_BobCama_CamaTarima nmBobCm   	
		INNER JOIN fichatec ft on nmBobCm.idCodPrdc = ft.id_codProduct
		SET numBobCama = CASE WHEN numBobCama <> 0 THEN numBobCama ELSE numBobCama END,
			camaTam = CASE WHEN camaTam <> 0 THEN camaTam ELSE camaTam END
		WHERE ft.cliente = Updt_Cliente;

		-- ACTUALIZA PESO_PROM_TARIMAimpr
		UPDATE Peso_prom_tarimaImpr psPrmTrm   	
		INNER JOIN fichatec ft on psPrmTrm.idCodPrdc = ft.id_codProduct
		SET pesoNto = CASE WHEN pesoNto <> 0 THEN pesoNto ELSE pesoNto END,
			tolerancia = CASE WHEN tol_psoNto <> 0 THEN tol_psoNto ELSE tol_psoNto END
		WHERE ft.cliente = Updt_Cliente;
        
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
 DELIMITER ;

-- //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


-- /////////////////////////// LAMINADO ///////////////////////////////////////////////////////////////////////////////////////////
	/* -- laminado general --*/

DROP PROCEDURE IF EXISTS UpdtMsvLamGen;
-- OBSERVACIÓNES
select * from LAMINADO;

-- OBSERVACIÓNES
CALL getLamGen(
	'2222'
);

-- PRUEBAS
CALL UpdtMsvLamGen(
    'ACTUALIZACIÓNES',      -- estructProduct
    0,                          -- maxEmpalmesBob
    'N/A',         -- orientBobRack
    'N/A',             -- tipoEmpaqBob
    'N/A',               -- etiquetado
    'N/A',            -- pesarProduct
    'N/A',                -- psoNtoBob
    0,                      -- medidaManga
    0,                       -- tol_Mng
    0,                       -- anchoCore
    0,                        -- tol_anchCore
    0,                       -- diametro
    0,                        -- grosorCore
    0,                       -- diametroBob
    0,                        -- tol_diamBob
    'N/A',         -- mtrlImprs
    'ACTUALIZACIÓNES',             -- tipoTratado
    0,                       -- calibre
    0,                        -- tol_cal
    70,                      -- anchoBob
    40,                        -- tol_bob
    
    'REYMA'                   -- Updt_Cliente
);

DELIMITER $$
	CREATE PROCEDURE UpdtMsvLamGen(			-- Update Masivo de Laminación general
		IN estructProduct VARCHAR(255),
		IN maxEmpalmesBob INT,
		IN orientBobRack VARCHAR(255),
		IN tipoEmpaqBob VARCHAR(255),
		IN etiquetado VARCHAR(255),
		IN pesarProduct VARCHAR(255),
		IN psoNtoBob VARCHAR(255),
		IN medidaManga 	DECIMAL(10,2),
		IN tol_Mng 	DECIMAL(10,2),
		IN anchoCore 	DECIMAL(10,2),
		IN tol_anchCore 	DECIMAL(10,2),
		IN diametro 	DECIMAL(10,2),
		IN grosorCore 	DECIMAL(10,2),
		IN diametroBob 	DECIMAL(10,2),
		IN tol_diamBob 	DECIMAL(10,2),	-- 15

		IN mtrlImprs VARCHAR(255),			-- MATERIAL IMPRESO
		IN tipoTratado VARCHAR(255),

			IN calibre 	DECIMAL(10,2),		-- Calibre de pelicula y Tolerancia	
			IN tol_cal  	DECIMAL(10,2),
	
			IN anchoBob  	DECIMAL(10,2),		-- Ancho de Bobina y Tolerancia
			IN tol_bob  	DECIMAL(10,2),
			
		IN Updt_Cliente VARCHAR(255)					-- id para wl WHERE
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
        
        -- Actualizar la tabla LAMINADO GENERAL
		UPDATE LAMINADO lmn   	
		INNER JOIN fichatec ft on lmn.idCodPrdc = ft.id_codProduct	
		SET estructProduct = CASE WHEN estructProduct <> 'N/A' THEN estructProduct ELSE estructProduct END,
			maxEmpalmesBob = CASE WHEN maxEmpalmesBob <> 0 THEN maxEmpalmesBob ELSE maxEmpalmesBob END,
			orientBobRack = CASE WHEN orientBobRack <> 'N/A' THEN orientBobRack ELSE orientBobRack END,
			tipoEmpaqBob = CASE WHEN tipoEmpaqBob <> 'N/A' THEN tipoEmpaqBob ELSE tipoEmpaqBob END,
			etiquetado = CASE WHEN etiquetado <> 'N/A' THEN etiquetado ELSE etiquetado END,
			pesarProduct = CASE WHEN pesarProduct <> 'N/A' THEN pesarProduct ELSE pesarProduct END,
			psoNtoBob = CASE WHEN psoNtoBob <> 'N/A' THEN psoNtoBob ELSE psoNtoBob END 
		WHERE ft.cliente = Updt_Cliente;

         -- Actualizar la tabla MedidManga
		UPDATE MedidManga mng 	
		INNER JOIN fichatec ft on mng.idCodPrdc = ft.id_codProduct	
		SET medidaManga = CASE WHEN medidaManga <> 0.0 THEN medidaManga ELSE medidaManga END,
			tolerancia = CASE WHEN tol_Mng <> 0.0 THEN tol_Mng ELSE tol_Mng END
		WHERE ft.cliente = Updt_Cliente;

         -- Actualizar la tabla AnchoCore_TolrLam
		UPDATE AnchoCore_TolrLam anchCr 	
		INNER JOIN fichatec ft on anchCr.idCodPrdc = ft.id_codProduct
		SET anchoCore = CASE WHEN anchoCore <> 0.0 THEN anchoCore ELSE tol_Mng END,
			tolerancia = CASE WHEN tol_anchCore <> 0.0 THEN tol_anchCore ELSE tol_anchCore END
		WHERE ft.cliente = Updt_Cliente;
        
		-- Actualizar la tabla Diametro_GrosCore
		UPDATE Diametro_GrosCore dmGrs 	
		INNER JOIN fichatec ft on dmGrs.idCodPrdc = ft.id_codProduct
        SET diametro = CASE WHEN diametro <> 0.0 THEN diametro ELSE diametro END,
			grosorCore = CASE WHEN grosorCore <> 0.0 THEN grosorCore ELSE grosorCore END
		WHERE ft.cliente = Updt_Cliente;
        
		-- Actualizar la tabla Diametro_Bob_Tolr
		UPDATE Diametro_Bob_Tolr dmBob 	
		INNER JOIN fichatec ft on dmBob.idCodPrdc = ft.id_codProduct
		SET diametroBob = CASE WHEN diametroBob <> 0.0 THEN diametroBob ELSE diametroBob END,
			tolerancia = CASE WHEN tol_diamBob <> 0.0 THEN tol_diamBob ELSE tol_diamBob END
		WHERE ft.cliente = Updt_Cliente;

		-- MATERIAL IMPRESO
		UPDATE Material_Impreso mtlImp 	
		INNER JOIN fichatec ft on mtlImp.idCodPrdc = ft.id_codProduct
		SET mtrlImprs = CASE WHEN mtrlImprs <> 'N/A' THEN mtrlImprs ELSE mtrlImprs END,
			tipoTratado = CASE WHEN tipoTratado <> 'N/A' THEN tipoTratado ELSE tipoTratado END
		WHERE ft.cliente = Updt_Cliente;

		UPDATE CalibrePelic_Tolr clbr 	
		INNER JOIN fichatec ft on clbr.idCodPrdc = ft.id_codProduct
		SET calibre = CASE WHEN calibre <> 0.0 THEN calibre ELSE calibre END,
			tolerancia = CASE WHEN tol_cal <> 0.0 THEN tol_cal ELSE tol_cal END
		WHERE ft.cliente = Updt_Cliente;
        
		UPDATE AnchoBob_TolrMtrl anchBob 	
		INNER JOIN fichatec ft on anchBob.idCodPrdc = ft.id_codProduct
		SET anchoBob = CASE WHEN anchoBob <> 0.0 THEN anchoBob ELSE anchoBob END,
			tolerancia =  CASE WHEN tol_bob <> 0.0 THEN tol_bob ELSE tol_bob END
		WHERE ft.cliente = Updt_Cliente;

		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
DELIMITER ;

/* ------------------------------------------------------------------------------------------------------------------------------ */

		/* -- MATERIALES LAMINAR -- */
-- OBSERVACIÓNES
CALL getLmns(
	'2222'
);

-- PRUEBAS
CALL UpdtMsvLaminas(
    'PANCH0',          -- Mtrl_1
    'N/A',           -- tipoTratado_1
    'N/A',          -- tipoLamin_1
    0.0,                 -- cal_1
    0.0,                  -- tol_cal_1
    0.0,                -- anchoBob_1
    0.0,                  -- tol_bob_1

    'PANCH0',          -- Mtrl_2
    'N/A',           -- tipoTratado_2
    'N/A',          -- tipoLamin_2
    0.0,                 -- cal_2
    0.0,                  -- tol_cal_2
    0.0,                -- anchoBob_2
    0.0,                  -- tol_bob_2

    'PANCH0',          -- Mtrl_3
    'N/A',           -- tipoTratado_3
    'N/A',          -- tipoLamin_3
    0.0,                 -- cal_3
    0.0,                  -- tol_cal_3
    0.0,                -- anchoBob_3
    0.0,                  -- tol_bob_3

    'PANCH0',          -- Mtrl_4
    'N/A',           -- tipoTratado_4
    'N/A',          -- tipoLamin_4
    0.0,                 -- cal_4
    0.0,                  -- tol_cal_4
    0.0,                -- anchoBob_4
    34.45,                  -- tol_bob_4

    'REYMA'           -- Updt_Cliente
);

 DROP PROCEDURE IF EXISTS UpdtMsvLaminas;

DELIMITER $$
	CREATE PROCEDURE UpdtMsvLaminas(			-- Update masivo de Materiales ha laminar
		IN Mtrl_1 VARCHAR(255),
		IN tipoTratado_1 VARCHAR(255),
		IN tipoLamin_1 VARCHAR(255),

			IN cal_1 	DECIMAL(10,2),
			IN tol_cal_1 	DECIMAL(10,2),

			IN anchoBob_1 	DECIMAL(10,2),
			IN tol_bob_1 	DECIMAL(10,2),

		IN Mtrl_2 VARCHAR(255),			-- Material_Laminar_2
		IN tipoTratado_2 VARCHAR(255),
		IN tipoLamin_2 VARCHAR(255),

			IN cal_2 	DECIMAL(10,2),
			IN tol_cal_2 	DECIMAL(10,2),

			IN anchoBob_2 	DECIMAL(10,2),
			IN tol_bob_2 	DECIMAL(10,2),

		IN Mtrl_3 VARCHAR(255),			-- Material_Laminar_3
		IN tipoTratado_3 VARCHAR(255),
		IN tipoLamin_3 VARCHAR(255),

			IN cal_3 	DECIMAL(10,2),
			IN tol_cal_3 	DECIMAL(10,2),

			IN anchoBob_3 	DECIMAL(10,2),
			IN tol_bob_3 	DECIMAL(10,2),

		IN Mtrl_4 VARCHAR(255),			-- Material_Laminar_4
		IN tipoTratado_4 VARCHAR(255),
		IN tipoLamin_4 VARCHAR(255),

			IN cal_4 	DECIMAL(10,2),
			IN tol_cal_4 	DECIMAL(10,2),

			IN anchoBob_4 	DECIMAL(10,2),
			IN tol_bob_4 	DECIMAL(10,2),
		
		IN Updt_Cliente VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
		
		-- Material_Laminar_1
		UPDATE Material_Laminar_1 mt1   	
		INNER JOIN fichatec ft on mt1.idCodPrdc = ft.id_codProduct			
		SET Material = CASE WHEN Mtrl_1 <> 'N/A' THEN Mtrl_1 ELSE Mtrl_1 END,
			tipoTratado = CASE WHEN tipoTratado_1 <> 'N/A' THEN tipoTratado_1 ELSE tipoTratado_1 END,
			tipoLamin =  CASE WHEN tipoLamin_1 <> 'N/A' THEN tipoLamin_1 ELSE tipoLamin_1 END
		WHERE ft.cliente = Updt_Cliente;

			UPDATE CalibrePelic_TolrLam1 clbPl1   	
			INNER JOIN fichatec ft on clbPl1.idCodPrdc = ft.id_codProduct	
			SET calibre = CASE WHEN cal_1 <> 0.0 THEN cal_1 ELSE cal_1 END,
				tolerancia =  CASE WHEN tol_cal_1 <> 0.0 THEN tol_cal_1 ELSE tol_cal_1 END
			WHERE ft.cliente = Updt_Cliente;

			UPDATE AnchoBob_TolrLam1 anchBob1   	
			INNER JOIN fichatec ft on anchBob1.idCodPrdc = ft.id_codProduct	
			SET anchoBob =  CASE WHEN anchoBob_1 <> 0.0 THEN anchoBob_1 ELSE anchoBob_1 END,
				tolerancia =  CASE WHEN tol_bob_1 <> 0.0 THEN tol_bob_1 ELSE tol_bob_1 END
			WHERE ft.cliente = Updt_Cliente;

		-- Material_Laminar_2
		UPDATE Material_Laminar_2 mt2   	
		INNER JOIN fichatec ft on mt2.idCodPrdc = ft.id_codProduct			
		SET Material = CASE WHEN Mtrl_2 <> 'N/A' THEN Mtrl_2 ELSE Mtrl_2 END,
			tipoTratado = CASE WHEN tipoTratado_2 <> 'N/A' THEN tipoTratado_2 ELSE tipoTratado_2 END,
			tipoLamin =  CASE WHEN tipoLamin_2 <> 'N/A' THEN tipoLamin_2 ELSE tipoLamin_2 END
		WHERE ft.cliente = Updt_Cliente;

			UPDATE CalibrePelic_TolrLam2 clbPl2   	
			INNER JOIN fichatec ft on clbPl2.idCodPrdc = ft.id_codProduct	
			SET calibre = CASE WHEN cal_2 <> 0.0 THEN cal_2 ELSE cal_2 END,
				tolerancia =  CASE WHEN tol_cal_2 <> 0.0 THEN tol_cal_2 ELSE tol_cal_2 END
			WHERE ft.cliente = Updt_Cliente;

			UPDATE AnchoBob_TolrLam2 anchBob2   	
			INNER JOIN fichatec ft on anchBob2.idCodPrdc = ft.id_codProduct	
			SET anchoBob =  CASE WHEN anchoBob_2 <> 0.0 THEN anchoBob_2 ELSE anchoBob_2 END,
				tolerancia = CASE WHEN tol_bob_2 <> 0.0 THEN tol_bob_2 ELSE tol_bob_2 END
			WHERE ft.cliente = Updt_Cliente;

		-- Material_Laminar_3	
		UPDATE Material_Laminar_3 mt3   	
		INNER JOIN fichatec ft on mt3.idCodPrdc = ft.id_codProduct			
		SET Material = CASE WHEN Mtrl_3 <> 'N/A' THEN Mtrl_3 ELSE Mtrl_3 END,
			tipoTratado = CASE WHEN tipoTratado_3 <> 'N/A' THEN tipoTratado_3 ELSE tipoTratado_3 END,
			tipoLamin =  CASE WHEN tipoLamin_3 <> 'N/A' THEN tipoLamin_3 ELSE tipoLamin_3 END
		WHERE ft.cliente = Updt_Cliente;

			UPDATE CalibrePelic_TolrLam3 clbPl3   	
			INNER JOIN fichatec ft on clbPl3.idCodPrdc = ft.id_codProduct	
			SET calibre = CASE WHEN cal_3 <> 0.0 THEN cal_3 ELSE cal_3 END,
				tolerancia =  CASE WHEN tol_cal_3 <> 0.0 THEN tol_cal_3 ELSE tol_cal_3 END
			WHERE ft.cliente = Updt_Cliente;

			UPDATE AnchoBob_TolrLam3 anchBob3   	
			INNER JOIN fichatec ft on anchBob3.idCodPrdc = ft.id_codProduct	
			SET anchoBob =  CASE WHEN anchoBob_3 <> 0.0 THEN anchoBob_3 ELSE anchoBob_3 END,
				tolerancia = CASE WHEN tol_bob_3 <> 0.0 THEN tol_bob_3 ELSE tol_bob_3 END
			WHERE ft.cliente = Updt_Cliente;

		-- Material_Laminar_4
		UPDATE Material_Laminar_4 mt4   	
		INNER JOIN fichatec ft on mt4.idCodPrdc = ft.id_codProduct			
		SET Material = CASE WHEN Mtrl_4 <> 'N/A' THEN Mtrl_4 ELSE Mtrl_4 END,
			tipoTratado = CASE WHEN tipoTratado_4 <> 'N/A' THEN tipoTratado_4 ELSE tipoTratado_4 END,
			tipoLamin =  CASE WHEN tipoLamin_4 <> 'N/A' THEN tipoLamin_4 ELSE tipoLamin_4 END
		WHERE ft.cliente = Updt_Cliente;

			UPDATE CalibrePelic_TolrLam4 clbPl4   	
			INNER JOIN fichatec ft on clbPl4.idCodPrdc = ft.id_codProduct	
			SET calibre = CASE WHEN cal_4 <> 0.0 THEN cal_4 ELSE cal_4 END,
				tolerancia =  CASE WHEN tol_cal_4 <> 0.0 THEN tol_cal_4 ELSE tol_cal_4 END
			WHERE ft.cliente = Updt_Cliente;

			UPDATE AnchoBob_TolrLam4 anchBob4   	
			INNER JOIN fichatec ft on anchBob4.idCodPrdc = ft.id_codProduct	
			SET anchoBob =  CASE WHEN anchoBob_4 <> 0.0 THEN anchoBob_4 ELSE anchoBob_4 END,
				tolerancia = CASE WHEN tol_bob_4 <> 0.0 THEN tol_bob_4 ELSE tol_bob_4 END
			WHERE ft.cliente = Updt_Cliente;
		

		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;

-- //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

-- /////////////////////////// REFILADO ///////////////////////////////////////////////////////////////////////////////////////////

		-- CALL PARA PRUEBAS
CALL UpdtMsvRefil(
    'EJEMPLO ALV',          -- proceso
    'N/A',          -- acabadoBob
    'N/A',           -- grosorCore
    'N/A',         -- figEmbob_impr
    'JIJI',           -- bobinaRefilar
    222,                   -- maximo_Empal
    'N/A',            -- señalEmpl
    'N/A',      -- orient_Bob_Tarima
    'N/A',      -- tipo_Empaque
    'N/A',            -- pesar_Prdct
    'N/A',       -- etiquetado
    'N/A',    -- tarima_emplaye
    'N/A',    -- tarima_flejada
    0,                  -- numBobTam
    0,              -- anchoFinalBob
    0,                -- tol_anchoBob
    0,              -- metros
    0,                -- tol_Mtrs
    0,               -- diametro
    0,                -- tol_dim
    0,              -- peso
    0,               -- tol_pso
    0,                -- num_Bob_Cama
    0,                -- camas_Tarima
    0,             -- pesoNeto
    0,               -- tol_psNto
    24.5,                -- core
    24.5,                -- tol_core
    'REYMA'           -- Updt_Cliente
);

select * from refilado;
		-- CALL QUE MUESTRA TODOS LOS ATRIBUTOS DEL PROCESO
CALL getRefil(
	'1111'
);


 DROP PROCEDURE IF EXISTS UpdtMsvRefil;
	-- REFILADO
DELIMITER $$
	CREATE PROCEDURE UpdtMsvRefil(
		IN proceso VARCHAR(255),
		IN acabadoBob VARCHAR(255),
		IN grosorCore VARCHAR(255),
		IN figEmbob_impr VARCHAR(255),
		IN bobinaRefilar VARCHAR(255),
		IN maximo_Empal INT,
		IN señalEmpl VARCHAR(255),
		IN orient_Bob_Tarima VARCHAR(255),
		IN tipo_Empaque VARCHAR(255),
		IN pesar_Prdct VARCHAR(255),
		IN etiquetado VARCHAR(255),
		IN tarima_emplaye VARCHAR(255),
		IN tarima_flejada VARCHAR(255),
		IN numBobTam INT,

		IN anchoFinalBob 	DECIMAL(10,2),
		IN tol_anchoBob 	DECIMAL(10,2),

		IN metros 	DECIMAL(10,2),
		IN tol_Mtrs 	DECIMAL(10,2),

		IN diametro 	DECIMAL(10,2),
		IN tol_dim 	DECIMAL(10,2),

		IN peso 	DECIMAL(10,2),
		IN tol_pso 	DECIMAL(10,2),

		IN num_Bob_Cama 	DECIMAL(10,2),
		IN camas_Tarima 	DECIMAL(10,2),

		IN pesoNeto 	DECIMAL(10,2),
		IN tol_psNto 	DECIMAL(10,2),

		IN core 	DECIMAL(10,2),
		IN tol_core 	DECIMAL(10,2),

		IN Updt_Cliente VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
			-- REFILADO
			UPDATE REFILADO ref   	
			INNER JOIN fichatec ft on ref.idCodPrdc = ft.id_codProduct
			SET proceso = CASE WHEN proceso <> 'N/A' THEN proceso ELSE proceso END,
				acabadoBob = CASE WHEN acabadoBob <> 'N/A' THEN acabadoBob ELSE acabadoBob END,
				grosorCore = CASE WHEN grosorCore <> 'N/A' THEN grosorCore ELSE grosorCore END,
				figEmbob_impr = CASE WHEN figEmbob_impr <> 'N/A' THEN figEmbob_impr ELSE figEmbob_impr END,
				bobinaRefilar = CASE WHEN bobinaRefilar <> 'N/A' THEN bobinaRefilar ELSE bobinaRefilar END,
				maximo_Empal = CASE WHEN maximo_Empal <> 0 THEN maximo_Empal ELSE maximo_Empal END,
				señalEmpl = CASE WHEN señalEmpl <> 'N/A' THEN señalEmpl ELSE señalEmpl END,
				orient_Bob_Tarima = CASE WHEN orient_Bob_Tarima <> 'N/A' THEN orient_Bob_Tarima ELSE orient_Bob_Tarima END,
				tipo_Empaque = CASE WHEN tipo_Empaque <> 'N/A' THEN tipo_Empaque ELSE tipo_Empaque END,
				pesar_Prdct = CASE WHEN pesar_Prdct <> 'N/A' THEN pesar_Prdct ELSE pesar_Prdct END,
				etiquetado = CASE WHEN etiquetado <> 'N/A' THEN etiquetado ELSE etiquetado END,
				tarima_emplaye = CASE WHEN tarima_emplaye <> 'N/A' THEN tarima_emplaye ELSE tarima_emplaye END,
				tarima_flejada = CASE WHEN tarima_flejada <> 'N/A' THEN tarima_flejada ELSE tarima_flejada END,
				numBobTam = CASE WHEN numBobTam <> 0 THEN numBobTam ELSE numBobTam END
			WHERE ft.cliente = Updt_Cliente;

			-- Ancho Bobina / Tol
			UPDATE AnchoFinalBob_TolrRef anchFnBob   	
			INNER JOIN fichatec ft on anchFnBob.idCodPrdc = ft.id_codProduct
			SET anchoFinalBob = CASE WHEN anchoFinalBob <> 0.0 THEN anchoFinalBob ELSE anchoFinalBob END,
				tolerancia = CASE WHEN tol_anchoBob <> 0.0 THEN tol_anchoBob ELSE tol_anchoBob END
			WHERE ft.cliente = Updt_Cliente;
			
			-- MetrosBobRefil_Tolr
			UPDATE MetrosBobRefil_Tolr mtrsBbRef   	
			INNER JOIN fichatec ft on mtrsBbRef.idCodPrdc = ft.id_codProduct
			SET metros = CASE WHEN metros <> 0.0 THEN metros ELSE metros END,
				tolerancia = CASE WHEN tol_Mtrs <> 0.0 THEN tol_Mtrs ELSE tol_Mtrs END
			WHERE ft.cliente = Updt_Cliente;

			-- MetrosBobRefil_Tolr
			UPDATE DiamBobRefil_Tolr dmBbRef   	
			INNER JOIN fichatec ft on dmBbRef.idCodPrdc = ft.id_codProduct
			SET diametro = CASE WHEN diametro <> 0.0 THEN diametro ELSE diametro END,
				tolerancia = CASE WHEN tol_dim <> 0.0 THEN tol_dim ELSE tol_dim END
			WHERE ft.cliente = Updt_Cliente;

			-- PesoNet_Prom_Bob
			UPDATE PesoNet_Prom_Bob psNtBb   	
			INNER JOIN fichatec ft on psNtBb.idCodPrdc = ft.id_codProduct
			SET peso = CASE WHEN peso <> 0.0 THEN peso ELSE peso END,
				tolerancia = CASE WHEN tol_pso <> 0.0 THEN tol_pso ELSE tol_pso END
			WHERE ft.cliente = Updt_Cliente;
			
			-- Num_BobCama_CamTamRefil
			UPDATE Num_BobCama_CamTamRefil numBbCm   	
			INNER JOIN fichatec ft on numBbCm.idCodPrdc = ft.id_codProduct
			SET num_Bob_Cama = CASE WHEN num_Bob_Cama <> 0.0 THEN num_Bob_Cama ELSE num_Bob_Cama END,
				camas_Tarima = CASE WHEN camas_Tarima <> 0.0 THEN camas_Tarima ELSE camas_Tarima END
			WHERE ft.cliente = Updt_Cliente;

			-- Peso_prom_tarimaRefil			
			UPDATE Peso_prom_tarimaRefil psPrmTam   	
			INNER JOIN fichatec ft on psPrmTam.idCodPrdc = ft.id_codProduct
			SET pesoNeto = CASE WHEN pesoNeto <> 0.0 THEN pesoNeto ELSE pesoNeto END,
				tolerancia = CASE WHEN tol_psNto <> 0.0 THEN tol_psNto ELSE tol_psNto END
			WHERE ft.cliente = Updt_Cliente;

			-- anchCre_TolRefil
			UPDATE anchCre_TolRefil anchCr  	
			INNER JOIN fichatec ft on anchCr.idCodPrdc = ft.id_codProduct
			SET core = CASE WHEN core <> 0.0 THEN core ELSE core END,
				tolerancia = CASE WHEN tol_core <> 0.0 THEN tol_core ELSE tol_core END
			WHERE ft.cliente = Updt_Cliente;
	
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
DELIMITER ;

-- //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

-- /////////////////////////// CONVERSIÓN ///////////////////////////////////////////////////////////////////////////////////////////

select * from conversion;

-- OBSERVACIÓNES
CALL getConvrs(
	'2222'
);

-- PRUEBAS
CALL UpdtMsvConvrs(
    'ACTUALIZADO',      -- tipo_Empaque
    'N/A',        -- tipoSello
    'ACTUALIZADO',      -- tipoAcabado
    'N/A',-- prdctPerf
    0,                 -- cntPerf
    'N/A',    -- prdctSuaje
    'N/A',        -- tipSuaje
    'N/A', -- empcdPrdct
    0.0,              -- cantPzsPacq
    'N/A',     -- tipEmblj
    0.0,                 -- medidEmblj
    'N/A',    -- pesarProd
    0.0,              -- pesoProm
    'N/A',       -- etiquetado
    'N/A',    -- tarima_Emplaye
    'N/A',    -- tarima_Flejada
    0.0,               -- ancho
    0.0,               -- alto
	0.0,                -- cajasCama
    0.0,               -- camasTarima
    0.0,               -- num
	2.0,                -- tol_num
    0.0,             -- peso
	34.4,                -- tol_pso
    'REYMA'           -- Updt_Cliente
);


DROP PROCEDURE IF EXISTS UpdtMsvConvrs;


DELIMITER $$
	CREATE PROCEDURE UpdtMsvConvrs(
		IN tipo_Empaque VARCHAR(255),
		IN tipoSello VARCHAR(255),
		IN tipoAcabado VARCHAR(255),
		IN prdctPerf VARCHAR(255),
		IN cntPerf INT,
		IN prdctSuaje VARCHAR(255),
		IN tipSuaje VARCHAR(255),
		IN empcdPrdct VARCHAR(255),
		IN cantPzsPacq 	DECIMAL(10,2),
		IN tipEmblj VARCHAR(255),
		IN medidEmblj INT,
		IN pesarProd VARCHAR(255),
		IN pesoProm 	DECIMAL(10,2),
		IN etiquetado VARCHAR(255),
		IN tarima_Emplaye VARCHAR(255),
		IN tarima_Flejada VARCHAR(255),

		/*Medida del empaque Ancho/Alto*/
		IN ancho 	DECIMAL(10,2),
		IN alto 	DECIMAL(10,2),
		/*Numero de bultos o cajas por camas y camas por tarima*/         
		IN cajasCama 	DECIMAL(10,2),
		IN camasTarima 	DECIMAL(10,2),
		/*Numero de bultos o cajas por camas y camas por tarima*/
		IN num 	DECIMAL(10,2),
		IN tol_num 	DECIMAL(10,2),
		/*Peso promedio en tarima*/
		IN peso 	DECIMAL(10,2),
		IN tol_pso 	DECIMAL(10,2),

		IN Updt_Cliente VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
			-- Conversión
			
			UPDATE CONVERSION cnvrs   	
			INNER JOIN fichatec ft on cnvrs.idCodPrdc = ft.id_codProduct
			SET tipo_Empaque = CASE WHEN tipo_Empaque <> 'N/A' THEN tipo_Empaque ELSE tipo_Empaque END,
				tipoSello = CASE WHEN tipoSello <> 'N/A' THEN tipoSello ELSE tipoSello END,
				tipoAcabado = CASE WHEN tipoAcabado <> 'N/A' THEN tipoAcabado ELSE tipoAcabado END,
				prdctPerf = CASE WHEN prdctPerf <> 'N/A' THEN prdctPerf ELSE prdctPerf END,
				cntPerf =  CASE WHEN cntPerf <> 0 THEN cntPerf ELSE cntPerf END,
				prdctSuaje = CASE WHEN prdctSuaje <> 'N/A' THEN prdctSuaje ELSE prdctSuaje END,
				tipSuaje = CASE WHEN tipSuaje <> 'N/A' THEN tipSuaje ELSE tipSuaje END,
				empcdPrdct = CASE WHEN tipEmblj <> 'N/A' THEN tipEmblj ELSE tipEmblj END,
				cantPzsPacq = CASE WHEN cantPzsPacq <> 0.0 THEN cantPzsPacq ELSE cantPzsPacq END,
				tipEmblj = CASE WHEN tipEmblj <> 'N/A' THEN tipEmblj ELSE tipEmblj END,
				medidEmblj = CASE WHEN medidEmblj <> 0 THEN medidEmblj ELSE medidEmblj END,
				pesarProd = CASE WHEN pesarProd <> 'N/A' THEN pesarProd ELSE pesarProd END,
				pesoProm = CASE WHEN pesoProm <> 0.0 THEN pesoProm ELSE pesoProm END,
				etiquetado = CASE WHEN etiquetado <> 'N/A' THEN etiquetado ELSE etiquetado END,
				tarima_Emplaye = CASE WHEN tarima_Emplaye <> 'N/A' THEN tarima_Emplaye ELSE tarima_Emplaye END,
				tarima_Flejada = CASE WHEN tarima_Flejada <> 'N/A' THEN tarima_Flejada ELSE tarima_Flejada END
				WHERE ft.cliente = Updt_Cliente;
			
			-- MedidEmpq
			UPDATE MedidEmpq mdEmpq   	
			INNER JOIN fichatec ft on mdEmpq.idCodPrdc = ft.id_codProduct
			SET ancho = CASE WHEN ancho <> 0.0 THEN ancho ELSE ancho END,
				alto = CASE WHEN alto <> 0.0 THEN alto ELSE alto END
			WHERE ft.cliente = Updt_Cliente;

			-- 	NumBlts_CajsCmas_CmasTarim
			
			UPDATE NumBlts_CajsCmas_CmasTarim cjsCms   	
			INNER JOIN fichatec ft on cjsCms.idCodPrdc = ft.id_codProduct
			SET cajasCama = CASE WHEN cajasCama <> 0.0 THEN cajasCama ELSE cajasCama END,
				camasTarima = CASE WHEN camasTarima <> 0.0 THEN camasTarima ELSE camasTarima END
			WHERE ft.cliente = Updt_Cliente;
            
			-- NumBlts_CajsTarim
			UPDATE NumBlts_CajsTarim nmBltsCjs   	
			INNER JOIN fichatec ft on nmBltsCjs.idCodPrdc = ft.id_codProduct
			SET num = CASE WHEN num <> 0.0 THEN num ELSE num END,
				tolerancia = CASE WHEN tol_num <> 0.0 THEN tol_num ELSE tol_num  END
			WHERE ft.cliente = Updt_Cliente;

			-- psPromTam
			UPDATE psPromTam nmBltsCjs   	
			INNER JOIN fichatec ft on nmBltsCjs.idCodPrdc = ft.id_codProduct
			SET peso = CASE WHEN peso <> 0.0 THEN peso ELSE peso END,
				tolerancia =  CASE WHEN tol_pso <> 0.0 THEN tol_pso ELSE tol_pso END
			WHERE ft.cliente = Updt_Cliente;

		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;

-- //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





