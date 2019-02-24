//
//  ViewController.swift
//  lavagui
//
//  Created by Scott Lombard on 2/24/19.
//  Copyright © 2019 Scott Lombard. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {
    
    
    @IBOutlet weak var myText: NSScrollView!
    
    @IBOutlet var wtfText: NSTextView!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let file = "file.txt" //this is the file. we will write to and read from it
        
        let text = "some text" //just a text
        
        if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            
            let fileURL = dir.appendingPathComponent(file)
            
            //writing
           // do {
            //    try text.write(to: fileURL, atomically: false, encoding: .utf8)
            //}
           // catch {/* error handling here */}
            
            //reading
            
            Timer.scheduledTimer(withTimeInterval: 0.5, repeats: true) { (timer) in
                do {
                    let text2 = try String(contentsOf: fileURL, encoding: .utf8)
                    self.wtfText.string = text2
                    self.wtfText.scrollToEndOfDocument(self)
                }
                catch {/* error handling here */}
            }
            
        }
        
        
        
        
        
        
        // Do any additional setup after loading the view.
    }
    override func viewDidAppear() {
        super.viewDidAppear()
        self.view.window?.title = "Lava"
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }


}

