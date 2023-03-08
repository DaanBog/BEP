\ Model Vertical farm schedule
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  - 0.0001 tank[D0,1] - 0.0001 tank[D0,2] - 0.0001 tank[D0,3]
   - 0.0001 tank[D1,1] - 0.0001 tank[D1,2] - 0.0001 tank[D1,3]
   - 0.0001 tank[D2,1] - 0.0001 tank[D2,2] - 0.0001 tank[D2,3]
   - 0.0001 tank[D3,1] - 0.0001 tank[D3,2] - 0.0001 tank[D3,3]
   - 0.0001 tank[D4,1] - 0.0001 tank[D4,2] - 0.0001 tank[D4,3]
   - 0.0001 tank[D5,1] - 0.0001 tank[D5,2] - 0.0001 tank[D5,3]
   - 0.0001 tank[D6,1] - 0.0001 tank[D6,2] - 0.0001 tank[D6,3]
   - 0.0001 tank[D7,1] - 0.0001 tank[D7,2] - 0.0001 tank[D7,3]
   - 0.0001 tank[D8,1] - 0.0001 tank[D8,2] - 0.0001 tank[D8,3]
   - 0.0001 irrigation[D0,1] - 0.0001 irrigation[D0,2]
   - 0.0001 irrigation[D0,3] - 0.0001 irrigation[D1,1]
   - 0.0001 irrigation[D1,2] - 0.0001 irrigation[D1,3]
   - 0.0001 irrigation[D2,1] - 0.0001 irrigation[D2,2]
   - 0.0001 irrigation[D2,3] - 0.0001 irrigation[D3,1]
   - 0.0001 irrigation[D3,2] - 0.0001 irrigation[D3,3]
   - 0.0001 irrigation[D4,1] - 0.0001 irrigation[D4,2]
   - 0.0001 irrigation[D4,3] - 0.0001 irrigation[D5,1]
   - 0.0001 irrigation[D5,2] - 0.0001 irrigation[D5,3]
   - 0.0001 irrigation[D6,1] - 0.0001 irrigation[D6,2]
   - 0.0001 irrigation[D6,3] - 0.0001 irrigation[D7,1]
   - 0.0001 irrigation[D7,2] - 0.0001 irrigation[D7,3]
   - 0.0001 irrigation[D8,1] - 0.0001 irrigation[D8,2]
   - 0.0001 irrigation[D8,3] + batch_is_state_on_day[D8,b1,h]
Subject To
 R0: tank[D0,1] + tank[D0,2] + tank[D0,3] <= 8
 R1: tank[D1,1] + tank[D1,2] + tank[D1,3] <= 8
 R2: tank[D2,1] + tank[D2,2] + tank[D2,3] <= 8
 R3: tank[D3,1] + tank[D3,2] + tank[D3,3] <= 8
 R4: tank[D4,1] + tank[D4,2] + tank[D4,3] <= 8
 R5: tank[D5,1] + tank[D5,2] + tank[D5,3] <= 8
 R6: tank[D6,1] + tank[D6,2] + tank[D6,3] <= 8
 R7: tank[D7,1] + tank[D7,2] + tank[D7,3] <= 8
 R8: tank[D8,1] + tank[D8,2] + tank[D8,3] <= 8
 R9: irrigation[D0,1] + irrigation[D0,2] + irrigation[D0,3] <= 96
 R10: irrigation[D1,1] + irrigation[D1,2] + irrigation[D1,3] <= 96
 R11: irrigation[D2,1] + irrigation[D2,2] + irrigation[D2,3] <= 96
 R12: irrigation[D3,1] + irrigation[D3,2] + irrigation[D3,3] <= 96
 R13: irrigation[D4,1] + irrigation[D4,2] + irrigation[D4,3] <= 96
 R14: irrigation[D5,1] + irrigation[D5,2] + irrigation[D5,3] <= 96
 R15: irrigation[D6,1] + irrigation[D6,2] + irrigation[D6,3] <= 96
 R16: irrigation[D7,1] + irrigation[D7,2] + irrigation[D7,3] <= 96
 R17: irrigation[D8,1] + irrigation[D8,2] + irrigation[D8,3] <= 96
 R18: - 12 tank[D0,1] + irrigation[D0,1] <= 0
 R19: - 12 tank[D0,2] + irrigation[D0,2] <= 0
 R20: - 12 tank[D0,3] + irrigation[D0,3] <= 0
 R21: - 12 tank[D1,1] + irrigation[D1,1] <= 0
 R22: - 12 tank[D1,2] + irrigation[D1,2] <= 0
 R23: - 12 tank[D1,3] + irrigation[D1,3] <= 0
 R24: - 12 tank[D2,1] + irrigation[D2,1] <= 0
 R25: - 12 tank[D2,2] + irrigation[D2,2] <= 0
 R26: - 12 tank[D2,3] + irrigation[D2,3] <= 0
 R27: - 12 tank[D3,1] + irrigation[D3,1] <= 0
 R28: - 12 tank[D3,2] + irrigation[D3,2] <= 0
 R29: - 12 tank[D3,3] + irrigation[D3,3] <= 0
 R30: - 12 tank[D4,1] + irrigation[D4,1] <= 0
 R31: - 12 tank[D4,2] + irrigation[D4,2] <= 0
 R32: - 12 tank[D4,3] + irrigation[D4,3] <= 0
 R33: - 12 tank[D5,1] + irrigation[D5,1] <= 0
 R34: - 12 tank[D5,2] + irrigation[D5,2] <= 0
 R35: - 12 tank[D5,3] + irrigation[D5,3] <= 0
 R36: - 12 tank[D6,1] + irrigation[D6,1] <= 0
 R37: - 12 tank[D6,2] + irrigation[D6,2] <= 0
 R38: - 12 tank[D6,3] + irrigation[D6,3] <= 0
 R39: - 12 tank[D7,1] + irrigation[D7,1] <= 0
 R40: - 12 tank[D7,2] + irrigation[D7,2] <= 0
 R41: - 12 tank[D7,3] + irrigation[D7,3] <= 0
 R42: - 12 tank[D8,1] + irrigation[D8,1] <= 0
 R43: - 12 tank[D8,2] + irrigation[D8,2] <= 0
 R44: - 12 tank[D8,3] + irrigation[D8,3] <= 0
 R45: batch_is_state_on_day[D0,b1,ns] + batch_is_state_on_day[D0,b1,se]
   = 1
 R46: batch_is_state_on_day[D0,b1,ns] + batch_is_state_on_day[D0,b1,se]
   + batch_is_state_on_day[D0,b1,t] + batch_is_state_on_day[D0,b1,sp]
   + batch_is_state_on_day[D0,b1,h] = 1
 R47: batch_is_state_on_day[D1,b1,ns] + batch_is_state_on_day[D1,b1,se]
   + batch_is_state_on_day[D1,b1,t] + batch_is_state_on_day[D1,b1,sp]
   + batch_is_state_on_day[D1,b1,h] = 1
 R48: batch_is_state_on_day[D2,b1,ns] + batch_is_state_on_day[D2,b1,se]
   + batch_is_state_on_day[D2,b1,t] + batch_is_state_on_day[D2,b1,sp]
   + batch_is_state_on_day[D2,b1,h] = 1
 R49: batch_is_state_on_day[D3,b1,ns] + batch_is_state_on_day[D3,b1,se]
   + batch_is_state_on_day[D3,b1,t] + batch_is_state_on_day[D3,b1,sp]
   + batch_is_state_on_day[D3,b1,h] = 1
 R50: batch_is_state_on_day[D4,b1,ns] + batch_is_state_on_day[D4,b1,se]
   + batch_is_state_on_day[D4,b1,t] + batch_is_state_on_day[D4,b1,sp]
   + batch_is_state_on_day[D4,b1,h] = 1
 R51: batch_is_state_on_day[D5,b1,ns] + batch_is_state_on_day[D5,b1,se]
   + batch_is_state_on_day[D5,b1,t] + batch_is_state_on_day[D5,b1,sp]
   + batch_is_state_on_day[D5,b1,h] = 1
 R52: batch_is_state_on_day[D6,b1,ns] + batch_is_state_on_day[D6,b1,se]
   + batch_is_state_on_day[D6,b1,t] + batch_is_state_on_day[D6,b1,sp]
   + batch_is_state_on_day[D6,b1,h] = 1
 R53: batch_is_state_on_day[D7,b1,ns] + batch_is_state_on_day[D7,b1,se]
   + batch_is_state_on_day[D7,b1,t] + batch_is_state_on_day[D7,b1,sp]
   + batch_is_state_on_day[D7,b1,h] = 1
 R54: batch_is_state_on_day[D8,b1,ns] + batch_is_state_on_day[D8,b1,se]
   + batch_is_state_on_day[D8,b1,t] + batch_is_state_on_day[D8,b1,sp]
   + batch_is_state_on_day[D8,b1,h] = 1
 R55: batch_is_state_on_day[D0,b1,ns] - batch_is_state_on_day[D1,b1,ns]
   - batch_is_state_on_day[D1,b1,se] <= 0
 R56: batch_is_state_on_day[D1,b1,ns] - batch_is_state_on_day[D2,b1,ns]
   - batch_is_state_on_day[D2,b1,se] <= 0
 R57: batch_is_state_on_day[D2,b1,ns] - batch_is_state_on_day[D3,b1,ns]
   - batch_is_state_on_day[D3,b1,se] <= 0
 R58: batch_is_state_on_day[D3,b1,ns] - batch_is_state_on_day[D4,b1,ns]
   - batch_is_state_on_day[D4,b1,se] <= 0
 R59: batch_is_state_on_day[D4,b1,ns] - batch_is_state_on_day[D5,b1,ns]
   - batch_is_state_on_day[D5,b1,se] <= 0
 R60: batch_is_state_on_day[D5,b1,ns] - batch_is_state_on_day[D6,b1,ns]
   - batch_is_state_on_day[D6,b1,se] <= 0
 R61: batch_is_state_on_day[D6,b1,ns] - batch_is_state_on_day[D7,b1,ns]
   - batch_is_state_on_day[D7,b1,se] <= 0
 R62: batch_is_state_on_day[D7,b1,ns] - batch_is_state_on_day[D8,b1,ns]
   - batch_is_state_on_day[D8,b1,se] <= 0
 R63: batch_is_state_on_day[D0,b1,se] - batch_is_state_on_day[D1,b1,se]
   - batch_is_state_on_day[D1,b1,t] <= 0
 R64: batch_is_state_on_day[D1,b1,se] - batch_is_state_on_day[D2,b1,se]
   - batch_is_state_on_day[D2,b1,t] <= 0
 R65: batch_is_state_on_day[D2,b1,se] - batch_is_state_on_day[D3,b1,se]
   - batch_is_state_on_day[D3,b1,t] <= 0
 R66: batch_is_state_on_day[D3,b1,se] - batch_is_state_on_day[D4,b1,se]
   - batch_is_state_on_day[D4,b1,t] <= 0
 R67: batch_is_state_on_day[D4,b1,se] - batch_is_state_on_day[D5,b1,se]
   - batch_is_state_on_day[D5,b1,t] <= 0
 R68: batch_is_state_on_day[D5,b1,se] - batch_is_state_on_day[D6,b1,se]
   - batch_is_state_on_day[D6,b1,t] <= 0
 R69: batch_is_state_on_day[D6,b1,se] - batch_is_state_on_day[D7,b1,se]
   - batch_is_state_on_day[D7,b1,t] <= 0
 R70: batch_is_state_on_day[D7,b1,se] - batch_is_state_on_day[D8,b1,se]
   - batch_is_state_on_day[D8,b1,t] <= 0
 R71: batch_is_state_on_day[D0,b1,t] - batch_is_state_on_day[D1,b1,t]
   - batch_is_state_on_day[D1,b1,sp] <= 0
 R72: batch_is_state_on_day[D1,b1,t] - batch_is_state_on_day[D2,b1,t]
   - batch_is_state_on_day[D2,b1,sp] <= 0
 R73: batch_is_state_on_day[D2,b1,t] - batch_is_state_on_day[D3,b1,t]
   - batch_is_state_on_day[D3,b1,sp] <= 0
 R74: batch_is_state_on_day[D3,b1,t] - batch_is_state_on_day[D4,b1,t]
   - batch_is_state_on_day[D4,b1,sp] <= 0
 R75: batch_is_state_on_day[D4,b1,t] - batch_is_state_on_day[D5,b1,t]
   - batch_is_state_on_day[D5,b1,sp] <= 0
 R76: batch_is_state_on_day[D5,b1,t] - batch_is_state_on_day[D6,b1,t]
   - batch_is_state_on_day[D6,b1,sp] <= 0
 R77: batch_is_state_on_day[D6,b1,t] - batch_is_state_on_day[D7,b1,t]
   - batch_is_state_on_day[D7,b1,sp] <= 0
 R78: batch_is_state_on_day[D7,b1,t] - batch_is_state_on_day[D8,b1,t]
   - batch_is_state_on_day[D8,b1,sp] <= 0
 R79: batch_is_state_on_day[D0,b1,sp] - batch_is_state_on_day[D1,b1,sp]
   - batch_is_state_on_day[D1,b1,h] <= 0
 R80: batch_is_state_on_day[D1,b1,sp] - batch_is_state_on_day[D2,b1,sp]
   - batch_is_state_on_day[D2,b1,h] <= 0
 R81: batch_is_state_on_day[D2,b1,sp] - batch_is_state_on_day[D3,b1,sp]
   - batch_is_state_on_day[D3,b1,h] <= 0
 R82: batch_is_state_on_day[D3,b1,sp] - batch_is_state_on_day[D4,b1,sp]
   - batch_is_state_on_day[D4,b1,h] <= 0
 R83: batch_is_state_on_day[D4,b1,sp] - batch_is_state_on_day[D5,b1,sp]
   - batch_is_state_on_day[D5,b1,h] <= 0
 R84: batch_is_state_on_day[D5,b1,sp] - batch_is_state_on_day[D6,b1,sp]
   - batch_is_state_on_day[D6,b1,h] <= 0
 R85: batch_is_state_on_day[D6,b1,sp] - batch_is_state_on_day[D7,b1,sp]
   - batch_is_state_on_day[D7,b1,h] <= 0
 R86: batch_is_state_on_day[D7,b1,sp] - batch_is_state_on_day[D8,b1,sp]
   - batch_is_state_on_day[D8,b1,h] <= 0
 R87: batch_is_state_on_day[D0,b1,h] - batch_is_state_on_day[D1,b1,h] <= 0
 R88: batch_is_state_on_day[D1,b1,h] - batch_is_state_on_day[D2,b1,h] <= 0
 R89: batch_is_state_on_day[D2,b1,h] - batch_is_state_on_day[D3,b1,h] <= 0
 R90: batch_is_state_on_day[D3,b1,h] - batch_is_state_on_day[D4,b1,h] <= 0
 R91: batch_is_state_on_day[D4,b1,h] - batch_is_state_on_day[D5,b1,h] <= 0
 R92: batch_is_state_on_day[D5,b1,h] - batch_is_state_on_day[D6,b1,h] <= 0
 R93: batch_is_state_on_day[D6,b1,h] - batch_is_state_on_day[D7,b1,h] <= 0
 R94: batch_is_state_on_day[D7,b1,h] - batch_is_state_on_day[D8,b1,h] <= 0
 R95: batch_is_state_on_day[D0,b1,sp] - batch_is_state_on_day[D2,b1,h]
   >= 0
 R96: batch_is_state_on_day[D0,b1,t] - batch_is_state_on_day[D2,b1,sp]
   >= 0
 R97: batch_is_state_on_day[D0,b1,se] - batch_is_state_on_day[D3,b1,t]
   >= 0
 R98: batch_is_state_on_day[D1,b1,sp] - batch_is_state_on_day[D3,b1,h]
   >= 0
 R99: batch_is_state_on_day[D1,b1,t] - batch_is_state_on_day[D3,b1,sp]
   >= 0
 R100: batch_is_state_on_day[D1,b1,se] - batch_is_state_on_day[D4,b1,t]
   >= 0
 R101: batch_is_state_on_day[D0,b1,ns] + batch_is_state_on_day[D1,b1,se]
   - batch_is_state_on_day[D4,b1,t] <= 1
 R102: batch_is_state_on_day[D0,b1,se] + batch_is_state_on_day[D1,b1,t]
   - batch_is_state_on_day[D3,b1,sp] <= 1
 R103: batch_is_state_on_day[D0,b1,t] + batch_is_state_on_day[D1,b1,sp]
   - batch_is_state_on_day[D3,b1,h] <= 1
 R104: batch_is_state_on_day[D2,b1,sp] - batch_is_state_on_day[D4,b1,h]
   >= 0
 R105: batch_is_state_on_day[D2,b1,t] - batch_is_state_on_day[D4,b1,sp]
   >= 0
 R106: batch_is_state_on_day[D2,b1,se] - batch_is_state_on_day[D5,b1,t]
   >= 0
 R107: batch_is_state_on_day[D1,b1,ns] + batch_is_state_on_day[D2,b1,se]
   - batch_is_state_on_day[D5,b1,t] <= 1
 R108: batch_is_state_on_day[D1,b1,se] + batch_is_state_on_day[D2,b1,t]
   - batch_is_state_on_day[D4,b1,sp] <= 1
 R109: batch_is_state_on_day[D1,b1,t] + batch_is_state_on_day[D2,b1,sp]
   - batch_is_state_on_day[D4,b1,h] <= 1
 R110: batch_is_state_on_day[D3,b1,sp] - batch_is_state_on_day[D5,b1,h]
   >= 0
 R111: batch_is_state_on_day[D3,b1,t] - batch_is_state_on_day[D5,b1,sp]
   >= 0
 R112: batch_is_state_on_day[D3,b1,se] - batch_is_state_on_day[D6,b1,t]
   >= 0
 R113: batch_is_state_on_day[D2,b1,ns] + batch_is_state_on_day[D3,b1,se]
   - batch_is_state_on_day[D6,b1,t] <= 1
 R114: batch_is_state_on_day[D2,b1,se] + batch_is_state_on_day[D3,b1,t]
   - batch_is_state_on_day[D5,b1,sp] <= 1
 R115: batch_is_state_on_day[D2,b1,t] + batch_is_state_on_day[D3,b1,sp]
   - batch_is_state_on_day[D5,b1,h] <= 1
 R116: batch_is_state_on_day[D4,b1,sp] - batch_is_state_on_day[D6,b1,h]
   >= 0
 R117: batch_is_state_on_day[D4,b1,t] - batch_is_state_on_day[D6,b1,sp]
   >= 0
 R118: batch_is_state_on_day[D4,b1,se] - batch_is_state_on_day[D7,b1,t]
   >= 0
 R119: batch_is_state_on_day[D3,b1,ns] + batch_is_state_on_day[D4,b1,se]
   - batch_is_state_on_day[D7,b1,t] <= 1
 R120: batch_is_state_on_day[D3,b1,se] + batch_is_state_on_day[D4,b1,t]
   - batch_is_state_on_day[D6,b1,sp] <= 1
 R121: batch_is_state_on_day[D3,b1,t] + batch_is_state_on_day[D4,b1,sp]
   - batch_is_state_on_day[D6,b1,h] <= 1
 R122: batch_is_state_on_day[D5,b1,sp] - batch_is_state_on_day[D7,b1,h]
   >= 0
 R123: batch_is_state_on_day[D5,b1,t] - batch_is_state_on_day[D7,b1,sp]
   >= 0
 R124: batch_is_state_on_day[D5,b1,se] - batch_is_state_on_day[D8,b1,t]
   >= 0
 R125: batch_is_state_on_day[D4,b1,ns] + batch_is_state_on_day[D5,b1,se]
   - batch_is_state_on_day[D8,b1,t] <= 1
 R126: batch_is_state_on_day[D4,b1,se] + batch_is_state_on_day[D5,b1,t]
   - batch_is_state_on_day[D7,b1,sp] <= 1
 R127: batch_is_state_on_day[D4,b1,t] + batch_is_state_on_day[D5,b1,sp]
   - batch_is_state_on_day[D7,b1,h] <= 1
 R128: batch_is_state_on_day[D6,b1,sp] - batch_is_state_on_day[D8,b1,h]
   >= 0
 R129: batch_is_state_on_day[D6,b1,t] - batch_is_state_on_day[D8,b1,sp]
   >= 0
 R130: batch_is_state_on_day[D5,b1,se] + batch_is_state_on_day[D6,b1,t]
   - batch_is_state_on_day[D8,b1,sp] <= 1
 R131: batch_is_state_on_day[D5,b1,t] + batch_is_state_on_day[D6,b1,sp]
   - batch_is_state_on_day[D8,b1,h] <= 1
 R132: - 15 irrigation[D0,1] + batch_is_state_on_day[D0,b1,se] <= 0
 R133: - 15 irrigation[D0,2] + 2 batch_is_state_on_day[D0,b1,t] <= 0
 R134: - 15 irrigation[D0,3] + 4 batch_is_state_on_day[D0,b1,sp] <= 0
 R135: - 15 irrigation[D1,1] + batch_is_state_on_day[D1,b1,se] <= 0
 R136: - 15 irrigation[D1,2] + 2 batch_is_state_on_day[D1,b1,t] <= 0
 R137: - 15 irrigation[D1,3] + 4 batch_is_state_on_day[D1,b1,sp] <= 0
 R138: - 15 irrigation[D2,1] + batch_is_state_on_day[D2,b1,se] <= 0
 R139: - 15 irrigation[D2,2] + 2 batch_is_state_on_day[D2,b1,t] <= 0
 R140: - 15 irrigation[D2,3] + 4 batch_is_state_on_day[D2,b1,sp] <= 0
 R141: - 15 irrigation[D3,1] + batch_is_state_on_day[D3,b1,se] <= 0
 R142: - 15 irrigation[D3,2] + 2 batch_is_state_on_day[D3,b1,t] <= 0
 R143: - 15 irrigation[D3,3] + 4 batch_is_state_on_day[D3,b1,sp] <= 0
 R144: - 15 irrigation[D4,1] + batch_is_state_on_day[D4,b1,se] <= 0
 R145: - 15 irrigation[D4,2] + 2 batch_is_state_on_day[D4,b1,t] <= 0
 R146: - 15 irrigation[D4,3] + 4 batch_is_state_on_day[D4,b1,sp] <= 0
 R147: - 15 irrigation[D5,1] + batch_is_state_on_day[D5,b1,se] <= 0
 R148: - 15 irrigation[D5,2] + 2 batch_is_state_on_day[D5,b1,t] <= 0
 R149: - 15 irrigation[D5,3] + 4 batch_is_state_on_day[D5,b1,sp] <= 0
 R150: - 15 irrigation[D6,1] + batch_is_state_on_day[D6,b1,se] <= 0
 R151: - 15 irrigation[D6,2] + 2 batch_is_state_on_day[D6,b1,t] <= 0
 R152: - 15 irrigation[D6,3] + 4 batch_is_state_on_day[D6,b1,sp] <= 0
 R153: - 15 irrigation[D7,1] + batch_is_state_on_day[D7,b1,se] <= 0
 R154: - 15 irrigation[D7,2] + 2 batch_is_state_on_day[D7,b1,t] <= 0
 R155: - 15 irrigation[D7,3] + 4 batch_is_state_on_day[D7,b1,sp] <= 0
 R156: - 15 irrigation[D8,1] + batch_is_state_on_day[D8,b1,se] <= 0
 R157: - 15 irrigation[D8,2] + 2 batch_is_state_on_day[D8,b1,t] <= 0
 R158: - 15 irrigation[D8,3] + 4 batch_is_state_on_day[D8,b1,sp] <= 0
