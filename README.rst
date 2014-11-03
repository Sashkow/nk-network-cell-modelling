KNOWLEDGE DOMAIN EXPLANATION

This software models life cell genetic regulation using Kauffman`s NK-automata. N stands for amount of genes a cell has. K represents amount of genes each gene behavior depends on. In this model gene is roughly a boolean variable which can be true or false (gene can be in to states: active or passive). States of all genes altogether at a particular discrete moment of time are a cell state. The model describes living cell regulatory mechanics i.e. how genes' interaction defines the sequence of cell states.

ExplanationPictures folder contains images that support the following text.

01. There are many organells in a living cell. But we are interested particualry in the nucleus (and partially with mitochondria)

.. image:: https://github.com/Sashkow/nk-network-cell-modelling/blob/master/ExplanationPictures/01.jpg
   :align: center
   :scale: 50 %
   
   

02. There are chromosomes floating in nucleus

03. A chromosome consists of genes. They regulate the cell.

04. But they are not isolated. They interact with each other on a massive scale.

05. Sometimes there are isolated subgroups of genes which interact only with genes from subgroup.

06. A gene is a functional unit of the genome. It can either do something and be activated (1) or do nothing and be deactivated (0). It can either dig or not dig, but not both. Lets call gene's "1" or "0" value - the state of the gene.

07. Let`s look at one of genes subgroup. They gather together and discuss their states which were taken on the previous meeting. (Yes, we assume that genes change their states synchroniously within descrete (certain) moments in time(steps)).

08. Having found out what the neighbours' states are genes take decision whether to change state or stay constant for this step. Their decisions are based on logical functions which take others' genes states as inputs and gives gene's new state as output. 

09. Genes evaluate their new state...

10. ...put them in line and pass foward...

11. Meanwhile other gene subgroups do the same...

12. and tell the outer cell what to do :) That long line of 1's and 0's from the previous picture is called cell`s state. It strictly defines the cell's behavior until the next step.

13. The cell changes it's state in time. But since there is finite amount of state and the state is strictly defined by previous state, guess what?

14. The behavior becomes cyclical!

This is first but not the only wonderful implication of the model. There are others: there are often more than one possible cycle for the cell. Furthermore, experiments suggest that amount of cell types in actual living organizm corelates with amount of cycles in a model!

This piece of software helps to explore dependence between genes' structure and the cell's behavior. E.g.how many cycles a cell can have, what makes them large or small... ect.

USAGE
The program takes two parameters: N and K.

On hitting submit button the program will draw a random cell
	- graph of links among Genes
	- graph of all cell states
	- graph of only those states which in cycle 
	
 
