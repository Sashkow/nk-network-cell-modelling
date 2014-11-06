import pygraphviz as p

def main():
	A=p.AGraph()
	A.add_edge(1,2)
	A.layout(prog="dot")
	A.draw("1.dot")

if __name__ == '__main__':
	main()
