import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-recommendation',
  templateUrl: './recommendation.component.html',
  styleUrls: ['./recommendation.component.scss']
})

export class RecommendationComponent implements OnInit {

  constructor(private $http: HttpClient, private route: ActivatedRoute) { }
  //cards=[1,2,3,4,5,6];
  cards=[];
  categories = [];

  ngOnInit(): void {
    //TODO: GET Cards from api
    console.log(this.route.snapshot.paramMap);
    // this.categories = this.route.snapshot.paramMap.get("categories").split('_');
    this.route.queryParamMap.subscribe(params => {
      let paramstr = params.get('categories');
      let paramsL = paramstr.split("_");
      console.log(paramstr);
      console.log(paramsL);
      this.$http.get('/recommend/').subscribe( (result) => {
        // console.log(result[0]);
        // result is list of string, try to parse it
        // console.log(JSON.parse(result));
        let usableResult = JSON.parse(result[0]);
        console.log(usableResult);
        this.cards=usableResult;
      });
    })
    console.log(this.categories);
  }

}
