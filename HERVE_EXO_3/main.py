import Classe_vehicules

UAV=Classe_vehicules.UAV(2)
UAV.Mission()
print(UAV.field,UAV.nombres_ailes)

UGV=Classe_vehicules.UGV()
UGV.Mission()
print(UGV.field)

UUV=Classe_vehicules.UUV()
UUV.Mission()
print(UUV.field)