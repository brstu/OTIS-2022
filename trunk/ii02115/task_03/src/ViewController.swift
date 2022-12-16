//
//  ViewController.swift
//  UICoreGraphics
//
//  Created by Андрей Худик on 14.11.22.
//

import UIKit

class ViewController: UIViewController {
    // MARK: - Variables
    @IBOutlet weak var toolbar: UINavigationItem!
    var nameOfGraph: String?
    var buttonsScrollView = UIScrollView()
    var pageScrollView = UIScrollView()
    var buttonBarView = UIView()
    var button = UIButton()
    var buttonFoAddPeak = UIButton()
    var deleteButton = UIButton()
    var colorButton = UIButton()
    var infoButton = UIButton()
    var data = ""
    var buttonsForPeaks: [UIButton] = []
    var buttonsForPages: [UIButton] = []
    var pseudoNames: [String] = []
    var tagOfSelectedButton: Int?
    var isClear = false
    var isAdd = false
    var isFirstCall = true
    var isChangeColorOfPeak = true
    var countOfGraphs = 1
    var totalWidthForPagesButtons = 0.0
    var edgeForChangeColor: [Int] = [0, 0]
    var selectedColor = UIColor(ciColor: .black)
    var activeGraph = 1
    
    @IBOutlet weak var drawingView: UIIntroductionView!
    // MARK: - LifeCycles
    override func viewDidLoad() {
        super.viewDidLoad()
        drawButtons()
        createButtonBarView()
        createScroll()
        createButtons()
        actionsForButtons()
        makePageScrollView()
        makeButtonsForPages()
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        if isAdd {
            let tempButton = UIButton()
            tempButton.tag = countOfGraphs
            makeButtonsForPages()
            changeGraph(param: tempButton)
        }
        isAdd = false
    }
    
