//
//  InfoViewController.swift
//  UICoreGraphics
//
//  Created by Андрей Худик on 12.12.22.
//

import UIKit

class InfoViewController: UIViewController {
    @IBOutlet weak var numberOfEdgesLabel: UILabel!
    @IBOutlet weak var numberOfPeaksLabel: UILabel!
    @IBOutlet weak var multiplicityCurrentPeakLabel: UILabel!
    @IBOutlet weak var multiplicityAllPeaksLabel: UILabel!
    var numberOfPeaks = ""
    var numberOfEdges = ""
    var multiplicityAll = ""
    var multiplicityCurrentPeak = ""
    override func viewDidLoad() {
        super.viewDidLoad()
        numberOfPeaksLabel.text? += numberOfPeaks
        numberOfEdgesLabel.text? += numberOfEdges
        multiplicityAllPeaksLabel.text? += multiplicityAll
        multiplicityCurrentPeakLabel.text? += multiplicityCurrentPeak
    }
    func getInfo(info: (Int, (Int, [Int])), peak: Int?) {
        numberOfPeaks +=  String(info.0)
        numberOfEdges += String(info.1.0)
        for (index, element) in info.1.1.enumerated() {
            multiplicityAll += String(index + 1) + ": " + String(element) + " "
        }
        guard let peak = peak else {
            multiplicityCurrentPeak = "Вершина не выбрана"
            return
        }
        multiplicityCurrentPeak += String(info.1.1[peak - 1])
    }
}
