import { Component, Inject, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatDialogClose } from '@angular/material/dialog';
import { Edge, GraphComponent, NgxGraphModule, Node } from '@swimlane/ngx-graph';


@Component({
  selector: 'app-alg-show',
  templateUrl: './alg-show.component.html',
  styleUrls: ['./alg-show.component.css']
})
export class AlgShowComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<AlgShowComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
  }

  ngOnInit(): void {
  }

  close() {
    this.dialogRef.close();
  }
}
