		/*---	QURY´S DE PRUEBAS	---*/
        
show databases;
use dbingbf;
create database dbingbf;

        
/*---------------------------- PRIND CARD ------------------------------------*/

									/*--CREATE TABLE--*/
select * from PrindCardLOCAL;
SELECT prindCrdPdf_URL FROM PrindCardLOCAL WHERE idCodPrdc = '2323'
drop table PrindCardLOCAL;


select * from PrindCardLOCAL;
CREATE TABLE PrindCardLOCAL(
        idCodPrdc VARCHAR(255),
		prindCrdPdf_URL VARCHAR(255),	
        FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
);

INSERT INTO PrindCardLOCAL(idCodPrdc,prindCrdPdf_URL)
VALUES ('1212','file/ytyty.pdf');

 INSERT INTO UrlImgsPdf(idCodPrdc,ExtrsImg,ImprsImg,LamImg,RefImg,CnvsImg)
			VALUES ('1212','12','12','12','12','12');

drop table UrlImgsPdf;
select * from UrlImgsPdf;

SELECT * FROM UrlImgsPdf WHERE idCodPrdc = '2424';
		# TABLAS HIJAS
CREATE TABLE UrlImgsPdf(
		idCodPrdc VARCHAR(255),
		ExtrsImg VARCHAR(255),
		ImprsImg VARCHAR(255),
		LamImg VARCHAR(255),
		RefImg VARCHAR(255),
		CnvsImg VARCHAR(255),
		FOREIGN KEY (idCodPrdc) REFERENCES PrindCardLOCAL(idCodPrdc) ON DELETE CASCADE
);

drop table FigImgPdf;

select * from FigImgPdf;
select * from FigImgPdf;

CREATE TABLE FigImgPdf(		/* ES LA FIGURA O EL "TITULO DE LA IMAGEN" */
		idCodPrdc VARCHAR(255),
		ExtrsFig VARCHAR(255),
		ImprsFig VARCHAR(255),
		LamFig VARCHAR(255),
		RefFig VARCHAR(255),
		CnvsFig VARCHAR(255),
		FOREIGN KEY (idCodPrdc) REFERENCES PrindCardLOCAL(idCodPrdc) ON DELETE CASCADE
);

drop table DescImgPdf;

select * from DescImgPdf;
select * from DescImgPdf;


CREATE TABLE DescImgPdf(		/* DESCRIPCIÓNES DE LA IMAGEN" */
	idCodPrdc VARCHAR(255),
	ExtrsDesc VARCHAR(255),
	ImprsDesc VARCHAR(255),
	LamDesc VARCHAR(255),
	RefDesc VARCHAR(255),
	CnvsDesc VARCHAR(255),
	FOREIGN KEY (idCodPrdc) REFERENCES PrindCardLOCAL(idCodPrdc) ON DELETE CASCADE
);

drop table SecPdf;
CREATE TABLE SecPdf(			/* SECUANCIAS DE PROCESOS PDF */
	idCodPrdc VARCHAR(255),
    sec1 VARCHAR(25),
    sec2 VARCHAR(25),
    sec3 VARCHAR(25),
    sec4 VARCHAR(25),
    sec5 VARCHAR(25),
	FOREIGN KEY (idCodPrdc) REFERENCES FichaTec(id_codProduct) ON DELETE CASCADE
);
        
        /* ------------ PROCEDIMIENTOS ALMACENADOS --------------------------- */
        
						/*--GET--*/

CALL getObsrv(
	'1111'
);

select * from fichatec;

DROP PROCEDURE IF EXISTS getObsrv;

DELIMITER $$
	CREATE PROCEDURE getObsrv(						/* --  GET OBSERVACIÓNES --  */
		IN id_idCodPrdct VARCHAR(255)
	)
	BEGIN 
		START TRANSACTION;

		SELECT * FROM UrlImgsPdf img
	        INNER JOIN FigImgPdf figImg ON img.idCodPrdc = figImg.idCodPrdc
			INNER JOIN DescImgPdf dcImg ON img.idCodPrdc = dcImg.idCodPrdc
		WHERE img.idCodPrdc = id_idCodPrdct;

		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;
        
									/*--INSERT--*/
                                    
DROP PROCEDURE IF EXISTS InsertPrindCardUrl_PRU;

	-- PRIND CARD
    
