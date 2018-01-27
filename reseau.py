import os 

'''tableau dpour chaque canal'''
t01 = []
t02 = []
t03 = []
t04 = []
t05 = []
t06 = []
t07 = []
t08 = []
t09 = []
t10 = []
t11 = []
t12 = []
t13 = []

quality = 1 
maxquality1 = 0
maxquality2 = 0
maxquality3 = 0
maxquality4 = 0
maxquality5 = 0
maxquality6 = 0
maxquality7 = 0
maxquality8 = 0
maxquality9 = 0
maxquality10 = 0
maxquality11 = 0
maxquality12 = 0
maxquality13 = 0
superquality = 0
supercanal = 0

i = 0
'''decouverte des reseaux '''
f = os.popen('iwlist wlan0 scan | egrep \'Quality|Channel\'')
'''on classe chaque qualite pour chaque channel'''
for line in f :
	t = line.replace('=',' ').replace('/',' ').replace(':',' ').split()
	if t[0] == 'Quality':
		quality = t[1]
	if t[0] == 'Channel':
		if t[1] == '1' :
			t01.append(quality)
		if t[1] == '2' :
			t02.append(quality)
		if t[1] == '3' :
			t03.append(quality)
		if t[1] == '4' :
			t04.append(quality)
		if t[1] == '5' :
			t05.append(quality)
		if t[1] == '6' :
			t06.append(quality)
		if t[1] == '7' :
			t07.append(quality)
		if t[1] == '8' :
			t08.append(quality)
		if t[1] == '9' :
			t09.append(quality)
		if t[1] == '10' :
			t10.append(quality)
		if t[1] == '11' :
			t11.append(quality)
		if t[1] == '12' :
			t12.append(quality)
		if t[1] == '13' :
			t13.append(quality)


'''Recherche de la meilleur qualite sur chaque canal'''
i = 0
while i < len(t01) : 
	if maxquality1 < t01[i] :
		maxquality1 = t01[i]
	i = i + 1
i = 0
while i < len(t02) : 
	if maxquality2 < t02[i] :
		maxquality2 = t02[i]
	i = i + 1
i = 0
while i < len(t03) : 
	if maxquality3 < t03[i] :
		maxquality3 = t03[i]
	i = i + 1
i = 0
while i < len(t04) : 
	if maxquality4 < t04[i] :
		maxquality4 = t04[i]
	i = i + 1
i = 0
while i < len(t05) : 
	if maxquality5 < t05[i] :
		maxquality5 = t05[i]
	i = i + 1

while i < len(t06) : 
	if maxquality6 < t06[i] :
		maxquality6 = t06[i]
	i = i + 1
i = 0
while i < len(t07) : 
	if maxquality7 < t07[i] :
		maxquality7 = t07[i]
	i = i + 1
i = 0
while i < len(t08) : 
	if maxquality8 < t08[i] :
		maxquality8 = t08[i]
	i = i + 1
i = 0
while i < len(t09) : 
	if maxquality9 < t09[i] :
		maxquality9 = t09[i]
	i = i + 1
i = 0
while i < len(t10) : 
	if maxquality10 < t10[i] :
		maxquality10 = t10[i]
	i = i + 1	
i = 0
while i < len(t11) : 
	if maxquality11 < t11[i] :
		maxquality11 = t11[i]
	i = i + 1

while i < len(t12) : 
	if maxquality12 < t12[i] :
		maxquality12 = t12[i]
	i = i + 1
i = 0
while i < len(t13) : 
	if maxquality13 < t13[i] :
		maxquality13 = t13[i]
	i = i + 1

