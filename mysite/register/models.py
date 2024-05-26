from django.db import models


class Administrador(models.Model):
    idadministrador = models.AutoField(db_column='idAdministrador', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    cpf = models.IntegerField(db_column='CPF')  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=16)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'


class Apartamento(models.Model):
    idapartamento = models.AutoField(db_column='idApartamento', primary_key=True)  # Field name made lowercase.
    bloco = models.IntegerField(db_column='Bloco')  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero')  # Field name made lowercase.
    condominio_idcondominio = models.ForeignKey('Condominio', models.DO_NOTHING, db_column='Condominio_idCondominio')

    class Meta:
        managed = False
        db_table = 'apartamento'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Condominio(models.Model):
    idcondominio = models.AutoField(db_column='idCondominio', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    cnpj = models.IntegerField(db_column='CNPJ')  # Field name made lowercase.
    rua = models.CharField(db_column='Rua', max_length=45)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero')  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=20)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=45)  # Field name made lowercase.
    cep = models.IntegerField(db_column='CEP')  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=45)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=20)  # Field name made lowercase.
    administrador_idadministrador = models.ForeignKey(Administrador, models.DO_NOTHING,
                                                      db_column='Administrador_idAdministrador')

    class Meta:
        managed = False
        db_table = 'condominio'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Morador(models.Model):
    idmorador = models.AutoField(db_column='idMorador', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    cpf = models.IntegerField(db_column='CPF')  # Field name made lowercase.
    telefone = models.IntegerField(db_column='Telefone')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    apartamento_idapartamento = models.ForeignKey(Apartamento, models.DO_NOTHING, db_column='Apartamento_idApartamento')

    class Meta:
        managed = False
        db_table = 'morador'


class Proprietario(models.Model):
    idproprietario = models.AutoField(db_column='idProprietario', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    cpf = models.IntegerField(db_column='CPF')  # Field name made lowercase.
    telefone = models.IntegerField(db_column='Telefone')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    rua = models.CharField(db_column='Rua', max_length=45)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero')  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=45)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=45)  # Field name made lowercase.
    cep = models.IntegerField(db_column='CEP')  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=45)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=20)  # Field name made lowercase.
    apartamento_idapartamento = models.ForeignKey(Apartamento, models.DO_NOTHING, db_column='Apartamento_idApartamento')

    class Meta:
        managed = False
        db_table = 'proprietario'