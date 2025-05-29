// src/app/services/agent.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AgentService {
  constructor(private http: HttpClient) {}
// Street address is just taken since it was in the requirements, but is not used anywhere!
  runAgent(address: string, city: string, state: string, description: string): Observable<any> {
  return this.http.post('http://localhost:8000/run', {
    street: address, 
    city,
    state,
    business_description: description
  });
}

}
