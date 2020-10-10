import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.scss']
})
export class CategoriesComponent implements OnInit {
  categories=[
    "Assistance and Support for Elderly" ,
    "Disaster and Emergency Services" ,
    "Education and Empowerment for Children and Youth" ,
    "Adult Education" ,
    "Environmental Conservation" ,
    "Education and Empowerment for Refugees and Asylum Seekers" ,
    "Health and Wellness" ,
    "Hunger and Homelessness"  ,
    "Support for Homeless People" ,
    "Empowerment and Support for Domestic and Migrant Workers" ,
    "International Service" ,
    "Internships and Employment" ,
    "Justice and Legal Services" ,
    "Refugee and Asylum Seekers Services" ,
    "Schools" ,
    "Sports and Recreation" ,
    "Technology" ,
    "Family Services" ,
    "Arts and Culture" ,
    "Civic and Community"
  ]
  constructor(
    private router: Router,
    private http: HttpClient,
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
    // Reach to Recommendation Service 
    
    //TODO: submit this.selectedCats to API
    console.log(this.selectedCats.join('_'));
    this.router.navigate(['/profile/recommendations'], {queryParams : { categories: this.selectedCats.join('_')}});
  }
}
