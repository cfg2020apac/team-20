package com.handsonconnect.useretl.model;
import javax.persistence.*;

@Entity
@Table(name = "ngo")
public class NGO {

    public NGO() {
    }

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    @Column(name = "ngo_id")
    private Integer ngo_id;

    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "population_served_id", referencedColumnName = "population_served_id")
    private PopulationServed populationServed;

    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "impact_area_id", referencedColumnName = "impact_area_id")
    private ImpactArea impactArea;

    public Integer getNgo_id() {
        return ngo_id;
    }

    public void setNgo_id(Integer ngo_id) {
        this.ngo_id = ngo_id;
    }

    public PopulationServed getPopulationServed() {
        return populationServed;
    }

    public void setPopulationServed(PopulationServed populationServed) {
        this.populationServed = populationServed;
    }

    public ImpactArea getImpactArea() {
        return impactArea;
    }

    public void setImpactArea(ImpactArea impactArea) {
        this.impactArea = impactArea;
    }

    //    occurrenceID
//    status
//
//    impactOutcome
//
//    scheduleType
//
//    location
//    startDateTime
//    endDateTime
//    opportunityCoordinator
//    OpportunityCoordinatorEmail
//    volunteerLeaderNeeded
//    maximumAttendance
//    minimumAttendance
//    totalConfirmed
//    volunteersStillNeeded
//    totalAttended
//    totalNotAttended
//    totalHoursServed




}
