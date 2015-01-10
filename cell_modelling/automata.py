import generate_automata
import boolfunction
import state

import sys
import drawgraph


from debug import log
from state import State

#automata_structure
#automata_states
#automata_analysis

class NK_Automata(object):
    #static
    graph_names_list = ['gene_links_graph','cell_states_graph','simplified_cell_states_graph']
    
    def __init__(self,p__n=None,p__k=None,p_functions_list=None,p_links_list=None,p_view_states_as_binary=False):
        if p__n==None or p__k==None:
            self.N=5
            self.K=5
        else:
            self.N=p__n
            self.K=p__k

        if p_functions_list==None:
            p_functions_list=[]
        else:
            self.functions_list= p_functions_list

        if p_links_list==None:
            self.links_list=[]
        else:
            self.links_list=p_links_list

        self.ordinal_number=-1

        
        self.state_span={}              #state_span: {current_state_number: next_state_number,...}
        self.state_list=[]           
        self.attractor_dict={}          #attractor_dict {attractor_number:[size,basin_size],...}
        self.attractor_states_dict ={}   #attractor_states_dict: {attractor_state_number:[next_attractor_state_number,attractor_state_weight],...} 

        self.basin_amount=0
        self.stability=0

        self.expected_return_time=100500

        self.view_states_as_binary=p_view_states_as_binary

        

    def __sizeof__(self):
        return sys.getsizeof(self.N) + sys.getsizeof(self.K) + sys.getsizeof(self.functions_list) + sys.getsizeof(self.links_list)+ sys.getsizeof(self.state_span)+ sys.getsizeof(self.basin_amount) + sys.getsizeof(self.stability)+ sys.getsizeof(self.attractor_dict)

    def __str__(self):
        #return "N = " + str(self.N)+ " K = " + str(self.K) +"\n"+"functions_list: "+str(self.functions_list)+"\n"+"links_list: " + str(self.links_list)
        return "N = " + str(self.N)+ " K = " + str(self.K) +"functions_list: "+str(self.functions_list)+"links_list: " + str(self.links_list)

    def __repr__(self):
        return self.__str__()

    def generate_random_automata(self):
        self.functions_list=[]
        self.links_list=[]
        generate_automata.generate_n_k_automata(self.N,self.K,self.functions_list,self.links_list)

    def step_automata(self,state):

        new_state_string=""
        for bool_fun_number in range(self.N):

            bool_fun_inputs=""
            for state_element_number in range(self.K):
                bool_fun_inputs+=state.as_string()[self.links_list[bool_fun_number][state_element_number]]


            new_state_string+=self.functions_list[bool_fun_number].evaluate(bool_fun_inputs)

        return State(new_state_string)


    def span_automata(self):
        if self.state_span:
            self.state_span={}

        #print "Iterating automata states:"
        current_state=State(0,self.N)
        next_state=State(0,self.N)
        for state_number in range(2**self.N):


            #print "Current state:", state_number
            current_state.set_state(state_number)

            next_state=self.step_automata(current_state)

            if self.view_states_as_binary:
                self.state_span[current_state.as_string()[::]]=next_state.as_string()[::]
            else:
                self.state_span[current_state.as_int()]=next_state.as_int()
            

    def create_state_list(self):
        for state_number in range(2**self.N):
            self.state_list.append(State(state_number,self.N))
