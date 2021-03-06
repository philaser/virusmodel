""" virusmodel simulation v0.2
    Philemon Johnson
    !!! WORK IN PROGRESS. DO NOT DISTRIBUTE!!!
"""
import random
import uuid
from inspect import stack
import pandas as pd


class Node:

    def __init__(self):
        self.id = uuid.uuid4()
        self.links = []
        self.status = 'normal'
        self.days_infected = 0
        self.links.append(str(self.id))
        


    # def __str__(self):
    #     return 'ID: {}, STATUS: {}, DAYS INFECTED: {}'.format(self.id, self.status, self.days_infected)

    def traverse(self):
        node = random.choice(self.links)
        return str(self.id), node
        

    def updateDaysInfected(self):
        if self.status == 'infected':
            self.days_infected = self.days_infected + 1



class Graph:
    
    def __init__(self):
        self.nodes = {}
        self.num_normal_nodes = 0
        self.num_infected_nodes = 0
        self.num_dead_nodes = 0
        self.interventions = []
        self.data = pd.DataFrame(columns = ['Day', 'Normal', 'Infected', 'Dead'])


    def createLinks(self):
        for id, node in self.nodes.items():
            number_of_nodes = len(self.nodes) - 1
            number_of_links = random.randint(0, number_of_nodes)
            # this is not the desired effect. for simplicity, the edges are directed atm
            samples = random.sample(list(self.nodes), k = number_of_links)
            
            for sample in samples:
                node.links.append(sample)


    def createNodes(self, number_of_nodes):
        for i in range(number_of_nodes):
            node = Node()
            self.nodes.update({str(node.id) : node})


    def infect(self, traversal, rate):
        node_a_id, node_b_id = traversal
        node_a = self.nodes[node_a_id]
        node_b = self.nodes[node_b_id]
        rate = float(rate)
        distribution = [rate, 1 - rate]
        choice = random.choices(['infected', 'normal'], distribution)

        # print(node_a.status, node_b.status)
    
        if node_a.status == 'infected' and node_a.status != 'dead' or node_b.status == 'infected' and node_b.status != 'dead':

            if choice[0] == 'infected':
                node_a.status = choice[0]
                node_b.status = choice[0]


    def updateNodeCount(self):
        self.num_normal_nodes = 0
        self.num_infected_nodes = 0
        self.num_dead_nodes = 0

        for key, node in self.nodes.items():
            if node.status == 'normal':
                self.num_normal_nodes =  self.num_normal_nodes + 1
            elif node.status == 'infected':
                self.num_infected_nodes =  self.num_infected_nodes + 1
            elif node.status == 'dead':
                self.num_dead_nodes =  self.num_dead_nodes + 1
    

    def addIntervention(self, infection_rate, start_day, name, end_day = None):
        self.interventions.append([infection_rate, start_day, name, end_day])


    def simulate(self, initial_infections, infection_rate, number_of_days):
        infected_nodes = random.sample(list(self.nodes), k = initial_infections)
        original_rate = infection_rate
        data_list = []
        
        
        for node in infected_nodes:
            self.nodes[node].status = 'infected'


        for i in range(number_of_days):

            if self.interventions != []:
                for intervention in self.interventions:
                    if intervention[1] == i + 1:
                        infection_rate = intervention[0]
                        print('{} intervention introduced. Infection rate changed to {}'.format(intervention[2],infection_rate))
                    if intervention[3] == i+1:
                        infection_rate = original_rate
                        print('{} intervention ended. Infection rate changed to {}'.format(intervention[2],infection_rate))

            traversals = []
            print('Day {}'.format(i + 1))
            
            for key, node in self.nodes.items():
                traversals.append(node.traverse())
            
            for traversal in traversals:
                self.infect(traversal, infection_rate)

# this code may need to be refactored, i dont like the way it's mutating Node properties like that
            for node in self.nodes.values():
                node.updateDaysInfected()
                if node.days_infected >= 7:
                    node.status = 'dead'

            self.updateNodeCount()
            day_dict = {'Day' : i+1, 'Normal' : self.num_normal_nodes, 'Infected' : self.num_infected_nodes, 'Dead' : self.num_dead_nodes}
            data_list.append(day_dict)
            print('Number of normal cases: {}'.format(self.num_normal_nodes))
            print('Number of infected cases: {}'.format(self.num_infected_nodes))
            print('Number of deceased: {}'.format(self.num_dead_nodes))
            print("______________________________________\n")

        self.data = pd.DataFrame(data_list)
