import { MainService } from './../main.service';
import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

import {Clipboard} from '@angular/cdk/clipboard';
import { Algorithm } from '../algorithm';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatDialogClose } from '@angular/material/dialog';
import { NodeEditComponent } from '../node-edit/node-edit.component';
import { Edge, GraphComponent, NgxGraphModule, Node } from '@swimlane/ngx-graph';
import { LinkEditComponent } from '../link-edit/link-edit.component';
import { AlgShowComponent } from '../alg-show/alg-show.component';

export class Graph {

  nodes: Node[] = [];
  links: Edge[] = [];
  name: string = '';
  type: string = 'UNORIENT';
  layout: string = 'dagre';
}

export class MDIGraph {
  graph: Graph;
  update: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  center: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);
  zoomToFit: BehaviorSubject<number> = new BehaviorSubject<number>(100);
}

@Component({
  selector: 'app-common',
  templateUrl: './common.component.html',
  styleUrls: ['./common.component.css']
})
export class CommonComponent implements OnInit {

  @ViewChild('inputNewNode') inputNewNode: ElementRef;

  graphs: MDIGraph[] = [];
  graphTab = 0;
  selectedMDIGraph: MDIGraph = null;
  graphType = 'ORIENT';
  layouts = ['d3ForceDirected', 'dagre'];

  newGraphName = '';
  newNodeName = '';
  newNodeColor = 'green';
  colors = ['red', 'green', 'blue'];
  graphWidth = 1024;
  graphHeight = 800;

  selectedNode: string = '';
  selected1Node: string = '';
  selected2Node: string = '';
  selectedLink: string = '';

  constructor(
    public mainService: MainService,
    public dialog: MatDialog) {

  }

  ngOnInit(): void {
    const savedGraphs = localStorage.getItem('graphs');
    if (savedGraphs != null) {}
    JSON.parse(savedGraphs).forEach((element: Graph) => {
      const newMdi = new MDIGraph();
      newMdi.graph = element;
      this.graphs.push(newMdi);
    });
    if (this.graphs.length > 0)
      this.selectedMDIGraph = this.graphs[0];
  }

  graphTabChange(event) {
    this.selectedMDIGraph = this.graphs[event.index];
    this.selectedNode = '';
  }

  saveGraphs() {
    const outGraphs = [];
    this.graphs.forEach(element => {
      outGraphs.push(element.graph);
    });
    localStorage.setItem('graphs', JSON.stringify(outGraphs));
  }

  //-------------------------------------------------------------------------------------------------------------------

  addEmptyGraph() {
    if (this.newGraphName == '') {
      this.mainService.infoMessage('Добавление графа', 'Имя не должно быть пустым');
      return;
    }
    const mdiGr = new MDIGraph();
    mdiGr.graph = new Graph();
    mdiGr.graph.name = this.newGraphName;
    this.newGraphName = '';
    mdiGr.graph.type = this.graphType;
    this.graphs.push(mdiGr);
  }

  removeGraph() {
    const mdi = this.getGraph();
    if (mdi == null)
      return;

    this.mainService.showMessage('Удаление графа', 'Удалить граф \"' + mdi.graph.name + '\"?', {buttons: ['Удалить', 'Отмена']}).then(value => {
      if (value == 0)
        this.graphs.splice(this.graphTab, 1);
    });
  }

  loadFromClipboard() {
    const value = navigator.clipboard.readText().then(value => {
      try {
      const mdiGr = new MDIGraph();
      mdiGr.graph = this.convertTextData(value);
      this.graphs.push(mdiGr);
      mdiGr.update.next(true);
      this.graphTab = this.graphs.length - 1;
      } catch (e) {
       this.mainService.errorMessage('Ошибка', 'Ошибка при чтении данных из буфера обмена');
      }
    });
  }

  loadFromFile(event) {
    const reader = new FileReader();
    reader.onload = (e: any) => {
      const mdiGr = new MDIGraph();
      mdiGr.graph = this.convertTextData(e.target.result);
      this.graphs.push(mdiGr);
      mdiGr.update.next(true);
      this.graphTab = this.graphs.length - 1;
    };
    reader.readAsText(event.target.files[0]);
  }

  convertTextData(value: string): Graph {

    const gr = new Graph();
    const lines = value.split(';');

    const namegr = lines[0].split(':');
    gr.name = namegr[0];
    gr.type = namegr[1];

    lines[1].split(',').forEach(element => {
      gr.nodes.push({id: element.trim(), label: element.trim(), data: {color2: 'red', colorText: 'white'}, dimension: {width: 35, height: 40}});
    });

    lines[2].split(',').forEach(element => {
      const link =  element.split('->')
        link[0] = link[0].trim();
        link[1] = link[1].trim();
        if (link[1].lastIndexOf('.') == link[1].length - 1)
          link[1] = link[1].substring(0, link[1].length - 1);
        gr.links.push({id: link[0].trim() + '_' + link[1].trim(), source: link[0].trim(), target: link[1].trim(), label: link[0]+'_'+link[1], data: {stroke: 'black', weight: 1}});
    });

    return gr;
  }


