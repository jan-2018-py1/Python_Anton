CREATE TABLE `mydb`.`login_data` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `f_name` VARCHAR(45) NOT NULL,
  `l_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` BINARY(16) NOT NULL,
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));
