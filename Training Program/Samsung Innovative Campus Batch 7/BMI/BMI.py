# -*- coding: utf-8 -*-
"""
Converted from IPYNB to PY
"""

# %% [code] Cell 1
#mengetahui tingkat kesehatan kalian
height_std_feet = 0
height_std_inches = 0
weight_std_pound = 0
height_metr_cm = 0
weight_metr_kg = 0
error = "Wrong Input. Please try again."
healthy_weight = "Congratulations, your weight is healthy!"
overweight = "You're overweight!"
obese = "You are obese, please eat more healthy food!"
extreme_obesity = "You have extreme obesity, please go to the doctor!"
std_metr = input("Standard or Metric: ").lower()
while True:
    if std_metr == "standard":
      height_std_feet = float(input("Height(feet): "))
      height_std_inches = float(input("Height(inches): "))
      weight_std_pound = float(input("Pounds: "))
    elif std_metr == "metric":
      height_metr_cm = float(input("Height(cm): "))
      weight_metr_kg = float(input("Weight(kg): "))
      height_std_feet = int(height_metr_cm * 0.0328084)
      height_std_inch = int(height_metr_cm * 0.393701 - float(int(height_metr_cm * 0.0328084)) * 12)
      weight_std_pound = weight_metr_kg * 2.20462
    else:
      print(error)
    if (height_std_feet == 4 and height_std_inches >= 10 and height_std_inches < 11):
      if weight_std_pound >= 91 and weight_std_pound < 119:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 119 and weight_std_pound < 143:
        print(overweight)
      elif weight_std_pound >= 143 and weight_std_pound < 191:
        print(obese)
      elif weight_std_pound >= 191:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 4 and height_std_inches >= 11 and height_std_inches < 12):
      if weight_std_pound >= 94 and weight_std_pound < 124:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 124 and weight_std_pound < 148:
        print(overweight)
      elif weight_std_pound >= 148 and weight_std_pound < 198:
        print(obese)
      elif weight_std_pound >= 198:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 0 and height_std_inches < 1):
      if weight_std_pound >= 97 and weight_std_pound < 124:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 124 and weight_std_pound < 153:
        print(overweight)
      elif weight_std_pound >= 153 and weight_std_pound < 204:
        print(obese)
      elif weight_std_pound >= 204:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 1 and height_std_inches < 2):
      if weight_std_pound >= 100 and weight_std_pound < 132:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 132 and weight_std_pound < 158:
        print(overweight)
      elif weight_std_pound >= 158 and weight_std_pound < 211:
        print(obese)
      elif weight_std_pound >= 211:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 2 and height_std_inches < 3):
      if weight_std_pound >= 104 and weight_std_pound < 136:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 136 and weight_std_pound < 164:
        print(overweight)
      elif weight_std_pound >= 164 and weight_std_pound < 218:
        print(obese)
      elif weight_std_pound >= 218:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 3 and height_std_inches < 4):
      if weight_std_pound >= 107 and weight_std_pound < 141:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 141 and weight_std_pound < 169:
        print(overweight)
      elif weight_std_pound >= 169 and weight_std_pound < 225:
        print(obese)
      elif weight_std_pound >= 225:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 4 and height_std_inches < 5):
      if weight_std_pound >= 110 and weight_std_pound < 145:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 145 and weight_std_pound < 174:
        print(overweight)
      elif weight_std_pound >= 174 and weight_std_pound < 232:
        print(obese)
      elif weight_std_pound >= 232:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 5 and height_std_inches < 6):
      if weight_std_pound >= 114 and weight_std_pound < 150:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 150 and weight_std_pound < 180:
        print(overweight)
      elif weight_std_pound >= 180 and weight_std_pound < 240:
        print(obese)
      elif weight_std_pound >= 240:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 6 and height_std_inches < 7):
      if weight_std_pound >= 118 and weight_std_pound < 155:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 155 and weight_std_pound < 186:
        print(overweight)
      elif weight_std_pound >= 186 and weight_std_pound < 247:
        print(obese)
      elif weight_std_pound >= 247:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 7 and height_std_inches < 8):
      if weight_std_pound >= 121 and weight_std_pound < 159:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 159 and weight_std_pound < 191:
        print(overweight)
      elif weight_std_pound >= 191 and weight_std_pound < 255:
        print(obese)
      elif weight_std_pound >= 255:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 8 and height_std_inches < 9):
      if weight_std_pound >= 125 and weight_std_pound < 164:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 164 and weight_std_pound < 197:
        print(overweight)
      elif weight_std_pound >= 197 and weight_std_pound < 262:
        print(obese)
      elif weight_std_pound >= 262:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 9 and height_std_inches < 10):
      if weight_std_pound >= 128 and weight_std_pound < 169:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 169 and weight_std_pound < 203:
        print(overweight)
      elif weight_std_pound >= 203 and weight_std_pound < 270:
        print(obese)
      elif weight_std_pound >= 270:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 10 and height_std_inches < 11):
      if weight_std_pound >= 132 and weight_std_pound < 174:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 174 and weight_std_pound < 209:
        print(overweight)
      elif weight_std_pound >= 209 and weight_std_pound < 278:
        print(obese)
      elif weight_std_pound >= 278:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 5 and height_std_inches >= 11 and height_std_inches < 12):
      if weight_std_pound >= 136 and weight_std_pound < 179:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 179 and weight_std_pound < 215:
        print(overweight)
      elif weight_std_pound >= 215 and weight_std_pound < 286:
        print(obese)
      elif weight_std_pound >= 286:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 6 and height_std_inches >= 0 and height_std_inches < 1):
      if weight_std_pound >= 140 and weight_std_pound < 184:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 184 and weight_std_pound < 221:
        print(overweight)
      elif weight_std_pound >= 221 and weight_std_pound < 294:
        print(obese)
      elif weight_std_pound >= 294:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 6 and height_std_inches >= 1 and height_std_inches < 2):
      if weight_std_pound >= 144 and weight_std_pound < 189:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 189 and weight_std_pound < 227:
        print(overweight)
      elif weight_std_pound >= 227 and weight_std_pound < 302:
        print(obese)
      elif weight_std_pound >= 302:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 6 and height_std_inches >= 2 and height_std_inches < 3):
      if weight_std_pound >= 148 and weight_std_pound < 194:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 194 and weight_std_pound < 233:
        print(overweight)
      elif weight_std_pound >= 233 and weight_std_pound < 311:
        print(obese)
      elif weight_std_pound >= 311:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 6 and height_std_inches >= 3 and height_std_inches < 4):
      if weight_std_pound >= 152 and weight_std_pound < 200:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 200 and weight_std_pound < 246:
        print(overweight)
      elif weight_std_pound >= 246 and weight_std_pound < 328:
        print(obese)
      elif weight_std_pound >= 328:
        print(extreme_obesity)
      else:
        print(error)
    elif (height_std_feet == 6 and height_std_inches >= 4 and height_std_inches < 5):
      if weight_std_pound >= 156 and weight_std_pound < 205:
        print(f"{healthy_weight}")
      elif weight_std_pound >= 205 and weight_std_pound < 205:
        print(overweight)
      elif weight_std_pound >= 205 and weight_std_pound < 246:
        print(obese)
      elif weight_std_pound >= 246:
        print(extreme_obesity)
      else:
        print(error)
    else:
      print(error)
    break
