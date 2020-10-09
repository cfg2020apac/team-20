import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.scss']
})
export class CategoriesComponent implements OnInit {
  categories=[
    "Assistance and Support for Elderly" ,
    "Disaster & Emergency Services" ,
    "Education and Empowerment for Children and Youth" ,
    "Adult Education" ,
    "Environmental Conservation" ,
    "Education and Empowerment for Refugees and Asylum Seekers" ,
    "Health and Wellness" ,
    "Hunger & Homelessness"  ,
    "Support for Homeless People" ,
    "Empowerment and Support for Domestic and Migrant Workers" ,
    "International Service" ,
    "Internships & Employment" ,
    "Justice & Legal Services" ,
    "Refugee & Asylum Seekers Services" ,
    "Schools" ,
    "Sports & Recreation" ,
    "Technology" ,
    "Family Services" ,
    "Arts & Culture" ,
    "Civic & Community"
  ]
  constructor(
    private router: Router,
  ) { }
  selectedCats=[];
  styles=[];
  ngOnInit(): void {
    for (let i = 0 ; i <this.categories.length;i++){
      this.styles.push(false);
    }
  }
  onClick(i){
    // console.log(this.categories[i]);
    this.styles[i]=!this.styles[i];
    if (this.selectedCats.includes(this.categories[i])){
      // console.log('selected'); 
      // console.log(this.selectedCats.indexOf(this.categories[i]));
      this.selectedCats.splice(this.selectedCats.indexOf(this.categories[i],1));
    }
    else{
      this.selectedCats.push(this.categories[i]);
    }
  }
  onSubmit(){
    console.log(this.selectedCats);
    //TODO: submit this.selectedCats to API
    this.router.navigate(['/profile/recommendations']);
  }
}
