import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile-nav',
  templateUrl: './profile-nav.component.html',
  styleUrls: ['./profile-nav.component.scss']
})
export class ProfileNavComponent implements OnInit {

  constructor() { }
  items=[
    {name:'Overview',link:'/profile'},
    {name:'Skills & Interests',link:'/info'},
    {name:'Personal Information',link:'/'},
    {name:'NGO Form',link:'/form'},
    {name:'Recommendation',link:'/'},
    {name:'Saved Searches',link:'/'},
  ]
  ngOnInit(): void {
  }

}
