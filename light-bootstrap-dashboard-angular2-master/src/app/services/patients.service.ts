import { CancerResponse } from '../model/CancerResponse';
import { Cancer } from '../model/Cancer';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Patient } from 'app/model/Patient';
@Injectable({
  providedIn: 'root'
})
export class PatientsService {
  apiUrl="http://localhost:8000/"

  constructor(private httpClient:HttpClient) { }

  getPatients():Observable<Patient[]>{
    return this.httpClient.get<Patient[]>(this.apiUrl+"patients/?skip=0&limit=100");
  }
  addPatient(patient:Patient):Observable<Patient>{
    return this.httpClient.post<Patient>(this.apiUrl+"addPatient",patient)
  }

  deletePatient(patientId: string): Observable<void> {
    const deletePath = `${this.apiUrl}/patients/`+patientId;
    return this.httpClient.delete<void>(deletePath);
  }
  updatePatient(patient:Patient): Observable<Patient> {
    const updatePath = `${this.apiUrl}updatePatient}`;
    return this.httpClient.put<Patient>(updatePath, patient);
  }
}
