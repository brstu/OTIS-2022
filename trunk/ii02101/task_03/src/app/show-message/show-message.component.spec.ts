import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowMessageComponent } from './show-message.component';

describe('ShowMessageComponent', () => {
  let component: ShowMessageComponent;
  let fixture: ComponentFixture<ShowMessageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowMessageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowMessageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
