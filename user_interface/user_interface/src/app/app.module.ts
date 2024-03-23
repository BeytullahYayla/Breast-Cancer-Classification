import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { HomeComponent } from './components/home/home.component';
import { PredictComponent } from './components/predict/predict.component';
import { FooterComponent } from './components/footer/footer.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { ToastrModule } from 'ngx-toastr';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';import {trigger,state,style,animate,transition}from '@angular/animations';
import { MalignantComponent } from './malignant/malignant.component';
import { BenignComponent } from './benign/benign.component';
@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    PredictComponent,
    FooterComponent,
    MalignantComponent,
    BenignComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatToolbarModule,
    MatButtonModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot({
      positionClass:"toast-bottom-right"
    })
   
  ],
  providers: [],
  bootstrap: [AppComponent],
  
})
export class AppModule { }
