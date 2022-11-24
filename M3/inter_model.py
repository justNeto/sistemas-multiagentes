import mesa
import numpy as np
import random
import math


def move(agent, to_):
    # According to status will do some different things.
    print("Will move!")
    if agent.status == 0:

        # Possible gments for an agent
        possible_steps = agent.model.grid.get_neighborhood(
            agent.pos, moore=False, include_center=False
        )

        depurated_steps = []

        for steps in possible_steps:
            cannot_use_step = False
            searching = agent.model.grid.get_cell_list_contents([steps])

            if len(searching) > 0:
                for stuff in searching:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance) or isinstance(stuff, Sidewalk):
                        cannot_use_step = True
                        break
                    elif isinstance(stuff, TrafficLight):
                        if agent.inside_int == True:
                            break

                        if stuff.status == 1:
                            agent.velocity = 0
                            return
                        if stuff.status == 3:
                            agent.velocity = agent.status + 1
                        else:
                            cannot_use_step = False
                    else:
                        print("Checking some stuff!")
                        x_cur, y_cur = agent.pos
                        curr_loc = [x_cur, y_cur]

                        print(curr_loc)
                        print(agent.model.intersection)

                        for val in agent.model.intersection:
                            if val == curr_loc:
                                print("Inside intersection")
                                agent.inside_int = True
                                break

            if cannot_use_step:
                continue
            else:
                print(steps)
                depurated_steps.append(steps)

        if (len(depurated_steps) == 0):
            return

        min = 1000
        best = []
        for opts in depurated_steps:
            x, y = opts
            new_point = [x,y]
            aux = get_distance(new_point, to_)
            if (aux < min):
                best = new_point
                min = aux

        agent.model.grid.move_agent(agent, tuple(e for e in best))

    if agent.status == 1:

        for i in range(agent.status):
            possible_steps = agent.model.grid.get_neighborhood(
                agent.pos, moore=False, include_center=False
            )

            depurated_steps = []

            for steps in possible_steps:
                cannot_use_step = False
                searching = agent.model.grid.get_cell_list_contents([steps])

                if len(searching) > 0:
                    for stuff in searching:
                        if isinstance(stuff, Car) or isinstance(stuff, Ambulance) or isinstance(stuff, Sidewalk):
                            cannot_use_step = True
                            break
                        elif isinstance(stuff, TrafficLight):
                            if agent.inside_int == True:
                                break

                            if stuff.status == 1:
                                agent.velocity = 0
                                return
                            if stuff.status == 3:
                                agent.velocity = agent.status + 1
                            else:
                                cannot_use_step = False
                        else:
                            print("Checking some stuff!")
                            x_cur, y_cur = agent.pos
                            curr_loc = [x_cur, y_cur]

                            print(curr_loc)
                            print(agent.model.intersection)

                            for val in agent.model.intersection:
                                if val == curr_loc:
                                    print("Inside intersection")
                                    agent.inside_int = True
                                    break

                if cannot_use_step:
                    continue
                else:
                    print(steps)
                    depurated_steps.append(steps)

            if (len(depurated_steps) == 0):
                return

            min = 1000
            best = []
            for opts in depurated_steps:
                x, y = opts
                new_point = [x,y]
                aux = get_distance(new_point, to_)
                if (aux < min):
                    best = new_point
                    min = aux

            agent.model.grid.move_agent(agent, tuple(e for e in best))

    if agent.status == 2:
        for i in range(agent.status):

            possible_steps = agent.model.grid.get_neighborhood(
                agent.pos, moore=False, include_center=False
            )

            depurated_steps = []

            for steps in possible_steps:
                cannot_use_step = False
                searching = agent.model.grid.get_cell_list_contents([steps])

                if len(searching) > 0:
                    for stuff in searching:
                        if isinstance(stuff, Car) or isinstance(stuff, Ambulance) or isinstance(stuff, Sidewalk):
                            cannot_use_step = True
                            break
                        elif isinstance(stuff, TrafficLight):
                            if agent.inside_int == True:
                                break

                            if stuff.status == 1:
                                agent.velocity = 0
                                return
                            if stuff.status == 3:
                                agent.velocity = agent.status + 1
                            else:
                                cannot_use_step = False
                        else:
                            print("Checking some stuff!")
                            x_cur, y_cur = agent.pos
                            curr_loc = [x_cur, y_cur]

                            print(curr_loc)
                            print(agent.model.intersection)

                            for val in agent.model.intersection:
                                if val == curr_loc:
                                    print("Inside intersection")
                                    agent.inside_int = True
                                    break

                if cannot_use_step:
                    continue
                else:
                    print(steps)
                    depurated_steps.append(steps)

            if (len(depurated_steps) == 0):
                return

            min = 1000
            best = []
            for opts in depurated_steps:
                x, y = opts
                new_point = [x,y]
                aux = get_distance(new_point, to_)
                if (aux < min):
                    best = new_point
                    min = aux

            agent.model.grid.move_agent(agent, tuple(e for e in best))


    if agent.status == 3:
        for i in range(agent.status):

            possible_steps = agent.model.grid.get_neighborhood(
                agent.pos, moore=False, include_center=False
            )

            depurated_steps = []

            for steps in possible_steps:
                cannot_use_step = False
                searching = agent.model.grid.get_cell_list_contents([steps])

                if len(searching) > 0:
                    for stuff in searching:
                        if isinstance(stuff, Car) or isinstance(stuff, Ambulance) or isinstance(stuff, Sidewalk):
                            cannot_use_step = True
                            break
                        elif isinstance(stuff, TrafficLight):
                            if agent.inside_int == True:
                                break

                            if stuff.status == 1:
                                agent.velocity = 0
                                return
                            if stuff.status == 3:
                                agent.velocity = agent.status + 1
                            else:
                                cannot_use_step = False
                        else:
                            print("Checking some stuff!")
                            x_cur, y_cur = agent.pos
                            curr_loc = [x_cur, y_cur]

                            print(curr_loc)
                            print(agent.model.intersection)

                            for val in agent.model.intersection:
                                if val == curr_loc:
                                    print("Inside intersection")
                                    agent.inside_int = True
                                    break

                if cannot_use_step:
                    continue
                else:
                    print(steps)
                    depurated_steps.append(steps)

            if (len(depurated_steps) == 0):
                return

            min = 1000
            best = []
            for opts in depurated_steps:
                x, y = opts
                new_point = [x,y]
                aux = get_distance(new_point, to_)
                if (aux < min):
                    best = new_point
                    min = aux

            agent.model.grid.move_agent(agent, tuple(e for e in best))


