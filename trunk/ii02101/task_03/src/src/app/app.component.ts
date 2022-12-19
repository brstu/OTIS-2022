import { MainService } from './main.service';
import { Edge, GraphComponent, NgxGraphModule, Node } from '@swimlane/ngx-graph';
import { AfterContentChecked, AfterViewInit, Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, AfterViewInit, AfterContentChecked {

  @ViewChild('ngxGraph') ngxGraph: GraphComponent; // спец тег для ngxGraph
  @ViewChild('divGraph') divGraph: ElementRef; // ELemetnRef - большинство html тегов

  title = 'gralex';

  constructor(public mainService: MainService) {

  }

  ngOnInit() {
  }

  ngAfterViewInit(): void {
  }

  ngAfterContentChecked(): void {
  }
}
