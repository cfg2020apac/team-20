function Submit() {
    console.table(
        getSubmitData()
    );
}

function getSubmitData() {
    data = {
        "data": [{
            "ngo": document.getElementById("NGO-field").value,
            "ird": document.getElementById("IRD-field").value,
            "program": document.getElementById("ProgramName-field").value,
            "objective": document.getElementById("ProgramDescription-field").value,
            "email": document.getElementById("KeyContact-Email-field").value,
            "phone": document.getElementById("KeyContact-Phone-field").value,
            "title": document.getElementById("KeyContact-Title-field").value,
            "location": document.getElementById("Location-field").value,
            "numberOfService":document.getElementById("NumberService-field").value,
            "description": document.getElementById("NeedsDescript-field").value,
            "numberSessions": document.getElementById("NumSessions-field").value,
            "date": document.getElementById("DatesSession-field").value,
            "timeStart": document.getElementById("StartTime-Field").value,
            "timeEnd": document.getElementById("EndTime-Field").value,
            "numberVolunteers": document.getElementById("NumVolunteers-field").value,
            "roleVolunteers": document.getElementById("VolunteerRoles-field").value,
            "minAge": document.getElementById("AgeRequirement-field").value,
            "language": document.getElementById("LangReq-field").value,
            "remarks": document.getElementById("Remarks-field").value,
            "gatherInfo": document.getElementById("Gather-field").value,
            "budget": document.getElementById("Budget-field").value
        }]
    }
    



    return data
}