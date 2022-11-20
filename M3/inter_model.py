import mesa
import numpy as np
from itertools import product
import random

class Sidewalk(mesa.Agent):
    """An agent that sims the sidewalk of the street"""

    def __init__(self, model):
        super().__init__(model)


class Sidewalk(mesa.Agent):
    """An agent that sims the sidewalk of the street"""

    def __init__(self, unique_id, model):
        super().__init__(model)

class Car(mesa.Agent):
    """An agent that sims a roomba"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 0 # 0 is normal, 1 is pressured, 2 is desesperated

    # def move(self):
    #     check_curr_pos = self.model.grid.get_cell_list_contents([self.pos])

    #     for agent in check_curr_pos:
    #         if isinstance(agent, DirtAgent):
    #             return True

    #     possible_steps = self.model.grid.get_neighborhood(
    #         self.pos, moore=True, include_center=False
    #     )

    #     result = random.sample(possible_steps, k=len(possible_steps)) # shuffle the list
    #     move_to = self.pos

    #     for steps in result:
    #         dirt_found = False
    #         searching = self.model.grid.get_cell_list_contents([steps])

    #         if len(searching) > 0:
    #             for agent in searching:
    #                 if isinstance(agent, RoombaAgent): # if is instance of roomba
    #                     dirt_found = False
    #                     break
    #                 elif isinstance(agent, DirtAgent):
    #                     dirt_found = True
    #         else:
    #             move_to = steps
    #             continue

    #         if dirt_found is True:
    #             move_to = steps
    #             self.model.grid.move_agent(self, move_to)
    #             self.num_mov += 1
    #             return True # did move
    #         else:
    #             continue # if normal found or roomba found continue

    #     self.model.grid.move_agent(self, move_to)
    #     self.num_mov += 1
    #     return False # random movement

    def step(self):
        if isinstance(self, RoombaAgent):
            moving = self.move() # check if agent can move
            if moving is True:
                self.clean() # clean the dirty cell

class IntersectionModel(mesa.Model):
    """A model that creates the space and spawns the required agents"""

    def __init__(self, max_cars_num):
        self.max_cars = max_cars_num
        self.curr_cars = 0

        # Paint the grid

        # self.datacollector = mesa.DataCollector(
        #         model_reporters={"Current_steps": get_current_model_steps},
        #         agent_reporters={}
        # )


    def step(self):
        # self.datacollector.collect(self)
        if self.curr_cars == self.max_cars:
            print("Do not spawn more cars and step")
            self.schedule.step() # continue the simulation
        else:
            # Spawn cars if cars can be spawned
            self.schedule.step()

            while self.kill_agents != []:
                for agent in self.kill_agents:
                    self.grid.remove_agent(agent)
                    self.schedule.remove(agent)
                    self.kill_agents.remove(agent)