# Some useful methods that are not dependent of an agent
def get_distance(p, q):
    """ Returns euclidean distance from A to B"""
    return math.sqrt((q[1] - p[1])**2 + (q[0] - p[0])**2)

def set_name(x, y):
    name_dict = {
            0:  { 26 : "sp-left", 24 : "dsp-left" },
            20: { 0 : "sp-down", 49 : "dsp-up" },
            22: { 49 : "sp-up", 0 : "dsp-down" },
            49: { 24 : "sp-right", 26 : "dsp-right" }
        }

    return name_dict[x][y]


def set_middle(origin, destiny):
    # print(f"Origin is {origin} and destiny is {destiny}")
    location_dict = {
            "sp-left" :  { "dsp-up" : [20, 26], "dsp-down" : [22, 26], "dsp-right" : [22, 26]},
            "sp-right" : { "dsp-up" : [20, 24], "dsp-down" : [22, 24], "dsp-left" : [20, 24]},
            "sp-down" : { "dsp-up" : [20, 26], "dsp-left" : [20, 24], "dsp-right" : [20, 26]},
            "sp-up" : { "dsp-down" : [22, 24], "dsp-left" : [22, 24], "dsp-right" : [22, 26]}
    }

    return location_dict[origin][destiny]


class Sidewalk(mesa.Agent):
    """An agent that sims the sidewalk of the street"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class DebugAgents(mesa.Agent):
    """A class for debugging spawning points"""
    def __init__(self, unique_id, status, model):
        super().__init__(unique_id, model)
        self.status = status


class TrafficLight(mesa.Agent):
    """ Traffic light agent """

    def __init__(self, unique_id, location, model):
        super().__init__(unique_id, model)
        self.status = 0
        self.location =  location


class Ambulance(mesa.Agent):
    """An ambulance agent"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 3 # 0 is normal, 1 is pressured, 2 is desesperated, 3 is ambulance
        self.velocity = 4 # it will travel only a meter at the time

        # Reference location with name
        self.origin = ""
        self.destiny = ""
        self.final_des = []
        self.curr_des = []

        self.inside_int = False

    def step(self):
        move(self, self.curr_des)

        des_x, des_y = self.pos
        curr_pos = [des_x, des_y]

        if self.pos[0] == self.curr_des[0] and self.pos[1] == self.curr_des[1]:
            if ((self.curr_des[0] == self.final_des[0]) and (self.curr_des[1] == self.final_des[1])):
                self.model.kill_agents.append(self)
                return
            else:
                self.curr_des = self.final_des

