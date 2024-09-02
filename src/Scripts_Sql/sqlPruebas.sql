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

CREATE TABLE FigImgPdf(		/* ES LA FIGURA O EL "TITULO DE LA IMAGEN" */
		idCodPrdc VARCHAR(255),
		ExtrsFig VARCHAR(255),
		ImprsFig VARCHAR(255),
		LamFig VARCHAR(255),
		RefFig VARCHAR(255),
		CnvsImg VARCHAR(255),
		FOREIGN KEY (idCodPrdc) REFERENCES PrindCardLOCAL(idCodPrdc) ON DELETE CASCADE
);

CREATE TABLE DescImgPdf(		/* DESCRIPCIÓNES DE LA IMAGEN" */
		idCodPrdc VARCHAR(255),
		ExtrsDesc VARCHAR(255),
		ImprsDesc VARCHAR(255),
		LamDesc VARCHAR(255),
		RefDesc VARCHAR(255),
		CnvsDesc VARCHAR(255),
		FOREIGN KEY (idCodPrdc) REFERENCES PrindCardLOCAL(idCodPrdc) ON DELETE CASCADE
);
        
        /* ------------ PROCEDIMIENTOS ALMACENADOS --------------------------- */
        
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
        IN CnvsImg VARCHAR(255)				
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
            
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;
    
							/*-- UPDATE --*/
    
    	-- PRIND CARD
DELIMITER $$
	CREATE PROCEDURE UpdatePrindCardUrl_PRU(
		IN prindCrdPdf_URL VARCHAR(255),
        
        IN ExtrsImg VARCHAR(255),			-- Url imagenes del pdf
        IN ImprsImg VARCHAR(255),
        IN LamImg VARCHAR(255),
        IN RefImg VARCHAR(255),
        IN CnvsImg VARCHAR(255),
        
        IN id_idCodPrdct VARCHAR(255)
	)
	BEGIN										/*INICIO DE LA TRANSACCIÓN EN EL PROCEDIMIENTO*/
		-- Iniciar la transacción
		START TRANSACTION;
			-- prindCrdPdf_URL
            
            # UPDATE prindCrdPdf_URL
			UPDATE PrindCardLOCAL SET
                prindCrdPdf_URL=prindCrdPdf_URL
            WHERE id_codProduct = id_idCodPrdct;
                   
			-- UrlImages
			UPDATE UrlImgsPdf SET
                ExtrsImg=ExtrsImg,
                ImprsImg=ImprsImg,
                LamImg=LamImg,
                RefImg=RefImg,
                CnvsImg=CnvsImg
            WHERE id_codProduct = id_idCodPrdct;
            
		-- Si todo fue exitoso, hacer commit
		COMMIT;
	END$$
	DELIMITER ;
    
