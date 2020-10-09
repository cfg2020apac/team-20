CREATE TABLE registration_type (
  registration_type_id INT NOT NULL AUTO_INCREMENT,
  description VARCHAR(1000) NOT NULL,
  PRIMARY KEY (registration_type_id)
);

INSERT INTO registration_type (description) VALUES ("Sign Up");
INSERT INTO registration_type (description) VALUES ("Express Interest");

DROP TABLE registration_type;
