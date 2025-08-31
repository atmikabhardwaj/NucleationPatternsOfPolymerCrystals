# This file relates to the work: Atmika Bhardwaj, Jens-Uwe Sommer, Marco Werner; "Nucleation patterns of polymer crystals analyzed by machine learning models".

BEGIN{
	print "# time, Cp, dv, du, dq, dT, T"
	sep=","
}
{
	time=$1;
	if (time > 0)
	{
		#print
		u=$5;v=$7/1e6;p=$6;Temp=$2;
		#print v0" "Temp" "T0
		if(v0>0 && Temp != T0)
		{
			du=u-u0;dv=v-v0;dT=Temp-T0;dq=du+p*dv;cp=dq/dT;
			print .5*(time+time0)""sep""cp""sep""dv""sep""du""sep""dq""sep""dT""sep""Temp
		}
		v0=v;T0=Temp;u0=u;time0=time
	}
}
