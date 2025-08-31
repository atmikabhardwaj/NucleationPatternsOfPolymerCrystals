# This file relates to the work: Atmika Bhardwaj, Jens-Uwe Sommer, Marco Werner; "Nucleation patterns of polymer crystals analyzed by machine learning models".
# Here, we set the externally controlled and tuned parameters such as characteric times, various cutoffs, etc. 

def get_defaults():
    p=dict()
    p["Rmax"]         = 3.201
    p["dR"]           = 0.4
    p["boundary_SL"]  = 15
    p["boundary_SL2"] = 18
    p["boundary_AO"]  = 0.68
    p["boundary_AO2"] = 0.600
    p["chainlength"]  = 1000
    p["F10min"]       = 45
    p["F10max"]       = 65
    p["t_pre"]        = 50
    p["t_tr"]         = 53
    p["t_min"]        = 58
    p["t_end"]        = 75
    return p

def calcLJTempAtTime(time): # time given in 10^6 MD steps (each 0.01 tau)
    totalTime = 75.         # in units of 10^6 MD steps
    T_end     = 0.75
    T_start   = 0.9
    return T_start + time/totalTime*(T_end-T_start)

def calcRealTemp(LJTemp):
    return 495.0/0.9*LJTemp
