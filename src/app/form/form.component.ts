import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.scss']
})
export class FormComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
   Submit() {
    console.table(
        this.getSubmitData()
    );
}

 getSubmitData() {
  let ngo=document.getElementById("NGO-field") as HTMLInputElement;
  // let ngo=document.getElementById("NGO-field") as HTMLInputElement;
  // let ngo=document.getElementById("NGO-field") as HTMLInputElement;
  // let ngo=document.getElementById("NGO-field") as HTMLInputElement;
  // let ngo=document.getElementById("NGO-field") as HTMLInputElement;
  // let ngo=document.getElementById("NGO-field") as HTMLInputElement;

  // let ngo=document.getElementById("NGO-field") as HTMLInputElement;


   console.log(ngo.value);
    let data = {
        "data": [{
            "ngo": (<HTMLInputElement>document.getElementById("NGO-field")).value ,
            "ird": (<HTMLInputElement>document.getElementById("IRD-field")).value,
            "program": (<HTMLInputElement>document.getElementById("ProgramName-field")).value,
            "objective": (<HTMLInputElement>document.getElementById("ProgramDescription-field")).value,
            "email": (<HTMLInputElement>document.getElementById("KeyContact-Email-field")).value,
            "phone": (<HTMLInputElement>document.getElementById("KeyContact-Phone-field")).value,
            "title": (<HTMLInputElement>document.getElementById("KeyContact-Title-field")).value,
            "location": (<HTMLInputElement>document.getElementById("Location-field")).value,
            "numberOfService":(<HTMLInputElement>document.getElementById("NumberService-field")).value,
            "description": (<HTMLInputElement>document.getElementById("NeedsDescript-field")).value,
            "numberSessions": (<HTMLInputElement>document.getElementById("NumSessions-field")).value,
            "date": (<HTMLInputElement>document.getElementById("DatesSession-field")).value,
            "timeStart": (<HTMLInputElement>document.getElementById("StartTime-Field")).value,
            "timeEnd": (<HTMLInputElement>document.getElementById("EndTime-Field")).value,
            "numberVolunteers": (<HTMLInputElement>document.getElementById("NumVolunteers-field")).value,
            "roleVolunteers": (<HTMLInputElement>document.getElementById("VolunteerRoles-field")).value,
            "minAge": (<HTMLInputElement>document.getElementById("AgeRequirement-field")).value,
            "language": (<HTMLInputElement>document.getElementById("LangReq-field")).value,
            "remarks": (<HTMLInputElement>document.getElementById("Remarks-field")).value,
            "gatherInfo": (<HTMLInputElement>document.getElementById("Gather-field")).value,
            "budget": (<HTMLInputElement>document.getElementById("Budget-field")).value
        }]
    }
    



    return data;
    return;
  }
}
