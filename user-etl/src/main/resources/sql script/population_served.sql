CREATE TABLE population_served (
  population_served_id INT NOT NULL AUTO_INCREMENT,
  description VARCHAR(1000) NOT NULL,
  PRIMARY KEY (population_served_id)
);

INSERT INTO population_served (description) VALUES ("Tacos");
INSERT INTO population_served (description) VALUES ("Environmental education; Integrated");
INSERT INTO population_served (description) VALUES ("Integrated");
INSERT INTO population_served (description) VALUES ("Hunger & homelessness");
INSERT INTO population_served (description) VALUES ("Environmental education");
INSERT INTO population_served (description) VALUES ("Children and youth; Elderly; Hunger & homelessness");
INSERT INTO population_served (description) VALUES ("Children and youth");
INSERT INTO population_served (description) VALUES ("Children and youth; People with disabilities");
INSERT INTO population_served (description) VALUES ("Environmental education; Women");
INSERT INTO population_served (description) VALUES ("Hungers and homeless");
INSERT INTO population_served (description) VALUES ("Elderly");
INSERT INTO population_served (description) VALUES ("Children and youth; Environmental education");
INSERT INTO population_served (description) VALUES ("Children and youth; Ethnic minorities");
INSERT INTO population_served (description) VALUES ("People with mental illness");
INSERT INTO population_served (description) VALUES ("Elderly; People with illness");
INSERT INTO population_served (description) VALUES ("Adults; Elderly; Environmental education");
INSERT INTO population_served (description) VALUES ("Adults; Children and youth; Elderly; People with disabilities");
INSERT INTO population_served (description) VALUES ("Adults; Children and youth; Elderly");
INSERT INTO population_served (description) VALUES ("Refugees and asylum seekers");
INSERT INTO population_served (description) VALUES ("Other");
INSERT INTO population_served (description) VALUES ("Adults; Children and youth; Elderly; Refugees and asylum seekers; Women");
INSERT INTO population_served (description) VALUES ("Animals");
INSERT INTO population_served (description) VALUES ("Women");
INSERT INTO population_served (description) VALUES ("Environmental education; Hunger & homelessness");
INSERT INTO population_served (description) VALUES ("People with disabilities; People with mental illness");
INSERT INTO population_served (description) VALUES ("Children and youth; Refugees and asylum seekers");

DROP TABLE population_served;
