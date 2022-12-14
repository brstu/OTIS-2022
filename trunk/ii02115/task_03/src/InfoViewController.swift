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
    override func viewDidLoad() {
        super.viewDidLoad()
        numberOfPeaksLabel.text? += numberOfPeaks
        numberOfEdgesLabel.text? += numberOfEdges
        multiplicityAllPeaksLabel.text? += multiplicityAll
    }
    
    func getInfo(info: (Int, Int, [Int])) {
        numberOfPeaks +=  String(info.0)
        numberOfEdges += String(info.1)
        for (index, element) in info.2.enumerated() {
            multiplicityAll += String(index + 1) + "." + String(element) + " "
        }
    }

}
