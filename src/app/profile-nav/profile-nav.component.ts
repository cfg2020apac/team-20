import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile-nav',
  templateUrl: './profile-nav.component.html',
  styleUrls: ['./profile-nav.component.scss']
})
export class ProfileNavComponent implements OnInit {

  constructor() { }
  items=[
    'Overview',
    'Personal Information',
    'Skills & Interest',
    'My Teams',
    'Recommendation',
    'Saved Searches'
  ]
  ngOnInit(): void {
  }

}