Bounds
 tank[D0,1] <= 8
 tank[D0,2] <= 8
 tank[D0,3] <= 8
 tank[D1,1] <= 8
 tank[D1,2] <= 8
 tank[D1,3] <= 8
 tank[D2,1] <= 8
 tank[D2,2] <= 8
 tank[D2,3] <= 8
 tank[D3,1] <= 8
 tank[D3,2] <= 8
 tank[D3,3] <= 8
 tank[D4,1] <= 8
 tank[D4,2] <= 8
 tank[D4,3] <= 8
 tank[D5,1] <= 8
 tank[D5,2] <= 8
 tank[D5,3] <= 8
 tank[D6,1] <= 8
 tank[D6,2] <= 8
 tank[D6,3] <= 8
 tank[D7,1] <= 8
 tank[D7,2] <= 8
 tank[D7,3] <= 8
 tank[D8,1] <= 8
 tank[D8,2] <= 8
 tank[D8,3] <= 8
 irrigation[D0,1] <= 96
 irrigation[D0,2] <= 96
 irrigation[D0,3] <= 96
 irrigation[D1,1] <= 96
 irrigation[D1,2] <= 96
 irrigation[D1,3] <= 96
 irrigation[D2,1] <= 96
 irrigation[D2,2] <= 96
 irrigation[D2,3] <= 96
 irrigation[D3,1] <= 96
 irrigation[D3,2] <= 96
 irrigation[D3,3] <= 96
 irrigation[D4,1] <= 96
 irrigation[D4,2] <= 96
 irrigation[D4,3] <= 96
 irrigation[D5,1] <= 96
 irrigation[D5,2] <= 96
 irrigation[D5,3] <= 96
 irrigation[D6,1] <= 96
 irrigation[D6,2] <= 96
 irrigation[D6,3] <= 96
 irrigation[D7,1] <= 96
 irrigation[D7,2] <= 96
 irrigation[D7,3] <= 96
 irrigation[D8,1] <= 96
 irrigation[D8,2] <= 96
 irrigation[D8,3] <= 96
