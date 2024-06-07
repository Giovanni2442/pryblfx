/*---Create database dbTienda---*/

create database dbTienda;
use dbTienda;

/*--Eliminar tablas--*/

drop table Calzado;
drop table images;
drop table sizes;
drop table color;
drop table characteristics;
drop table details;

CREATE TABLE Calzado(
	id INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(255),
    cantidad LONG NOT NULL,
    price FLOAT NOT NULL
);

	CREATE TABLE images(
		id INT NOT NULL,
        clzd_id INT,
        url VARCHAR(255) NOT NULL,
        FOREIGN KEY (clzd_id) REFERENCES Calzado(id) ON DELETE CASCADE
    );
    
    CREATE TABLE sizes(
		id INT NOT NULL,
        clzd_id INT,
        size FLOAT NOT NULL,
		FOREIGN KEY (clzd_id) REFERENCES Calzado(id) ON DELETE CASCADE
    );
	
    CREATE TABLE color(
		id INT NOT NULL,
        clzd_id INT,
        color VARCHAR(50),
		FOREIGN KEY (clzd_id) REFERENCES Calzado(id) ON DELETE CASCADE
    );
    
    CREATE TABLE characteristics(
		id INT NOT NULL PRIMARY KEY,
		clzd_id INT,
        category VARCHAR(50),
        sex VARCHAR(20),
        leyend VARCHAR(255),
		FOREIGN KEY (clzd_id) REFERENCES Calzado(id) ON DELETE CASCADE
    );
    
		CREATE TABLE details(
			id INT NOT NULL,
            charc_id INT,
            descript VARCHAR(255),
			FOREIGN KEY (charc_id) REFERENCES characteristics(id) ON DELETE CASCADE
        );
        
        
/*---INSERTAR DATOS DE PRUEBA---*/
        
	/*--CALZADO--*/
INSERT INTO Calzado(id,nombre,cantidad,price) VALUES (1,"Clazado_Prueba",22,33.55);
INSERT INTO images(id,clzd_id,url) VALUES (1,1,"assets/img/calzado.jpeg");
INSERT INTO sizes(id,clzd_id,size) VALUES (1,1,23.5);

INSERT INTO color(id,clzd_id,color) VALUES (1,1,"Red");
INSERT INTO color(id,clzd_id,color) VALUES (2,1,"Red");
INSERT INTO color(id,clzd_id,color) VALUES (3,1,"Blue");
INSERT INTO color(id,clzd_id,color) VALUES (4,1,"Green");

INSERT INTO characteristics(id,clzd_id,category,sex,leyend) VALUES (1,1,"tenis","Male","jijijija");
INSERT INTO details(id,charc_id,descript) VALUES (1,1,"pruebas");

INSERT INTO Calzado(id,nombre,cantidad,price) VALUES (2,"Clazado_Prueba_2",13,13);

INSERT INTO images(id,clzd_id,url) VALUES (1,2,"assets/img/calzado.jpeg");
INSERT INTO images(id,clzd_id,url) VALUES (2,2,"assets/img/calzado.jpeg");
INSERT INTO images(id,clzd_id,url) VALUES (3,2,"assets/img/calzado.jpeg");

INSERT INTO sizes(id,clzd_id,size) VALUES (1,2,23.5);

INSERT INTO color(id,clzd_id,color) VALUES (1,2,"Red");
INSERT INTO color(id,clzd_id,color) VALUES (2,2,"Blue");
INSERT INTO color(id,clzd_id,color) VALUES (1,2,"Green");

INSERT INTO characteristics(id,clzd_id,category,sex,leyend) VALUES (2,2,"tenis","Male","jijijija");
INSERT INTO details(id,charc_id,descript) VALUES (1,2,"pruebas");

/*--SHOWS--*/

SELECT * FROM color;

	/*--TABLE CALZADO--*/
SELECT 
 JSON_OBJECT(
	'id',clz.id,
    'nombre',clz.nombre,
    'cantidad',clz.cantidad,
    'price',clz.price,
	'images',(
		SELECT
			json_objectagg(img.id, img.url)
		FROM dbtienda.images img
        WHERE img.clzd_id = clz.id 
    ),
    'sizes',(
		SELECT 
			json_objectagg(s.id, s.size)
		FROM 
			dbtienda.sizes s
		WHERE s.clzd_id = clz.id 
    ),
    'color',(
		SELECT 
			json_objectagg(cl.id, cl.color)
		FROM 
			dbtienda.color cl 
		WHERE cl.clzd_id = clz.id 
    ),
     'characteristics',(
		SELECT 
			json_arrayagg(
				json_object(
					'id',cat.id,
                    'category',cat.category,		
                    'sex', cat.sex,
                    'leyend',cat.leyend,
                    'details',(
						SELECT 
							json_objectagg(dtl.id, dtl.descript)
						FROM 
							dbtienda.details dtl
						WHERE dtl.charc_id = cat.id))
				)
		FROM 
			dbtienda.characteristics cat
		WHERE cat.clzd_id = clz.id 
    )
)
 AS dato
 FROM Calzado clz
 WHERE clz.id = 1;


CREATE TABLE details(    id INT NOT NULL,             charc_id INT,             descript VARCHAR(255),    FOREIGN KEY (charc_id) REFERENCES characteristics(id) ON DELETE CASCADE         )
