# Cheems API

API para la gestión de cómics, novelas y mangas de la aplicación `django_cheems`.

## Cómo funciona

La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los elementos de la aplicación `django_cheems`.

Usando la API, los usuarios pueden interactuar con los datos de la aplicación de manera programática, facilitando la integración con otras aplicaciones o servicios. Se pueden realizar solicitudes HTTP a los endpoints de la API para obtener información sobre los elementos, crear nuevos elementos, actualizar los existentes o eliminarlos según sea necesario.

Todo eso se facilita mediante el uso de la biblioteca Django REST Framework, que proporciona herramientas y funcionalidades para construir APIs de manera eficiente y segura. Además del uso de Postman para probar y documentar la API, lo que permite a los desarrolladores explorar y comprender cómo interactuar con los diferentes endpoints de la API de manera sencilla.

## SQL

```sql
CREATE DATABASE IF NOT EXISTS `cheemsapi_db`
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE `cheemsapi_db`;

CREATE TABLE `comic` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(70) NULL DEFAULT NULL,
  `description` VARCHAR(100) NULL DEFAULT NULL,
  `editorial` VARCHAR(60) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `novel` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(70) NULL DEFAULT NULL,
  `description` VARCHAR(100) NULL DEFAULT NULL,
  `editorial` VARCHAR(60) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `manga` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(70) NULL DEFAULT NULL,
  `description` VARCHAR(100) NULL DEFAULT NULL,
  `editorial` VARCHAR(60) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;
```
