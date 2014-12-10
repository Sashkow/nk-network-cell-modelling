from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD

=======
from cell_modelling import automata	
from django.core.urlresolvers import reverse
import pickle



class Cell(models.Model):
	n = models.IntegerField()
	k = models.IntegerField()
	pickled_automata = models.TextField()
>>>>>>> second_strange_branch

# class Cell(models.Model):
# 	n = models.IntegerField()
# 	k = models.IntegerField()
# 	serialized_object = models.TextField()

# 	def __str__(self):	
# 		return "ID_"+str(self.id)+"_N_"+str(self.n)+"_K_"+str(self.k)
	# 	return "N = "+str(n)+", K = "+str(k)

<<<<<<< HEAD
# class Like(models.Model):
# 	user = models.ForeignKey(User)
# 	# cell = models.ForeignKey(Cell)
=======
class LikeManager(models.Manager):
	class CellViewInfo(object):
		def __init__(self):
			self.graphs_list=[]
			self.id=None
			self.n=None
			self.k=None
			self.like_count=None

	def getMostLikedCellsInfo(self):
		from django.db import connection
		cursor = connection.cursor()
		cursor.execute("SELECT graphs_like.cell_id, graphs_cell.n, graphs_cell.k, COUNT(graphs_like.id) AS like_count \
		 				FROM graphs_like \
		 				LEFT JOIN graphs_cell\
		 				ON graphs_like.cell_id=graphs_cell.id \
		 		 		GROUP BY cell_id \
		 				ORDER BY like_count DESC;")
		rows = cursor.fetchall()
		infoList=[]
		for row in rows:
			cellViewInfoObject=LikeManager.CellViewInfo()
			graphs_list=[]
			for graph_name in automata.NK_Automata.graphNamesList:
				graphs_list.append(str(reverse('dynamic-image-by-cell-id', args=[row[0],graph_name])))
			cellViewInfoObject.graphs_list=graphs_list
			cellViewInfoObject.id=row[0]
			cellViewInfoObject.n=row[1]
			cellViewInfoObject.k=row[2]
			cellViewInfoObject.like_count=row[3]
			infoList.append(cellViewInfoObject)
		return infoList

class Like(models.Model):
	user=models.ForeignKey(User)
	cell=models.ForeignKey(Cell)
	objects = LikeManager()

	def __str__(self):
		return str(self.user)+" liked "+str(self.cell)

>>>>>>> second_strange_branch
