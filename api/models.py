from django.db import models

class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Sector(models.Model):
    nombre = models.CharField(max_length=100)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    calle_principal = models.CharField(max_length=100)
    numero_casa = models.CharField(max_length=20)
    calle_transversal = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Dirección: {self.calle_principal}, {self.numero_casa}"

class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    pasaporte = models.CharField(max_length=20, unique=True, blank=True, null=True)
    parentesco_familiar = models.CharField(max_length=50)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    institucion_trabajo = models.CharField(max_length=100)
    direccion_laboral = models.OneToOneField(Direccion, on_delete=models.CASCADE, related_name='direccion_laboral', blank=True, null=True)
    telefono_laboral = models.CharField(max_length=20, blank=True, null=True)
    extension_laboral = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