Binaries
 batch_is_state_on_day[D0,b1,ns] batch_is_state_on_day[D0,b1,se]
 batch_is_state_on_day[D0,b1,t] batch_is_state_on_day[D0,b1,sp]
 batch_is_state_on_day[D0,b1,h] batch_is_state_on_day[D1,b1,ns]
 batch_is_state_on_day[D1,b1,se] batch_is_state_on_day[D1,b1,t]
 batch_is_state_on_day[D1,b1,sp] batch_is_state_on_day[D1,b1,h]
 batch_is_state_on_day[D2,b1,ns] batch_is_state_on_day[D2,b1,se]
 batch_is_state_on_day[D2,b1,t] batch_is_state_on_day[D2,b1,sp]
 batch_is_state_on_day[D2,b1,h] batch_is_state_on_day[D3,b1,ns]
 batch_is_state_on_day[D3,b1,se] batch_is_state_on_day[D3,b1,t]
 batch_is_state_on_day[D3,b1,sp] batch_is_state_on_day[D3,b1,h]
 batch_is_state_on_day[D4,b1,ns] batch_is_state_on_day[D4,b1,se]
 batch_is_state_on_day[D4,b1,t] batch_is_state_on_day[D4,b1,sp]
 batch_is_state_on_day[D4,b1,h] batch_is_state_on_day[D5,b1,ns]
 batch_is_state_on_day[D5,b1,se] batch_is_state_on_day[D5,b1,t]
 batch_is_state_on_day[D5,b1,sp] batch_is_state_on_day[D5,b1,h]
 batch_is_state_on_day[D6,b1,ns] batch_is_state_on_day[D6,b1,se]
 batch_is_state_on_day[D6,b1,t] batch_is_state_on_day[D6,b1,sp]
 batch_is_state_on_day[D6,b1,h] batch_is_state_on_day[D7,b1,ns]
 batch_is_state_on_day[D7,b1,se] batch_is_state_on_day[D7,b1,t]
 batch_is_state_on_day[D7,b1,sp] batch_is_state_on_day[D7,b1,h]
 batch_is_state_on_day[D8,b1,ns] batch_is_state_on_day[D8,b1,se]
 batch_is_state_on_day[D8,b1,t] batch_is_state_on_day[D8,b1,sp]
 batch_is_state_on_day[D8,b1,h]
