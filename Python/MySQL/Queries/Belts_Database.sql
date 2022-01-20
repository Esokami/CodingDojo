-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema belts
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema belts
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `belts` DEFAULT CHARACTER SET utf8 ;
USE `belts` ;

-- -----------------------------------------------------
-- Table `belts`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belts`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` VARCHAR(255) NULL,
  `updated_at` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belts`.`belts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belts`.`belts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belts`.`belt_certifications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `belts`.`belt_certifications` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `user_id` INT NOT NULL,
  `belt_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_belt_certifications_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_belt_certifications_belts1_idx` (`belt_id` ASC) VISIBLE,
  CONSTRAINT `fk_belt_certifications_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `belts`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_belt_certifications_belts1`
    FOREIGN KEY (`belt_id`)
    REFERENCES `belts`.`belts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
