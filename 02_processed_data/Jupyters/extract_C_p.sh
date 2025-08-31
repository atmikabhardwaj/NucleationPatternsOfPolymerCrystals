# This file relates to the work: Atmika Bhardwaj, Jens-Uwe Sommer, Marco Werner; "Nucleation patterns of polymer crystals analyzed by machine learning models".

logfile="../../01_raw_data/dump_files/simulation_files/log.lammps"
export LC_NUMERIC=C
#for interval in 10 20 30 40 50 100 200 ;
for interval in 40 100 ;
do
sep="\",\""
outfile="../Cp_t_interval$interval.dat"
cat $logfile | awk '{if (NR>50 && NF==14 && $1 != "Step") print} ' | awk -v interval=$interval -f time_avg.awk  | awk -f calc_cp.awk  > $outfile
done;

