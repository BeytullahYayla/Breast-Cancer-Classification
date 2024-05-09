import { ToastrModule, ToastrService } from 'ngx-toastr';
import { Cancer } from './../../model/Cancer';
import { CancerPredictionService } from './../../services/cancer-prediction.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
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
    private toastrService:ToastrService,
    private router:Router
    ) {
      this.createPredictForm()
      
    
  }
  ngOnInit(): void {
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

  





  predict(){
    
      
     if (this.cancerFeatureForm.valid) {
      let cancerModel=Object.assign({},this.cancerFeatureForm.value)
      console.log(cancerModel)
      this.cancerPredictionService.predict(cancerModel).subscribe(response=>{
        if(response.prediction.includes(0)){
          this.toastrService.success("Prediction is successfully completed!")
          this.router.navigate(["/malignant"])
          console.log("malignant")
          
          return 0
        }
        else{
          console.log("Benign")
          this.toastrService.success("Prediction is successfully completed!")
          this.router.navigate(["/benign"])
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

