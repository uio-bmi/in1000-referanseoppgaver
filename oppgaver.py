


a = 2
b = a
b += 1
print(a)

##

a = [1, 2, 3]
b = a
b[0] = 10
print(a)

##

a = [1, 2, 3]
b = a
b[0] += 1
print(a)

##
a = [1, 2, 3]
b = a
c = b[0]
c += 1
print(b)
print(a)

##

def oek_tall_med_en(tall):
    tall += 1

tall = 4
oek_tall_med_en(tall)
print(tall)

##

def oek_forste_tall_med_en(talliste):
    talliste[0] += 1

tall = [1, 2, 3]
oek_forste_tall_med_en(tall)
print(tall)

##

class Tall():
    def __init__(self, tall):
        self.tall = tall

def legg_til_en(tall):
    tall.tall += 1

t = Tall(4)
legg_til_en(t)
print(t.tall)

##

def nullstill_foerste_element_i_liste(liste):
    liste[0] = 0

a = [1, 2, 3]
nullstill_foerste_element_i_liste(a)
print(a)


##

def nullstill_liste(liste):
    for element in liste:
        element = 0

a = [1, 2, 3]
nullstill_liste(a)
print(a)

##

def erstatt_element_i_liste(liste, erstatt_posisjon, erstatt_med):
    liste[erstatt_posisjon] = erstatt_med

a = [1, 2, 3]
erstatt_element_i_liste(a, 1, 1)
print(a)

##

def erstatt_liste(liste, erstatt_med_liste):
    liste = erstatt_med_liste

liste = [1, 2, 3]
erstatt_liste(liste, [1, 1, 3])
print(liste)

##

def ok_alt_med_en(liste):
    for tall in liste:
        tall += 1

a  = [1, 2, 3]
ok_alt_med_en(a)
print(a)

##

def ok_forste_tre_tall_med_1(liste):
    liste[0] += 1
    liste[1] += 1
    liste[2] += 1

tall = [1, 2, 3]
ok_forste_tre_tall_med_1(tall)
print(tall)

