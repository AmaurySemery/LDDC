CREATE SCHEMA IF NOT EXISTS `lddc` DEFAULT CHARACTER SET utf8 ;
USE `lddc` ;

-- -----------------------------------------------------
-- Table `lddc`.`Localisation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lddc`.`Localisation` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `world` VARCHAR(45) NULL,
  `coordinates` JSON NULL,
  `description` VARCHAR(45) NULL,
  `places` JSON NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lddc`.`ChronologyCharacter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lddc`.`Character` (
  `idCharacter` INT NOT NULL AUTO_INCREMENT,
  `background` VARCHAR(45) NULL,
  `picture` VARCHAR(45) NULL,
  `race` VARCHAR(45) NULL,
  `name` VARCHAR(45) NULL,
  `idLocalisation` INT NOT NULL,
  PRIMARY KEY (`idCharacter`),
  KEY `fk_Character_Localisation_idx` (`idLocalisation`),
  CONSTRAINT `fk_Character_Localisation`
    FOREIGN KEY (`idLocalisation`)
    REFERENCES `lddc`.`Localisation` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;




-- -----------------------------------------------------
-- Table `lddc`.`Chronology`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lddc`.`Chronology` (
  `idChronology` INT NOT NULL AUTO_INCREMENT,
  `events` JSON NULL,
  `idLocalisation` INT NOT NULL,
  PRIMARY KEY (`idChronology`, `idLocalisation`),
  INDEX `fk_Chronology_Localisation1_idx` (`idLocalisation` ASC),
  CONSTRAINT `fk_Chronology_Localisation1`
    FOREIGN KEY (`idLocalisation`)
    REFERENCES `lddc`.`Localisation` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `lddc`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lddc`.`User` (
  `idUser` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `role` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB;