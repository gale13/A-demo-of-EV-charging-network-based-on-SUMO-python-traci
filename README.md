# A demo of EV charging network (based on SUMO with python-traci)

/input file:
h.net.xml  (network topology)
vehicle.rou.xml (contains two EVs)
char.add.xml (contains a charging station on E4)

/configuration file:
con.sumocfg

/control file
tra.py (when the remaining capacity of an EV is lower than 600(max 2000), it will change the target and go to the charging station. After the charging finished, it will go to its original destination.)

/output file
battery.xml
chargingstations.xml
(showing energyconsumed or currentenergy each step (s))
