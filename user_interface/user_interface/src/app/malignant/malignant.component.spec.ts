import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MalignantComponent } from './malignant.component';

describe('MalignantComponent', () => {
  let component: MalignantComponent;
  let fixture: ComponentFixture<MalignantComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MalignantComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MalignantComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