  //-------------------------------------------------------------------------------------------------------------------

  getGraph(): MDIGraph {
    if (this.graphs.length > 0 && this.graphTab < this.graphs.length) {
      return this.graphs[this.graphTab];
    }
    return null;
  }

  addNode() {
    if (this.newNodeName == '') {
      this.mainService.infoMessage("Добавление вершины", 'Пустое имя');
      return;
    }

    const mdi = this.getGraph();
    if (mdi == null)
      return;

    if (this.isNode(this.newNodeName, mdi)) {
      this.mainService.infoMessage("Добавление вершины", 'Такая вершина уже есть');
      return;
    }

    mdi.graph.nodes.push({
      id: this.newNodeName,
      label: this.newNodeName,
      data: {color2: this.newNodeColor, colorText: 'white'},
      dimension: {width: 42, height: 42}
    });
    mdi.update.next(true);

    this.newNodeName = '';
    this.inputNewNode.nativeElement.focus();
    //mdi.saveGraph();
  } // добавление вершины

  addLink() {
    if (this.selected1Node == this.selected2Node) {
      this.mainService.infoMessage("Добавление ребра", 'Выбрана одна и та же вершина');
      return;
    }

    const mdi = this.getGraph();
    if (mdi == null)
      return;

    if (!this.isNode(this.selected1Node, mdi) || !this.isNode(this.selected2Node, mdi)) {
      this.mainService.infoMessage("Добавление ребра", 'Не выбрана вершина');
      return;
    }

    let found = mdi.graph.links.find((value) => {
      return (value.source == this.selected1Node && value.target == this.selected2Node) || (value.target == this.selected1Node && value.source == this.selected2Node);
    });
    if (!found) {
        mdi.graph.links.push(
          {
            id: this.selected1Node + '_' + this.selected2Node,
            source: this.selected1Node,
            target: this.selected2Node,
            label: this.selected1Node + '->' + this.selected2Node,
            data: {weight: 1}
          }
        );
      mdi.update.next(true);
      this.mainService.infoMessage("Добавление связи", 'Добавлена связь');
    } else {
      this.mainService.infoMessage("Добавление связи", 'Такая связь уже есть');
    }
    // this.saveGraph();
  } // добавление связи

  removeNode() {
    const mdi = this.getGraph();
    if (mdi == null)
      return;

    if (!this.isNode(this.selectedNode, mdi)) {
      this.mainService.infoMessage("Удаление вершины", 'Не выбрана вершина');
      return;
    }

    let nodeIdx = mdi.graph.nodes.findIndex(value =>{
      return value.id == this.selectedNode;
    });
    let id = mdi.graph.nodes[nodeIdx].id;
    mdi.graph.nodes.splice(nodeIdx, 1);

    let linkIdx = -1;
    do {
      linkIdx = mdi.graph.links.findIndex(link => {
        return (link.source == id || link.target == id);
      });
      if (linkIdx >= 0)
      mdi.graph.links.splice(linkIdx, 1);
    } while (linkIdx >= 0);

    mdi.update.next(true);
    this.selectedNode = '';
    // this.saveGraph();
  } // удаление вершины

  renameNode() {
    const mdi = this.getGraph();
    if (mdi == null)
      return;

      if (!this.isNode(this.selectedNode, mdi)) {
        this.mainService.infoMessage('Вершина переименована', 'Не выбрана вершина');
        return;
      }
  }

  isNode(id: string, mdi: MDIGraph) {
    return mdi.graph.nodes.find(value => {
      return value.id == id;
    });
  } // проверка на вершину

  isLink(id: string, mdi: MDIGraph) {
    return mdi.graph.links.find(value => {
      return value.id == id;
    });
  } // проверка на ребро

  removeLink() {
    const mdi = this.getGraph();
    if (mdi == null)
      return;
    if (!this.isLink(this.selectedLink, mdi)) {
      this.mainService.infoMessage("Удаление ребра", 'Не выбрано ребро');
      return;
    }

    let linkIdx = mdi.graph.links.findIndex(value =>{
      return value.id == this.selectedLink;
    });
    mdi.graph.links.splice(linkIdx, 1);
    mdi.update.next(true);
  }

