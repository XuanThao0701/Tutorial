//
//  ViewController.swift
//  MyMap
//
//  Created by Thao Nguyen on 10/13/20.
//

import UIKit

class CurrentLocationViewController: UIViewController {

    @IBOutlet weak var messageLabel : UILabel!
    @IBOutlet weak var latitudeLabel : UILabel!
    @IBOutlet weak var longitudeLabel : UILabel!
    @IBOutlet weak var addressLabel : UILabel!
    @IBOutlet weak var tagButton : UIButton!
    @IBOutlet weak var getButton : UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    // MARK:- Actions
    @IBAction func getLocation(){
        
    }
}

