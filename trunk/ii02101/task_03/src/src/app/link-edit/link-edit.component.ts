import { Component, Inject, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatDialogClose } from '@angular/material/dialog';
import { Edge, GraphComponent, NgxGraphModule, Node } from '@swimlane/ngx-graph';

@Component({
  selector: 'app-link-edit',
  templateUrl: './link-edit.component.html',
  styleUrls: ['./link-edit.component.css']
})
export class LinkEditComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<LinkEditComponent>,
    @Inject(MAT_DIALOG_DATA) public data: Edge
  ) {
    if (data.data == undefined || data.data.weight == undefined) {
      data.data = {weight: 1};
    }

  }

  ngOnInit(): void {
  }

  close() {
    this.dialogRef.close(this.data);
  }

}
