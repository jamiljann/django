from django.db import models
from django.shortcuts import reverse

class interface(models.Model):
  int_types = (
    ('ISIS', 'UpLink'), ('IPOSS', 'Uplink'), ('Shut', 'ShutDown'),
    ('loopBack','LoopBack'), ('vlan','Vlan'), ('null','NULL'), 
    ('vty','vty'), ('vlanIF','VlanIF')
  )
  #Date = models.DateField()
  Router_Name = models.CharField(blank=True, max_length=50)
  int_Name =    models.CharField(blank=True, max_length=50)
  Description = models.CharField(blank=True, max_length=155)
  int_ID =      models.CharField(blank=True, max_length=15)
  IP =          models.CharField(blank=True, max_length=35)
  Profile =     models.CharField(blank=True, max_length=25)
  Int_type =    models.CharField(blank=True, choices= int_types, max_length=12)

  def get_absolute_url(self):
      return reverse("add", kwargs={"pk": self.pk})
  
 
