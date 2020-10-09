import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProfileComponent } from './profile/profile.component';
import { CategoriesComponent } from './categories/categories.component';
import { RecommendationComponent } from './recommendation/recommendation.component';
import { PersonalInfoComponent } from './personal-info/personal-info.component';

const routes: Routes = [
  { path: 'profile', component: ProfileComponent },
  { path: 'profile/categories', component: CategoriesComponent },
  { path: 'profile/recommendations', component: RecommendationComponent},
  { path: 'info', component: PersonalInfoComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
