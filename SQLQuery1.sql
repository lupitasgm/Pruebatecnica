CREATE DATABASE GestionEmpleados;
DROP DATABASE GestionEmpleados;
USE GestionEmpleados;

CREATE TABLE Departamentos(
IdDepartamento int IDENTITY(1,1) PRIMARY KEY,
NombreDepartamento varchar(30)
);

CREATE TABLE Empleados(
IdEmpleado int IDENTITY(101,1) PRIMARY KEY,
Nombre varchar(50),
Apellido varchar(50),
Cargo varchar(50),
FechaContratacion date, 
Salario decimal(10, 2),
IdDepartamento int FOREIGN KEY REFERENCES Departamentos(IdDepartamento),
);


INSERT INTO Departamentos VALUES
('Ventas'),
('Desarrollo'),
('Recursos Humanos'),
('Finanzas'),
('Marketing');

SELECT * FROM Departamentos


INSERT INTO Empleados (Nombre, Apellido, Cargo, FechaContratacion, Salario, IdDepartamento) VALUES
('Juan','Perez','Vendedor','2022-01-15',3000,1),
('Maria','Lopez','Desarrollador','2021-08-20',3500,2),
('Carlos','Ramirez','Gerente RH','2020-11-10',8000,3),
('Laura','Martinez','Contador','2023-02-28',5000,4),
('Oscar','Diaz','Analista MKT','2022-09-03',2000,5),
('Sofia','Guzman','Vendedor','2021-07-12',1500,1),
('Javier','Torres','Desarrollador','2020-03-15',900,2),
('Ana','Navarro','Asistente RH','2023-01-05',1000,3),
('Luis','Gonzalez','Analista Financiero','2022-06-18',3900,4),
('Patricia','Silva','Coordinador','2021-08-30',2500,5);

SELECT * FROM Empleados