import { ShowMessageComponent } from './show-message/show-message.component';
import { SnackComponent } from './snack/snack.component';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatDialog } from '@angular/material/dialog';
import { catchError, take } from 'rxjs/operators';

export class PopupMessage {
  severity: 'success' | 'error' | 'info' | 'debug' | 'warn';
  summary: string;
  detail: string;
}


@Injectable({
  providedIn: 'root'
})
export class MainService {

  constructor(
    private _snackBar: MatSnackBar,
    public dialog: MatDialog) {

  }

  //--------------------------------------------------------------------------------------------------------------------
  //

  popupMessage(msg: PopupMessage) {
    this._snackBar.openFromComponent(SnackComponent, {
      duration: msg.severity === 'info'? 5000 : 0,
      horizontalPosition: 'end',
      verticalPosition: 'top',
      data: {msg: msg}
    });
  }

  debugMessage(obj: object) {
    this._snackBar.openFromComponent(SnackComponent, {
      duration: 0,
      horizontalPosition: 'end',
      verticalPosition: 'top',
      data: {msg: {severity: 'debug', summary: 'Отладочное сообщение', detail: JSON.stringify(obj, null, ' ')}}
    });
  }

  infoMessage(title: string, text: string, dura = 3000) {
    this._snackBar.openFromComponent(SnackComponent, {
      duration: dura,
      horizontalPosition: 'end',
      verticalPosition: 'top',
      data: {msg: {severity: 'info', summary: title, detail: text}}
    });
  }

  warnMessage(title: string, text: string) {
    this._snackBar.openFromComponent(SnackComponent, {
      duration: 0,
      horizontalPosition: 'end',
      verticalPosition: 'top',
      data: {msg: {severity: 'warn', summary: title, detail: text}}
    });
  }

  errorMessage(title: string, text: string) {
    this._snackBar.openFromComponent(SnackComponent, {
      duration: 0,
      horizontalPosition: 'end',
      verticalPosition: 'top',
      data: {msg: {severity: 'error', summary: title, detail: text}}
    });
  }

  showMessage(title: string, text: string, options: {buttons: any, object?: any, icon?: string | null}): Promise<number> {
    return new Promise<number>((resolve, reject) => {
      const dialog = this.dialog.open(ShowMessageComponent, {
        restoreFocus: false,
        height: 'unset',
        maxHeight: 'calc(100vh - 50px)',
        maxWidth: '900px',
        minWidth: '300px',
        data: {title: title, text: text, options: options},
        autoFocus: false,
        disableClose: true,
        closeOnNavigation: true
      });
      dialog.afterClosed().pipe(take(1)).subscribe(value => {
          resolve(value);
      })
    });
  }

}
