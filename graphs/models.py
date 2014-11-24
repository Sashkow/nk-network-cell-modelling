from django.db import models

class Cell(models.Model):
	n = models.IntegerField()
	k = models.IntegerField()
	serialized_object = models.TextField()

	def __str__(self):	
		return "ID_"+str(self.id)+"_N_"+str(self.n)+"_K_"+str(self.k)
	# 	return "N = "+str(n)+", K = "+str(k)
# Create your models here.
