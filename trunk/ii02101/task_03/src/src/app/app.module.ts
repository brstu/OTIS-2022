import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NgxGraphModule } from '@swimlane/ngx-graph'

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import {MatIconModule} from '@angular/material/icon';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatRadioModule} from '@angular/material/radio';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import {MatTabsModule} from '@angular/material/tabs';
import { MatDividerModule} from '@angular/material/divider';
import {MatSelectModule} from '@angular/material/select';
import { MatDialogModule } from '@angular/material/dialog';

import { SnackComponent } from './snack/snack.component';
import { CommonComponent } from './common/common.component';
import { ColorPickerModule } from 'ngx-color-picker';
import { ShowMessageComponent } from './show-message/show-message.component';
import { NodeEditComponent } from './node-edit/node-edit.component';
import { LinkEditComponent } from './link-edit/link-edit.component';
import { AlgShowComponent } from './alg-show/alg-show.component';

@NgModule({
  declarations: [
    AppComponent,
    SnackComponent,
    CommonComponent,
    ShowMessageComponent,
    NodeEditComponent,
    LinkEditComponent,
    AlgShowComponent
  ],
  imports: [
    BrowserModule,
    NgxGraphModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatInputModule,
    FormsModule,
    MatIconModule,
    MatCheckboxModule,
    MatRadioModule,
    MatSnackBarModule,
    MatTabsModule,
    ColorPickerModule,
    MatDividerModule,
    MatSelectModule,
    MatDialogModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
