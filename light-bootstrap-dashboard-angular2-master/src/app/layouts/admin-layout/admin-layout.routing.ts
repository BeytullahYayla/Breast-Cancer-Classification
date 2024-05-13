import { Routes } from '@angular/router';

import { HomeComponent } from '../../home/home.component';
import { UserComponent } from '../../user/user.component';
import { TablesComponent } from '../../tables/tables.component';


export const AdminLayoutRoutes: Routes = [
    { path: 'predict',      component: HomeComponent },
    { path: 'patient',           component: UserComponent },
    { path: 'patientList',          component: TablesComponent }

];
