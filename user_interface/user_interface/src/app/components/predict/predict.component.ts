import { ToastrModule, ToastrService } from 'ngx-toastr';
import { Cancer } from './../../model/Cancer';
import { CancerPredictionService } from './../../services/cancer-prediction.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent implements OnInit {

  prediction:any
  cancerFeatureForm: FormGroup = new FormGroup({});

  /**
   *
   */
  constructor(private cancerPredictionService:CancerPredictionService,
    private formBuilder:FormBuilder,
    private toastrService:ToastrService
    ) {
      this.createPredictForm()
      
    
  }
  ngOnInit(): void {
    this.createPredictForm()
  }
  
 

  createPredictForm(){
    this.cancerFeatureForm=this.formBuilder.group({
     
      radius_mean:["",Validators.required],
      texture_mean:["",Validators.required],
      perimeter_mean:["",Validators.required],
      area_mean:["",Validators.required],
      smoothness_mean:["",Validators.required],
      compactness_mean:["",Validators.required],
      concavity_mean:["",Validators.required],
      concave_points_mean:["",Validators.required],
      symmetry_mean:["",Validators.required],
      fractal_dimension_mean:["",Validators.required],
      radius_se:["",Validators.required],
      texture_se:["",Validators.required],
      perimeter_se:["",Validators.required],
      area_se:["",Validators.required],
      smoothness_se:["",Validators.required],
      compactness_se:["",Validators.required],
      concavity_se:["",Validators.required],
      concave_points_se:["",Validators.required],
      symmetry_se:["",Validators.required],
      fractal_dimension_se:["",Validators.required],
      radius_worst:["",Validators.required],
      texture_worst:["",Validators.required],
      perimeter_worst:["",Validators.required],
      area_worst:["",Validators.required],
      smoothness_worst:["",Validators.required],
      compactness_worst:["",Validators.required],
      concavity_worst:["",Validators.required],
      concave_points_worst:["",Validators.required],
      symmetry_worst:["",Validators.required],
      fractal_dimension_worst:["",Validators.required]
     

    })
  }

  





  predict(){
    
      
     if (this.cancerFeatureForm.valid) {
      let cancerModel=Object.assign({},this.cancerFeatureForm.value)
      console.log(cancerModel)
      this.cancerPredictionService.predict(cancerModel).subscribe(response=>{
        if(response.prediction.includes(0)){
          console.log("Malignant")
          return 0
        }
        else{
          console.log("Benign")
          return 1
        }
      })
      
     }
     else{
      this.toastrService.error("Form is not valid!")
     }
     
    
   

  }
}
console.log("Gecersiz")

