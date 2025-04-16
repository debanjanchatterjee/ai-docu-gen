# Machine Translation

This repository contains the code and report for a machine translation project. The project focuses on translating text from one language (e.g., English) to another (e.g., Hindi).  This project was developed in phases, iteratively improving the translation quality.


## Project Description

This project explores different techniques for machine translation, potentially including statistical machine translation (SMT) or neural machine translation (NMT) methods. The `report.pdf` document provides a detailed explanation of the methodology, implementation, and results achieved.  The code is organized into different phases, showcasing the evolution of the translation system.

## Features

* Phased development approach demonstrating iterative improvements.
* Evaluation scripts and results included for transparency and reproducibility.
* Detailed report explaining the technical details and findings.

## File Structure

* **`code/`**: Contains the Jupyter notebooks (`.ipynb`) for each phase of the project:
    * `phase1.ipynb`, `phase2.ipynb`, `phase3.ipynb`, `phase4.ipynb`, `final.ipynb`: Notebooks containing the code for each phase and potentially the final implementation.
* **`data/`**: Contains the data used for training and testing:  (Inferred based on the project description, adjust if different)
    * `train/train.csv`: Training dataset.
    * `test/testhindistatements.csv`: Test dataset.
* **`evaluationscript/`**: Contains scripts for evaluating the translation quality:
    * `evaluation_script.py`:  The primary evaluation script.
    * Various subdirectories containing outputs from different submissions and weeks.
* **`report.pdf`**:  The project report detailing the methods and findings.
* **`LICENSE`**:  The license governing the use of this project.
* **`README.md`**:  This file.


## Setup Instructions

While specific setup instructions are dependent on the dependencies of the notebooks, general guidelines are as follows:

1. **Clone the repository:**  `git clone https://github.com/debanjanchatterjee/machine-translarion.git`
2. **Navigate to the `code` directory:** `cd machine-translarion/code`
3. **Install required libraries:**  You'll likely need libraries like `nltk`, `tensorflow`, `pytorch`, or others depending on the implementation. Use `pip install -r requirements.txt` if a `requirements.txt` file is present.  If not, you will need to install the libraries based on the imports in the notebooks. For example:
     ```bash
     pip install nltk tensorflow pandas numpy scikit-learn
     ```
4. **Run the Jupyter notebooks:**  `jupyter notebook`



## Usage Example (Illustrative)


Assuming `final.ipynb` contains the final trained model and a function `translate_text(text, source_lang, target_lang)`:

```python
# Within the final.ipynb notebook, after training or loading the model:

text_to_translate = "This is a sample sentence."
translated_text = translate_text(text_to_translate, "en", "hi")
print(translated_text) # Output: यह एक उदाहरण वाक्य है। (Illustrative Hindi translation)
```


**Disclaimer:** The actual usage will depend on the specific functions and classes defined in your notebooks. Refer to the `report.pdf` and the notebooks themselves for detailed instructions and explanations.


## Contributing


This project is currently not accepting contributions.  However, feel free to open issues for any bugs or suggestions.




## License


This project is licensed under the [License Name - e.g., MIT License](LICENSE). See the `LICENSE` file for details.
