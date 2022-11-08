import mesa
import numpy as np
from itertools import product
from numpy.random import default_rng
import random

class DirtAgent(mesa.Agent):
    """An agent that sims dirt"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class RoombaAgent(mesa.Agent):
    """An agent that sims a roomba"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.num_mov = 0

    def move(self):
        check_curr_pos = self.model.grid.get_cell_list_contents([self.pos])

        for agent in check_curr_pos:
            if isinstance(agent, DirtAgent):
                return True

        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )

        result = random.sample(possible_steps, k=len(possible_steps)) # shuffle the list
        move_to = self.pos

        for steps in result:
            dirt_found = False
            searching = self.model.grid.get_cell_list_contents([steps])

            if len(searching) > 0:
                for agent in searching:
                    if isinstance(agent, RoombaAgent): # if is instance of roomba
                        dirt_found = False
                        break
                    elif isinstance(agent, DirtAgent):
                        dirt_found = True
            else:
                move_to = steps
                continue

            if dirt_found is True:
                move_to = steps
                self.model.grid.move_agent(self, move_to)
                self.num_mov += 1
                return True # did move
            else:
                continue # if normal found or roomba found continue

        self.model.grid.move_agent(self, move_to)
        self.num_mov += 1
        return False # random movement

    def clean(self):
        agents = self.model.grid.get_cell_list_contents([self.pos])

        for agent in agents:
            if isinstance(agent, DirtAgent):
                self.model.kill_agents.append(agent)

    def step(self):
        if isinstance(self, RoombaAgent):
            moving = self.move() # check if agent can move
            if moving is True:
                self.clean() # clean the dirty cell

class CleaningModel(mesa.Model):
    """A model that creates the space and spawns the required agents"""

    def __init__(self, num_of_roombas, dirt_percentage, room_width, room_height, max_num_steps):

        # Before doing anything check data type of dirt_percentage
        if isinstance(dirt_percentage, int) is False:
            print("Error: invalid value of percentage")
            exit(1)

        print("START OF THE PROGRAM")

        # Declare initial data of the model
        self.roombas = num_of_roombas
        self.dirt = dirt_percentage
        self.total_dirts = 0
        self.curr_steps = 0
        self.ids = 0
        self.max_steps = max_num_steps
        self.kill_agents = [] # agents to kill after each step
        self.grid = mesa.space.MultiGrid(room_width, room_height, False) # create the space of a width and height room_width, room_height and no torodoidal
        self.schedule = mesa.time.RandomActivation(self) # scheduler for steps
        self.running = True # running while this is true

        # Populate the grid with dirt agents
        total_cells = room_width * room_height
        # print(f"Total number of cells are {total_cells}")
        i_val = round(total_cells * (self.dirt / 100))
        self.total_dirts = i_val
        # print(f"Dirt percentage is {self.dirt}")
        # print(f"Number of cells to dirt will actually be {i_val}")

        w_list = [i for i in range(self.grid.width)]
        h_list = [i for i in range(self.grid.height)]

        com_list = list(product(w_list, h_list))
        result = random.sample(com_list, k=i_val)


        for i in range(i_val):
            x, y = result[i]
            agent = DirtAgent(i, self) # constructor DirtAgent(id)
            self.schedule.add(agent) # adds agent to scheduler

            # Add the agent to a random grid cell
            self.grid.place_agent(agent, (x, y))
            self.ids += 1 # update the self.ids adding one

        # print(f"A number of {self.ids} dirt agents have been added")
        # print(f"A number of {i_val} been added")

        roomba_list = [i for i in range(self.roombas)]

        roomba_list = list(product(h_list, w_list))
        result = random.sample(roomba_list, k=self.roombas)

        # Create all the roomba agents
        for i in range(self.roombas):
            x, y = result[i]

            agent = RoombaAgent(self.ids, self) # constructor RoombaAgent(id)
            self.schedule.add(agent) # adds agent to scheduler

            self.grid.place_agent(agent, (x, y))

            self.ids += 1

        # print(f"Roombas {self.roombas} agents have been added")
        # print(f"Total number of agents is {self.ids}")

        # self.datacollector = mesa.DataCollector(
        #     model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        # )

    def step(self):
        #self.datacollector.collect(self)

        if self.curr_steps == self.max_steps:
            print("Warning: maximum number of steps reached!!!")
            self.running = False
        elif self.total_dirts == 0:
            print("No more to clean")
            self.running = False
        else:
            self.schedule.step()
            self.curr_steps += 1

            while self.kill_agents != []:
                for dirt_agent in self.kill_agents:
                    self.grid.remove_agent(dirt_agent)
                    self.schedule.remove(dirt_agent)
                    self.kill_agents.remove(dirt_agent)
                    self.total_dirts -= 1
