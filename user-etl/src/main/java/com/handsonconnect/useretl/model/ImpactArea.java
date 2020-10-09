package com.handsonconnect.useretl.model;

import javax.persistence.*;

@Entity
@Table(name = "impact_area")
public class ImpactArea {

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    @Column(name = "impact_area_id")
    private Integer impactArea_id;

    @Column(name = "description")
    private String description;

    public Integer getImpactArea_id() {
        return impactArea_id;
    }

    public void setImpactArea_id(Integer impactArea_id) {
        this.impactArea_id = impactArea_id;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
