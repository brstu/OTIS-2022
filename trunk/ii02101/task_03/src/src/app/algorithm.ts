import { Graph } from "./common/common.component";

export class Algorithm {

    matrixAjency(gr: Graph) {
        const matrix = new Array(gr.nodes.length);

        for (let i = 0; i < gr.nodes.length; i++) {
            matrix[i] = new Array(gr.nodes.length).fill(0);
        }
        for (let i = 0; i < gr.links.length; i++) {
            const source = gr.nodes.findIndex(value => {
                return value.id == gr.links[i].source;
            });
            const target = gr.nodes.findIndex(value => {
                return value.id == gr.links[i].target;
            });
            if (i >= gr.links.length) {

            }
            matrix[source][target] = gr.links[i].data.weight;
            matrix[target][source] = gr.links[i].data.weight;
        }
        return matrix;
    } // матрица смежности

    matrixIncidency(gr: Graph) {
        const matrix = new Array(gr.nodes.length);

        for (let i = 0; i < gr.nodes.length; i++) {
            matrix[i] = new Array(gr.links.length).fill(0);
        }
        for (let i = 0; i < gr.links.length; i++) {
            const source = gr.nodes.findIndex(value => {
                return value.id == gr.links[i].source;
            });
            const target = gr.nodes.findIndex(value => {
                return value.id == gr.links[i].target;
            });
            matrix[source][i] = gr.links[i].data.weight;
            matrix[target][i] = gr.links[i].data.weight;
        }
        return matrix;
    } // матрица инцидентности

    eylerCycle(gr: Graph) {
        const matrix = this.matrixAjency(gr);
        const degree = new Array(gr.nodes.length).fill(0);
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                degree[i] += matrix[i][j];
            }
        }
        let odd = 0;
        for (let i = 0; i < gr.nodes.length; i++) {
            if (degree[i] % 2 == 1) {
                odd++;
            }
        }
        if (odd == 0) {
            return true;
        }
        return false;
    } // эйлеров цикл или нет

    hamiltonCycle(gr: Graph) {
        const matrix = this.matrixAjency(gr);
        const degree = new Array(gr.nodes.length).fill(0);
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                degree[i] += matrix[i][j];
            }
        }
        let odd = 0;
        for (let i = 0; i < gr.nodes.length; i++) {
            if (degree[i] % 2 == 1) {
                odd++;
            }
        }
        if (odd == 0) {
            return true;
        }
        return false;
    } // гамильтонов цикл или нет

    completeGraph(gr: Graph) {
        const matrix = this.matrixAjency(gr);
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                if (matrix[i][j] == 0 && i != j) {
                    return false;
                }
            }
        }
        return true;
    } // полный граф или нет

    planarGraph(gr: Graph) {
        const matrix = this.matrixAjency(gr);
        const degree = new Array(gr.nodes.length).fill(0);
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                degree[i] += matrix[i][j];
            }
        }
        for (let i = 0; i < gr.nodes.length; i++) {
            if (degree[i] > 3) {
                return false;
            }
        }
        return true;
    } // планарный граф или нет

    degrees(gr: Graph) {
        const matrix = this.matrixAjency(gr);
        const degree = new Array(gr.nodes.length).fill(0);
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                if (matrix[i][j] == 1) {
                    degree[i] += 1;
                }
            }
        }
        return degree;
    } // степень всех вершин

    radiusGraph(gr: Graph){
        const matrix = this.matrixAjency(gr);
        const distance = new Array(gr.nodes.length);
        for (let i = 0; i < gr.nodes.length; i++) {
            distance[i] = new Array(gr.nodes.length);
            for (let j = 0; j < gr.nodes.length; j++) {
                if (matrix[i][j] == 0 && i != j) {
                    distance[i][j] = Infinity;
                }
                else {
                    distance[i][j] = matrix[i][j];
                }
            }
        }
        for (let k = 0; k < gr.nodes.length; k++) {
            for (let i = 0; i < gr.nodes.length; i++) {
                for (let j = 0; j < gr.nodes.length; j++) {
                    if (distance[i][j] > distance[i][k] + distance[k][j]) {
                        distance[i][j] = distance[i][k] + distance[k][j];
                    }
                }
            }
        }
        let min = Infinity;
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                if (distance[i][j] < min) {
                    min = distance[i][j];
                }
            }
        }
        const center = [];
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                if (distance[i][j] == min) {
                    center.push(i);
                }
            }
        }
        return Math.ceil(((center.length - 1)/2));
    } // радиус графа

    centerGraph(gr: Graph){
        const matrix = this.matrixAjency(gr);
        const distance = new Array(gr.nodes.length);
        for (let i = 0; i < gr.nodes.length; i++) {
            distance[i] = new Array(gr.nodes.length);
            for (let j = 0; j < gr.nodes.length; j++) {
                if (matrix[i][j] == 0 && i != j) {
                    distance[i][j] = Infinity;
                }
                else {
                    distance[i][j] = matrix[i][j];
                }
            }
        }
        for (let k = 0; k < gr.nodes.length; k++) {
            for (let i = 0; i < gr.nodes.length; i++) {
                for (let j = 0; j < gr.nodes.length; j++) {
                    if (distance[i][j] > distance[i][k] + distance[k][j]) {
                        distance[i][j] = distance[i][k] + distance[k][j];
                    }
                }
            }
        }
        let min = Infinity;
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                if (distance[i][j] < min) {
                    min = distance[i][j];
                }
            }
        }
        const center = [];
        for (let i = 0; i < gr.nodes.length; i++) {
            for (let j = 0; j < gr.nodes.length; j++) {
                if (distance[i][j] == min) {
                    center.push(i);
                }
            }
        }
        const tempf = new Array(); 
        for(let i = 0; i < center.length; i++) {
            for(let j = i + 1; j < center.length; j++) {
                if(center[i] == (center.length-1)/2) {                    
                    tempf.push(center[i]);
                }
            }
        }
        const fs = tempf[0];
        return fs;
    } // центр графа, где находятся вершины и центры графа(вершины конкретные) по условию (center.length - 1)/2
}
