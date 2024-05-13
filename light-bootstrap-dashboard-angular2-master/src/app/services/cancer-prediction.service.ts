import { CancerResponse } from './../model/CancerResponse';
import { Cancer } from './../model/Cancer';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Record } from 'app/model/Record';
@Injectable({
  providedIn: 'root'
})
export class CancerPredictionService {
  apiUrl="http://localhost:8000/"


  constructor(private httpClient:HttpClient) { }

  predict(cancer:Cancer):Observable<CancerResponse>{
    let newPath=this.apiUrl+"predict"
    return this.httpClient.post<CancerResponse>(newPath,cancer)
  }
  savePrediction(cancer:Cancer,patient_name:string):Observable<Cancer>{
    let newPath=this.apiUrl+"savePrediction?patient_name="+patient_name
    return this.httpClient.post<Cancer>(newPath,cancer)

  }
   

}

