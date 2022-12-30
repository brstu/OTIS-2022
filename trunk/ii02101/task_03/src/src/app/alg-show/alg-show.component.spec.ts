import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlgShowComponent } from './alg-show.component';

describe('AlgShowComponent', () => {
  let component: AlgShowComponent;
  let fixture: ComponentFixture<AlgShowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlgShowComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AlgShowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
