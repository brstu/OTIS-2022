import { AnyTools } from './../helpers/tools';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Component, Inject, OnInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-show-message',
  templateUrl: './show-message.component.html',
  styleUrls: ['./show-message.component.css']
})
export class ShowMessageComponent implements OnInit {

  @ViewChild('divObject') divObject: ElementRef;
  objectHtml = '';
  textAreaString = '';

  constructor(
    public dialogRefMsg: MatDialogRef<ShowMessageComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    ) {
      if (this.data.options.object !== undefined) {
        this.textAreaString = JSON.stringify(this.data.options.object, null, 4);
        //this.objectHtml = new AnyTools().highlight(this.data.options.object, {useTabs: true});
      }
    }

  ngOnInit(): void {
  }

  close(value: number) {
    this.dialogRefMsg.close(value);
  }

  syntaxHighlight(json: string) {
    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    let spCnt = 0;
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|\b({|})\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        } else if (match === '{')
          spCnt ++;
        else if (match === '}')
          spCnt --;

        let sp = '';
        for (let i = 0; i < spCnt; i ++)
          sp += '&nbsp;';

        return (cls==='key'? '<br/>' : '') + sp + '<span class="' + cls + '">' + match + '</span>';
    });
  }
}