'''ajout des perturbations de chaque canal'''
quality1 = maxquality1
quality2 = maxquality2
quality3 = maxquality3
quality4 = maxquality4
quality5 = maxquality5
quality6 = maxquality6
quality7 = maxquality7
quality8 = maxquality8
quality9 = maxquality9
quality10 = maxquality10
quality11 = maxquality11
quality12 = maxquality12
quality13 = maxquality13
maxquality1 = int(quality1) + int(quality2) / 2 + int(quality3) / 3
maxquality2 = int(quality2) + int(quality1) / 2 + int(quality3) / 2 + int(quality4) /3
maxquality3 = int(quality3) + int(quality1) / 3 + int(quality2) / 2 + int(quality4) / 2 + int(quality5) / 3
maxquality4 = int(quality4) + int(quality2) / 3 + int(quality3) / 2 + int(quality5) / 2 + int(quality6) / 3
maxquality5 = int(quality5) + int(quality3) / 3 + int(quality4) / 2 + int(quality6) / 2 + int(quality7) / 3 
maxquality6 = int(quality6) + int(quality4) / 3 + int(quality5) / 2 + int(quality7) / 2 + int(quality8) / 3
maxquality7 = int(quality7) + int(quality5) / 3 + int(quality6) / 2 + int(quality8) / 2 + int(quality9) / 3
maxquality8 = int(quality8) + int(quality6) / 3 + int(quality7) / 2 + int(quality9) / 2 + int(quality10) / 3
maxquality9 = int(quality9) + int(quality7) / 3 + int(quality8) / 2 + int(quality10) / 2 + int(quality11) / 3
maxquality10 = int(quality10) + int(quality8) / 3 + int(quality9) / 2 + int(quality11) / 2 + int(quality12) / 3
maxquality11 = int(quality11) + int(quality9) / 3 + int(quality10) / 2 + int(quality12) / 2 + int(quality13) / 3
maxquality12 = int(quality12) + int(quality10) / 3 + int(quality11) / 2 + int(quality13) / 2
maxquality13 = int(quality13) + int(quality11) / 3 + int(quality12) / 2

'''comparaison des qualites entre chaque reseau'''
if maxquality1 == maxquality2 :
	if maxquality1 <= superquality :
		superquality = maxquality1
		canal = 1.2
elif maxquality1 < maxquality2 :
	superquality = maxquality1
	supercanal = 1
else :
	superquality = maxquality2
	supercanal = 2


if maxquality3 == maxquality4 :
	if maxquality3 <= superquality :
		superquality = maxquality3
		canal = 3.4
elif maxquality3 < maxquality4 :
	if maxquality3 <= superquality :
		superquality = maxquality3
		supercanal = 3
else :
	if maxquality4 <= superquality :
		superquality = maxquality4
		supercanal = 4

if maxquality5 == maxquality6 :
	if maxquality5 <= superquality :
		superquality = maxquality5
		canal = 5.6
elif maxquality5 < maxquality6 :
	if maxquality5 <= superquality :
		superquality = maxquality5
		supercanal = 5
else :
	if maxquality6 <= superquality :
		superquality = maxquality6
		supercanal = 6

if maxquality7 == maxquality8 :
	if maxquality7 <= superquality :
		superquality = maxquality7
		supercanal = 7.8
elif maxquality7 < maxquality8 :
	if maxquality7 <= superquality :
		superquality = maxquality7
		supercanal = 7
else :
	if maxquality8 <= superquality :
		superquality = maxquality8
		supercanal = 8

if maxquality9 == maxquality10 :
	if maxquality9 <= superquality :
		superquality = maxquality9
		supercanal = 9.10
elif maxquality9 < maxquality10 :
	if maxquality9 <= superquality :
		superquality = maxquality9
		supercanal = 9
else :
	if maxquality10 <= superquality :
		superquality = maxquality10
		supercanal = 10

if maxquality11 == maxquality12 :
	if maxquality11 <= superquality :
		superquality = maxquality11
		supercanal = 11.12
elif maxquality11 < maxquality12 :
	if maxquality11 <= superquality :
		superquality = maxquality11
		supercanal = 11
else :
	if maxquality12 <= superquality :
		superquality = maxquality12
		supercanal = 12

if maxquality13 <= superquality :
		superquality = maxquality13
		supercanal = 13


'''affiche tous les canaux avec leur affaiflissement'''
print(maxquality1)
print(maxquality2)
print(maxquality3)
print(maxquality4)
print(maxquality5)
print(maxquality6)
print(maxquality7)
print(maxquality8)
print(maxquality9)
print(maxquality10)
print(maxquality11)
print(maxquality12)
print(maxquality13)


'''affichage du meilleur canal sur lequel generer le signal wiwi'''
print('le meilleur canal pour se connecter sera : ')
print(supercanal)