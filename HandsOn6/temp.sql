-- MySQL Script generated by MySQL Workbench
-- Tue Sep  6 16:43:21 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SAM
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SAM
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SAM` DEFAULT CHARACTER SET utf8 ;
USE `SAM` ;

-- -----------------------------------------------------
-- Table `SAM`.`AREA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAM`.`AREA` (
  `Sigla` VARCHAR(5) NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `SuperArea` VARCHAR(5) NULL,
  PRIMARY KEY (`Sigla`),
  INDEX `fk_AREA_SUPERAREA` (`SuperArea` ASC, `Sigla` ASC) VISIBLE,
  UNIQUE INDEX `Sigla_UNIQUE` (`Sigla` ASC) VISIBLE,
  CONSTRAINT `SuperArea`
    FOREIGN KEY (`SuperArea` , `Sigla`)
    REFERENCES `SAM`.`AREA` (`Sigla` , `SuperArea`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAM`.`CURSO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAM`.`CURSO` (
  `Sigla` VARCHAR(5) NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Horas` INT NULL,
  `Custo` FLOAT NULL,
  `Area` VARCHAR(5) NULL,
  PRIMARY KEY (`Sigla`),
  INDEX `fk_CURSO_AREA` (`Area` ASC) VISIBLE,
  UNIQUE INDEX `Sigla_UNIQUE` (`Sigla` ASC) VISIBLE,
  CONSTRAINT `fk_CURSO_AREA1`
    FOREIGN KEY (`Area`)
    REFERENCES `SAM`.`AREA` (`Sigla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAM`.`MODULO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAM`.`MODULO` (
  `Sigla` VARCHAR(5) NOT NULL,
  `Nome` VARCHAR(45) NULL,
  `Curso` VARCHAR(5) NOT NULL,
  INDEX `fk_MODULO_CURSO` (`Curso` ASC) VISIBLE,
  UNIQUE INDEX `Sigla_UNIQUE` (`Sigla` ASC) VISIBLE,
  PRIMARY KEY (`Sigla`),
  CONSTRAINT `fk_MODULO_CURSO1`
    FOREIGN KEY (`Curso`)
    REFERENCES `SAM`.`CURSO` (`Sigla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAM`.`TOPICO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAM`.`TOPICO` (
  `Modulo` VARCHAR(5) NOT NULL,
  `Sigla` VARCHAR(5) NOT NULL,
  `Nome` VARCHAR(45) NULL,
  `Horas` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`Modulo`, `Sigla`),
  CONSTRAINT `fk_TOPICO_MODULO1`
    FOREIGN KEY (`Modulo`)
    REFERENCES `SAM`.`MODULO` (`Sigla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAM`.`ALUNO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAM`.`ALUNO` (
  `CPF` INT(11) NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Sobrenome` VARCHAR(80) NULL,
  `Sexo` CHAR(1) NULL,
  `DataNasc` DATE NULL,
  PRIMARY KEY (`CPF`),
  UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAM`.`MATRICULA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAM`.`MATRICULA` (
  `Curso` VARCHAR(5) NOT NULL,
  `Aluno` INT(11) NOT NULL,
  `Data` DATE NULL,
  `Pago` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`Curso`, `Aluno`),
  INDEX `fk_MATRICULA_ALUNO` (`Aluno` ASC) VISIBLE,
  CONSTRAINT `fk_MATRICULA_CURSO1`
    FOREIGN KEY (`Curso`)
    REFERENCES `SAM`.`CURSO` (`Sigla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MATRICULA_ALUNO1`
    FOREIGN KEY (`Aluno`)
    REFERENCES `SAM`.`ALUNO` (`CPF`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SAM`.`PROFESSOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SAM`.`PROFESSOR` (
  `Curso` VARCHAR(5) NOT NULL,
  `CPF` INT(11) NOT NULL,
  `Nome` VARCHAR(125) NOT NULL,
  PRIMARY KEY (`Curso`, `CPF`),
  CONSTRAINT `fk_PROFESSOR_CURSO1`
    FOREIGN KEY (`Curso`)
    REFERENCES `SAM`.`CURSO` (`Sigla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;