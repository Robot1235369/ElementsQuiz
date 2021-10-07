from random import randint

elements = {"Hydrogen":"H", "Helium":"He", "Lithium":"Li", "Beryllium":"Be", "Boron":"B", "Carbon":"C", "Nitrogen":"N", "Oxygen":"O", "Fluorine":"F", "Neon":"Ne", "Sodium":"Na", "Magnesium":"Mg", "Aluminum":"Al", "Silicon":"Si", "Phosphorus":"P", "Chlorine":"Cl", "Argon":"Ar", "Potassium":"K", "Calcium":"Ca", "Vanadium":"V", "Chromium":"Cr", "Manganese":"Mn", "Iron": "Fe", "Cobalt":"Co", "Nickel":"Ni", "Copper":"Cu", "Zinc":"Zn", "Arsenic":"As", "Selenium":"Se", "Bromine":"Br", "Krypton":"Kr", "Zirconium":"Zr", "Silver":"Ag", "Cadmium":"Cd", "Tin":"Sn", "Antimony":"Sb", "Iodine":"I", "Cesium":"Cs", "Barium":"Ba", "Platinum":"Pt", "Gold":"Au", "Mercury":"Hg", "Lead":"Pb", "Uranium":"U", "Radium":"Ra", "Bismuth":"Bi","Strontium":"Sr", "Titanium":"Ti", "Tungsten":"W", "Sulfur":"S"}
finished = []

keys = list(elements.keys())
values = list(elements.values())

i = 1
right = 0
wrong = 0

while i <= len(keys) * 2:

    a = True

    while a:
        
        num1 = randint(0, 50)
        num2 = randint(0, 2)

        if num2 == 0:
            answer = values[num1]

            if answer in finished:
                a = True
            else:
                a = False
                finished.append(answer)
                guess = input("\n" + keys[num1] + " = ")
        elif num2 == 1:
            answer = keys[num1]

            if answer in finished:
                a = True
            else:
                a = False
                finished.append(answer)
                guess = input("\n" + values[num1] + " = ")

    if guess == "?":
        print("answer: " + answer)
        wrong += 1
    elif guess == answer:
            right += 1
            print("correct")
    else:
        print("incorrect")
        wrong += 1
        print("answer: " + answer)
    i += 1

print("correct: " + right)
print("incorrect: " + wrong)
print("total: " + right + wrong)