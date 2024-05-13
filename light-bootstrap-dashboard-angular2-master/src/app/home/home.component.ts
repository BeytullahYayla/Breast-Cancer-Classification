import { Component, OnInit } from '@angular/core';
import { LocationStrategy, PlatformLocation, Location } from '@angular/common';
import { LegendItem, ChartType } from '../lbd/lbd-chart/lbd-chart.component';
import * as Chartist from 'chartist';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CancerPredictionService } from 'app/services/cancer-prediction.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  prediction:any
  cancerFeatureForm: FormGroup = new FormGroup({});
  patientInfoForm:FormGroup=new FormGroup({});

  constructor(private formBuilder:FormBuilder,private router:Router,private cancerPredictionService:CancerPredictionService) {
    this.createPredictForm()
  


   }

   createPredictForm(){
    this.cancerFeatureForm=this.formBuilder.group({
      radius_worst:["",Validators.required],
      perimeter_worst:["",Validators.required],
      area_worst:["",Validators.required],
      perimeter_mean:["",Validators.required],
      radius_mean:["",Validators.required],
      area_mean:["",Validators.required],
      concavity_worst:["",Validators.required],
      concavity_mean:["",Validators.required],
      concave_points_mean:["",Validators.required],
      concave_points_worst:["",Validators.required],
    })
  }
  createPatientForm(){
    this.patientInfoForm=this.formBuilder.group({
      patient_name:["",Validators.required]
    })
  }
  ngOnInit() {
    this.createPatientForm();
    this.createPredictForm();
      

    }

    predict(){
    
      
      if (this.cancerFeatureForm.valid) {
       let cancerModel=Object.assign({},this.cancerFeatureForm.value)
       let patient_name=Object.assign({},this.patientInfoForm.value)
       console.log(patient_name)
       console.log(cancerModel)
       this.cancerPredictionService.savePrediction(cancerModel,patient_name.patient_name).subscribe(response=>{
        console.log("Saved Successfully")
        this.router.navigate(["/patientList"])
       },
      error=>{
        console.log("Hata!")
        this.router.navigate(["/predict"])
      }
      )
         
       }
       
      }
      // else{
      //  this.toastrService.error("Form is not valid!")
      // }
      
     
    
 
   }


  