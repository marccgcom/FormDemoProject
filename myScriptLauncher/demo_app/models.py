from django.db import models

class Lectura(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=255)
    maquinaria = models.CharField(max_length=255)
    fecha_lectura = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lecturas"
        verbose_name = "Lectura"
        verbose_name_plural = "Lecturas"

    def __str__(self):
        return f"{self.maquinaria} - {self.ubicacion} ({self.fecha_lectura})"
