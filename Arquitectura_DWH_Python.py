DDL_QUERY = '''
CREATE TABLE IF NOT EXISTS dim_tiempo (
  date_key INT NOT NULL,
  full_date DATE NULL,
  day_of_week INT NULL,
  day_of_month INT NULL,
  day_name VARCHAR(45) NULL,
  month INT NULL,
  month_name VARCHAR(45) NULL,
  yearmo VARCHAR(45) NULL,
  PRIMARY KEY (date_key)
  );


CREATE TABLE IF NOT EXISTS dim_persona (
  idpersona INT NOT NULL,
  tipo_persona VARCHAR(20) NULL,
  num_documento VARCHAR(20) NULL,
  direccion VARCHAR(70) NULL,
  telefono VARCHAR(20) NULL,
  email VARCHAR(50) NULL,
  PRIMARY KEY (idpersona)
  );


CREATE TABLE IF NOT EXISTS dim_articulo (
  idarticulo INT NOT NULL,
  codigo VARCHAR(50) NULL,
  nombre VARCHAR(100) NULL,
  precio_venta DECIMAL(11,2) NULL,
  stock INT NULL,
  descripcion VARCHAR(255) NULL,
  estado BIT NULL,
  PRIMARY KEY (idarticulo)
  );


CREATE TABLE IF NOT EXISTS dim_categoria (
  idcategoria INT NOT NULL,
  nombre VARCHAR(50) NULL,
  descripcion VARCHAR(255) NULL,
  estado BIT NULL,
  PRIMARY KEY (idcategoria)
  );


CREATE TABLE IF NOT EXISTS fact_ventas (
  num_comprobante VARCHAR(10) NULL,
  date_key INT NULL,
  idcliente INT NULL,
  idarticulo INT NULL,
  idcategoria INT NULL,
  cantidad INT NULL,
  precio DECIMAL(11,2) NULL,
  descuento DECIMAL(11,2) NULL,
  impuesto DECIMAL(11,2) NULL,
  fecha DATE NULL,
  CONSTRAINT fk_fact_ventas_dim_tiempo1
    FOREIGN KEY (date_key)
    REFERENCES dim_tiempo (date_key),
  CONSTRAINT fk_fact_ventas_dim_persona1
    FOREIGN KEY (idcliente)
    REFERENCES dim_persona (idpersona),
  CONSTRAINT fk_fact_ventas_dim_articulo1
    FOREIGN KEY (idarticulo)
    REFERENCES dim_articulo (idarticulo),
  CONSTRAINT fk_fact_ventas_dim_categoria1
    FOREIGN KEY (idcategoria)
    REFERENCES dim_categoria (idcategoria)
	);
'''