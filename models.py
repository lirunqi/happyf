# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class HappyfDbqueryBeforematch(models.Model):
    id = models.BigAutoField(primary_key=True)
    matchid = models.CharField(max_length=200)
    series = models.CharField(max_length=200)
    compid = models.CharField(max_length=200)
    home_odd = models.CharField(max_length=200)
    guest_odd = models.CharField(max_length=200)
    odd_term = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'happyf_dbquery_beforematch'


class HappyfDbqueryMatchresult(models.Model):
    id = models.BigAutoField(primary_key=True)
    matchid = models.CharField(max_length=200)
    homeplayer = models.CharField(max_length=200)
    guestplayer = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    home_conner_reslut = models.CharField(max_length=200)
    home_attact = models.CharField(max_length=200)
    home_dgattact = models.CharField(max_length=200)
    guest_conner_reslut = models.CharField(max_length=200)
    guest_attact = models.CharField(max_length=200)
    guest_dgattact = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'happyf_dbquery_matchresult'


class HappyfDbqueryRealtimematch(models.Model):
    id = models.BigAutoField(primary_key=True)
    matchid = models.CharField(max_length=200)
    compid = models.CharField(max_length=200)
    realtimeresult = models.CharField(max_length=200)
    home_odd = models.CharField(max_length=200)
    guest_odd = models.CharField(max_length=200)
    odd_term = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'happyf_dbquery_realtimematch'


class TestData(models.Model):
    matchid = models.IntegerField(blank=True, null=True)
    date_time = models.DateField(blank=True, null=True)
    homeplayer = models.CharField(max_length=50, blank=True, null=True)
    guestplayer = models.CharField(max_length=50, blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)
    home_shoot = models.IntegerField(blank=True, null=True)
    home_onshoot = models.IntegerField(blank=True, null=True)
    home_outshoot = models.IntegerField(blank=True, null=True)
    home_downshoot = models.IntegerField(blank=True, null=True)
    home_nearshoot = models.IntegerField(blank=True, null=True)
    home_corner = models.IntegerField(blank=True, null=True)
    home_ever = models.IntegerField(blank=True, null=True)
    home_board = models.IntegerField(blank=True, null=True)
    home_rob = models.IntegerField(blank=True, null=True)
    home_band = models.IntegerField(blank=True, null=True)
    home_foul = models.IntegerField(blank=True, null=True)
    home_yello_c = models.IntegerField(blank=True, null=True)
    home_red_c = models.IntegerField(blank=True, null=True)
    home_control = models.IntegerField(blank=True, null=True)
    home_pass = models.IntegerField(blank=True, null=True)
    home_pass_r = models.IntegerField(blank=True, null=True)
    home_att = models.IntegerField(blank=True, null=True)
    home_dan_att = models.IntegerField(blank=True, null=True)
    guest_shoot = models.IntegerField(blank=True, null=True)
    guest_onshoot = models.IntegerField(blank=True, null=True)
    guest_outshoot = models.IntegerField(blank=True, null=True)
    guest_downshoot = models.IntegerField(blank=True, null=True)
    guest_nearshoot = models.IntegerField(blank=True, null=True)
    guest_corner = models.IntegerField(blank=True, null=True)
    guest_ever = models.IntegerField(blank=True, null=True)
    guest_board = models.IntegerField(blank=True, null=True)
    guest_rob = models.IntegerField(blank=True, null=True)
    guest_band = models.IntegerField(blank=True, null=True)
    guest_foul = models.IntegerField(blank=True, null=True)
    guest_yello_c = models.IntegerField(blank=True, null=True)
    guest_red_c = models.IntegerField(blank=True, null=True)
    guest_control = models.IntegerField(blank=True, null=True)
    guest_pass = models.IntegerField(blank=True, null=True)
    guest_pass_r = models.IntegerField(blank=True, null=True)
    guest_att = models.IntegerField(blank=True, null=True)
    guest_dan_att = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_data'


class Testft(models.Model):
    t = models.DateTimeField(blank=True, null=True)
    p = models.BigIntegerField(blank=True, null=True)
    h = models.FloatField(blank=True, null=True)
    a = models.FloatField(blank=True, null=True)
    rt = models.TextField(blank=True, null=True)
    hg = models.BigIntegerField(blank=True, null=True)
    ag = models.BigIntegerField(blank=True, null=True)
    st = models.BigIntegerField(blank=True, null=True)
    matchid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testft'
