
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