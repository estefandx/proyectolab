

from django.db import models
from django.contrib.auth.models import User

# CEDULA_CIUDADANIA="CEDULA_CIUDADANIA"
# CEDULA_EXTRANJERA="CEDULA_EXTRANJERA"
# MASCULINO="MASULIINO"
# FEMENINO="FEMENINO"
#
# TIPO_DOCUMENTO=(
#     (CEDULA_CIUDADANIA,'Cedula ciudadania'),
#     (CEDULA_CIUDADANIA,'Cedula extranjeria'),
# )
#
# GENERO=(
#     (MASCULINO,'Masculino'),
#     (FEMENINO,'Femenino'),
# )

class USUARIO(User):
    TIPODOCUMENTO =((1,"cedula ciudadania"),(2, "cedula extranjera"))
    GENERO =((1, "masculino"),(2,  "femenino"))
   # TIPOUSUARIO =((1,"Dueno"),(2, "Jefe"), (3, "Trabajador"))
    genero =models.IntegerField(choices=GENERO, default=1)
    tipoDocumento = models.IntegerField(choices= TIPODOCUMENTO,default=1)
    numero_Documento = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    tipo_usuario = models.CharField(max_length=15)

    def __str__(self):
        return str(self.nombres)



class DUENO(models.Model):
    documento = models.OneToOneField(USUARIO,primary_key=True)




class JEFE(models.Model):
      dueno = models.ForeignKey(DUENO)
      documento = models.OneToOneField(USUARIO,primary_key=True)



class TRABAJADOR(models.Model):
      jefe =models.ForeignKey(JEFE)
      documento = models.OneToOneField(USUARIO,primary_key=True)

class Cultivo(models.Model):
    dueno = models.ForeignKey(DUENO, null=True)
    jefe = models.OneToOneField(JEFE,null=True)
    tamano = models.IntegerField()
    nombre = models.CharField(max_length=20,null=True)
    dimension = models.IntegerField()
    ubicacion = models.CharField(max_length=40)
    numero_lotes = models.IntegerField(null=True)


class Lote(models.Model):
      cultivo = models.ForeignKey(Cultivo,null=True)
      trabajador = models.ForeignKey(TRABAJADOR,null=True)
      nombre = models.CharField(max_length=20)


