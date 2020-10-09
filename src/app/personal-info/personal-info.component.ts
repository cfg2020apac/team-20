import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-personal-info',
  templateUrl: './personal-info.component.html',
  styleUrls: ['./personal-info.component.scss']
})
export class PersonalInfoComponent implements OnInit {

  constructor() { }
  skills=[
    "Accounting / finance 會計 / 金融",
    "Administrative/general office support 行政 / 一般辦公室支援", 
    "Communications and marketing 傳播學及市場管銷", 
    "Fundraising 籌款活動",
    "Gardening 園藝", 
    "Graphic design 平面設計", 
    "Health / medical 保健 / 醫療", 
    "Event management 活動管理", 
    "Human resources 人力資源", 
    "IT 資訊科技", 
    "Legal 法律",
    "Photography 攝影",
    "Project management 項目管理",
    "Teaching /Training教學/ Fine arts 藝術", 
    "Teaching /Training教學/Fitness/sports 體能/運動", 
    "Teaching /Training教學 /Music/drama 音樂 / 戲劇",
    "Teaching /Training教學 /Health 保健", 
    "Teaching /Training教學/IT 資訊科技", 
    "Translation 翻譯",
    "Videography 影片製作"
  ];
  interests=[
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
  ];
  langs;
  allLangs=["Cantonese","English","Mandarin","Written Chinese"];
  selectedSkills=[];
  selectedInterests=[];
  clickedSkills=[];
  clickedInterests=[];
  ngOnInit(): void {
    for (let i = 0 ; i <this.skills.length;i++){
      this.clickedSkills.push(false);
    }
    for (let i = 0 ; i <this.interests.length;i++){
      this.clickedInterests.push(false);
    }
  }
  updateLangs(){
    console.log(this.langs);
  }
  skillOnClick(i){
    console.log(this.skills[i]);
    this.clickedSkills[i]=!this.clickedSkills[i];
    if (this.selectedSkills.includes(this.skills[i])){
      this.selectedSkills.splice(this.selectedSkills.indexOf(this.skills[i],1));
    }
    else{
      this.selectedSkills.push(this.skills[i]);
    }
  }
  interestOnClick(i){
    console.log(this.interests[i]);
    this.clickedInterests[i]=!this.clickedInterests[i];
    if (this.selectedInterests.includes(this.interests[i])){
      this.selectedInterests.splice(this.selectedInterests.indexOf(this.interests[i],1));
    }
    else{
      this.selectedInterests.push(this.interests[i]);
    }

  }
  onSubmit(){
    console.log(this.selectedSkills);
    console.log(this.selectedInterests)
  }
}
