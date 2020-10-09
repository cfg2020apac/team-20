import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor() { }
  menuItems=[
    'Volunteer',
    'NGO Partners',
    'Corporate Volunteering',
    'Events & Fundraisers',
    'Donate',
    'About Us',
    'Contact Us'
  ];
  
  ngOnInit(): void {
  }

}
