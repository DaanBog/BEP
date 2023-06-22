\ Model Vertical farm positioning
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize multi-objectives
  OBJ0: Priority=2 Weight=1 AbsTol=1e-06 RelTol=0
   fertillizerTank[2,1] + fertillizerTank[3,1] + fertillizerTank[4,1]
   + fertillizerTank[5,1]
  OBJ1: Priority=1 Weight=1 AbsTol=1e-06 RelTol=0
   containerMovements[2,1,1,1,1] + containerMovements[2,1,2,1,1]
   + containerMovements[2,1,3,1,1] + containerMovements[2,1,4,1,1]
   + containerMovements[2,1,5,1,1] + containerMovements[3,1,1,1,1]
   + containerMovements[3,1,2,1,1] + containerMovements[3,1,3,1,1]
   + containerMovements[3,1,4,1,1] + containerMovements[3,1,5,1,1]
   + containerMovements[4,1,1,1,1] + containerMovements[4,1,2,1,1]
   + containerMovements[4,1,3,1,1] + containerMovements[4,1,4,1,1]
   + containerMovements[4,1,5,1,1] + containerMovements[5,1,1,1,1]
   + containerMovements[5,1,2,1,1] + containerMovements[5,1,3,1,1]
   + containerMovements[5,1,4,1,1] + containerMovements[5,1,5,1,1]
  OBJ2: Priority=0 Weight=1 AbsTol=1e-06 RelTol=0
   allocated[1,1,1,1,1] + allocated[1,1,2,1,1] + allocated[1,1,3,1,1]
   + allocated[1,1,4,1,1] + allocated[1,1,5,1,1] + allocated[2,1,1,1,1]
   + allocated[2,1,2,1,1] + allocated[2,1,3,1,1] + allocated[2,1,4,1,1]
   + allocated[2,1,5,1,1] + allocated[3,1,1,1,1] + allocated[3,1,2,1,1]
   + allocated[3,1,3,1,1] + allocated[3,1,4,1,1] + allocated[3,1,5,1,1]
   + allocated[4,1,1,1,1] + allocated[4,1,2,1,1] + allocated[4,1,3,1,1]
   + allocated[4,1,4,1,1] + allocated[4,1,5,1,1] + allocated[5,1,1,1,1]
   + allocated[5,1,2,1,1] + allocated[5,1,3,1,1] + allocated[5,1,4,1,1]
   + allocated[5,1,5,1,1]
