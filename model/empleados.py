import pymongo

class Empleados:
    def __str__(self, cedula=1, Nombre=2, Apellidos=3, Telefono=4, Direccion=5, Puesto=6, FechaIngreso=7, Jefatura=8):
        self.Cedula= cedula
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Telefono =Telefono
        self.Direccion =Direccion
        self.Puesto =Puesto
        self.FechaIngreso = FechaIngreso
        self.Jefatura =Jefatura

    def guardarEM(self):
        estado=0
        #abrir la conexión mediante un objeto cliente
        Empleados = pymongo.MongoClient("mongodb://localhost:27017")
        #seleccionar la tabla a utilizar
        bd = Empleados["Los Patitos"]
        try:
            #definir la tabla a utilizar
            tbl = bd["empleados"]
            #crear diccionario
            doc={"cedula":self.Cedula,
                "nombre":self.Nombre,
                "apellidos":self.Apellidos,
                "telefono":self.Telefono,
                "direccion":self.Direccion,
                "puesto": self.Puesto,
                "fecha de ingreso":self.FechaIngreso,
                "jefatura":self.Jefatura}
            #insertar en la tabla
            tbl.insert_one(doc)
            estado=1
        except Exception:
            print("Error al guardar")
            estado=0
        finally:
            Empleados.close        
        return estado

    def editarEM(self):
        estado = 0
        # abrir la conexión mediante un objeto cliente
        Empleados = pymongo.MongoClient("mongodb://localhost:27017")
        # seleccionar la tabla a utilizar
        bd = Empleados ["Los Patitos"]
        try:
            # definir la tabla a utilizar
            tbl = bd["empleados"]
            # filtro
            filtro = {"nombre": self}
            # crear diccionario
            doc={"cedula":self.Cedula,
                "nombre":self.Nombre,
                "apellidos":self.Apellidos,
                "telefono":self.Telefono,
                "direccion":self.Direccion,
                "puesto": self.Puesto,
                "fecha de ingreso":self.FechaIngreso,
                "jefatura":self.Jefatura}
            # modifcar en la tabla
            tbl.update_one(filtro,doc)
            estado = 1
        except Exception:
            print("Error al editar")
            estado = 0
        finally:
            Empleados.close
        return estado

    def eliminarEM(self):
        estado = 0
        # abrir la conexión mediante un objeto cliente
        Empleados = pymongo.MongoClient("mongodb://localhost:27017")
        # seleccionar la tabla a utilizar
        bd = Empleados ["Los Patitos"]
        try:
            # definir la tabla a utilizar
            tbl = bd["empleados"]
            # filtro
            filtro = {"nombre": self}
            # modifcar en la tabla
            tbl.delete_one(filtro)
            estado = 1
        except Exception:
            print("Error al eliminar")
            estado = 0
        finally:
            Empleados.close()
        return estado

    def getEmpleados(self):
        Empleados = pymongo.MongoClient("mongodb://localhost:27017")
        bd = Empleados["Los Patitos"]
        tbl = bd["empleados"]
        return tbl.find()

    def getNumeroRegistrosEM(self):
        Usuarios = pymongo.MongoClient("mongodb://localhost:27017")
        bd = Empleados["Los Patitos"]
        size=bd.command("collstats","empleados")
        return size["count"]