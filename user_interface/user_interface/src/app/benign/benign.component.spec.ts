import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BenignComponent } from './benign.component';

describe('BenignComponent', () => {
  let component: BenignComponent;
  let fixture: ComponentFixture<BenignComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BenignComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BenignComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
