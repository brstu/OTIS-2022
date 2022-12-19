import { Component, Inject, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatDialogClose } from '@angular/material/dialog';
import { Edge, GraphComponent, NgxGraphModule, Node } from '@swimlane/ngx-graph';

@Component({
  selector: 'app-node-edit',
  templateUrl: './node-edit.component.html',
  styleUrls: ['./node-edit.component.css']
})
export class NodeEditComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<NodeEditComponent>,
    @Inject(MAT_DIALOG_DATA) public data: Node) { }

  ngOnInit(): void {

  }

  close() {
    this.dialogRef.close(this.data);
  }
}