Subject To
 R0: containers[1,1,1,1,1] + containers[1,1,2,1,1] + containers[1,1,3,1,1]
   + containers[1,1,4,1,1] + containers[1,1,5,1,1] = 1
 R1: containers[2,1,1,1,1] + containers[2,1,2,1,1] + containers[2,1,3,1,1]
   + containers[2,1,4,1,1] + containers[2,1,5,1,1] = 1
 R2: containers[3,1,1,1,1] + containers[3,1,2,1,1] + containers[3,1,3,1,1]
   + containers[3,1,4,1,1] + containers[3,1,5,1,1] = 1
 R3: containers[4,1,1,1,1] + containers[4,1,2,1,1] + containers[4,1,3,1,1]
   + containers[4,1,4,1,1] + containers[4,1,5,1,1] = 1
 R4: containers[5,1,1,1,1] + containers[5,1,2,1,1] + containers[5,1,3,1,1]
   + containers[5,1,4,1,1] + containers[5,1,5,1,1] = 1
 R5: containers[1,1,1,1,1] <= 1
 R6: containers[1,1,2,1,1] <= 1
 R7: containers[1,1,3,1,1] <= 1
 R8: containers[1,1,4,1,1] <= 1
 R9: containers[1,1,5,1,1] <= 1
 R10: containers[2,1,1,1,1] <= 1
 R11: containers[2,1,2,1,1] <= 1
 R12: containers[2,1,3,1,1] <= 1
 R13: containers[2,1,4,1,1] <= 1
 R14: containers[2,1,5,1,1] <= 1
 R15: containers[3,1,1,1,1] <= 1
 R16: containers[3,1,2,1,1] <= 1
 R17: containers[3,1,3,1,1] <= 1
 R18: containers[3,1,4,1,1] <= 1
 R19: containers[3,1,5,1,1] <= 1
 R20: containers[4,1,1,1,1] <= 1
 R21: containers[4,1,2,1,1] <= 1
 R22: containers[4,1,3,1,1] <= 1
 R23: containers[4,1,4,1,1] <= 1
 R24: containers[4,1,5,1,1] <= 1
 R25: containers[5,1,1,1,1] <= 1
 R26: containers[5,1,2,1,1] <= 1
 R27: containers[5,1,3,1,1] <= 1
 R28: containers[5,1,4,1,1] <= 1
 R29: containers[5,1,5,1,1] <= 1
 R30: containers[1,1,1,1,1] - allocated[1,1,1,1,1] <= 0
 R31: containers[1,1,2,1,1] - allocated[1,1,2,1,1] <= 0
 R32: containers[1,1,3,1,1] - allocated[1,1,3,1,1] <= 0
 R33: containers[1,1,4,1,1] - allocated[1,1,4,1,1] <= 0
 R34: containers[1,1,5,1,1] - allocated[1,1,5,1,1] <= 0
 R35: containers[2,1,1,1,1] - allocated[2,1,1,1,1] <= 0
 R36: containers[2,1,2,1,1] - allocated[2,1,2,1,1] <= 0
 R37: containers[2,1,3,1,1] - allocated[2,1,3,1,1] <= 0
 R38: containers[2,1,4,1,1] - allocated[2,1,4,1,1] <= 0
 R39: containers[2,1,5,1,1] - allocated[2,1,5,1,1] <= 0
 R40: containers[3,1,1,1,1] - allocated[3,1,1,1,1] <= 0
 R41: containers[3,1,2,1,1] - allocated[3,1,2,1,1] <= 0
 R42: containers[3,1,3,1,1] - allocated[3,1,3,1,1] <= 0
 R43: containers[3,1,4,1,1] - allocated[3,1,4,1,1] <= 0
 R44: containers[3,1,5,1,1] - allocated[3,1,5,1,1] <= 0
 R45: containers[4,1,1,1,1] - allocated[4,1,1,1,1] <= 0
 R46: containers[4,1,2,1,1] - allocated[4,1,2,1,1] <= 0
 R47: containers[4,1,3,1,1] - allocated[4,1,3,1,1] <= 0
 R48: containers[4,1,4,1,1] - allocated[4,1,4,1,1] <= 0
 R49: containers[4,1,5,1,1] - allocated[4,1,5,1,1] <= 0
 R50: containers[5,1,1,1,1] - allocated[5,1,1,1,1] <= 0
 R51: containers[5,1,2,1,1] - allocated[5,1,2,1,1] <= 0
 R52: containers[5,1,3,1,1] - allocated[5,1,3,1,1] <= 0
 R53: containers[5,1,4,1,1] - allocated[5,1,4,1,1] <= 0
 R54: containers[5,1,5,1,1] - allocated[5,1,5,1,1] <= 0
 R55: - containers[1,1,1,1,1] + allocated[1,1,1,1,1] <= 0
 R56: - containers[1,1,2,1,1] + allocated[1,1,2,1,1] <= 0
 R57: - containers[1,1,3,1,1] + allocated[1,1,3,1,1] <= 0
 R58: - containers[1,1,4,1,1] + allocated[1,1,4,1,1] <= 0
 R59: - containers[1,1,5,1,1] + allocated[1,1,5,1,1] <= 0
 R60: - containers[2,1,1,1,1] + allocated[2,1,1,1,1] <= 0
 R61: - containers[2,1,2,1,1] + allocated[2,1,2,1,1] <= 0
 R62: - containers[2,1,3,1,1] + allocated[2,1,3,1,1] <= 0
 R63: - containers[2,1,4,1,1] + allocated[2,1,4,1,1] <= 0
 R64: - containers[2,1,5,1,1] + allocated[2,1,5,1,1] <= 0
 R65: - containers[3,1,1,1,1] + allocated[3,1,1,1,1] <= 0
 R66: - containers[3,1,2,1,1] + allocated[3,1,2,1,1] <= 0
 R67: - containers[3,1,3,1,1] + allocated[3,1,3,1,1] <= 0
 R68: - containers[3,1,4,1,1] + allocated[3,1,4,1,1] <= 0
 R69: - containers[3,1,5,1,1] + allocated[3,1,5,1,1] <= 0
 R70: - containers[4,1,1,1,1] + allocated[4,1,1,1,1] <= 0
 R71: - containers[4,1,2,1,1] + allocated[4,1,2,1,1] <= 0
 R72: - containers[4,1,3,1,1] + allocated[4,1,3,1,1] <= 0
 R73: - containers[4,1,4,1,1] + allocated[4,1,4,1,1] <= 0
 R74: - containers[4,1,5,1,1] + allocated[4,1,5,1,1] <= 0
 R75: - containers[5,1,1,1,1] + allocated[5,1,1,1,1] <= 0
 R76: - containers[5,1,2,1,1] + allocated[5,1,2,1,1] <= 0
 R77: - containers[5,1,3,1,1] + allocated[5,1,3,1,1] <= 0
 R78: - containers[5,1,4,1,1] + allocated[5,1,4,1,1] <= 0
 R79: - containers[5,1,5,1,1] + allocated[5,1,5,1,1] <= 0
 R80: fertillizerTank[1,1,1] = 1
 R81: fertillizerTank[2,1,1] = 1
 R82: fertillizerTank[3,1,1] = 1
 R83: fertillizerTank[4,1,1] = 1
 R84: fertillizerTank[5,1,1] = 1
 R85: - fertillizerTank[1,1,1] + allocated[1,1,1,1,1] <= 0
 R86: - fertillizerTank[1,1,1] + allocated[1,1,2,1,1] <= 0
 R87: - fertillizerTank[1,1,1] + allocated[1,1,3,1,1] <= 0
 R88: - fertillizerTank[1,1,1] + allocated[1,1,4,1,1] <= 0
 R89: - fertillizerTank[1,1,1] + allocated[1,1,5,1,1] <= 0
 R90: - fertillizerTank[2,1,1] + allocated[2,1,1,1,1] <= 0
 R91: - fertillizerTank[2,1,1] + allocated[2,1,2,1,1] <= 0
 R92: - fertillizerTank[2,1,1] + allocated[2,1,3,1,1] <= 0
 R93: - fertillizerTank[2,1,1] + allocated[2,1,4,1,1] <= 0
 R94: - fertillizerTank[2,1,1] + allocated[2,1,5,1,1] <= 0
 R95: - fertillizerTank[3,1,1] + allocated[3,1,1,1,1] <= 0
 R96: - fertillizerTank[3,1,1] + allocated[3,1,2,1,1] <= 0
 R97: - fertillizerTank[3,1,1] + allocated[3,1,3,1,1] <= 0
 R98: - fertillizerTank[3,1,1] + allocated[3,1,4,1,1] <= 0
 R99: - fertillizerTank[3,1,1] + allocated[3,1,5,1,1] <= 0
 R100: - fertillizerTank[4,1,1] + allocated[4,1,1,1,1] <= 0
 R101: - fertillizerTank[4,1,1] + allocated[4,1,2,1,1] <= 0
 R102: - fertillizerTank[4,1,1] + allocated[4,1,3,1,1] <= 0
 R103: - fertillizerTank[4,1,1] + allocated[4,1,4,1,1] <= 0
 R104: - fertillizerTank[4,1,1] + allocated[4,1,5,1,1] <= 0
 R105: - fertillizerTank[5,1,1] + allocated[5,1,1,1,1] <= 0
 R106: - fertillizerTank[5,1,1] + allocated[5,1,2,1,1] <= 0
 R107: - fertillizerTank[5,1,1] + allocated[5,1,3,1,1] <= 0
 R108: - fertillizerTank[5,1,1] + allocated[5,1,4,1,1] <= 0
 R109: - fertillizerTank[5,1,1] + allocated[5,1,5,1,1] <= 0
 R110: irrigationRegime[1,1,1,1,1] + irrigationRegime[1,1,1,1,2]
   + irrigationRegime[1,1,1,1,3] + irrigationRegime[1,1,1,1,4]
   + irrigationRegime[1,1,1,1,5] = 1
 R111: irrigationRegime[1,2,1,1,1] + irrigationRegime[1,2,1,1,2]
   + irrigationRegime[1,2,1,1,3] + irrigationRegime[1,2,1,1,4]
   + irrigationRegime[1,2,1,1,5] = 1
 R112: irrigationRegime[1,3,1,1,1] + irrigationRegime[1,3,1,1,2]
   + irrigationRegime[1,3,1,1,3] + irrigationRegime[1,3,1,1,4]
   + irrigationRegime[1,3,1,1,5] = 1
 R113: irrigationRegime[1,4,1,1,1] + irrigationRegime[1,4,1,1,2]
   + irrigationRegime[1,4,1,1,3] + irrigationRegime[1,4,1,1,4]
   + irrigationRegime[1,4,1,1,5] = 1
 R114: irrigationRegime[1,5,1,1,1] + irrigationRegime[1,5,1,1,2]
   + irrigationRegime[1,5,1,1,3] + irrigationRegime[1,5,1,1,4]
   + irrigationRegime[1,5,1,1,5] = 1
 R115: irrigationRegime[2,1,1,1,1] + irrigationRegime[2,1,1,1,2]
   + irrigationRegime[2,1,1,1,3] + irrigationRegime[2,1,1,1,4]
   + irrigationRegime[2,1,1,1,5] = 1
 R116: irrigationRegime[2,2,1,1,1] + irrigationRegime[2,2,1,1,2]
   + irrigationRegime[2,2,1,1,3] + irrigationRegime[2,2,1,1,4]
   + irrigationRegime[2,2,1,1,5] = 1
 R117: irrigationRegime[2,3,1,1,1] + irrigationRegime[2,3,1,1,2]
   + irrigationRegime[2,3,1,1,3] + irrigationRegime[2,3,1,1,4]
   + irrigationRegime[2,3,1,1,5] = 1
 R118: irrigationRegime[2,4,1,1,1] + irrigationRegime[2,4,1,1,2]
   + irrigationRegime[2,4,1,1,3] + irrigationRegime[2,4,1,1,4]
   + irrigationRegime[2,4,1,1,5] = 1
 R119: irrigationRegime[2,5,1,1,1] + irrigationRegime[2,5,1,1,2]
   + irrigationRegime[2,5,1,1,3] + irrigationRegime[2,5,1,1,4]
   + irrigationRegime[2,5,1,1,5] = 1
 R120: irrigationRegime[3,1,1,1,1] + irrigationRegime[3,1,1,1,2]
   + irrigationRegime[3,1,1,1,3] + irrigationRegime[3,1,1,1,4]
   + irrigationRegime[3,1,1,1,5] = 1
 R121: irrigationRegime[3,2,1,1,1] + irrigationRegime[3,2,1,1,2]
   + irrigationRegime[3,2,1,1,3] + irrigationRegime[3,2,1,1,4]
   + irrigationRegime[3,2,1,1,5] = 1
 R122: irrigationRegime[3,3,1,1,1] + irrigationRegime[3,3,1,1,2]
   + irrigationRegime[3,3,1,1,3] + irrigationRegime[3,3,1,1,4]
   + irrigationRegime[3,3,1,1,5] = 1
 R123: irrigationRegime[3,4,1,1,1] + irrigationRegime[3,4,1,1,2]
   + irrigationRegime[3,4,1,1,3] + irrigationRegime[3,4,1,1,4]
   + irrigationRegime[3,4,1,1,5] = 1
 R124: irrigationRegime[3,5,1,1,1] + irrigationRegime[3,5,1,1,2]
   + irrigationRegime[3,5,1,1,3] + irrigationRegime[3,5,1,1,4]
   + irrigationRegime[3,5,1,1,5] = 1
 R125: irrigationRegime[4,1,1,1,1] + irrigationRegime[4,1,1,1,2]
   + irrigationRegime[4,1,1,1,3] + irrigationRegime[4,1,1,1,4]
   + irrigationRegime[4,1,1,1,5] = 1
 R126: irrigationRegime[4,2,1,1,1] + irrigationRegime[4,2,1,1,2]
   + irrigationRegime[4,2,1,1,3] + irrigationRegime[4,2,1,1,4]
   + irrigationRegime[4,2,1,1,5] = 1
 R127: irrigationRegime[4,3,1,1,1] + irrigationRegime[4,3,1,1,2]
   + irrigationRegime[4,3,1,1,3] + irrigationRegime[4,3,1,1,4]
   + irrigationRegime[4,3,1,1,5] = 1
 R128: irrigationRegime[4,4,1,1,1] + irrigationRegime[4,4,1,1,2]
   + irrigationRegime[4,4,1,1,3] + irrigationRegime[4,4,1,1,4]
   + irrigationRegime[4,4,1,1,5] = 1
 R129: irrigationRegime[4,5,1,1,1] + irrigationRegime[4,5,1,1,2]
   + irrigationRegime[4,5,1,1,3] + irrigationRegime[4,5,1,1,4]
   + irrigationRegime[4,5,1,1,5] = 1
 R130: irrigationRegime[5,1,1,1,1] + irrigationRegime[5,1,1,1,2]
   + irrigationRegime[5,1,1,1,3] + irrigationRegime[5,1,1,1,4]
   + irrigationRegime[5,1,1,1,5] = 1
 R131: irrigationRegime[5,2,1,1,1] + irrigationRegime[5,2,1,1,2]
   + irrigationRegime[5,2,1,1,3] + irrigationRegime[5,2,1,1,4]
   + irrigationRegime[5,2,1,1,5] = 1
 R132: irrigationRegime[5,3,1,1,1] + irrigationRegime[5,3,1,1,2]
   + irrigationRegime[5,3,1,1,3] + irrigationRegime[5,3,1,1,4]
   + irrigationRegime[5,3,1,1,5] = 1
 R133: irrigationRegime[5,4,1,1,1] + irrigationRegime[5,4,1,1,2]
   + irrigationRegime[5,4,1,1,3] + irrigationRegime[5,4,1,1,4]
   + irrigationRegime[5,4,1,1,5] = 1
 R134: irrigationRegime[5,5,1,1,1] + irrigationRegime[5,5,1,1,2]
   + irrigationRegime[5,5,1,1,3] + irrigationRegime[5,5,1,1,4]
   + irrigationRegime[5,5,1,1,5] = 1
 R135: - irrigationRegime[1,1,1,1,1] + allocated[1,1,1,1,1] <= 0
 R136: - irrigationRegime[1,2,1,1,1] + allocated[1,1,2,1,1] <= 0
 R137: - irrigationRegime[1,3,1,1,1] + allocated[1,1,3,1,1] <= 0
 R138: - irrigationRegime[1,4,1,1,1] + allocated[1,1,4,1,1] <= 0
 R139: - irrigationRegime[1,5,1,1,1] + allocated[1,1,5,1,1] <= 0
 R140: - irrigationRegime[2,1,1,1,2] + allocated[2,1,1,1,1] <= 0
 R141: - irrigationRegime[2,2,1,1,2] + allocated[2,1,2,1,1] <= 0
 R142: - irrigationRegime[2,3,1,1,2] + allocated[2,1,3,1,1] <= 0
 R143: - irrigationRegime[2,4,1,1,2] + allocated[2,1,4,1,1] <= 0
 R144: - irrigationRegime[2,5,1,1,2] + allocated[2,1,5,1,1] <= 0
 R145: - irrigationRegime[3,1,1,1,3] + allocated[3,1,1,1,1] <= 0
 R146: - irrigationRegime[3,2,1,1,3] + allocated[3,1,2,1,1] <= 0
 R147: - irrigationRegime[3,3,1,1,3] + allocated[3,1,3,1,1] <= 0
 R148: - irrigationRegime[3,4,1,1,3] + allocated[3,1,4,1,1] <= 0
 R149: - irrigationRegime[3,5,1,1,3] + allocated[3,1,5,1,1] <= 0
 R150: - irrigationRegime[4,1,1,1,4] + allocated[4,1,1,1,1] <= 0
 R151: - irrigationRegime[4,2,1,1,4] + allocated[4,1,2,1,1] <= 0
 R152: - irrigationRegime[4,3,1,1,4] + allocated[4,1,3,1,1] <= 0
 R153: - irrigationRegime[4,4,1,1,4] + allocated[4,1,4,1,1] <= 0
 R154: - irrigationRegime[4,5,1,1,4] + allocated[4,1,5,1,1] <= 0
 R155: - irrigationRegime[5,1,1,1,5] + allocated[5,1,1,1,1] <= 0
 R156: - irrigationRegime[5,2,1,1,5] + allocated[5,1,2,1,1] <= 0
 R157: - irrigationRegime[5,3,1,1,5] + allocated[5,1,3,1,1] <= 0
 R158: - irrigationRegime[5,4,1,1,5] + allocated[5,1,4,1,1] <= 0
 R159: - irrigationRegime[5,5,1,1,5] + allocated[5,1,5,1,1] <= 0
 R160: - fertillizerTank[1,1,1] + fertillizerTank[2,1,1]
   - fertillizerTank[2,1] <= 0
 R161: - fertillizerTank[2,1,1] + fertillizerTank[3,1,1]
   - fertillizerTank[3,1] <= 0
 R162: - fertillizerTank[3,1,1] + fertillizerTank[4,1,1]
   - fertillizerTank[4,1] <= 0
 R163: - fertillizerTank[4,1,1] + fertillizerTank[5,1,1]
   - fertillizerTank[5,1] <= 0
 R164: fertillizerTank[1,1,1] - fertillizerTank[2,1,1]
   - fertillizerTank[2,1] <= 0
 R165: fertillizerTank[2,1,1] - fertillizerTank[3,1,1]
   - fertillizerTank[3,1] <= 0
 R166: fertillizerTank[3,1,1] - fertillizerTank[4,1,1]
   - fertillizerTank[4,1] <= 0
 R167: fertillizerTank[4,1,1] - fertillizerTank[5,1,1]
   - fertillizerTank[5,1] <= 0
 R168: - allocated[1,1,1,1,1] + allocated[2,1,1,1,1]
   - containerMovements[2,1,1,1,1] <= 0
 R169: - allocated[1,1,2,1,1] + allocated[2,1,2,1,1]
   - containerMovements[2,1,2,1,1] <= 0
 R170: - allocated[1,1,3,1,1] + allocated[2,1,3,1,1]
   - containerMovements[2,1,3,1,1] <= 0
 R171: - allocated[1,1,4,1,1] + allocated[2,1,4,1,1]
   - containerMovements[2,1,4,1,1] <= 0
 R172: - allocated[1,1,5,1,1] + allocated[2,1,5,1,1]
   - containerMovements[2,1,5,1,1] <= 0
 R173: - allocated[2,1,1,1,1] + allocated[3,1,1,1,1]
   - containerMovements[3,1,1,1,1] <= 0
 R174: - allocated[2,1,2,1,1] + allocated[3,1,2,1,1]
   - containerMovements[3,1,2,1,1] <= 0
 R175: - allocated[2,1,3,1,1] + allocated[3,1,3,1,1]
   - containerMovements[3,1,3,1,1] <= 0
 R176: - allocated[2,1,4,1,1] + allocated[3,1,4,1,1]
   - containerMovements[3,1,4,1,1] <= 0
 R177: - allocated[2,1,5,1,1] + allocated[3,1,5,1,1]
   - containerMovements[3,1,5,1,1] <= 0
 R178: - allocated[3,1,1,1,1] + allocated[4,1,1,1,1]
   - containerMovements[4,1,1,1,1] <= 0
 R179: - allocated[3,1,2,1,1] + allocated[4,1,2,1,1]
   - containerMovements[4,1,2,1,1] <= 0
 R180: - allocated[3,1,3,1,1] + allocated[4,1,3,1,1]
   - containerMovements[4,1,3,1,1] <= 0
 R181: - allocated[3,1,4,1,1] + allocated[4,1,4,1,1]
   - containerMovements[4,1,4,1,1] <= 0
 R182: - allocated[3,1,5,1,1] + allocated[4,1,5,1,1]
   - containerMovements[4,1,5,1,1] <= 0
 R183: - allocated[4,1,1,1,1] + allocated[5,1,1,1,1]
   - containerMovements[5,1,1,1,1] <= 0
 R184: - allocated[4,1,2,1,1] + allocated[5,1,2,1,1]
   - containerMovements[5,1,2,1,1] <= 0
 R185: - allocated[4,1,3,1,1] + allocated[5,1,3,1,1]
   - containerMovements[5,1,3,1,1] <= 0
 R186: - allocated[4,1,4,1,1] + allocated[5,1,4,1,1]
   - containerMovements[5,1,4,1,1] <= 0
 R187: - allocated[4,1,5,1,1] + allocated[5,1,5,1,1]
   - containerMovements[5,1,5,1,1] <= 0
 R188: allocated[1,1,1,1,1] - allocated[2,1,1,1,1]
   - containerMovements[2,1,1,1,1] <= 0
 R189: allocated[1,1,2,1,1] - allocated[2,1,2,1,1]
   - containerMovements[2,1,2,1,1] <= 0
 R190: allocated[1,1,3,1,1] - allocated[2,1,3,1,1]
   - containerMovements[2,1,3,1,1] <= 0
 R191: allocated[1,1,4,1,1] - allocated[2,1,4,1,1]
   - containerMovements[2,1,4,1,1] <= 0
 R192: allocated[1,1,5,1,1] - allocated[2,1,5,1,1]
   - containerMovements[2,1,5,1,1] <= 0
 R193: allocated[2,1,1,1,1] - allocated[3,1,1,1,1]
   - containerMovements[3,1,1,1,1] <= 0
 R194: allocated[2,1,2,1,1] - allocated[3,1,2,1,1]
   - containerMovements[3,1,2,1,1] <= 0
 R195: allocated[2,1,3,1,1] - allocated[3,1,3,1,1]
   - containerMovements[3,1,3,1,1] <= 0
 R196: allocated[2,1,4,1,1] - allocated[3,1,4,1,1]
   - containerMovements[3,1,4,1,1] <= 0
 R197: allocated[2,1,5,1,1] - allocated[3,1,5,1,1]
   - containerMovements[3,1,5,1,1] <= 0
 R198: allocated[3,1,1,1,1] - allocated[4,1,1,1,1]
   - containerMovements[4,1,1,1,1] <= 0
 R199: allocated[3,1,2,1,1] - allocated[4,1,2,1,1]
   - containerMovements[4,1,2,1,1] <= 0
 R200: allocated[3,1,3,1,1] - allocated[4,1,3,1,1]
   - containerMovements[4,1,3,1,1] <= 0
 R201: allocated[3,1,4,1,1] - allocated[4,1,4,1,1]
   - containerMovements[4,1,4,1,1] <= 0
 R202: allocated[3,1,5,1,1] - allocated[4,1,5,1,1]
   - containerMovements[4,1,5,1,1] <= 0
 R203: allocated[4,1,1,1,1] - allocated[5,1,1,1,1]
   - containerMovements[5,1,1,1,1] <= 0
 R204: allocated[4,1,2,1,1] - allocated[5,1,2,1,1]
   - containerMovements[5,1,2,1,1] <= 0
 R205: allocated[4,1,3,1,1] - allocated[5,1,3,1,1]
   - containerMovements[5,1,3,1,1] <= 0
 R206: allocated[4,1,4,1,1] - allocated[5,1,4,1,1]
   - containerMovements[5,1,4,1,1] <= 0
 R207: allocated[4,1,5,1,1] - allocated[5,1,5,1,1]
   - containerMovements[5,1,5,1,1] <= 0
