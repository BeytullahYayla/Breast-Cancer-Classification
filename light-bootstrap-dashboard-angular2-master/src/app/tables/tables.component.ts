import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Patient } from 'app/model/Patient';
import { PatientsService } from 'app/services/patients.service';

declare interface TableData {
    headerRow: string[];
    dataRows: string[][];
}

@Component({
  selector: 'app-tables',
  templateUrl: './tables.component.html',
  styleUrls: ['./tables.component.css']
})
export class TablesComponent implements OnInit {
    public tableData1: TableData;
    public tableData2: TableData;
    patients: Patient[] = [];

  constructor(private patientsService:PatientsService,private router:Router) { }

  ngOnInit() {
      this.tableData1 = {
          headerRow: [ 'First Name', 'Middle Name', 'Last Name', 'Age', 'Gender',"Result"],
          dataRows: [
              ['1', 'Dakota Rice', 'Niger', 'Oud-Turnhout', '$36,738',"M"],
              ['2', 'Minerva Hooper', 'Curaçao', 'Sinaai-Waas', '$23,789',"M"],
              ['3', 'Sage Rodriguez', 'Netherlands', 'Baileux', '$56,142',"M"],
              ['4', 'Philip Chaney', 'Korea, South', 'Overland Park', '$38,735',"M"],
              ['5', 'Doris Greene', 'Malawi', 'Feldkirchen in Kärnten', '$63,542',"M"],
              ['6', 'Mason Porter', 'Chile', 'Gloucester', '$78,615',"M"]
          ]
      };
      this.loadPatients();
      
  }
  loadPatients(): void {
    this.patientsService.getPatients().subscribe(
      (data) => {
        this.patients = data;
        console.log('Patients loaded:', this.patients);
      },
      (error) => {
        console.error('Error loading patients:', error);
      }
    );
  }
  onDeletePatient(patientId: string): void {
    this.patientsService.deletePatient(patientId)
      .subscribe(
        () => {
          console.log('Patient deleted successfully.');
          // Handle any additional logic after deletion
        },
        error => {
          console.error('Error deleting patient:', error);
          // Handle error cases
        }
      );
  }
  updatePatient(patient: Patient): void {
    // Seçilen hastanın ID'si ile yeni bir sayfaya yönlendirme işlemi yap
    this.router.navigate(['/update-patient', patient.id]); // /update-patient/:id şeklinde parametre gönder
  }
   



}
