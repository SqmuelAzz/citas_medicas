import os
from paciente import Paciente
from medico import Medico
from cita import Cita

get_paciente = Paciente()
get_medico = Medico()
get_cita = Cita()



def pedir_datos_pacientes():
    nombre = input("Digite el nombre completo del paciente: ")
    email = input("Digite correctamente el e-mail del paciente: ")
    telefono = input("Digite correctamente el telefono del paciente: ")
    direccion = input("Digite correctamente la direccion del paciente: ")
    notificacion = input("Digite el modo de notificacion preferido del paciente: ")
    return (nombre,email,telefono,direccion,notificacion)

def pedir_datos_cita():
    listar_pacientes = get_paciente.mostrar_pacientes()
    print()
    print("Pacientes en el sistema")
    for paciente in listar_pacientes:
        print(f"{paciente[0]} : {paciente[1]}")
    print()
    listar_medicos = get_medico.mostrar_medicos()
    print("Medicos disponibles")
    for medico in listar_medicos:
        print(f"{medico[0]} : {medico[1]}")
    print()
    resp = input("Desea crear agendar la cita?, <S/N>: ")
    if resp.upper() == 'S':
        fecha = input("Dgite fecha de la cita <YYYY-DD-MM>: ")
        idPaciente = input("Digite el id del paciente: ")
        idMedico = input("Digite el id del medico: ")
        motivo = input("Digite el motivo de consulta: ")
        duracion = input("Digite la duracion de la cita en minutos: ")
        return (fecha,idPaciente,idMedico,motivo,duracion)
    else:
        return False

def pedir_datos_cancelar():
    listar_citas = get_cita.mostrar_citas()
    print()
    print("Citas pendientes")
    for cita in listar_citas:
        print(f"ID Cita: {cita[0]},  Paciente: {cita[1]}, Medico: {cita[2]}, Motivo consulta: {cita[3]}")
    print()
    resp = input("Desea cancelar la cita?, <S/N>: ")
    if resp.upper() == 'S':
        idCita = input("Dgite el id de la cita a cancelar ")
        return idCita
    else:
        return False

def pedir_datos_recordatorio():
    listar_citas = get_cita.notificar_cita_paciente()
    print("Citas pendientes")
    for cita in listar_citas:
        print(f"ID Cita: {cita[0]},  Paciente: {cita[1]}, Medico: {cita[2]}, Motivo consulta: {cita[3]}")
    print()
    idCita = input("Dgite el id de la cita a notificar: ")
    return idCita
      

def menu_pacientes():
    os.system("cls")
    continuar = True 
    while continuar:
        print("\n\nSeleccione una Opcion ")
        print("    (1) Agregar paciente")
        print("    (2) Agendar_cita")
        print("    (3) Cancelar cita")
        print("    (4) Enviar recordatorio")
        print("    (9) Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            os.system("cls")
            print("Agregar paciente")
            datos_paciente = pedir_datos_pacientes()
            #print(datos_paciente)
            get_paciente.crear_paciente(datos_paciente)
        elif opcion == 2:
            print("Agendar citas")
            datos_cita = pedir_datos_cita()
            if datos_cita:
                get_cita.crear_cita(datos_cita)
        elif opcion == 3:
            print("Cancelar citas")
            cancelar = pedir_datos_cancelar()
            if cancelar:
                get_cita.cancelar_cita(cancelar)
        elif opcion == 4:
            print("Enviar recordatorio")
            recordatorio = pedir_datos_recordatorio()
            print(recordatorio)

        elif opcion == 9:
            continuar = False
            break
        else:
            print("Debe elegir una opcion entre 1 y 9")
        input("Presione una tecla para continmuar...")
        os.system("cls")


def menu_principal():
    os.system("cls")
    continuar = True 
    while continuar:
        print("\n\nSeleccione una Opcion ")
        print("    (1) Gestion de Pacientes")



        print("    (9) Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            os.system("cls")
            print("Manejo de pacientes")
            menu_pacientes()
        elif opcion == 9:
            continuar = False
            break
        else:
            print("Debe elegir una opcion entre 1 y 9")
        input("Presione una tecla para continmuar...")
        os.system("cls")





if __name__ == "__main__":
    menu_principal()