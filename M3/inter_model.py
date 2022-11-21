import mesa
import numpy as np
import random
import math

class Sidewalk(mesa.Agent):
    """An agent that sims the sidewalk of the street"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Ambulance(mesa.Agent):
    """An ambulance agent"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 0

class DebugAgents(mesa.Agent):
    """A class for debugging spawning points"""
    def __init__(self, unique_id, status, model):
        super().__init__(unique_id, model)
        self.status = status

class Sensor(mesa.Agent):
    """An agent that actually senses a car and does stuff with it """
    def __init__(self, unique_id, direction, model):
        super().__init__(unique_id, model)
        self.status = 0
        self.direction = direction

    def step(self):
        pass
        # Check if there is traffic on each road
        #   If inside a certain range from the sensors there is already traffic, then given the cars number assign priority
        #       continue the algorithm
        #   Else
        #       Sensors will throw "infrared" to cars in their corresponding direction and find the car agents' velocity
        #           Get the average velocity for each street. Make priority queue given the average speed of cars

        # Wait some time (a.k.a) wait some arbitrary number of steps
        #   After time is over
        #       Check if there are still cars in the intersection
        #       Set all the traffic lights red
        #       Wait until intersection is freed
        #       Continue
        #   Go through the rest of the streets in the queu and assign the same time. Go to wait so time. Pop the current street in queue

        # Repeat

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
        self.velocity = 1 # it will travel only a meter at the time
        self.destination = []

        if self.status == 1:
            self.velocity = 2
        elif self.status == 2:
            self.velocity = 3

    def step(self):
        pass
        # Check for the sorrounding areas
        #   These are current agent status dependent:
        #   if found an ambulance then "go to the nearest wall" -> for this the car will have to check its sorroundings and find the nearest Sidewalk agent
        #       continue
        #   else check for traffic light ahead
        #       if traffic light is red then velocity will turn 0 and will not move
        #       if traffic light yellow reduce and in range of sensors (by 5) reduce speed by one
        #       if traffic light green continue

        #  If right at the insersection then turn to the proper destination. Will do this in several steps.

def get_distance(p, q):
    return math.sqrt((q[1] - p[1])**2 + (q[0] - p[0])**2)