    // MARK: - Functions
    // рисование кнопок поверх вершин
    private func drawButtons() {
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.2) {
            let paths = UserDefaults.standard.object(forKey: "coordinatesGraph\(self.activeGraph)") as? [CGFloat]
            guard let paths = paths else { return }
            var count = 0
            for element in 1...paths.count / 2 {
                if self.isFirstCall {
                    self.pseudoNames.append(String(element))
                }
                let button = UIButton(frame: CGRect(x: paths[count] - 10,
                                                    y: paths[count + 1] - 10,
                                                    width: 20, height: 20))
                button.setTitle(self.pseudoNames[element - 1], for: .normal)
                button.setTitleColor(.magenta, for: .normal)
                let doubleTap = UITapGestureRecognizer(target: self, action: #selector(self.renamePeak(param:)))
                doubleTap.numberOfTapsRequired = 2
                let drag = UIPanGestureRecognizer(target: self, action: #selector(self.movePeak(param:)))
                button.addTarget(self, action: #selector(self.forButton(param:)), for: .touchUpInside)
                button.addGestureRecognizer(drag)
                button.addGestureRecognizer(doubleTap)
                button.tag = element
                self.drawingView.addSubview(button)
                self.buttonsForPeaks.append(button)
                count += 2
            }
            self.isFirstCall = false
        }
    }
    
    // переименование вершины
    @objc func renamePeak(param: UITapGestureRecognizer) {
        let tag = param.view?.tag
        guard let tag = tag else { return }
        self.present(alertWithTextField(title: "Внимание",
                                        message: "Введите новое имя вершины",
                                        placeholder: "56") { name, _ in
            self.pseudoNames[tag - 1] = String(name[0])
            for element in self.buttonsForPeaks {
                element.removeFromSuperview()
            }
            self.drawButtons()
        }, animated: true, completion: nil)
    }
    
    // создание pageScrollView
    func makePageScrollView() {
        pageScrollView = UIScrollView()
        pageScrollView.translatesAutoresizingMaskIntoConstraints = false
        pageScrollView.showsHorizontalScrollIndicator = false
        view.addSubview(pageScrollView)
        pageScrollView.alwaysBounceHorizontal = true
        NSLayoutConstraint.activate([
            pageScrollView.topAnchor.constraint(equalTo: view.topAnchor, constant: 85),
            pageScrollView.bottomAnchor.constraint(equalTo: drawingView.topAnchor),
            pageScrollView.leftAnchor.constraint(equalTo: view.leftAnchor),
            pageScrollView.rightAnchor.constraint(equalTo: view.rightAnchor)
        ])
        pageScrollView.contentInset.right = view.bounds.width
    }
    
    @IBAction func addPageButtonTapped(_ sender: Any) {
        countOfGraphs += 1
        isFirstCall = true
        activeGraph = countOfGraphs
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        let viewController = storyboard.instantiateViewController(withIdentifier: "first")
        as? StartViewController
        guard let viewController = viewController else { return }
        viewController.modalPresentationStyle = .fullScreen
        viewController.modalTransitionStyle = .crossDissolve
        isAdd = true
        viewController.getData(value: isAdd, currentGraph: countOfGraphs)
        show(viewController, sender: nil)
    }
    
    // кнопки для pageScrollView
    func makeButtonsForPages() {
        let button = UIButton()
        nameOfGraph = UserDefaults.standard.string(forKey: "nameOfGraph\(countOfGraphs)")
        button.translatesAutoresizingMaskIntoConstraints = false
        button.setTitle(nameOfGraph, for: .normal)
        button.backgroundColor = .darkGray
        button.tag = countOfGraphs
        if button.tag == 1 {
            button.backgroundColor = #colorLiteral(red: 0.8039215803, green: 0.8039215803, blue: 0.8039215803, alpha: 1)
        } else if isAdd {
            button.backgroundColor = #colorLiteral(red: 0.8039215803, green: 0.8039215803, blue: 0.8039215803, alpha: 1)
        }
        button.setTitleColor(.black, for: .normal)
        let doubleTap = UITapGestureRecognizer(target: self, action: #selector(renamePage(param:)))
        doubleTap.numberOfTapsRequired = 2
        button.addGestureRecognizer(doubleTap)
        button.addTarget(self, action: #selector(changeGraph(param:)), for: .touchUpInside)
        pageScrollView.addSubview(button)
        NSLayoutConstraint.activate([
            button.leftAnchor.constraint(equalTo: pageScrollView.leftAnchor,
                                         constant: CGFloat(150 * buttonsForPages.count)),
            button.topAnchor.constraint(equalTo: pageScrollView.topAnchor),
            button.bottomAnchor.constraint(equalTo: pageScrollView.bottomAnchor),
            button.widthAnchor.constraint(equalToConstant: 150)
        ])
        totalWidthForPagesButtons += 150
        if totalWidthForPagesButtons > view.bounds.width {
            pageScrollView.contentInset.right = totalWidthForPagesButtons
        }
        buttonsForPages.append(button)
    }
    
    // переименование страницы
    @objc func renamePage(param: UITapGestureRecognizer) {
        let tag = param.view?.tag
        guard let tag = tag else { return }
        self.present(alertWithTextField(title: "Внимание",
                                        message: "Введите новое имя страницы",
                                        placeholder: "Some graph",
                                        handler: { _, name in
            UserDefaults.standard.set(name, forKey: "nameOfGraph\(tag)")
            for element in self.buttonsForPages {
                element.removeFromSuperview()
            }
            self.buttonsForPages.removeAll()
            self.totalWidthForPagesButtons -= 150
            self.makeButtonsForPages()
        }), animated: true, completion: nil)
    }
    
    // action дл кнопок в pages
    @objc func changeGraph(param: UIButton) {
        param.backgroundColor = #colorLiteral(red: 0.8039215803, green: 0.8039215803, blue: 0.8039215803, alpha: 1)
        for element in buttonsForPages where element.tag != param.tag {
            element.backgroundColor = .darkGray
        }
        drawingView.changeGraph(countOfGraphs: countOfGraphs, tag: param.tag, isAddGraph: isAdd)
        for element in 0..<buttonsForPeaks.count {
            buttonsForPeaks[element].removeFromSuperview()
        }
        activeGraph = param.tag
        buttonsForPeaks.removeAll()
        drawButtons()
        isAdd = false
    }
    
    // определение выыбранной вершины
    @objc func forButton(param: UIButton) {
        if tagOfSelectedButton == param.tag {
            tagOfSelectedButton = nil
            param.setTitleColor(.purple, for: .normal)
        } else {
            for element in buttonsForPeaks {
                element.setTitleColor(.purple, for: .normal)
            }
            tagOfSelectedButton = param.tag
            param.setTitleColor(.green, for: .normal)
        }
    }
    
    // передвижение вершины
    @objc private func movePeak(param: UIPanGestureRecognizer) {
        guard let tagOfSelectedButton = tagOfSelectedButton else { return }
        var dragButton = UIButton()
        for element in buttonsForPeaks where element.tag == tagOfSelectedButton {
            dragButton = element
        }
        dragButton.center = param.location(in: drawingView)
        drawingView.changePosition(coordx: param.location(in: drawingView).x,
                                   coordy: param.location(in: drawingView).y,
                                   tag: dragButton.tag)
        print(param.location(in: drawingView))
    }
    
    // создание нижнего scrollView
    func createScroll() {
        buttonsScrollView = UIScrollView(frame: CGRect(x: buttonBarView.bounds.origin.x,
                                                       y: buttonBarView.bounds.origin.y,
                                                       width: buttonBarView.bounds.width,
                                                       height: buttonBarView.bounds.height))
        buttonsScrollView.showsHorizontalScrollIndicator = false
        buttonsScrollView.isPagingEnabled = true
        buttonsScrollView.contentSize = CGSize(width: buttonBarView.bounds.width * 3, height: 50)
        buttonBarView.addSubview(buttonsScrollView)
    }
    
    // создание view для scrolView
    func createButtonBarView() {
        buttonBarView = UIView(frame: CGRect(x: 13.0,
                                             y: view.bounds.maxY - 90,
                                             width: view.bounds.width - 26,
                                             height: 50.0))
        buttonBarView.layer.cornerRadius = 10
        buttonBarView.backgroundColor = #colorLiteral(red: 0.7665868509, green: 0.6989096012, blue: 1, alpha: 1)
        view.addSubview(buttonBarView)
    }
    // создание кнопок для нижнего бара
    func createButtons() {
        // button for add peak
        buttonFoAddPeak = UIButton(frame: CGRect(x: buttonsScrollView.bounds.minX + 10, y: 0, width: 100, height: 35))
        buttonFoAddPeak.center.y = buttonsScrollView.center.y
        buttonFoAddPeak.setTitle("Add", for: .normal)
        buttonFoAddPeak.setTitleColor(.black, for: .normal)
        buttonFoAddPeak.backgroundColor = .white
        buttonFoAddPeak.layer.cornerRadius = 10
        buttonsScrollView.addSubview(buttonFoAddPeak)
        
        // button for change color of peak
        colorButton = UIButton(frame: CGRect(x: buttonsScrollView.bounds.minX + 125, y: 0, width: 100, height: 35))
        colorButton.center.y = buttonsScrollView.center.y
        colorButton.center.x = buttonsScrollView.center.x
        colorButton.setTitle("Color", for: .normal)
        colorButton.setTitleColor(.black, for: .normal)
        colorButton.backgroundColor = .white
        colorButton.layer.cornerRadius = 10
        buttonsScrollView.addSubview(colorButton)
        
        // кнопка для удаления вершины
        deleteButton = UIButton(frame: CGRect(x: buttonsScrollView.bounds.minX + 250, y: 0, width: 100, height: 35))
        deleteButton.center.y = buttonsScrollView.center.y
        deleteButton.setTitle("Delete", for: .normal)
        deleteButton.backgroundColor = .white
        deleteButton.setTitleColor(.black, for: .normal)
        deleteButton.layer.cornerRadius = 10
        buttonsScrollView.addSubview(deleteButton)
        
        // кнопка для вывода информации
        infoButton = UIButton(frame: CGRect(x: buttonsScrollView.bounds.minX + 375, y: 0, width: 100, height: 35))
        infoButton.center.y = buttonsScrollView.center.y
        infoButton.setTitle("Info", for: .normal)
        infoButton.backgroundColor = .white
        infoButton.setTitleColor(.black, for: .normal)
        infoButton.layer.cornerRadius = 10
        buttonsScrollView.addSubview(infoButton)
    }
    
    // кастомные кнопки
    // TODO: доделать эту функцию
    func customButton(button: UIButton, title: String) {
        button.center.y = buttonsScrollView.center.y
        button.setTitle(title, for: .normal)
        button.backgroundColor = .white
        button.setTitleColor(.black, for: .normal)
        button.layer.cornerRadius = 10
    }
    
    // добавление таргетов для кнопок из нижнего бара
    func actionsForButtons() {
        buttonFoAddPeak.addTarget(self, action: #selector(addPeak), for: .touchUpInside)
        colorButton.addTarget(self, action: #selector(changeColorButton), for: .touchUpInside)
        deleteButton.addTarget(self, action: #selector(deletePeak), for: .touchUpInside)
        infoButton.addTarget(self, action: #selector(info), for: .touchUpInside)
    }
    
    // вывод инфо
    @objc func info() {
        let information = drawingView.getInfo()
        guard let viewController = storyboard?.instantiateViewController(withIdentifier: "info")
                as? InfoViewController else { return }
        viewController.getInfo(info: information, peak: tagOfSelectedButton)
        viewController.modalPresentationStyle = .pageSheet
        viewController.modalTransitionStyle = .coverVertical
        present(viewController, animated: true, completion: nil)
    }
    
    // удаление вершины
    @objc func deletePeak() {
        self.present(actionSheet(titleForFirstAction: "Удалить вершину",
                                 titleForSecondAction: "Удалить ребро",
                                 closureForFirstAction: {
            guard let tagOfSelectedButton = self.tagOfSelectedButton else {
                self.present(alert(title: "Ошибка", message: "Выберите вершину"), animated: true, completion: nil)
                return
            }
            self.drawingView.deleteDrawPeak(tag: tagOfSelectedButton)
            for element in self.buttonsForPeaks where element.tag > tagOfSelectedButton {
                    element.tag -= 1
            }
            self.buttonsForPeaks[tagOfSelectedButton - 1].removeFromSuperview()
            self.buttonsForPeaks.remove(at: tagOfSelectedButton - 1)
        }, closureForSecondAction: {
            self.present(alertWithTextField(title: "Внимание",
                                            message: "Введите две вершины ребра",
                                            placeholder: "1 2",
                                            handler: { peaksInt, _ in
                self.drawingView.deleteEdge(edge: peaksInt)
            }), animated: true, completion: nil)
        }), animated: true)
        
    }
    
    // изменение цвета вершины
    @objc func changeColorButton() {
        guard tagOfSelectedButton != nil else {
            self.present(alert(title: "Ошибка", message: "Выберите вершину"), animated: true, completion: nil)
            return
        }
        self.present(actionSheet(titleForFirstAction: "Изменить цвет вершины",
                                 titleForSecondAction: "Изменить цвет ребра",
                                 closureForFirstAction: {
            self.isChangeColorOfPeak = true
            let picker = UIColorPickerViewController()
            picker.selectedColor = self.selectedColor
            picker.delegate = self
            self.present(picker, animated: true, completion: nil)
        }, closureForSecondAction: {
            self.isChangeColorOfPeak = false
            self.present(alertWithTextField(title: "Внимание",
                                            message: "Введите вторую вершину",
                                            placeholder: "6",
                                            handler: { peaksInt, _ in
                self.edgeForChangeColor[0] = (self.tagOfSelectedButton ?? 0) - 1
                self.edgeForChangeColor[1] = peaksInt[0] - 1
                let picker = UIColorPickerViewController()
                picker.selectedColor = self.selectedColor
                picker.delegate = self
                self.present(picker, animated: true, completion: nil)
            }), animated: true, completion: nil)
        }), animated: true, completion: nil)
    }
    
    // создание кнопок поверх вершин
    func addButton() {
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.2) {
            let paths = UserDefaults.standard.object(forKey: "coordinatesGraph\(self.activeGraph)") as? [CGFloat]
            guard let paths = paths else { return }
            let button = UIButton(frame: CGRect(x: paths[paths.count - 2] - 10,
                                                y: paths[paths.count - 1] - 10, width: 20,
                                                height: 20))
            button.setTitle("\(self.buttonsForPeaks.count + 1)", for: .normal)
            button.setTitleColor(.magenta, for: .normal)
            let drag = UIPanGestureRecognizer(target: self, action: #selector(self.movePeak(param:)))
            button.addTarget(self, action: #selector(self.forButton(param:)), for: .touchUpInside)
            button.addGestureRecognizer(drag)
            button.tag = self.buttonsForPeaks.count + 1
            self.drawingView.addSubview(button)
            self.buttonsForPeaks.append(button)
        }
    }
    
    // создание новой вершины
    @objc func addPeak() {
        self.present(actionSheet(titleForFirstAction: "Добавить вершину",
                                 titleForSecondAction: "Добавить ребро",
                                 closureForFirstAction: {
            self.present(alertWithTextField(title: "Добавить",
                                            message: "Перечислите вершины с которыми новая вершина связывается",
                                            placeholder: "1 2 3",
                                            handler: { peaksInt, _ in
                self.drawingView.addPeakInView(peaks: peaksInt)
                self.addButton()
            }), animated: true, completion: nil)
        }, closureForSecondAction: {
            self.present(alertWithTextField(title: "Внимание",
                                            message: "Введите две вершины ребра",
                                            placeholder: "1 2",
                                            handler: { peaksInt, _ in
                self.drawingView.addEdge(edge: peaksInt)
            }), animated: true, completion: nil)
        }), animated: true, completion: nil)
    }
}

extension ViewController: UIColorPickerViewControllerDelegate {
    func colorPickerViewControllerDidFinish(_ viewController: UIColorPickerViewController) {
        guard let tagOfSelectedButton = tagOfSelectedButton else { return }
        self.selectedColor = viewController.selectedColor
        if isChangeColorOfPeak {
            drawingView.changeColor(color: self.selectedColor, tag: tagOfSelectedButton - 1)
        } else {
            drawingView.changeColorOfEdge(color: self.selectedColor, edge: edgeForChangeColor)
        }
    }
}