Generals
 tank[D0,1] tank[D0,2] tank[D0,3] tank[D1,1] tank[D1,2] tank[D1,3]
 tank[D2,1] tank[D2,2] tank[D2,3] tank[D3,1] tank[D3,2] tank[D3,3]
 tank[D4,1] tank[D4,2] tank[D4,3] tank[D5,1] tank[D5,2] tank[D5,3]
 tank[D6,1] tank[D6,2] tank[D6,3] tank[D7,1] tank[D7,2] tank[D7,3]
 tank[D8,1] tank[D8,2] tank[D8,3] irrigation[D0,1] irrigation[D0,2]
 irrigation[D0,3] irrigation[D1,1] irrigation[D1,2] irrigation[D1,3]
 irrigation[D2,1] irrigation[D2,2] irrigation[D2,3] irrigation[D3,1]
 irrigation[D3,2] irrigation[D3,3] irrigation[D4,1] irrigation[D4,2]
 irrigation[D4,3] irrigation[D5,1] irrigation[D5,2] irrigation[D5,3]
 irrigation[D6,1] irrigation[D6,2] irrigation[D6,3] irrigation[D7,1]
 irrigation[D7,2] irrigation[D7,3] irrigation[D8,1] irrigation[D8,2]
 irrigation[D8,3]
End
