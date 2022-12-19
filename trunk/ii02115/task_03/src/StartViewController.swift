//
//  StartViewController.swift
//  UICoreGraphics
//
//  Created by Андрей Худик on 14.11.22.
//

// сделать проверку на дурака в textView(проверка на одну вершину и текст)

import UIKit

class StartViewController: UIViewController {
    // MARK: - variables
    public var peaks = Set<String>()
    @IBOutlet weak var dataTextView: UITextView!
    @IBOutlet weak var nameOfGraphTextField: UITextField!
    @IBOutlet weak var doneButton: UIButton!
    var isAddGraph = false
    var currentGraph = 1
    var allPeaks: [Int] = []
    public var isPreview = true
    var placeholderForTextView = """
                            Пример ввода
                            1 2
                            3 2
                            4 5
                            6 7
                            """
    var nameOfGraph = ""
    override func viewDidLoad() {
        super.viewDidLoad()
        dataTextView.delegate = self
        customTextView()
        customButton()
    }
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        peaks.removeAll()
        allPeaks.removeAll()
    }
    // кастомизация кнопки
    private func customButton() {
        doneButton.layer.cornerRadius = 15
    }
    // кастомизация textView
    private func customTextView() {
        dataTextView.layer.cornerRadius = 15
        dataTextView.text = placeholderForTextView
    }
    // переход на новый view и передача данных
    @IBAction func doneButtonTapped(_ sender: Any) {
        countOfPeaks()
        if isAddGraph {
            if dataTextView.text == ""
                || dataTextView.text == placeholderForTextView {
                let alert = alert(title: "Внимание", message: "Заполните все поля")
                present(alert, animated: true, completion: nil)
            } else if nameOfGraphTextField.text == "" {
                nameOfGraph = "Graph\(currentGraph)"
            }
            nameOfGraph = nameOfGraphTextField.text ?? "Graph\(currentGraph)"
            UserDefaults.standard.set(peaks.count, forKey: "peaksGraph\(currentGraph)")
            UserDefaults.standard.set(allPeaks, forKey: "allPeaksGraph\(currentGraph)")
            UserDefaults.standard.set(nameOfGraph, forKey: "nameOfGraph\(currentGraph)")
            self.navigationController?.popViewController(animated: true)
        } else {
            if nameOfGraphTextField.text == ""
                || dataTextView.text == ""
                || dataTextView.text == placeholderForTextView {
                let alert = alert(title: "Внимание", message: "Заполните все поля")
                present(alert, animated: true, completion: nil)
            } else if nameOfGraphTextField.text == "" {
                nameOfGraph = "Graph\(currentGraph)"
            }
            nameOfGraph = nameOfGraphTextField.text ?? "Graph\(currentGraph)"
            UserDefaults.standard.set(nameOfGraph, forKey: "nameOfGraph\(currentGraph)")
            UserDefaults.standard.set(dataTextView.text, forKey: "data")
            UserDefaults.standard.set(peaks.count, forKey: "peaks")
            UserDefaults.standard.set(allPeaks, forKey: "allPeaks")
            performSegue(withIdentifier: "detail", sender: self)
        }
    }
    // скрытие клавиатуры
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        dataTextView.resignFirstResponder()
        dataTextView.layer.shadowOpacity = 0
    }
    // подсчет вершин
    public func countOfPeaks() {
        var number = ""
        for symbol in dataTextView.text {
            if symbol != " " && symbol != "\n" {
                number += String(symbol)
                continue
            } else {
                peaks.insert(number)
                allPeaks.append(Int(number)! - 1)
                number = ""
            }
        }
        let str = dataTextView.text
        guard let str = str else { return }
        for (index, element) in str.enumerated() where index == str.count - 1 {
                let char = String(element)
                allPeaks.append(Int(char)! - 1)
                peaks.insert(String(element))
        }
    }
    func getData(value: Bool, currentGraph: Int) {
        isAddGraph = value
        self.currentGraph = currentGraph
    }
}
extension StartViewController: UITextViewDelegate {
    func textViewDidBeginEditing(_ textView: UITextView) {
        if isPreview {
            textView.text = ""
            isPreview = false
        }
        dataTextView.layer.shadowColor = UIColor.black.cgColor
        dataTextView.layer.shadowOpacity = 1.0
        dataTextView.layer.shadowOffset = CGSize(width: 0, height: 0)
        dataTextView.layer.shadowRadius = 15.0
    }
}
