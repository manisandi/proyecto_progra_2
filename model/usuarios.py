import pymongo

class Usuarios:
    def __init__(self, usuario=1, contrasenia=2):
        self.usuario=usuario
        self.contrasenia = contrasenia

    def guardarUS(self):
        estado=0
        #abrir la conexión mediante un objeto 
        Usuarios = pymongo.MongoClient("mongodb://localhost:27017")
        #seleccionar la tabla a utilizar
        bd = Usuarios["Los Patitos"]
        try:
            #definir la tabla a utilizar
            tbl = bd["usuarios"]
            #crear diccionario
            doc={"usuario":self.usuario,
                "contrasenia":self.contrasenia,
                }
            #insertar en la tabla
            tbl.insert_one(doc)
            estado=1
        except Exception:
            print("Error al guardar")
            estado=0
        finally:
            Usuarios.close        
        return estado

    def editarUS(self):
        estado = 0
        # abrir la conexión mediante un objeto 
        Usuarios = pymongo.MongoClient("mongodb://localhost:27017")
        # seleccionar la tabla a utilizar
        bd = Usuarios ["Los Patitos"]
        try:
            # definir la tabla a utilizar
            tbl = bd["usuarios"]
            # filtro
            filtro = {"nombre": self.nombre}
            # crear diccionario
            doc={"usuario":self.usuario,
                "contrasenia":self.contrasenia,
                }
            # modifcar en la tabla
            tbl.update_one(filtro,doc)
            estado = 1
        except Exception:
            print("Error al editar")
            estado = 0
        finally:
            Usuarios.close
        return estado

    def eliminarUS(self):
        estado = 0
        # abrir la conexión mediante un objeto
        Usuarios = pymongo.MongoClient("mongodb://localhost:27017")
        # seleccionar la tabla a utilizar
        bd = Usuarios ["Los Patitos"]
        try:
            # definir la tabla a utilizar
            tbl = bd["usuarios"]
            # filtro
            filtro = {"nombre": self.nombre}
            # modifcar en la tabla
            tbl.delete_one(filtro)
            estado = 1
        except Exception:
            print("Error al eliminar")
            estado = 0
        finally:
            Usuarios.close
        return estado

    def getUsuarios(self):
        Usuarios = pymongo.MongoClient("mongodb://localhost:27017")
        bd = Usuarios["Los Patitos"]
        tbl = bd["usuarios"]
        return tbl.find()

    def getNumeroRegistrosUS(self):
        Usuarios = pymongo.MongoClient("mongodb://localhost:27017")
        bd = Usuarios["Los Patitos"]
        size=bd.command("collstats","usuario")
        return size["count"]