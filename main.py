from random import randint

elements = {"Hydrogen":"H", "Helium":"He", "Lithium":"Li", "Beryllium":"Be", "Boron":"B", "Carbon":"C", "Nitrogen":"N", "Oxygen":"O", "Fluorine":"F", "Neon":"Ne", "Sodium":"Na", "Magnesium":"Mg", "Aluminum":"Al", "Silicon":"Si", "Phosphorus":"P", "Chlorine":"Cl", "Argon":"Ar", "Potassium":"K", "Calcium":"Ca", "Vanadium":"V", "Chromium":"Cr", "Manganese":"Mn", "Iron": "Fe", "Cobalt":"Co", "Nickel":"Ni", "Copper":"Cu", "Zinc":"Zn", "Arsenic":"As", "Selenium":"Se", "Bromine":"Br", "Krypton":"Kr", "Zirconium":"Zr", "Silver":"Ag", "Cadmium":"Cd", "Tin":"Sn", "Antimony":"Sb", "Iodine":"I", "Cesium":"Cs", "Barium":"Ba", "Platinum":"Pt", "Gold":"Au", "Mercury":"Hg", "Lead":"Pb", "Uranium":"U", "Radium":"Ra", "Bismuth":"Bi","Strontium":"Sr", "Titanium":"Ti", "Tungsten":"W", "Sulfur":"S"}
finished = []

again = True

while again:
    num1 = randint(0, 50)
    num2 = randint(0, 2)

    if num2 == 0:
        answer = input(elements[num1] + " = ")
    elif num2 == 1:
        answer = input("")
    else:
        print("ERROR, num2 wasn't 0 or 1")