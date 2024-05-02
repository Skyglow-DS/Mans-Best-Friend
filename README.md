<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<h3 align="center">Identifying Man's Best Friend</h3>

  <p align="center">
    Leveraging CNN to identify dog breeds.
    <br />
    <a href="https://github.com/Skyglow-DS/Mans-Best-Friend/blob/main/Reports/Final_Report.pdf"><strong>Final Report »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Skyglow-DS/Mans-Best-Friend/tree/main/Code">View Code</a>
    ·
    <a href="https://github.com/Skyglow-DS/Mans-Best-Friend/tree/main/Reports">View Reports</a>

  </p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#coding-files">Coding Files</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a final project for a OMSA course. The specific references to the course are removed in order to abide by Georgia Tech's Code of Conduct. 

The objective of this project is to explore and develop a Neural Network capable of accurately identifying various breeds of dogs. In this project, the Working dog group from AKC.org is used.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

The required packages for this project are located in `requirements.txt`. An IDE, such as VSCode, to view the jupyter notebooks is preferred. 

```sh
pip install -r requirements.txt
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Skyglow-DS/Mans-Best-Friend.git
   ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Download dataset and config training locations
   ```py
   from file_processer import run_all
   run_all()
   ```
   or  

   Run the notebook:
   <a href="https://github.com/Skyglow-DS/Mans-Best-Friend/blob/main/Code/prototype.ipynb">prototype.ipynb</a>
4. Train model:   
   Use <a href="https://github.com/Skyglow-DS/Mans-Best-Friend/blob/main/Code/modeling.ipynb">modeling.ipynb</a>
5. Validate model:  
   Use <a href="https://github.com/Skyglow-DS/Mans-Best-Friend/blob/main/Code/model_evaluation.ipynb">model_evaluation.ipynb</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Coding Files 

### .py files

`Config.py`: Contains all variables and folder paths.

`dataset_splitter.py`: Splits dataset into 80/20. Automatically removes groups with too little training data.

`dog_breed_orginizer.py`: Creates file paths for training and testing datasets.

`dog_breed_scrapers.py`: Scrapes AKC.org for dog groups if the file `dog_breeds.json` is not available. 

`download_dataset.py`: Automatically downloads the Stanford Dogs Dataset if not available.

`file_processer.py`: Automatically prepares environment for model training.

`utils.py`: Helper functions called by other files.

`visualizations.py`: Contains visualizations such as image augmentation.

### Jupyter Notebooks

`prototype.ipynb`: Used to prepare environment for model training.

`modeling.ipynb`: Code used to train the model

`model_evaluation.ipynb`: Various model evaluation methods are shown. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
