DDL_QUERY = '''
CREATE TABLE IF NOT EXISTS categoria (
  idcategoria INT NOT NULL,
  nombre VARCHAR(50) NULL,
  descripcion VARCHAR(255) NULL,
  estado BIT NULL,
  PRIMARY KEY (idcategoria)
  );


CREATE TABLE IF NOT EXISTS articulo (
  idarticulo INT NOT NULL,
  idcategoria INT NOT NULL,
  codigo VARCHAR(50) NULL,
  nombre VARCHAR(100) NULL,
  precio_venta DECIMAL(11,2) NULL,
  stock INT NULL,
  descripcion VARCHAR(255) NULL,
  imagen VARCHAR(20) NULL,
  estado BIT NULL,
  PRIMARY KEY (idarticulo),
  INDEX fk_articulo_categoria_idx (idcategoria) ,
  
  CONSTRAINT fk_articulo_categoria
    FOREIGN KEY (idcategoria)
    REFERENCES categoria (idcategoria)
    );


CREATE TABLE IF NOT EXISTS rol (
  idrol INT NOT NULL,
  nombre VARCHAR(30) NULL,
  descripcion VARCHAR(255) NULL,
  estado BIT NULL,
  PRIMARY KEY (idrol)
  );


CREATE TABLE IF NOT EXISTS usuario (
  idusuario INT NOT NULL,
  idrol INT NOT NULL,
  nombre VARCHAR(100) NULL,
  tipo_documento VARCHAR(20) NULL,
  num_documento VARCHAR(20) NULL,
  direccion VARCHAR(70) NULL,
  telefono VARCHAR(20) NULL,
  email VARCHAR(50) NULL,
  clave VARBINARY(200) NULL,
  estado BIT NULL,
  PRIMARY KEY (idusuario),
  INDEX fk_usuario_rol1_idx (idrol) ,
  CONSTRAINT fk_usuario_rol1
    FOREIGN KEY (idrol)
    REFERENCES rol (idrol)
    );


CREATE TABLE IF NOT EXISTS persona (
  idpersona INT NOT NULL,
  tipo_persona VARCHAR(20) NULL,
  nombre VARCHAR(100) NULL,
  tipo_documento VARCHAR(20) NULL,
  num_documento VARCHAR(20) NULL,
  direccion VARCHAR(70) NULL,
  telefono VARCHAR(20) NULL,
  email VARCHAR(50) NULL,
  PRIMARY KEY (idpersona)
  );



CREATE TABLE IF NOT EXISTS ingreso (
  idingreso INT NOT NULL,
  idproveedor INT NOT NULL,
  idusuario INT NOT NULL,
  tipo_comprobante VARCHAR(20) NULL,
  serie_comprobante VARCHAR(7) NULL,
  num_comprobante VARCHAR(10) NULL,
  fecha DATETIME NULL,
  impuesto DECIMAL(4,2) NULL,
  total DECIMAL(11,2) NULL,
  estado VARCHAR(20) NULL,
  PRIMARY KEY (idingreso),
  INDEX fk_ingreso_usuario1_idx (idusuario) ,
  INDEX fk_ingreso_persona1_idx (idproveedor) ,
  CONSTRAINT fk_ingreso_usuario1
    FOREIGN KEY (idusuario)
    REFERENCES usuario (idusuario),
  CONSTRAINT fk_ingreso_persona1
    FOREIGN KEY (idproveedor)
    REFERENCES persona (idpersona)
    );


CREATE TABLE IF NOT EXISTS detalle_ingreso (
  iddetalle_ingreso INT NOT NULL,
  idingreso INT NULL,
  idarticulo INT NULL,
  cantidad INT NULL,
  precio DECIMAL(11,2) NULL,
  PRIMARY KEY (iddetalle_ingreso),
  INDEX fk_detalle_ingreso_articulo1_idx (idarticulo) ,
  INDEX fk_detalle_ingreso_ingreso1_idx (idingreso) ,
  CONSTRAINT fk_detalle_ingreso_articulo1
    FOREIGN KEY (idarticulo)
    REFERENCES articulo (idarticulo),
  CONSTRAINT fk_detalle_ingreso_ingreso1
    FOREIGN KEY (idingreso)
    REFERENCES ingreso (idingreso)
    );


CREATE TABLE IF NOT EXISTS venta (
  idventa INT NOT NULL,
  idcliente INT NOT NULL,
  idusuario INT NOT NULL,
  tipo_comprobante VARCHAR(20) NULL,
  serie_comprobante VARCHAR(7) NULL,
  num_comprobante VARCHAR(10) NULL,
  fecha DATETIME NULL,
  impuesto DECIMAL(4,2) NULL,
  total DECIMAL(11,2) NULL,
  estado VARCHAR(20) NULL,
  PRIMARY KEY (idventa),
  INDEX fk_venta_usuario1_idx (idusuario) ,
  INDEX fk_venta_persona1_idx (idcliente) ,
  CONSTRAINT fk_venta_usuario1
    FOREIGN KEY (idusuario)
    REFERENCES usuario (idusuario),
  CONSTRAINT fk_venta_persona1
    FOREIGN KEY (idcliente)
    REFERENCES persona (idpersona)
    );


CREATE TABLE IF NOT EXISTS detalle_venta (
  iddetalle_venta INT NOT NULL,
  idventa INT NOT NULL,
  idarticulo INT NOT NULL,
  cantidad INT NULL,
  precio DECIMAL(11,2) NULL,
  descuento DECIMAL(11,2) NULL,
  PRIMARY KEY (iddetalle_venta),
  INDEX fk_detalle_venta_articulo1_idx (idarticulo),
  INDEX fk_detalle_venta_venta1_idx (idventa) ,
  CONSTRAINT fk_detalle_venta_articulo1
    FOREIGN KEY (idarticulo)
    REFERENCES articulo(idarticulo),
  CONSTRAINT fk_detalle_venta_venta1
    FOREIGN KEY (idventa)
    REFERENCES venta (idventa)
    );
'''