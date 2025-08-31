# This file relates to the work: Atmika Bhardwaj, Jens-Uwe Sommer, Marco Werner; "Nucleation patterns of polymer crystals analyzed by machine learning models".
# This file can be used to consecutively run all the notebooks from the terminal window.

rm -r __pycache__

bash extract_C_p.sh

for f in SL_AO_pointcloud.ipynb TrainingModels.ipynb Quantifying_cluster_compactness.ipynb  Q_tensor_domaincluster.ipynb ;
do 
    echo $f;
      cp $f $f.backup 
      jupyter nbconvert --clear-output --inplace $f
      jupyter execute $f --allow-errors

done
