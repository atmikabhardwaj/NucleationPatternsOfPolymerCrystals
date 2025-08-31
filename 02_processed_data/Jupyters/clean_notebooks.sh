# This file relates to the work: Atmika Bhardwaj, Jens-Uwe Sommer, Marco Werner; "Nucleation patterns of polymer crystals analyzed by machine learning models".
# This cleans and backs-up all the output generated within the jupyter notebooks. 

for f in *.ipynb;
do 
cp $f $f.backup 
jupyter nbconvert --clear-output --inplace $f
done;


