import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormRunner } from './form-runner';

describe('FormRunner', () => {
  let component: FormRunner;
  let fixture: ComponentFixture<FormRunner>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormRunner]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FormRunner);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
