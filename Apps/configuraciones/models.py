from django.db import models

# Create your models here.

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=False,null=False,max_length=50)
    apellido = models.CharField(blank=False,null=False,max_length=50)
    cedula = models.CharField(blank=False,null=False,max_length=50)

    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name = 'Persona',
        verbose_name_plural = 'Personas',
        db_table = 'mant_persona'

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=False,null=False,max_length=50)

    def __unicode__(self):
        return self.id_rol

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Rol',
        verbose_name_plural = 'Roles',
        db_table = 'conf_rol'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona,on_delete=models.CASCADE, related_name='fk_persona')
    usuario = models.CharField(blank=False,null=False,max_length=50)
    clave = models.CharField(blank=False,null=False,max_length=50)


    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name = 'Usuario',
        verbose_name_plural = 'Usuarios',
        db_table = 'conf_usuario'

class ConfUsuario_rol(models.Model):
    id_usuario_rol = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="fkusuario_rol", db_column='id_usuario')
    id_rol =models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="fkrol_usuario", db_column='id_rol')

    class Meta:
        verbose_name = 'Rol de usuario',
        verbose_name_plural = 'Roles de usuarios',
        db_table = 'usuario_rol'

    def __int__(self):
        return self.id_usuario_rol

class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre = models.CharField(null=False,blank=False,max_length=50)
    url = models.CharField(null=False,blank=False,max_length=50)
    estado = models.BooleanField(null=False)

    class Meta:
        verbose_name = 'Menu',
        verbose_name_plural = 'Menus',
        db_table = 'conf_menu'

    def __int__(self):
        return self.id_padre

    def __str__(self):
        return self.nombre



class Permisos(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=False,related_name="fk_mod_menu", db_column='id_menu')
    usuario_rol = models.ForeignKey(ConfUsuario_rol,on_delete=models.CASCADE,null=False,related_name="fk_usurol", db_column='id_usuario_rol')


    class Meta:
        verbose_name = 'Permiso',
        verbose_name_plural = 'Permisos',
        db_table = 'permisos'

    def __unicode__(self):
        return self.usuario_rol,self.menu