class Car(mesa.Agent):
    """An agent that sims a roomba"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 0 # 0 is normal, 1 is pressured, 2 is desesperated
        self.velocity = 0 # it will travel only a meter at the time

        # Reference location with name
        self.origin = ""
        self.destiny = ""
        self.final_des = []
        self.curr_des = []

        self.inside_int = False

    def step(self):
        #move(self, self.curr_des)

        if self.pos[0] == self.curr_des[0] and self.pos[1] == self.curr_des[1]:
            if ((self.curr_des[0] == self.final_des[0]) and (self.curr_des[1] == self.final_des[1])):
                self.model.kill_agents.append(self)
                return
            else:
                self.curr_des = self.final_des

        # g for the sorrounding areas
        #   These are current agent status dependent:
        #   if found an ambulance then "go to the nearest wall" -> for this the car will have to check its sorroundings and find the nearest Sidewalk agent
        #       if ambulanced found and not near a wall then go to wall
        #       but if ambulance found then just continue going
        #       continue
        #   else check for traffic light ahead
        #       if traffic light is red then velocity will turn 0 and will not g
        #       if traffic light yellow reduce and in range of sensors (by 5) reduce speed by one
        #       if traffic light green continue

        #  If right at the insersection then turn to the proper destination. Will do this in several steps.


class IntersectionModel(mesa.Model):
    """A model that creates the space and spawns the required agents"""

    def __init__(self, max_cars_num, debug=False):
        self.max_cars = max_cars_num
        self.debug = debug
        self.curr_cars = 0 # initially zero

        self.kill_agents = [] # agents to kill after each step

        self.grid = mesa.space.MultiGrid(50, 50, False) # create the space of a width and height room_width, room_height and no torodoidal

        # Creating different schedulers
        self.tl_scheduler = mesa.time.RandomActivation(self) # scheduler for steps
        self.vh_scheduler = mesa.time.RandomActivation(self) # scheduler for steps

        self.running = True # running while this is true
        self.priority = []

        # self.vel_time = 0
        # self.tl_time = 0

        # self.cycle = False

        # Sidewalks:
        x_val = np.union1d(np.array([i for i in range(18)]), np.array([i for i in range(24, 50)]))
        y_val = np.union1d(np.array([i for i in range(22)]), np.array([i for i in range(28, 50)]))

        self.unique_ids = 0

        # Creating the map
        for x in x_val:
            for y in y_val:
                agent = Sidewalk(self.unique_ids, self) # constructor for Sidewalk
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        # Creating the traffic lights agents
        tl_one_x = [17]
        tl_one_y = [25, 26, 27]

        for x in tl_one_x:
            for y in tl_one_y:
                agent = TrafficLight(self.unique_ids, "left", self) # constructor for Sidewalk
                self.tl_scheduler.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        tl_two_x = [24]
        tl_two_y = [22, 23, 24]

        for x in tl_two_x:
            for y in tl_two_y:
                agent = TrafficLight(self.unique_ids, "right", self) # constructor for Sidewalk
                self.tl_scheduler.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        tl_three_x = [18, 19, 20]
        tl_three_y = [21]

        for x in tl_three_x:
            for y in tl_three_y:
                agent = TrafficLight(self.unique_ids, "down", self) # constructor for Sidewalk
                self.tl_scheduler.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        tl_four_x = [21, 22, 23]
        tl_four_y = [28]

        for x in tl_four_x:
            for y in tl_four_y:
                agent = TrafficLight(self.unique_ids, "up", self) # constructor for Sidewalk
                self.tl_scheduler.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                self.unique_ids += 1

        """ CREATING STATIC AGENTS FOR TESTING BEHAVIOR OR DEBUGGING"""
        self.spawn = [
                    [22,49], # up
                    [19, 0], # down
                    [0, 26], # left
                    [49, 23] # right
                ]

        self.dispawn = [
                    [19,49], # up
                    [22, 0], # down
                    [0,23], # left
                    [49, 26] # right
                ]



        self.intersection = []

        x_val_int = [20, 21]
        y_val_int = [i for i in range(0, 22)]

        for x in x_val_int:
            for y in y_val_int:
                self.intersection.append([x, y])

        # self.intersection = []

        # x_val_int = [i for i in range(18, 24)]
        # y_val_int = [i for i in range(22, 28)]

        # for x in x_val_int:
        #     for y in y_val_int:
        #         self.intersection.append([x, y])
        # self.intersection = [
        #         [19, 22], [19, 23], [19, 24],[19, 25], [19, 26], [19, 27], [20, 23], [20, 24], [20, 25], [20, 26], [20, 27],
        #         [21, 23], [21, 24], [21, 25], [21, 26], [21, 27], [22, 23], [22, 24], [22, 25], [22, 26], [22, 27],
        #         [23, 23], [23, 24], [23, 25], [23, 26], [23, 27]
        #         ]

        self.down_streets = {
                "down" : {"left" : [], "right" : []},
                "up" : {"left" : [], "right" : []},
                "left" : {"up" :[], "down" : []},
                "right" : {"up" : [], "down" : []}
        }

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


    """ STEP FOR SENSOR """
    def change_tl(self, prio_arr):
        for conditions in prio_arr:
            if (conditions == "up"):
                for lights in self.tl_up:
                    lights.status = 3

                for lights in self.tl_down:
                    lights.status = 1

                for lights in self.tl_left:
                    lights.status = 1

                for lights in self.tl_right:
                    lights.status = 1

            elif (conditions == "down"):
                for lights in self.tl_down:
                    lights.status = 3

                for lights in self.tl_up:
                    lights.status = 1

                for lights in self.tl_right:
                    lights.status = 1

                for lights in self.tl_left:
                    lights.status = 1

            elif (conditions == "left"):

                for lights in self.tl_left:
                    lights.status = 3

                for lights in self.tl_down:
                    lights.status = 1

                for lights in self.tl_up:
                    lights.status = 1

                for lights in self.tl_right:
                    lights.status = 1

            else:
                for lights in self.tl_left:
                    lights.status = 3

                for lights in self.tl_down:
                    lights.status = 1

                for lights in self.tl_up:
                    lights.status = 1

                for lights in self.tl_right:
                    lights.status = 3

    """ STEP FOR SENSOR """
    def get_vel_reads(self):
        pass
        # decide = {}
        # count = 0
        # vel = 0

        # for one in self.s_up:
        #     res_up = list()
        #     # print(f"Up: searching with sensor in position {one.pos}")

        #     for i in range(7, 18):
        #         aux = (one.pos[0], one.pos[1] + i)
        #         res_up.append(self.grid.get_cell_list_contents(aux))

        #     for val in res_up:
        #         for stuff in val:
        #             if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
        #                 count += 1
        #                 vel += stuff.velocity

        # if (count != 0):
        #     decide["up"] = vel/count

        # count = 0
        # vel = 0

        # for two in self.s_down:
        #     res_down = list()
        #     # print(f"Down: searching with sensor in position {two.pos}")

        #     for i in range(5, 18):
        #         aux = (two.pos[0], two.pos[1] - i)
        #         res_down.append(self.grid.get_cell_list_contents(aux))

        #     for val in res_down:
        #         for stuff in val:
        #             if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
        #                 count += 1
        #                 vel += vel

        # if (count != 0):
        #     decide["down"] = vel/count

        # count = 0
        # vel = 0

        # for three in self.s_left:
        #     res_left = list()
        #     # print(f"Left: {three}")

        #     for i in range(5, 18):
        #         aux = (three.pos[0] - i, three.pos[1])
        #         res_left.append(self.grid.get_cell_list_contents(aux))

        #     for val in res_left:
        #         for stuff in val:
        #             if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
        #                 count += 1
        #                 vel += vel

        # if (count != 0):
        #     decide["left"] = vel/count

        # count = 0
        # vel = 0

        # for four in self.s_right:
        #     res_right = list()
        #     # print(f"Right: {four}")

        #     for i in range(5, 18):
        #         aux = (four.pos[0] + i, four.pos[1])
        #         res_right.append(self.grid.get_cell_list_contents(aux))

        #     for val in res_right:
        #         for stuff in val:
        #             if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
        #                 count += 1
        #                 vel += vel

        # if (count != 0):
        #     decide["right"] = vel/count

        # print(f"The priority list will be {decide}")
        # return sorted(decide, key=decide.get, reverse=True)

    # """ STEP FOR SENSOR """
    # def get_tf_reads(self):
        # decide = {}
        # count = 0

        # for one in self.s_up:
        #     res_up = list()
        #     # print(f"Up: searching with sensor in position {one.pos}")

        #     for i in range(1, 5):
        #         aux = (one.pos[0], one.pos[1] + i)
        #         res_up.append(self.grid.get_cell_list_contents(aux))

        #     for val in res_up:
        #         for stuff in val:
        #             if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
        #                 count += 1

        # if (count != 0):
        #     decide["up"] = count

        # count = 0

        # for two in self.s_down:
        #     res_down = list()
        #     # print(f"Down: searching with sensor in position {two.pos}")

        #     for i in range(1, 5):
        #         aux = (two.pos[0], two.pos[1] - i)
        #         res_down.append(self.grid.get_cell_list_contents(aux))

        #     for val in res_down:
        #         for stuff in val:
        #             if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
        #                 count += 1

        # if (count != 0):
        #     decide["down"] = count

        # count = 0

        # for three in self.s_left:
        #     res_left = list()
        #     # print(f"Left: {three}")

        #     for i in range(1, 5):
        #         aux = (three.pos[0] - i, three.pos[1])
        #         res_left.append(self.grid.get_cell_list_contents(aux))

        #     for val in res_left:
        #         for stuff in val:
        #             if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
        #                 count += 1

        # if (count != 0):
        #     decide["left"] = count

        # count = 0

        # for four in self.s_right:
        #     res_right = list()
        #     # print(f"Right: {four}")

        #     for i in range(1, 5):
        #         aux = (four.pos[0] + i, four.pos[1])
        #         res_right.append(self.grid.get_cell_list_contents(aux))

        #     for val in res_right:
        #         for stuff in val:
        #             if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
        #                 count += 1

        # if (count != 0):
        #     decide["right"] = count

        # return sorted(decide, key=decide.get, reverse=True)


    # SPAWN VEHICLES
    def spawnVehicles(self):
        for location in self.spawn:
            if self.curr_cars == self.max_cars:
                return

            spawn_prob = round(random.uniform(0, 1), 2)

            if spawn_prob > .30:
                x, y = location # extract the location
                agent = Car(self.unique_ids, self) # creates agent

                self.vh_scheduler.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                agent.origin = set_name(x, y)

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
                copy_of_dispawn = self.dispawn
                random.shuffle(copy_of_dispawn)

                for destination in copy_of_dispawn:
                    if (get_distance(location, destination) <= 2):
                        continue
                    else:
                        agent.final_des = destination
                        x_end, y_end = destination
                        agent.destiny = set_name(x_end, y_end)
                        break

                # if self.debug is True:
                #     print(f" [[ Car ]] spawned at ({x}. {y}) with status of {status_debug}")
                #     print(f"    ::- Will go to {agent.final_des}")

                # At spawn set self.curr_des to the middle point
                agent.curr_des = set_middle(agent.origin, agent.destiny)

                # move(agent, agent.curr_des)
                self.unique_ids += 1
                self.curr_cars += 1

            elif spawn_prob < .20:
                x, y = location # extract the location
                agent = Ambulance(self.unique_ids, self) # creates agent

                self.vh_scheduler.add(agent) # adds agent to scheduler
                self.grid.place_agent(agent, (x, y))
                agent.origin = set_name(x, y)

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
                copy_of_dispawn = self.dispawn
                random.shuffle(copy_of_dispawn)

                for destination in copy_of_dispawn:
                    if (get_distance(location, destination) <= 2):
                        continue
                    else:
                        agent.final_des = destination
                        x_end, y_end = destination
                        agent.destiny = set_name(x_end, y_end)
                        break

                agent.curr_des = set_middle(agent.origin, agent.destiny)

                # move(agent, agent.curr_des)
                self.unique_ids += 1
                self.curr_cars += 1
            else:
                continue


    def step(self):

        # if self.debug is True:
        #     print(f"The max number of cars is {self.max_cars}")
        #     print(f"The current number of cars is {self.curr_cars}")

        if self.curr_cars < self.max_cars:
            self.spawnVehicles()

        self.tl_scheduler.step() # first make tl detect stuff
        self.vh_scheduler.step() # then VEHICLES can move

        # LIFECYCLE
        # if self.cycle is False:
        #     # print("Cycle is false")
        #     self.priority = self.get_vel_reads()
        #     self.change_tl(self.priority)

        #     if self.priority == []:
        #         # print("Priority not found yet")
        #         return
        #     else:
        #         self.vel_time += 1
        #         self.cycle = True

        #     # TODO: add that all agents have to stop if light is red

        # if self.cycle is True:
        #     if self.vel_time == 60:
        #         self.priority = self.get_tf_reads()
        #         self.change_tl(self.priority)

        #         if self.tf_time == 60:
        #             self.cycle = False
        #             self.vel_time = 0
        #             self.tf_time = 0
        #         else:
        #             self.tf_time += 1
        #     else:
        #         self.vel_time += 1

        for to_kill in self.kill_agents:
            self.grid.remove_agent(to_kill)
            self.vh_scheduler.remove(to_kill)
            self.kill_agents.remove(to_kill)
            self.curr_cars -= 1