class IntersectionModel(mesa.Model):
    """A model that creates the space and spawns the required agents"""

    def __init__(self, max_cars_num, debug=False):
        self.max_cars = max_cars_num
        self.debug = debug
        self.curr_cars = 0

        self.kill_agents = [] # agents to kill after each step
        self.grid = mesa.space.MultiGrid(50, 50, False) # create the space of a width and height room_width, room_height and no torodoidal
        self.schedule = mesa.time.RandomActivation(self) # scheduler for steps
        self.running = True # running while this is true

        self.s_one = []
        self.s_two = []
        self.s_three = []
        self.s_four = []

        self.spawn = [
                    [22,49], # up
                    [20, 0], # down
                    [0, 26], # left
                    [49, 24] # right
                ]

        self.dispawn = [
                    [20,49], # up
                    [22, 0], # down
                    [0,24], # left
                    [49, 26] # right
                ]

        self.intersection = [
                [19, 23], [19, 24],[19, 25], [19, 26], [19, 27], [20, 23], [20, 24], [20, 25], [20, 26], [20, 27],
                [21, 23], [21, 24], [21, 25], [21, 26], [21, 27], [22, 23], [22, 24], [22, 25], [22, 26], [22, 27],
                [23, 23], [23, 24], [23, 25], [23, 26], [23, 27]]

        print(self.intersection)

        # Sidewalks:
        x_val = np.union1d(np.array([i for i in range(19)]), np.array([i for i in range(24, 50)]))
        y_val = np.union1d(np.array([i for i in range(23)]), np.array([i for i in range(28, 50)]))

        self.unique_ids = 0

        for x in x_val:
            for y in y_val:
                agent = Sidewalk(self.unique_ids, self) # constructor for Sidewalk
                #self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        # Paint the traffic lights
        tl_one_x = [18]
        tl_one_y = [23,24,25]

        for x in tl_one_x:
            for y in tl_one_y:
                agent = TrafficLight(self.unique_ids, self) # constructor for Sidewalk
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        sensor_one_x = [18]
        sensor_one_y = [i for i in range(23,28) ]

        for x in sensor_one_x:
            for y in sensor_one_y:
                agent = Sensor(self.unique_ids, "left", self)
                self.s_one.append(agent)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        tl_two_x = [24]
        tl_two_y = [26,27,28]

        for x in tl_two_x:
            for y in tl_two_y:
                agent = TrafficLight(self.unique_ids, self) # constructor for Sidewalk
                # self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        sensor_two_x = [24]
        sensor_two_y = [i for i in range(23,28) ]

        for x in sensor_two_x:
            for y in sensor_two_y:
                agent = Sensor(self.unique_ids, "right", self) # constructor for sensor
                self.s_two.append(agent)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        tl_three_x = [21, 22, 23]
        tl_three_y = [22]

        for x in tl_three_x:
            for y in tl_three_y:
                agent = TrafficLight(self.unique_ids, self) # constructor for Sidewalk
                # self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        sensor_three_x = [i for i in range(19, 24)]
        sensor_three_y = [22]

        for x in sensor_three_x:
            for y in sensor_three_y:
                agent = Sensor(self.unique_ids, "down", self) # constructor for sensor
                self.s_three.append(agent)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        tl_four_x = [19, 20, 21]
        tl_four_y = [28]

        for x in tl_four_x:
            for y in tl_four_y:
                agent = TrafficLight(self.unique_ids, self) # constructor for Sidewalk
                # self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        sensor_four_x = [i for i in range(19, 24)]
        sensor_four_y = [28]

        for x in sensor_four_x:
            for y in sensor_four_y:
                agent = Sensor(self.unique_ids, "up", self) # constructor for Sidewalk
                self.s_four.append(agent)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        # Create a spawn agent in each spawning area
        for location in self.spawn:
            x, y = location
            agent = DebugAgents(self.unique_ids, "spawn", self)
            self.grid.place_agent(agent, (x, y))
            self.unique_ids += 1

        for location in self.dispawn:
            x, y = location
            agent = DebugAgents(self.unique_ids, "dispawn", self)
            self.grid.place_agent(agent, (x, y))
            self.unique_ids += 1

        for location in self.intersection:
            x, y = location
            agent = DebugAgents(self.unique_ids, "intersection", self)
            self.grid.place_agent(agent, (x, y))
            self.unique_ids += 1

        # self.datacollector = mesa.DataCollector(
        #         model_reporters={"Current_steps": get_current_model_steps},
        #         agent_reporters={}
        # )


    def spawnVehicles(self):
        for location in self.spawn:
            spawn_prob = round(random.uniform(0, 1), 2)

            if spawn_prob > .30:
                x, y = location # extract the location
                agent = Car(self.unique_ids, self)
                self.schedule.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                status_prob = round(random.uniform(0, 1), 2)
                status_debug = ""

                if .80 < status_prob <= .98:
                    if self.debug is True:
                        status_debug = "[ pressured ]"
                    agent.status = 1
                elif status_prob > .98:
                    if self.debug is True:
                        status_debug = "[ desesperated ]"
                    agent.status = 2
                else:
                    if self.debug is True:
                        status_debug = "[ normal ]"

                # Set cars' destination
                print("This is dispawn:", self.dispawn)
                copy_of_dispawn = self.dispawn
                print("This is a copy of dispanw:", copy_of_dispawn)

                print("This is a copy of dispanw after shuffle:", copy_of_dispawn)
                random.shuffle(copy_of_dispawn)
                print("This is dispanw after shuffle:", copy_of_dispawn)

                go_to = round(random.uniform(0, 1), 2)

                if (go_to < .25):
                    agent.destination = self.dispawn[1]
                elif (go_to < .50):
                    agent.destination = self.dispawn[1]
                elif (go_to < .75):
                    agent.destination = self.dispawn[2]
                else:
                    agent.destination = self.dispawn[3]
                    break

                if self.debug is True:
                    print(f"Car spawned at ({x}. {y}) with status of {status_debug}")
                    print(f"Car will go to {agent.destination}")

                self.unique_ids += 1
            else:
                continue

    def step(self):
        # self.datacollector.collect(self)
        if self.curr_cars == self.max_cars:
            #print("Do not spawn more cars and just step")
            self.schedule.step() # continue the simulation
        else:
            # Spawn cars if cars can be spawned
            # Check spawning positions in grid if empty
            #print("First will try to spawn stufF")
            self.spawnVehicles()
            self.schedule.step()

            while self.kill_agents != []:
                for agent in self.kill_agents:
                    self.grid.remove_agent(agent)
                    self.schedule.remove(agent)
                    self.kill_agents.remove(agent)