Bounds
 containers[1,1,1,1,1] <= 1
 containers[1,1,2,1,1] <= 1
 containers[1,1,3,1,1] <= 1
 containers[1,1,4,1,1] <= 1
 containers[1,1,5,1,1] <= 1
 containers[2,1,1,1,1] <= 1
 containers[2,1,2,1,1] <= 1
 containers[2,1,3,1,1] <= 1
 containers[2,1,4,1,1] <= 1
 containers[2,1,5,1,1] <= 1
 containers[3,1,1,1,1] <= 1
 containers[3,1,2,1,1] <= 1
 containers[3,1,3,1,1] <= 1
 containers[3,1,4,1,1] <= 1
 containers[3,1,5,1,1] <= 1
 containers[4,1,1,1,1] <= 1
 containers[4,1,2,1,1] <= 1
 containers[4,1,3,1,1] <= 1
 containers[4,1,4,1,1] <= 1
 containers[4,1,5,1,1] <= 1
 containers[5,1,1,1,1] <= 1
 containers[5,1,2,1,1] <= 1
 containers[5,1,3,1,1] <= 1
 containers[5,1,4,1,1] <= 1
 containers[5,1,5,1,1] <= 1
Binaries
 fertillizerTank[1,1,1] fertillizerTank[2,1,1] fertillizerTank[3,1,1]
 fertillizerTank[4,1,1] fertillizerTank[5,1,1] irrigationRegime[1,1,1,1,1]
 irrigationRegime[1,1,1,1,2] irrigationRegime[1,1,1,1,3]
 irrigationRegime[1,1,1,1,4] irrigationRegime[1,1,1,1,5]
 irrigationRegime[1,2,1,1,1] irrigationRegime[1,2,1,1,2]
 irrigationRegime[1,2,1,1,3] irrigationRegime[1,2,1,1,4]
 irrigationRegime[1,2,1,1,5] irrigationRegime[1,3,1,1,1]
 irrigationRegime[1,3,1,1,2] irrigationRegime[1,3,1,1,3]
 irrigationRegime[1,3,1,1,4] irrigationRegime[1,3,1,1,5]
 irrigationRegime[1,4,1,1,1] irrigationRegime[1,4,1,1,2]
 irrigationRegime[1,4,1,1,3] irrigationRegime[1,4,1,1,4]
 irrigationRegime[1,4,1,1,5] irrigationRegime[1,5,1,1,1]
 irrigationRegime[1,5,1,1,2] irrigationRegime[1,5,1,1,3]
 irrigationRegime[1,5,1,1,4] irrigationRegime[1,5,1,1,5]
 irrigationRegime[2,1,1,1,1] irrigationRegime[2,1,1,1,2]
 irrigationRegime[2,1,1,1,3] irrigationRegime[2,1,1,1,4]
 irrigationRegime[2,1,1,1,5] irrigationRegime[2,2,1,1,1]
 irrigationRegime[2,2,1,1,2] irrigationRegime[2,2,1,1,3]
 irrigationRegime[2,2,1,1,4] irrigationRegime[2,2,1,1,5]
 irrigationRegime[2,3,1,1,1] irrigationRegime[2,3,1,1,2]
 irrigationRegime[2,3,1,1,3] irrigationRegime[2,3,1,1,4]
 irrigationRegime[2,3,1,1,5] irrigationRegime[2,4,1,1,1]
 irrigationRegime[2,4,1,1,2] irrigationRegime[2,4,1,1,3]
 irrigationRegime[2,4,1,1,4] irrigationRegime[2,4,1,1,5]
 irrigationRegime[2,5,1,1,1] irrigationRegime[2,5,1,1,2]
 irrigationRegime[2,5,1,1,3] irrigationRegime[2,5,1,1,4]
 irrigationRegime[2,5,1,1,5] irrigationRegime[3,1,1,1,1]
 irrigationRegime[3,1,1,1,2] irrigationRegime[3,1,1,1,3]
 irrigationRegime[3,1,1,1,4] irrigationRegime[3,1,1,1,5]
 irrigationRegime[3,2,1,1,1] irrigationRegime[3,2,1,1,2]
 irrigationRegime[3,2,1,1,3] irrigationRegime[3,2,1,1,4]
 irrigationRegime[3,2,1,1,5] irrigationRegime[3,3,1,1,1]
 irrigationRegime[3,3,1,1,2] irrigationRegime[3,3,1,1,3]
 irrigationRegime[3,3,1,1,4] irrigationRegime[3,3,1,1,5]
 irrigationRegime[3,4,1,1,1] irrigationRegime[3,4,1,1,2]
 irrigationRegime[3,4,1,1,3] irrigationRegime[3,4,1,1,4]
 irrigationRegime[3,4,1,1,5] irrigationRegime[3,5,1,1,1]
 irrigationRegime[3,5,1,1,2] irrigationRegime[3,5,1,1,3]
 irrigationRegime[3,5,1,1,4] irrigationRegime[3,5,1,1,5]
 irrigationRegime[4,1,1,1,1] irrigationRegime[4,1,1,1,2]
 irrigationRegime[4,1,1,1,3] irrigationRegime[4,1,1,1,4]
 irrigationRegime[4,1,1,1,5] irrigationRegime[4,2,1,1,1]
 irrigationRegime[4,2,1,1,2] irrigationRegime[4,2,1,1,3]
 irrigationRegime[4,2,1,1,4] irrigationRegime[4,2,1,1,5]
 irrigationRegime[4,3,1,1,1] irrigationRegime[4,3,1,1,2]
 irrigationRegime[4,3,1,1,3] irrigationRegime[4,3,1,1,4]
 irrigationRegime[4,3,1,1,5] irrigationRegime[4,4,1,1,1]
 irrigationRegime[4,4,1,1,2] irrigationRegime[4,4,1,1,3]
 irrigationRegime[4,4,1,1,4] irrigationRegime[4,4,1,1,5]
 irrigationRegime[4,5,1,1,1] irrigationRegime[4,5,1,1,2]
 irrigationRegime[4,5,1,1,3] irrigationRegime[4,5,1,1,4]
 irrigationRegime[4,5,1,1,5] irrigationRegime[5,1,1,1,1]
 irrigationRegime[5,1,1,1,2] irrigationRegime[5,1,1,1,3]
 irrigationRegime[5,1,1,1,4] irrigationRegime[5,1,1,1,5]
 irrigationRegime[5,2,1,1,1] irrigationRegime[5,2,1,1,2]
 irrigationRegime[5,2,1,1,3] irrigationRegime[5,2,1,1,4]
 irrigationRegime[5,2,1,1,5] irrigationRegime[5,3,1,1,1]
 irrigationRegime[5,3,1,1,2] irrigationRegime[5,3,1,1,3]
 irrigationRegime[5,3,1,1,4] irrigationRegime[5,3,1,1,5]
 irrigationRegime[5,4,1,1,1] irrigationRegime[5,4,1,1,2]
 irrigationRegime[5,4,1,1,3] irrigationRegime[5,4,1,1,4]
 irrigationRegime[5,4,1,1,5] irrigationRegime[5,5,1,1,1]
 irrigationRegime[5,5,1,1,2] irrigationRegime[5,5,1,1,3]
 irrigationRegime[5,5,1,1,4] irrigationRegime[5,5,1,1,5]
 allocated[1,1,1,1,1] allocated[1,1,2,1,1] allocated[1,1,3,1,1]
 allocated[1,1,4,1,1] allocated[1,1,5,1,1] allocated[2,1,1,1,1]
 allocated[2,1,2,1,1] allocated[2,1,3,1,1] allocated[2,1,4,1,1]
 allocated[2,1,5,1,1] allocated[3,1,1,1,1] allocated[3,1,2,1,1]
 allocated[3,1,3,1,1] allocated[3,1,4,1,1] allocated[3,1,5,1,1]
 allocated[4,1,1,1,1] allocated[4,1,2,1,1] allocated[4,1,3,1,1]
 allocated[4,1,4,1,1] allocated[4,1,5,1,1] allocated[5,1,1,1,1]
 allocated[5,1,2,1,1] allocated[5,1,3,1,1] allocated[5,1,4,1,1]
 allocated[5,1,5,1,1] fertillizerTank[2,1] fertillizerTank[3,1]
 fertillizerTank[4,1] fertillizerTank[5,1] containerMovements[2,1,1,1,1]
 containerMovements[2,1,2,1,1] containerMovements[2,1,3,1,1]
 containerMovements[2,1,4,1,1] containerMovements[2,1,5,1,1]
 containerMovements[3,1,1,1,1] containerMovements[3,1,2,1,1]
 containerMovements[3,1,3,1,1] containerMovements[3,1,4,1,1]
 containerMovements[3,1,5,1,1] containerMovements[4,1,1,1,1]
 containerMovements[4,1,2,1,1] containerMovements[4,1,3,1,1]
 containerMovements[4,1,4,1,1] containerMovements[4,1,5,1,1]
 containerMovements[5,1,1,1,1] containerMovements[5,1,2,1,1]
 containerMovements[5,1,3,1,1] containerMovements[5,1,4,1,1]
 containerMovements[5,1,5,1,1]
Generals
 containers[1,1,1,1,1] containers[1,1,2,1,1] containers[1,1,3,1,1]
 containers[1,1,4,1,1] containers[1,1,5,1,1] containers[2,1,1,1,1]
 containers[2,1,2,1,1] containers[2,1,3,1,1] containers[2,1,4,1,1]
 containers[2,1,5,1,1] containers[3,1,1,1,1] containers[3,1,2,1,1]
 containers[3,1,3,1,1] containers[3,1,4,1,1] containers[3,1,5,1,1]
 containers[4,1,1,1,1] containers[4,1,2,1,1] containers[4,1,3,1,1]
 containers[4,1,4,1,1] containers[4,1,5,1,1] containers[5,1,1,1,1]
 containers[5,1,2,1,1] containers[5,1,3,1,1] containers[5,1,4,1,1]
 containers[5,1,5,1,1]
End
