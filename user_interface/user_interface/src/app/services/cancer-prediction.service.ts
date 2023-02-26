import { CancerResponse } from './../model/CancerResponse';
import { Cancer } from './../model/Cancer';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class CancerPredictionService {
  apiUrl="http://127.0.0.1:8000/"


  constructor(private httpClient:HttpClient) { }

  predict(cancer:Cancer):Observable<CancerResponse>{
    let newPath=this.apiUrl+"predict"
    return this.httpClient.post<CancerResponse>(newPath,cancer)
  }

}
