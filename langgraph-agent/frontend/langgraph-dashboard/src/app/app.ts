import { Component } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { FormRunner } from './components/form-runner/form-runner';
import { provideHttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormRunner],
  template: `<app-form-runner></app-form-runner>`
})
export class App {}

bootstrapApplication(App, {
  providers: [provideHttpClient()]
});
