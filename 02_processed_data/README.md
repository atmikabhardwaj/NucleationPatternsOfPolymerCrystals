# About

This dataset contains all files to recreate the plots in the paper  
Atmika Bhardwaj, Jens-Uwe Sommer, Marco Werner
"Nucleation patterns of polymer crystals analyzed by machine learning models".

# Dependencies

* Jupyter Notebook 
* python3
* matplotlib >= 3.4.3
* numpy      >= 1.20.3
* scipy      >= 1.7.1
* keras      >= 2.8.0
* sklearn    >= 1.2.2
* h5py       >= 3.3.0

# Preparing a virtual environment

First, you would have to install [Jupyter Notebook](https://jupyter.org/install) or [Anaconda](https://www.anaconda.com/download) to be able to create and manage virtual environments. 

We have prepared a folder '01_raw_data' that contains all the dump files (contains coordinates of 1000 chains with 1000 coarse-grained beads each). The simulation, if needed, can be re-run on LAMMPS and the files are located in a folder within called 'simulation_files'.

The folder '02_processed_data' contains all the .py and .ipynb files to employ the following machine learning models: AutoEncoders, Hierarchical Clustering, Gaussian Mixture Model, Multilayer Perceptron. 

The folder '03_figures' contains all the .csv files to regenerate the respective figures in the paper.
