import { BenignComponent } from './benign/benign.component';
import { MalignantComponent } from './malignant/malignant.component';
import { PredictComponent } from './components/predict/predict.component';
import { HomeComponent } from './components/home/home.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [

{path:"",pathMatch:'full',component:HomeComponent},
{path:"home",pathMatch:"full",component:HomeComponent},
{path:"home/predict",pathMatch:"full",component:PredictComponent},
{path:"predict",component:PredictComponent},
{path:"malignant",component:MalignantComponent},
{path:"benign",component:BenignComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