#
    def process_sample(self,seed):
        current_state_number=seed
        sample_list=[]
        while not (current_state_number in sample_list):

            if self.state_list[current_state_number].in_attractor:

                for sample_state_number in sample_list:
                    self.state_list[sample_state_number].in_basin=True
                    self.state_list[sample_state_number].basin_number=self.state_list[current_state_number].basin_number
                    self.state_list[sample_state_number].first_attractor_state_number=current_state_number
                self.state_list[current_state_number].weight+=len(sample_list)
                return

            if self.state_list[current_state_number].in_basin:
                first_attractor_state_number = self.state_list[current_state_number].first_attractor_state_number
                for sample_state_number in sample_list:
                    self.state_list[sample_state_number].in_basin=True
                    self.state_list[sample_state_number].basin_number=self.state_list[current_state_number].basin_number
                    self.state_list[sample_state_number].first_attractor_state_number=first_attractor_state_number
                self.state_list[first_attractor_state_number].weight+=len(sample_list)
                return

            sample_list.append(current_state_number)
            current_state_number=(self.step_automata(State(current_state_number,self.N))).as_int()


        attractor_start_state_number=current_state_number

        attractor_start_index=sample_list.index(attractor_start_state_number)
        basin_list=sample_list[:attractor_start_index]
        attractor_list=sample_list[attractor_start_index:]

        for state_number in basin_list:
            self.state_list[state_number].in_basin=True
            self.state_list[state_number].basin_number=self.basin_amount+1
            self.state_list[state_number].first_attractor_state_number=attractor_start_state_number

        for state_number in attractor_list:
            self.state_list[state_number].in_attractor=True
            self.state_list[state_number].basin_number=self.basin_amount+1

        self.state_list[attractor_start_state_number].weight=len(basin_list)

        self.basin_amount+=1
    ###

    #next state object

    def next_state(self,state):
        next_state_string=self.state_span[state.as_string()]
        next_state_number=State(next_state_string).state_number
        next_state_object=self.state_list[next_state_number]
        return next_state_object
    ###

    def analyse_automata(self):
        #print "starting analysis:"
        self.create_state_list()
        sample_number=0
        for state_number in range(2**self.N):
            if self.state_list[state_number].in_basin==False and self.state_list[state_number].in_attractor==False:
                #print "  taking_sample:", sample_number
                self.process_sample(state_number)
            sample_number+=1

    def initialize_attractor_dict(self):
        for attractor_number in range(1,self.basin_amount+1):
            self.attractor_dict[attractor_number]=[0,0] # {attractor_number:[size,basin_size],...}

    def make_attractor_stat_dictionary(self):
        
        self.initialize_attractor_dict()
        for state in self.state_list:
            if state.in_attractor==True:
                self.attractor_dict[state.basin_number][0]+=1
            if state.in_basin==True:
                self.attractor_dict[state.basin_number][1]+=1

    def count_stability(self):
        basin_size_square_sum=0
        for attractor_number in self.attractor_dict:
            basin_size_square_sum+=(self.attractor_dict[attractor_number][0]+self.attractor_dict[attractor_number][1])**2
        self.stability=float(basin_size_square_sum)/(2**(self.N))**2

    def distance_between_states(self,from_state,to_state):

        current_state=from_state
        distance = 0
        while current_state!=to_state:
            distance+=1
            current_state=self.next_state(current_state)

           # print "      CurrentState:", current_state
            if distance>100500:
                print "err"
                return -1
        #print "FromState:", from_state, "ToState:", to_state, "distance:", distance

        return distance


    def count_expected_return_time(self):
        # average timesteps needed to reach some cycle in case of random state change i.e. average distance to the nearest cycle
        average_return_time = 0
        basin_states_amount = 0
        for current_state in self.state_list:

            if current_state.in_basin==True:
                basin_states_amount+=1
                first_attractor_state=self.state_list[current_state.first_attractor_state_number]

                average_return_time+=self.distance_between_states(current_state,first_attractor_state)
        if basin_states_amount==0:
            self.expected_return_time=0
            return 0
        average_return_time=float(average_return_time)/basin_states_amount
        self.expected_return_time=average_return_time
        return average_return_time


    #outdated method. Never used

    def make_attractor_states_dictionary(self):
        self.attractor_states_dict={}
        for state in self.state_list:
            if state.in_attractor==True:
                if self.view_states_as_binary:
                    self.attractor_states_dict[state.as_string()]=[(self.step_automata(state)).as_string(),state.weight]
                else:
                    self.attractor_states_dict[state.as_int()]=[(self.step_automata(state)).as_int(),state.weight]
        
    def fill_automata(self):

        self.generate_random_automata()
        # print "automata", self

        self.span_automata()
        # print "satespan",self.state_span

        self.analyse_automata()
        # print self.state_list

        self.make_attractor_states_dictionary()
        # print "attractor states:", self.attractor_states_dict