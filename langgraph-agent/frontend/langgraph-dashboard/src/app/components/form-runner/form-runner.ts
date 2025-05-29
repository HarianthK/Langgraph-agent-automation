import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AgentService } from '../../services/agent';

@Component({
  selector: 'app-form-runner',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './form-runner.html',
  styleUrls: ['./form-runner.css']
})
export class FormRunner {
  address: string = '';
  city: string = '';
  state: string = '';
  description: string = '';
  isLoading: boolean = false;
  result: any = null;
  error: string | null = null;

  constructor(private agentService: AgentService) {}

  runAgent() {
    this.isLoading = true;
    this.result = null;
    this.error = null;

    this.agentService.runAgent(this.address, this.city, this.state, this.description).subscribe({
      next: (res: any) => {
        this.result = res;
        this.isLoading = false;
      },
      error: (err: any) => {
        this.error = '❌ Agent failed to run';
        console.error(err);
        this.isLoading = false;
      }
    });
  }
}
