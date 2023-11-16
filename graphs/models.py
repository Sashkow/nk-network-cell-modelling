from django.db import models
from django.contrib.auth.models import User


from cell_modelling import automata
from django.urls import reverse
import pickle


class Cell(models.Model):
    n = models.IntegerField()
    k = models.IntegerField()
    pickled_automata = models.TextField()


class LikeManager(models.Manager):
    class CellViewInfo(object):
        def __init__(self):
            self.graphs_list = []
            self.id = None
            self.n = None
            self.k = None
            self.like_count = None

    def get_most_liked_cells_info(self):
        from django.db import connection

        cursor = connection.cursor()
        cursor.execute(
            "SELECT graphs_like.cell_id, graphs_cell.n, graphs_cell.k, COUNT(graphs_like.id) AS like_count \
		 				FROM graphs_like \
		 				LEFT JOIN graphs_cell\
		 				ON graphs_like.cell_id=graphs_cell.id \
		 		 		GROUP BY cell_id \
		 				ORDER BY like_count DESC;"
        )
        rows = cursor.fetchall()
        info_list = []
        for row in rows:
            cell_view_info_object = LikeManager.CellViewInfo()
            graphs_list = []
            for graph_name in automata.NK_Automata.graph_names_list:
                graphs_list.append(
                    str(reverse("dynamic-image-by-cell-id", args=[row[0], graph_name]))
                )
            cell_view_info_object.graphs_list = graphs_list
            cell_view_info_object.id = row[0]
            cell_view_info_object.n = row[1]
            cell_view_info_object.k = row[2]
            cell_view_info_object.like_count = row[3]
            info_list.append(cell_view_info_object)
        return info_list


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    cell = models.ForeignKey(Cell, on_delete=models.PROTECT)
    objects = LikeManager()

    def __str__(self):
        return str(self.user) + " liked " + str(self.cell)
