-- Creación de la base de datos
CREATE DATABASE DunderMifflin;

--Usar base de datos creada
USE DunderMifflin;

-- Tabla Empleados (creada primero sin FK para evitar dependencias circulares)
CREATE TABLE Empleados (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(15),
    Correo VARCHAR(100),
    ID_Departamento INT,
    ID_Jefe INT
);

-- Tabla Departamentos
CREATE TABLE Departamentos (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Ubicacion VARCHAR(50) NOT NULL,
    Presupuesto DECIMAL(12,2) NOT NULL,
    ID_Jefe INT
);

-- Agregar FKs después de crear ambas tablas
ALTER TABLE Empleados
ADD CONSTRAINT FK_Empleado_Departamento 
FOREIGN KEY (ID_Departamento) REFERENCES Departamentos(ID);

ALTER TABLE Empleados
ADD CONSTRAINT FK_Empleado_Jefe 
FOREIGN KEY (ID_Jefe) REFERENCES Empleados(ID);

ALTER TABLE Departamentos
ADD CONSTRAINT FK_Departamento_Jefe 
FOREIGN KEY (ID_Jefe) REFERENCES Empleados(ID);

-- Insertar departamentos (sin jefes inicialmente)
INSERT INTO Departamentos (Nombre, Ubicacion, Presupuesto) VALUES
('Ventas', 'Scranton', 150000),
('Recepción', 'Scranton', 50000),
('Contabilidad', 'Scranton', 80000),
('Recursos Humanos', 'Scranton', 60000),
('Proveedores', 'Scranton', 70000),
('Servicio al Cliente', 'Scranton', 40000),
('Almacén', 'Scranton', 50000),
('Corporativo', 'Nueva York', 200000);

-- Insertar empleados (sin jefes inicialmente)
INSERT INTO Empleados (Nombre, Apellido, Telefono, Correo, ID_Departamento) VALUES
('Michael', 'Scott', '555-1234', 'michael.scott@dundermifflin.com', 1),
('Jim', 'Halpert', '555-2345', 'jim.halpert@dundermifflin.com', 1),
('Dwight', 'Schrute', '555-3456', 'dwight.schrute@dundermifflin.com', 1);

-- Actualizar jefes después
UPDATE Departamentos SET ID_Jefe = 1 WHERE ID = 1; -- Michael Scott jefe de Ventas
UPDATE Empleados SET ID_Jefe = 19 WHERE ID IN (1, 2, 3); -- Jan Levinson como jefe