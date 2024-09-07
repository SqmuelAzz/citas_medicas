import os
from paciente import Paciente
from medico import Medico
from cita import Cita
from horario import Horario
from admnistrador import Administrador
from reportes import Reporte

get_paciente = Paciente()
get_medico = Medico()
get_cita = Cita()
get_horario = Horario()
get_administrdor = Administrador()
get_reportes = Reporte()



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
    listar_citas = get_cita.mostrar_citas()
    print("Citas pendientes")
    for cita in listar_citas:
        print(f"ID Cita: {cita[0]} |  Paciente: {cita[1]}")
    print()
    idCita = input("Dgite el id de la cita a notificar: ")
    lst_citas = get_cita.notificar_cita_paciente(idCita)
    #print(lst_citas)
    if lst_citas[6] == 'email':
        tipo = "correo electronico"
        medio = lst_citas[4]
    else:
        tipo = "celular"
        medio = lst_citas[5]
    mensaje = f"Señor(a) <<{lst_citas[3]}>> se le recuerda su cita medica para la fecha <<{lst_citas[1]}>>, la cual a sido enviada a su {tipo} <<{medio}>>, gracias por su puntual asistencia."
    #print(mensaje)
    return (lst_citas[0],lst_citas[2],mensaje,medio,"enviada")
    

def menu_pacientes():
    os.system("cls")
    continuar = True 
    while continuar:
        print("\n\nSeleccione una Opcion ")
        print("    (1) Agregar paciente")
        print("    (2) Agendar_cita")
        print("    (3) Cancelar cita")
        print("    (4) Enviar recordatorio")
        print("    (5) Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            os.system("cls")
            print("Agregar paciente")
            datos_paciente = pedir_datos_pacientes()
            
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
            get_cita.crear_notificacion(recordatorio)

        elif opcion == 5:
            continuar = False
            break
        else:
            print("Debe elegir una opcion entre 1 y 9")
        input("Presione una tecla para continmuar...")
        os.system("cls")

#Medicos
def pedir_datos_medico():
    nombre = input("Digite el nombre completo del medico: ")
    especialidad = input("Digite la especialidad del medico: ")
    telefono = input("Digite el telefono celular del medico: ")
    email = input("Digite el correo electronico del medico: ")
    return (nombre,especialidad,telefono,email)

def pedir_datos_agenda():
    listar_medicos = get_medico.mostrar_medicos()
    print("Medicos disponibles")
    for medico in listar_medicos:
        print(f"{medico[0]} : {medico[1]}")
    print()
    resp = input("Desea crear la agenda del medico?, <S/N>: ")
    if resp.upper() == 'S':
        dia = input("Dgite el nombre deldia (Lunes - Viernes): ")
        hora_inicio = input("Digite la hora de inicio: ")
        hora_fin = input("Digite la hora de finalizacion: ")
        idMedico = input("Digite el id del medico: ")
        return (dia,hora_inicio,hora_fin,idMedico)
    else:
        return False

def pedir_datos_medico_cancelar_citas():
    listado_citas = get_medico.mostrar_citas_medicas()
    print()
    #print(listado_citas)
    for cita in listado_citas:
        print(f"ID Cita: {cita[0]}| Fecha: {cita[1]}| Estado: {cita[2]}| Medico:  {cita[4]}")
    print()
    resp = input("Desea cancelar una cita?, <S/N>: ")
    if resp.upper() == 'S':
        idCita = input("Dgite el id de la cita a cancelar: ")
        medico = get_cita.cargar_una_cita(idCita)
        motivo = input("Digite el moitvo de cancelacion: ")
        mensaje = f"Cita cancelada por el medico {medico[0]}"
        return (idCita,motivo,mensaje)
    else:
        return False


def menu_medicos():
    os.system("cls")
    continuar = True 
    while continuar:
        print("\n\nSeleccione una Opcion ")
        print("    (1) Agregar medico")
        print("    (2) Agregar disponibilidad")
        print("    (3) Cancelar cita")
        print("    (4) Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            os.system("cls")
            print("Agregar medico")
            datos_medico = pedir_datos_medico()
            get_medico.crear_medico(datos_medico)
        elif opcion == 2:
            print("Agendar disponibilidad")
            datos_agenda = pedir_datos_agenda()
            if datos_agenda:
                get_horario.crear_agenda(datos_agenda)
        elif opcion == 3:
            print("Cancelar citas")
            cancelar_citas = pedir_datos_medico_cancelar_citas()
            if cancelar_citas:
                get_medico.cancelar_cita(cancelar_citas)
        elif opcion == 4:
            continuar = False
            break
        else:
            print("Debe elegir una opcion entre 1 y 9")
        input("Presione una tecla para continmuar...")
        os.system("cls")



#Administradores
def pedir_datos_adm():
    nombre = input("Digite el nombre completo: ")
    email = input("Digite la email: ")
    telefono = input("Digite el telefono: ")
    cargo = input("Digite el cargo: ")
    return (nombre,email,telefono,cargo)

def menu_administradores():
    os.system("cls")
    continuar = True
    idAdm = 1 
    while continuar:
        print("\n\nSeleccione una Opcion ")
        print("    (1) Agregar administrador")
        print("    (2) Reporce citas programadas")
        print("    (3) Reporte citas canceladas")
        print("    (4) Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            os.system("cls")
            print("Agregar Administrador")
            datos_adm = pedir_datos_adm()
            get_administrdor.crear_administrador(datos_adm)
        elif opcion == 2:
            print("Reporte citas programadas")
            reporte_citas_programadas = get_administrdor.generar_reporte_citas_programadas()
            for rep in reporte_citas_programadas:
                print(F"Fecha: {rep[0]} | Paciente: {rep[1]} | Medico: {rep[2]} | Especialidad: {rep[3]} | Estado: {rep[4]}")
                get_reportes.guardar_reporte_citas_programadas(idAdm,'ReporteCitasProgramadas',rep[0],rep[1],rep[2],rep[3],rep[4])
            print()
            #rep_citas = (idAdm,rep[0],rep[1],rep[2],rep[3],rep[4])
            
        elif opcion == 3:
            print("Reporte citas canceladas")
            citas_canceladas = get_administrdor.generar_reporte_citas_canceladas()
            for rep in citas_canceladas:
                print(F"Fecha: {rep[0]} | Paciente: {rep[1]} | Medico: {rep[2]} | Modifico: {rep[3]} | Motivo: {rep[4]}")
                get_reportes.guardar_reporte_citas_canceladas(idAdm,'ReporteCitasCanceladas',rep[0],rep[1],rep[2],rep[3],rep[4])
            print()
            
        elif opcion == 4:
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
        print("    (2) Gestion de Medicos")
        print("    (3) Gestion de Administradores")



        print("    (9) Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            os.system("cls")
            print("Manejo de pacientes")
            menu_pacientes()
        if opcion == 2:
            os.system("cls")
            print("Manejo de Medicos")
            menu_medicos()
        if opcion == 3:
            os.system("cls")
            print("Manejo de Administradores")
            menu_administradores()
        elif opcion == 9:
            continuar = False
            break
        else:
            print("Debe elegir una opcion entre 1 y 9")
        input("Presione una tecla para continmuar...")
        os.system("cls")





if __name__ == "__main__":
    menu_principal()