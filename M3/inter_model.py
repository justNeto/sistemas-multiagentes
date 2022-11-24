import mesa
import numpy as np
import random
import math


def move(agent, to_):
    # According to status will do some different things.
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
                        x_cur, y_cur = agent.pos
                        curr_loc = [x_cur, y_cur]

                        # print(curr_loc)
                        # print(agent.model.intersection)

                        for val in agent.model.intersection:
                            if val == curr_loc:
                                # print("Inside intersection")
                                agent.inside_int = True
                                break

            if cannot_use_step:
                continue
            else:
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
                            # print("Checking some stuff!")
                            x_cur, y_cur = agent.pos
                            curr_loc = [x_cur, y_cur]

                            # print(curr_loc)
                            # print(agent.model.intersection)

                            for val in agent.model.intersection:
                                if val == curr_loc:
                                    # print("Inside intersection")
                                    agent.inside_int = True
                                    break

                if cannot_use_step:
                    continue
                else:
                    # print(steps)
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
        self.location = location

    def step(self):
        # Detect towards a certain direction according to location
        print("Detecting some stuff!")

        if self.location == "up":
            pass
        elif self.location == "down":
            pass
        elif self.location == "left":
            pass
        else:
            pass


class Ambulance(mesa.Agent):
    """An ambulance agent"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 3 # 0 is normal, 1 is pressured, 2 is desesperated, 3 is ambulance
        self.velocity = 4 # it will travel only a meter at the time

        # Reference location with name
        self.curr_street = ""
        self.final_des = []

        self.inside_int = False

    def step(self):
        des_x, des_y = self.pos
        curr_pos = [des_x, des_y]

        if (curr_pos == self.final_des):
            self.model.kill_agents.append(self)
            return
        else:
            # move(self, self.final_des)
            pass


class Car(mesa.Agent):
    """An agent that sims a roomba"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 0 # 0 is normal, 1 is pressured, 2 is desesperated
        self.velocity = 0 # it will travel only a meter at the time

        # Reference location with name
        self.curr_street = ""
        self.final_des = []

        self.inside_int = False

    def step(self):
        des_x, des_y = self.pos
        curr_pos = [des_x, des_y]

        if (curr_pos == self.final_des):
            self.model.kill_agents.append(self)
            return
        else:
            # move(self, self.final_des)
            pass


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
                    [21, 49], # up-one
                    [22, 49], # up-one
                    [23, 49], # up-one

                    [18, 0], # down
                    [19, 0], # down
                    [20, 0], # down

                    [0, 25], # left
                    [0, 26], # left
                    [0, 27], # left

                    [49, 22], # right
                    [49, 23], # right
                    [49, 24], # right
                ]

        self.dispawn = [
                    [18, 49], # up
                    [19, 49], # up
                    [20, 49], # up

                    [21, 0], # down
                    [22, 0], # down
                    [23, 0], # down

                    [0,22], # left
                    [0,23], # left
                    [0,24], # left

                    [49, 25], # right
                    [49, 26], # right
                    [49, 27], # right
                ]

        # Intersections
        self.intersection = []

        x_val_int = [i for i in range(18, 24)]
        y_val_int = [i for i in range(22, 28)]

        for x in x_val_int:
            for y in y_val_int:
                self.intersection.append([x, y])

        self.streets = {}

        down_dict = {}
        down_left = []
        down_right = []

        # Down left street
        x_val_int = [18, 19, 20]
        y_val_int = [i for i in range(0, 22)]

        for x in x_val_int:
            for y in y_val_int:
                down_left.append([x, y])

        # Down right street
        x_val_int = [21, 22, 23]
        y_val_int = [i for i in range(0, 22)]

        for x in x_val_int:
            for y in y_val_int:
                down_right.append([x, y])

        down_dict["right"] = down_right
        down_dict["left"] = down_left
        self.streets["down"] = down_dict

        up_dict = {}
        up_left = []
        up_right = []

        # Up left street
        x_val_int = [18, 19, 20]
        y_val_int = [i for i in range(28, 50)]

        for x in x_val_int:
            for y in y_val_int:
                up_left.append([x, y])

        # Up right street
        x_val_int = [21, 22, 23]
        y_val_int = [i for i in range(28, 50)]

        for x in x_val_int:
            for y in y_val_int:
                up_right.append([x, y])

        up_dict["right"] = up_right
        up_dict["left"] = up_left
        self.streets["up"] = up_dict

        left_down = []
        left_up = []
        left_dict = {}

        # Left down street
        x_val_int = [i for i in range(0, 18)]
        y_val_int = [22, 23, 24]

        for x in x_val_int:
            for y in y_val_int:
                left_down.append([x, y])

        # Left up street
        x_val_int = [i for i in range(0, 18)]
        y_val_int = [25, 26, 27]

        for x in x_val_int:
            for y in y_val_int:
                left_up.append([x, y])

        left_dict["up"] = left_up
        left_dict["down"] = left_down
        self.streets["left"] = left_dict

        right_down = []
        right_up = []
        right_dict = {}

        # Right down street
        x_val_int = [i for i in range(24, 50)]
        y_val_int = [22, 23, 24]

        for x in x_val_int:
            for y in y_val_int:
                right_down.append([x, y])

        # Right up street
        x_val_int = [i for i in range(24, 50)]
        y_val_int = [25, 26, 27]

        for x in x_val_int:
            for y in y_val_int:
                right_up.append([x, y])

        right_dict["up"] =  right_up
        right_dict["down"] = right_down
        self.streets["right"] = right_dict

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

        # for key in self.streets:
        #     for vals in self.streets[key]:
        #         for side in self.streets[key][vals]:
        #             x, y = side
        #             agent = DebugAgents(self.unique_ids, "street", self)
        #             self.grid.place_agent(agent, (x, y))
        #             self.unique_ids += 1


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
                        break

                # if self.debug is True:
                #     print(f" [[ Car ]] spawned at ({x}. {y}) with status of {status_debug}")
                #     print(f"    ::- Will go to {agent.final_des}")

                # move(agent, agent.curr_des)
                self.unique_ids += 1
                self.curr_cars += 1

            elif spawn_prob < .20:
                x, y = location # extract the location
                agent = Ambulance(self.unique_ids, self) # creates agent

                self.vh_scheduler.add(agent) # adds agent to scheduler
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
                copy_of_dispawn = self.dispawn
                random.shuffle(copy_of_dispawn)

                for destination in copy_of_dispawn:
                    if (get_distance(location, destination) <= 2):
                        continue
                    else:
                        agent.final_des = destination
                        x_end, y_end = destination
                        break

                move(agent, agent.final_des)
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

        for to_kill in self.kill_agents:
            self.grid.remove_agent(to_kill)
            self.vh_scheduler.remove(to_kill)
            self.kill_agents.remove(to_kill)
            self.curr_cars -= 1
