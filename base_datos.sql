DROP DATABASE IF EXISTS gestion_proyectos;
CREATE DATABASE gestion_proyectos
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_spanish_ci;

USE gestion_proyectos;

CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    rol VARCHAR(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE Proyecto (
    id_proyecto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion DATE NOT NULL,
    id_lider INT NOT NULL,
    FOREIGN KEY (id_lider) REFERENCES Usuario(id_usuario)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE Tablero (
    id_tablero INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_proyecto INT NOT NULL,
    FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id_proyecto)
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE Columna (
    id_columna INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    orden INT NOT NULL,
    id_tablero INT NOT NULL,
    FOREIGN KEY (id_tablero) REFERENCES Tablero(id_tablero)
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE Tarea (
    id_tarea INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    fecha_creacion DATE NOT NULL,
    fecha_limite DATE,
    estado VARCHAR(30) NOT NULL,
    id_columna INT NOT NULL,
    id_responsable INT,
    FOREIGN KEY (id_columna) REFERENCES Columna(id_columna)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_responsable) REFERENCES Usuario(id_usuario)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE Miembro_Proyecto (
    id_proyecto INT NOT NULL,
    id_usuario INT NOT NULL,
    PRIMARY KEY (id_proyecto, id_usuario),
    FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id_proyecto)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

INSERT INTO Usuario (nombre, apellido, correo, contrasena, rol) VALUES
('Oscar', 'Carrillo', 'oscar@correo.cl', '123456', 'líder'),
('María', 'López', 'maria@correo.cl', '123456', 'miembro');

INSERT INTO Proyecto (nombre, descripcion, fecha_creacion, id_lider) VALUES
('Sistema de Gestión', 'Plataforma tipo Trello', CURDATE(), 1);

INSERT INTO Miembro_Proyecto (id_proyecto, id_usuario) VALUES (1, 1), (1, 2);

INSERT INTO Tablero (nombre, id_proyecto) VALUES ('Tablero Principal', 1);

INSERT INTO Columna (nombre, orden, id_tablero) VALUES
('Pendiente', 1, 1), ('En Progreso', 2, 1), ('Terminado', 3, 1);

INSERT INTO Tarea (titulo, descripcion, fecha_creacion, estado, id_columna, id_responsable) VALUES
('Diseñar UML', 'Elaborar diagrama de clases', CURDATE(), 'Pendiente', 1, 1),
('Codificar clases', 'Implementar en Python', CURDATE(), 'Pendiente', 1, 2);