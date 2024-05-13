import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Patient } from 'app/model/Patient';
import { PatientsService } from 'app/services/patients.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  
  patientForm: FormGroup;

  constructor(private formBuilder: FormBuilder, private patientsService: PatientsService,private router:Router) { }

  ngOnInit(): void {
    this.patientForm = this.formBuilder.group({
      first_name: ['', Validators.required],
      middle_name: [''],
      last_name: ['', Validators.required],
      age: ['', [Validators.required, Validators.min(0)]],
      gender: ['', Validators.required]
    });
  }

  // Form submit işlemi
  onSubmit() {
    if (this.patientForm.valid) {
      this.patientsService.addPatient(this.patientForm.value)
        .subscribe(
          (addedPatient) => {
            console.log('Hasta başarıyla eklendi:', addedPatient);
            
            // Başarılı mesaj veya yönlendirme işlemi eklenebilir
            this.router.navigate(["/patientList"])
          },
          (error) => {
            console.error('Hasta eklenirken hata oluştu:', error);
            this.router.navigate(["/patient"])
            // Hata mesajı gösterilebilir veya işlem tekrar denenebilir
          }
        );
    } else {
      // Form hatalıysa kullanıcıya uyarı verilebilir
    }
  }

 

}
