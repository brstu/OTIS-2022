//
//  Extensions.swift
//  UICoreGraphics
//
//  Created by Андрей Худик on 29.11.22.
//

import Foundation
import UIKit

extension String {
    func arrayStringToInt(content: [String]) -> [Int] {
        var intArray: [Int] = []
        for element in content {
                intArray.append(Int(element) ?? 1)
        }
        return intArray
    }
}
public func alertWithTextField(title: String,
                               message: String,
                               placeholder: String?,
                               handler: ((_ int: [Int], _ string: String) -> Void)?) -> UIViewController {
    var peaksString: [String] = []
    var peaksInt: [Int] = []
    var name = String()
    let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
    alert.addTextField { (textField: UITextField!) -> Void in
        textField.placeholder = placeholder
    }
    let okey = UIAlertAction(title: "Ok", style: .default) { _ in
        name = alert.textFields![0].text ?? ""
        peaksString = (alert.textFields![0].text?.components(separatedBy: " "))!
        peaksInt = peaksString.description.arrayStringToInt(content: peaksString)
        if let handler = handler {
            handler(peaksInt, name)
        }
    }
    alert.addAction(okey)
    return alert
}
public func actionSheet(titleForFirstAction: String,
                        titleForSecondAction: String,
                        closureForFirstAction: @escaping  () -> Void,
                        closureForSecondAction: @escaping () -> Void) -> UIViewController {
    let alert = UIAlertController(title: "Внимание", message: "Выберите действие", preferredStyle: .actionSheet)
    let deletePeak = UIAlertAction(title: titleForFirstAction, style: .default) { _ in
        closureForFirstAction()
    }
    let deleteEdge = UIAlertAction(title: titleForSecondAction, style: .default) { _ in
        closureForSecondAction()
    }
    let cancel = UIAlertAction(title: "Отмена", style: .cancel)
    alert.addAction(deletePeak)
    alert.addAction(deleteEdge)
    alert.addAction(cancel)
    return alert
}
public func alert(title: String, message: String) -> UIViewController {
    let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
    let okey = UIAlertAction(title: "OK", style: .default)
    alert.addAction(okey)
    return alert
}
