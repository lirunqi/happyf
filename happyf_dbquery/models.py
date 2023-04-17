from django.db import models


# Create your models here.
class BeforeMatch(models.Model):
    date_time = models.DateTimeField()
    matchid = models.CharField(max_length=200)
    series = models.CharField(max_length=200)
    compid = models.CharField(max_length=200)
    home_odd = models.CharField(max_length=200)
    guest_odd = models.CharField(max_length=200)
    odd_term = models.CharField(max_length=200)


class RealTimeMatch(models.Model):
    date_time = models.DateTimeField()
    matchid = models.CharField(max_length=200)
    compid = models.CharField(max_length=200)
    realtimeresult = models.CharField(max_length=200)
    home_odd = models.CharField(max_length=200)
    guest_odd = models.CharField(max_length=200)
    odd_term = models.CharField(max_length=200)


class MatchResult(models.Model):
    matchid = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    homeplayer = models.CharField(max_length=200)
    guestplayer = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    home_conner_reslut = models.CharField(max_length=200)
    home_attact = models.CharField(max_length=200)
    home_dgattact = models.CharField(max_length=200)
    guest_conner_reslut = models.CharField(max_length=200)
    guest_attact = models.CharField(max_length=200)
    guest_dgattact = models.CharField(max_length=200)


class Testft(models.Model):
    t = models.DateTimeField(blank=True,  primary_key=True)
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
        auto_created = False

class Testft(models.Model):
    t = models.DateTimeField(primary_key=True)
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