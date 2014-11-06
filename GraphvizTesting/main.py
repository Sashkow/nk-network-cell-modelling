import pygraphviz as p

def main():
	A=p.AGraph()
	A.add_edge(1,2)
	
	A.draw("1.svg",prog="dot")

if __name__ == '__main__':
	main()