DELIMITER $$
	CREATE PROCEDURE InsertPrindCardUrl_PRU(
		IN idCodPrdc VARCHAR(255),			-- TABLA PADRE
		IN prindCrdPdf_URL VARCHAR(255),
        
        IN ExtrsImg VARCHAR(255),			-- Url imagenes del pdf
        IN ImprsImg VARCHAR(255),
        IN LamImg VARCHAR(255),
        IN RefImg VARCHAR(255),
        IN CnvsImg VARCHAR(255),	
        
		IN ExtrsFig VARCHAR(255),
        IN ImprsFig VARCHAR(255),
		IN LamFig VARCHAR(255),
		IN RefFig VARCHAR(255),
		IN CnvsFig VARCHAR(255),

		IN ExtrsDesc VARCHAR(255),
		IN ImprsDesc VARCHAR(255),
		IN LamDesc VARCHAR(255),
		IN RefDesc VARCHAR(255),
		IN CnvsDesc VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
			-- prindCrdPdf_URL
			INSERT INTO PrindCardLOCAL(idCodPrdc,prindCrdPdf_URL)
			VALUES (idCodPrdc,prindCrdPdf_URL);
            
            -- UrlImages
            INSERT INTO UrlImgsPdf(idCodPrdc,ExtrsImg,ImprsImg,LamImg,RefImg,CnvsImg)
			VALUES (idCodPrdc,ExtrsImg,ImprsImg,LamImg,RefImg,CnvsImg);
            
             -- figuras PDF
            INSERT INTO FigImgPdf(idCodPrdc,ExtrsFig,ImprsFig,LamFig,RefFig,CnvsFig)
			VALUES (idCodPrdc,ExtrsFig,ImprsFig,LamFig,RefFig,CnvsFig);
            
			-- DESCRIPCIÓN FIGURAS
			INSERT INTO DescImgPdf(idCodPrdc,ExtrsDesc,ImprsDesc,LamDesc,RefDesc,CnvsDesc)
			VALUES (idCodPrdc,ExtrsDesc,ImprsDesc,LamDesc,RefDesc,CnvsDesc);

		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;
    
							/*-- UPDATE --*/
 
DROP PROCEDURE IF EXISTS UpdatePrindCardUrl_PRU;

    	-- PRIND CARD
DELIMITER $$
	CREATE PROCEDURE UpdatePrindCardUrl_PRU(
		IN prindCrdPdf_URL VARCHAR(255),
        
        IN ExtrsImg VARCHAR(255),			-- Url imagenes del pdf
        IN ImprsImg VARCHAR(255),
        IN LamImg VARCHAR(255),
        IN RefImg VARCHAR(255),
        IN CnvsImg VARCHAR(255),	
        
		IN ExtrsFig VARCHAR(255),			-- Texto Numero de Figura
        IN ImprsFig VARCHAR(255),
		IN LamFig VARCHAR(255),
		IN RefFig VARCHAR(255),
		IN CnvsFig VARCHAR(255),

		IN ExtrsDesc VARCHAR(255),			-- Texto Descripciónes
		IN ImprsDesc VARCHAR(255),
		IN LamDesc VARCHAR(255),
		IN RefDesc VARCHAR(255),
		IN CnvsDesc VARCHAR(255),
        
        IN id_idCodPrdct VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
			-- prindCrdPdf_URL
			UPDATE PrindCardLOCAL SET
                prindCrdPdf_URL=prindCrdPdf_URL
            WHERE id_idCodPrdct = id_idCodPrdct;
                   
			-- UrlImages
			UPDATE UrlImgsPdf SET
                ExtrsImg=ExtrsImg,
                ImprsImg=ImprsImg,
                LamImg=LamImg,
                RefImg=RefImg,
                CnvsImg=CnvsImg
            WHERE id_idCodPrdct = id_idCodPrdct;

			-- Numero de Figura
			UPDATE FigImgPdf SET
				ExtrsFig=ExtrsFig,
				ImprsFig=ImprsFig,
				LamFig=LamFig,
				RefFig=RefFig,
				CnvsFig=CnvsFig
			WHERE id_idCodPrdct = id_idCodPrdct;

			-- Descripción del Proceso
			UPDATE DescImgPdf SET
				ExtrsDesc=ExtrsDesc,
				ImprsDesc=ImprsDesc,
				LamDesc=LamDesc,
				RefDesc=RefDesc,
				CnvsDesc=CnvsDesc
			WHERE id_idCodPrdct = id_idCodPrdct;
            
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;
    
    
-- ########## PROCESOS DEL PRIND CARD ######################


select * from secpdf;

select * from fichatec;
CALL InsertSecPdf(
	"1111",
	"1",
    "1",
    "1",
    "1",
    "1"
);
	/*-- INSERT -- */
DELIMITER $$
	CREATE PROCEDURE InsertSecPdf(
		IN idCodPrdc VARCHAR(255),			-- TABLA PADRE
		IN sec1 VARCHAR(25),
        IN sec2 VARCHAR(25),
        IN sec3 VARCHAR(25),
        IN sec4 VARCHAR(25),
        IN sec5 VARCHAR(25)
    )
    BEGIN 
		START TRANSACTION;
			INSERT INTO SecPdf(idCodPrdc,sec1,sec2,sec3,sec4,sec5)
            VALUES (idCodPrdc,sec1,sec1,sec3,sec4,sec5);
		COMMIT;
	END$$
    DELIMITER ; 


	/*-- UPDATE -- */
DELIMITER $$
	CREATE PROCEDURE UpdateSecPdf(
		IN sec1 VARCHAR(25),
        IN sec2 VARCHAR(25),
        IN sec3 VARCHAR(25),
        IN sec4 VARCHAR(25),
        IN sec5 VARCHAR(25),
        
        IN id_idCodPrdct VARCHAR(255)
    )
    BEGIN 
		START TRANSACTION;
			UPDATE SecPdf SET
				sec1=sec1,
                sec2=sec2,
                sec3=sec3,
                sec4=sec4,
                sec5=sec5
			WHERE id_idCodPrdct = id_idCodPrdct;
		COMMIT;
	END$$
    DELIMITER ; 