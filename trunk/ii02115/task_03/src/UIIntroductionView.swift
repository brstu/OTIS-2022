//
//  UIIntroductionView.swift
//  UICoreGraphics
//
//  Created by Андрей Худик on 14.11.22.
//

import UIKit

@IBDesignable
class UIIntroductionView: UIView {
    // MARK: - Variables
    public var countOfPeaks = 0
    var allPeaks: [Int] = []
    var data = UserDefaults.standard.string(forKey: "data")
    var peaks = UserDefaults.standard.integer(forKey: "peaks")
    var coordinatesArray: [CGFloat] = []
    var peaksColor: [UIColor] = []
    var edgesColor: [UIColor] = []
    var firstCall = true
    var isAddPeaks = false
    var activeGraph = 1
    // MARK: - Functions
    override func draw(_ rect: CGRect) {
        guard let allPeaks = UserDefaults.standard.object(forKey: "allPeaks")
                as? [Int] else { return }
        self.allPeaks = allPeaks
        drawmth()
    }
    // изменение активного графа
    func changeGraph(countOfGraphs: Int, tag: Int, isAddGraph: Bool) {
        activeGraph = tag
        if isAddGraph {
            firstCall = true
            coordinatesArray = []
        } else {
            guard let coordinatesArray = UserDefaults.standard.object(forKey: "coordinatesGraph\(activeGraph)")
                    as? [CGFloat] else { return }
            self.coordinatesArray = coordinatesArray
        }
        guard let allPeaks = UserDefaults.standard.object(forKey: "allPeaksGraph\(activeGraph)")
                as? [Int] else { return }
        self.allPeaks = allPeaks
        guard let peaks = UserDefaults.standard.object(forKey: "peaksGraph\(activeGraph)")
                as? Int else { return }
        self.peaks = peaks
        setNeedsDisplay()
    }
    // добавление ребра
    func addEdge(edge: [Int]) {
        var edges = [Int]()
        edges.append(edge[0] - 1)
        edges.append(edge[1] - 1)
        edges.sort(by: <)
        edgesColor.append(.black)
        for element in edges {
            allPeaks.append(element)
        }
        UserDefaults.standard.set(allPeaks, forKey: "allPeaks")
        setNeedsDisplay()
    }
    // удаление ребра
    func deleteEdge(edge: [Int]) {
        var edges = [Int]()
        edges.append(edge[0] - 1)
        edges.append(edge[1] - 1)
        if allPeaks.contains(edges[0]) && allPeaks.contains(edges[1]) {
            for (index, element) in allPeaks.enumerated() {
                if element == edges[1] && allPeaks.index(before: index) == edges[0] {
                    allPeaks.remove(at: index)
                    allPeaks.remove(at: index - 1)
                    break
                } else if element == edges[0] {
                    if allPeaks.indices.contains(index + 1) {
                        if allPeaks[index + 1] == edges[1] {
                            allPeaks.remove(at: index)
                            allPeaks.remove(at: index)
                            break
                        } else if allPeaks[index - 1] == edges[1] {
                            allPeaks.remove(at: index)
                            allPeaks.remove(at: index - 1)
                            break
                        }
                    } else {
                        if allPeaks[index - 1] == edges[1] {
                            allPeaks.remove(at: index)
                            allPeaks.remove(at: index - 1)
                            break
                        }
                    }
                }
            }
        }
        setNeedsDisplay()
    }
    // удаление вершины
    func deleteDrawPeak(tag: Int) {
        var tag = tag
        tag -= 1
        coordinatesArray.remove(at: tag + 1 * tag)
        coordinatesArray.remove(at: tag + 1 * tag)
        peaks -= 1
        var count = 0
        for element in allPeaks {
            count = count < 0 ? 0 : count
            if tag == element {
                if count % 2 == 0 {
                    allPeaks.remove(at: count)
                    allPeaks.remove(at: count)
                    count -= 2
                } else {
                    allPeaks.remove(at: count)
                    allPeaks.remove(at: count - 1)
                    count -= 2
                }
            } else if element > tag && count < allPeaks.count {
                allPeaks[count] -= 1
            }
            count += 1
        }
        count = 0
        setNeedsDisplay()
    }
    // передвижение вершины
    func changePosition(coordx: CGFloat, coordy: CGFloat, tag: Int) {
        var tag = tag
        tag -= 1
        coordinatesArray[tag + 1 * tag] = coordx
        coordinatesArray[tag + 1 + 1 * tag] = coordy
        setNeedsDisplay()
    }
    // изменение цвета вершины
    func changeColor(color: UIColor, tag: Int) {
        peaksColor[tag] = color
        setNeedsDisplay()
    }
    // изменение цвета вершины
    func changeColorOfEdge(color: UIColor, edge: [Int]) {
        var indexOfEdge = 0
        for (index, element) in allPeaks.enumerated() {
            if element == edge[1] && allPeaks.index(before: index) == edge[0] {
                indexOfEdge = index / 2
                break
            } else if element == edge[0] {
                if allPeaks.indices.contains(index + 1) {
                    if allPeaks[index + 1] == edge[1] {
                        indexOfEdge = index / 2
                        break
                    }
                }
            }
        }
        edgesColor[indexOfEdge] = color
        setNeedsDisplay()
    }
    // добавление вершины
    func addPeakInView(peaks: [Int]) {
        isAddPeaks = true
        let path = CGPoint(x:
                            CGFloat(Int.random(in: 30...Int(self.frame.width - 30))),
                           y: CGFloat(Int.random(in: 30...Int(self.frame.height - 30))))
        coordinatesArray.append(path.x)
        coordinatesArray.append(path.y)
        peaksColor.append(UIColor(ciColor: .red))
        self.peaks += 1
        for element in peaks {
            edgesColor.append(.black)
            allPeaks.append(self.peaks - 1)
            allPeaks.append(element - 1)
        }
        setNeedsDisplay()
    }
    public func drawmth() {
        var path: CGRect
        // рисуются вершины
        var count2 = 0
        for element in 0..<peaks {
            if firstCall {
                path = CGRect(x: CGFloat(Int.random(in: 30...Int(self.frame.width - 30))),
                              y: CGFloat(Int.random(in: 30...Int(self.frame.height - 30))),
                              width: 10, height: 10)
                peaksColor.append(UIColor(ciColor: .red))
            } else {
                path = CGRect(x: coordinatesArray[count2], y: coordinatesArray[count2 + 1], width: 10, height: 10)
            }
            count2 += 2
            drawCircle(in: path, count: element)
        }
        // рисуются линии
        var count = 0
        for element in 0..<allPeaks.count / 2 {
            let xx1 = coordinatesArray[allPeaks[count] + 1 * allPeaks[count]]
            let yy1 = coordinatesArray[allPeaks[count] + 1 + 1 * allPeaks[count]]
            let xx2 = coordinatesArray[allPeaks[count + 1] + 1 * allPeaks[count + 1]]
            let yy2 = coordinatesArray[allPeaks[count + 1] + 1 + 1 * allPeaks[count + 1]]
            count += 2
            if firstCall {
                edgesColor.append(.black)
            }
            drawLine(point1: CGPoint(x: xx1, y: yy1), point2: CGPoint(x: xx2, y: yy2), count: element)
        }
        firstCall = false
        UserDefaults.standard.set(coordinatesArray, forKey: "coordinates")
        UserDefaults.standard.set(coordinatesArray, forKey: "coordinatesGraph\(activeGraph)")
        UserDefaults.standard.set(allPeaks, forKey: "allPeaksGraph\(activeGraph)")
        UserDefaults.standard.set(peaks, forKey: "peaksGraph\(activeGraph)")
//        UserDefaults.standard.set(peaksColor, forKey: "colorPeaksGraph\(activeGraph)")
    }
    // рисование вершин
    public func drawCircle(in rect: CGRect, count: Int) {
        let center = CGPoint(x: rect.origin.x, y: rect.origin.y)
        let radius = (rect.width * 1.2)
        let path = UIBezierPath(arcCenter: center, radius: radius, startAngle: 0, endAngle: 360, clockwise: true)
        if firstCall {
            coordinatesArray.append(center.x)
            coordinatesArray.append(center.y)
        }
        isAddPeaks = false
        path.lineWidth = 4
        path.lineCapStyle = .round
        var color = peaksColor[count]
        color.setStroke()
        path.stroke()
        color = UIColor.white
        color.setFill()
        path.fill()
    }
    // получение информации
    func getInfo() -> (Int, (Int, [Int])) {
        let countOfPeaks = peaks
        let countOfEdges = allPeaks.count / 2
        var peaksMultiplicity: [Int] = []
        var count = 0
        for element in 0...peaks - 1 {
            for element2 in allPeaks where element2 == element {
                    count += 1
            }
            peaksMultiplicity.append(count)
            count = 0
        }
        return (countOfPeaks, (countOfEdges, peaksMultiplicity))
    }
    // рисование линии для соединения вершин
    public func drawLine(point1: CGPoint, point2: CGPoint, count: Int) {
        let path = UIBezierPath()
        path.move(to: point1)
        path.addLine(to: point2)
        path.lineWidth = 2
        let color = edgesColor[count]
        color.setStroke()
        path.stroke()
    }
}
