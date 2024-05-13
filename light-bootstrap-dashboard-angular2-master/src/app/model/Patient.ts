import { Record } from "./Record";

export class Patient {
    first_name: string;
    middle_name: string; // İsteğe bağlı olarak string veya null olabilir
    last_name: string;
    age: number;
    gender: string;
    created_at: string;
    id: string;
    records: Record[];
  }