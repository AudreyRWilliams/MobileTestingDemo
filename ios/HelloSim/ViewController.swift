
import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var helloLabel: UILabel!

    @IBAction func didTap(_ sender: UIButton) {
        helloLabel.text = "Tapped!"
    }

    override func viewDidLoad() {
        super.viewDidLoad()
    }
}
