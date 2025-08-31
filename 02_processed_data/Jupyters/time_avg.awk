# This file relates to the work: Atmika Bhardwaj, Jens-Uwe Sommer, Marco Werner; "Nucleation patterns of polymer crystals analyzed by machine learning models".

{
t=$1;
if (t > 0)
{
	for (i=1;i<=NF;++i){ s[i]+=$i ;} n+=1; 
	if(n == interval)
	{
		line="";
		for (i=1;i<=NF;++i){
		line=line" \t"s[i]/n; 
		s[i]=0
		};n=0;
		print line
	}
	}
}

