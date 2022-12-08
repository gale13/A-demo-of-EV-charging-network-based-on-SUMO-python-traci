#coding=utf-8
import traci
import time
import traci.constants as tc
import pytz
from random import randrange
import pandas as pd


sumoCmd = ["sumo-gui","-c","con.sumocfg"]
traci.start(sumoCmd)

maxcap=2000

wait = []
charge = []
cache={}
step = 0
while traci.simulation.getMinExpectedNumber()>0:
	traci.simulationStep()
	vehicles=traci.vehicle.getIDList()
	step+=1
	for i in range(len(vehicles)):
		vehid = vehicles[i]
		rembat=float(traci.vehicle.getParameter(vehid, "device.battery.actualBatteryCapacity"))
		#print(rembat)
		if (rembat<600 and (vehid not in wait) and (vehid not in charge)):
			#edge = traci.vehicle.getRoadID(vehid)
			target = traci.vehicle.getRoute(vehid)
			#print(target)
			target = target[len(target)-1]
			cache[vehid]=target
			traci.vehicle.changeTarget(vehid,"E4")
			traci.vehicle.setChargingStationStop(vehid, "char1", duration=5, flags=0)
			wait.append(vehid)
		if (vehid in wait):
			chargedev=traci.chargingstation.getVehicleIDs("char1")
			if (vehid in chargedev):
				wait.remove(vehid)
				charge.append(vehid)
		if (vehid in charge):
			if (float(traci.vehicle.getParameter(vehid, "device.battery.actualBatteryCapacity"))>maxcap-0.1):
				charge.remove(vehid)
				traci.vehicle.changeTarget(vehid,cache[vehid])
			else:
				print(traci.vehicle.getParameter(vehid, "device.battery.actualBatteryCapacity"))
				traci.vehicle.setChargingStationStop(vehid, "char1", duration=5,flags=0)


traci.close()