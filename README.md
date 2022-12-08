# A demo of EV charging network (based on SUMO with python-traci)

# input file:
h.net.xml  (network topology)  
vehicle.rou.xml (contains two EVs)  
char.add.xml (contains a charging station on E4)  

# configuration file:
con.sumocfg

# control file
tra.py (when the remaining capacity of an EV is lower than 600(max 2000), it will change the target and go to the charging station. After the charging finished, it will go to its original destination.)

# output file
battery.xml  
chargingstations.xml  
(showing energyconsumed or currentenergy each step (s))

# sumo-gui


![微信截图_20221208213348](https://user-images.githubusercontent.com/28706554/206461029-d7ff1d7c-bee2-49e8-8381-d2eb7a214cc8.png)




https://user-images.githubusercontent.com/28706554/206466697-4dc7612f-f938-40bb-8561-812bb677c72f.mp4

