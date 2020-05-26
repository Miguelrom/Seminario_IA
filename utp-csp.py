
def imprimir_horario(horas, horario):

    print("____________" + "_______________" * 7)

    print("|%10s| %12s | %12s | %12s | %12s | %12s | %12s | %12s |" 
    % ("Hora/Salón", "S101", "s102", "s103", "L201", "L202", "L203", "VIP"))

    print("|__________|" + "______________|" * 7)

    for i in range(len(horas)):
        print("|%10s| %12s | %12s | %12s | %12s | %12s | %12s | %12s |" 
        % (horas[i], horario[7*i], horario[7*i+1], horario[7*i+2], 
        horario[7*i+3], horario[7*i+4], horario[7*i+5], horario[7*i+6]))

        print("|__________|" + "______________|" * 7)

#---------------------------------------------------------------------------


from constraint import Problem, AllDifferentConstraint

problema = Problem()

#Primer semestre
problema.addVariable("calc_1", [7])
problema.addVariable("geom", [14])
problema.addVariable("alg_sup", [21])
problema.addVariable("apren", [28])
problema.addVariable("intro_cc", [35, 39, 40])
problema.addVariable("diseño_algo", [42, 46, 47])

#Tercer semestre
problema.addVariable("calc_3", [43, 44])
problema.addVariable("ec_difs", [15, 22, 29])
problema.addVariable("fluidos", [22, 15, 29])
problema.addVariable("progra_avan", [33, 40, 47])
problema.addVariable("análi_num1", [39, 32, 46])
problema.addVariable("expre_oe", [8])

#Quinto semestre
problema.addVariable("estadística", [29, 22])
problema.addVariable("análi_log", [36])
problema.addVariable("sist_dig", [16])
problema.addVariable("leng_prog", [48, 29])
problema.addVariable("ing_II", [26, 19, 12])
problema.addVariable("contexto_reg", [51, 44])

#Séptimo semestre
problema.addVariable("opt_esp_2", [40, 39, 33])
problema.addVariable("opt_esp_3", [47, 46])
problema.addVariable("sis_ops", [23])
problema.addVariable("redes_comp", [30])
problema.addVariable("adoo", [12, 19])
problema.addVariable("opt_int_2", [54, 53, 46, 47])

#Extras
problema.addVariable("análisis_alg", [10])
problema.addVariable("graficación", [17])
problema.addVariable("estructuras", [39, 47])

#RESTRICCIONES

#R1.- No se puede impartir una materia a la misma hora y en el mismo salón que otra
problema.addConstraint(AllDifferentConstraint())

#R2.- Materias del mismo semestre no pueden impartirse a la misma hora.

sem_1 = ["calc_1", "geom", "alg_sup", "apren", "intro_cc", "diseño_algo"]
sem_3 = ["calc_3", "ec_difs", "fluidos", "progra_avan", "análi_num1", "expre_oe"]
sem_5 = ["estadística", "análi_log", "sist_dig", "leng_prog", "ing_II", "contexto_reg"]
sem_7 = ["opt_esp_2", "opt_esp_3", "sis_ops", "redes_comp", "adoo", "opt_int_2"]

for i in range(len(sem_1)):
    for j in range(i+1, len(sem_1)):
        problema.addConstraint(lambda var_1, var_2: var_1 // 7 != var_2 // 7, (sem_1[i], sem_1[j])) 


for i in range(len(sem_3)):
    for j in range(i+1, len(sem_3)):
        problema.addConstraint(lambda var_1, var_2: var_1 // 7 != var_2 // 7, (sem_3[i], sem_3[j]))


for i in range(len(sem_5)):
    for j in range(i+1, len(sem_5)):
        problema.addConstraint(lambda var_1, var_2: var_1 // 7 != var_2 // 7, (sem_5[i], sem_5[j]))


for i in range(len(sem_7)):
    for j in range(i+1, len(sem_7)):
        problema.addConstraint(lambda var_1, var_2: var_1 // 7 != var_2 // 7, (sem_7[i], sem_7[j]))


#R3.- Materias optativas no pueden impartirse a la misma hora.
optativas = ["opt_int_2", "opt_esp_2", "opt_esp_3"]

for i in range(len(optativas)):
    for j in range(i+1, len(optativas)):
        problema.addConstraint(lambda var_1, var_2: var_1 // 7 != var_2 // 7, (optativas[i], optativas[j]))

        

horas = ["7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]

horario_uno = [" " for i in range(63)]
horario_dos = [" " for i in range(63)]
horario_tres = [" " for i in range(63)]

soluciones = problema.getSolutions()

for materia, posicion in soluciones[0].items():
    horario_uno[posicion] = materia

for materia, posicion in soluciones[20].items():
    horario_dos[posicion] = materia

for materia, posicion in soluciones[40].items():
    horario_tres[posicion] = materia


print(soluciones[0])

imprimir_horario(horas, horario_uno)
print()
imprimir_horario(horas, horario_dos)
print()
imprimir_horario(horas, horario_tres)
print()


print("Número de soluciones:", len(soluciones))


#--------------------------------------------------------------------