  fAdjencyMatrix() {
    const g = this.getGraph();
    const gr = new Algorithm();
    let fs = gr.matrixAjency(g.graph);
    this.algShow(fs);

  }
  fIncendencyMatrix() {
    this.getGraph();
    const gr = new Algorithm();
    let fs = gr.matrixIncidency(this.selectedMDIGraph.graph);    
    this.algShow(fs);

  }

  fEylerCycle() {
    this.getGraph();
    const gr = new Algorithm();
    let fs = gr.eylerCycle(this.selectedMDIGraph.graph);
    if (fs == true) {
      this.mainService.showMessage('Проверка на Эйлеров цикл', JSON.stringify('есть Эйлеров цикл'), {buttons: ['Закрыть']});
    }
    else{
      this.mainService.showMessage('Проверка на Эйлеров цикл', JSON.stringify('нет Эйлерова цикла'), {buttons: ['Закрыть']});
    }
  }

  fHamiltonCycle() {
    this.getGraph();
    const gr = new Algorithm();
    let fs = gr.hamiltonCycle(this.selectedMDIGraph.graph);
    if (fs == true) {
      this.mainService.showMessage('Проверка на Эйлеров цикл', JSON.stringify('есть Гамильнов цикл'), {buttons: ['Закрыть']});
    }
    else{
      this.mainService.showMessage('Проверка на Эйлеров цикл', JSON.stringify('нет Гамильнова цикла') , {buttons: ['Закрыть']});
    }
  }

  fCompleteGraph() {
    this.getGraph();
    const gr = new Algorithm();
    let fs = gr.completeGraph(this.selectedMDIGraph.graph);
    if(fs == true) {
    this.mainService.showMessage('Проверка на полность графа', JSON.stringify('Граф полный'), {buttons: ['Закрыть']});
    } else {
      this.mainService.showMessage('Проверка на полность графа', JSON.stringify('Граф не полный'), {buttons: ['Закрыть']});
    }
  }

  fPlanarGraph() {
    this.getGraph();
    const gr = new Algorithm();
    let fs = gr.planarGraph(this.selectedMDIGraph.graph);
    if(fs == true) {
    this.mainService.showMessage('Проверка на планарность графа', JSON.stringify('Граф планарный'), {buttons: ['Закрыть']});
    } else {
      this.mainService.showMessage('Проверка на планарность графа', JSON.stringify('Граф не планарный'), {buttons: ['Закрыть']});
    }
  }

  fDegrees() {
    this.getGraph();
    const gr = new Algorithm();
    let fs = gr.degrees(this.selectedMDIGraph.graph);
    this.mainService.showMessage('Степени вершин', JSON.stringify(fs), {buttons: ['Закрыть']});
  }
  
  fRadiusGraph() {
    this.getGraph();
    const gr = new Algorithm();
    let fs = gr.radiusGraph(this.selectedMDIGraph.graph);
    this.mainService.showMessage('Радиус графа', JSON.stringify(fs), {buttons: ['Закрыть']});
  }

  fCenterGraph() {
    this.getGraph();
    const gr = new Algorithm();
    let fs = gr.centerGraph(this.selectedMDIGraph.graph);
    this.mainService.showMessage('Центр графа', JSON.stringify(fs), {buttons: ['Закрыть']});
  }

  nodeDblClick(graph: MDIGraph, node: Node) {

    const dialogRef = this.dialog.open(NodeEditComponent, {
      restoreFocus: false,
      width: '400px',
      data: node,
      autoFocus: false,
      disableClose: true
    });

    const s = dialogRef.afterClosed().subscribe((result: Node) => {
      const fnode = graph.graph.nodes.find(value => {
        return value.id == node.id;
      });
      fnode.label = result.label;
      graph.update.next(true);
      s.unsubscribe();
      this.saveGraphs();
    });
  }

  linkDblClick(graph: MDIGraph, link: Edge) {

    const dialogRef = this.dialog.open(LinkEditComponent, {
      restoreFocus: false,
      width: '300px',
      data: link,
      autoFocus: false,
      disableClose: true
    });

    const s = dialogRef.afterClosed().subscribe((result: Edge) => {
      const flink = graph.graph.links.find(value => {
        return value.id == link.id;
      });
      flink.data = {weight: result.data.weight};
      graph.update.next(true);
      s.unsubscribe();
      this.saveGraphs();
    });

  }

  toCenter() {
    const mdi = this.getGraph();
    if (mdi == null)
      return;
    mdi.center.next(true);
  }
  zoomToFit() {
    const mdi = this.getGraph();
    if (mdi == null)
      return;
    mdi.zoomToFit.next(100);
  }

  algShow(data: any) {
    const dialogRef = this.dialog.open(AlgShowComponent, {
      restoreFocus: false,
      width: '400px',
      data: data,
      autoFocus: false,
      disableClose: true
    });
  }
}
