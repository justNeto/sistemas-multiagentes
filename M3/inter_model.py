import mesa
import numpy as np
from itertools import product
import random

class Sidewalk(mesa.Agent):
    """An agent that sims the sidewalk of the street"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Ambulance(mesa.Agent):
    """An ambulance agent"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 0

class Sensor(mesa.Agent):
    """An agent that actually senses a car and does stuff with it """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 0

class TrafficLight(mesa.Agent):
    """An agent that sims the light colors but is only for painting of the street"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 0

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

        self.kill_agents = [] # agents to kill after each step
        self.grid = mesa.space.MultiGrid(50, 50, False) # create the space of a width and height room_width, room_height and no torodoidal
        self.schedule = mesa.time.RandomActivation(self) # scheduler for steps
        self.running = True # running while this is true

        self.s_one = []
        self.s_two = []
        self.s_three = []
        self.s_four = []

        # Intersection via y:
        x_val = np.union1d(np.array([i for i in range(19)]), np.array([i for i in range(24, 50)]))
        y_val = np.union1d(np.array([i for i in range(22)]), np.array([i for i in range(29, 50)]))

        i = 0
        for x in x_val:
            for y in y_val:
                #print(f"x: {x} ; y = {y}")
                print(f"Unique sidewalk id: {i}")
                agent = Sidewalk(i, self) # constructor for Sidewalk
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        # Paint the traffic light
        tl_one_x = [18]
        tl_one_y = [22,23,24]

        for x in tl_one_x:
            for y in tl_one_y:
                print(f"Unique traffic id: {i}")
                agent = TrafficLight(i, self) # constructor for Sidewalk
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        sensor_one_x = [18]
        sensor_one_y = [i for i in range(22,29) ]

        for x in sensor_one_x:
            for y in sensor_one_y:
                print(f"Unique sensor id: {i}")
                agent = Sensor(i, self) # constructor for Sidewalk
                self.s_one.append(agent)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        tl_two_x = [24]
        tl_two_y = [26,27,28]

        for x in tl_two_x:
            for y in tl_two_y:
                print(f"Unique traffic id: {i}")
                agent = TrafficLight(i, self) # constructor for Sidewalk
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        sensor_two_x = [24]
        sensor_two_y = [i for i in range(22,29) ]

        for x in sensor_two_x:
            for y in sensor_two_y:
                print(f"Unique sensor id: {i}")
                agent = Sensor(i, self) # constructor for Sidewalk
                self.s_two.append(agent)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        tl_three_x = [21, 22, 23]
        tl_three_y = [21]

        for x in tl_three_x:
            for y in tl_three_y:
                print(f"Unique traffic id: {i}")
                agent = TrafficLight(i, self) # constructor for Sidewalk
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        sensor_three_x = [i for i in range(19, 24)]
        sensor_three_y = [21]

        for x in sensor_three_x:
            for y in sensor_three_y:
                print(f"Unique sensor id: {i}")
                agent = Sensor(i, self) # constructor for Sidewalk
                self.s_three.append(agent)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        tl_four_x = [19, 20, 21]
        tl_four_y = [29]

        for x in tl_four_x:
            for y in tl_four_y:
                print(f"Unique traffic id: {i}")
                agent = TrafficLight(i, self) # constructor for Sidewalk
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        sensor_four_x = [i for i in range(19, 24)]
        sensor_four_y = [29]

        for x in sensor_four_x:
            for y in sensor_four_y:
                print(f"Unique sensor id: {i}")
                agent = Sensor(i, self) # constructor for Sidewalk
                print(agent)
                print(agent.unique_id)
                self.s_four.append(agent)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                i += 1

        # Print all sensor arrays
        for val in self.s_one:
            print(val.unique_id)
        for val in self.s_two:
            print(val.unique_id)
        for val in self.s_three:
            print(val.unique_id)
        for val in self.s_four:
            print(val.unique_id)

        # Spawning areas

        # print("Spawn up")
        # agent = TrafficLight(i, self)
        # self.grid.place_agent(agent, (21,49))
        # i += 1

        # print("Spawn down")
        # agent = TrafficLight(i, self)
        # self.grid.place_agent(agent, (21,0))
        # i += 1

        # print("Spawn left down")
        # agent = TrafficLight(i, self)
        # self.grid.place_agent(agent, (0,24))
        # i += 1

        # print("Spawn left up")
        # agent = TrafficLight(i, self)
        # self.grid.place_agent(agent, (0,26))
        # i += 1

        # print("Spawn right down")
        # agent = TrafficLight(i, self)
        # self.grid.place_agent(agent, (49,24))
        # i += 1

        # print("Spawn right up")
        # agent = TrafficLight(i, self)
        # self.grid.place_agent(agent, (49,26))
        # i += 1

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
            # Check spawning positions in grid if empty
            # Spawn cars
            self.schedule.step()

            while self.kill_agents != []:
                for agent in self.kill_agents:
                    self.grid.remove_agent(agent)
                    self.schedule.remove(agent)
                    self.kill_agents.remove(agent)
