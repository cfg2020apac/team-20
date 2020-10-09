import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-recommendation',
  templateUrl: './recommendation.component.html',
  styleUrls: ['./recommendation.component.scss']
})

export class RecommendationComponent implements OnInit {

  constructor() { }
  cards=[1,2,3,4,5,6];
  ngOnInit(): void {
    //TODO: GET Cards from api
  }

}
