CREATE TABLE impact_area (
  impact_area_id INT NOT NULL AUTO_INCREMENT,
  description VARCHAR(1000) NOT NULL,
  PRIMARY KEY (impact_area_id)
);

INSERT INTO impact_area (description) VALUES ("Environmental Conservation");
INSERT INTO impact_area (description) VALUES ("Hunger & Homelessness");
INSERT INTO impact_area (description) VALUES ("Education and Empowerment for Children and Youth");
INSERT INTO impact_area (description) VALUES ("Assistance and Support for Elderly");
INSERT INTO impact_area (description) VALUES ("Civic & Community");
INSERT INTO impact_area (description) VALUES ("Education and Empowerment for Children and Youth");
INSERT INTO impact_area (description) VALUES ("Hygiene");
INSERT INTO impact_area (description) VALUES ("Disaster & Emergency Services");
INSERT INTO impact_area (description) VALUES ("Health and Wellness");
INSERT INTO impact_area (description) VALUES ("Refugee & Asylum Seekers Services");
INSERT INTO impact_area (description) VALUES ("Animal Welfare");
INSERT INTO impact_area (description) VALUES ("Empowerment and Support for Domestic and Migrant Workers");
INSERT INTO impact_area (description) VALUES ("Health & Wellness");

DROP TABLE impact_area;