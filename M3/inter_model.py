import mesa
import numpy as np
import random
import math


def move(agent, to_):
    print("WILL MOVE!")
    print(f" ::: - CURRENT AGENT LOCATION: {agent.pos}")

    # According to status will do some different things.
    if agent.status == 0:

        # Possible movements for an agent
        possible_steps = agent.model.grid.get_neighborhood(
            agent.pos, moore=False, include_center=False
        )

        print(f"Possible steps: {possible_steps}")

        depurated_steps = []

        for steps in possible_steps:
            cannot_use_step = False
            can_use_street = False
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
                        x_cur, y_cur = agent.pos
                        curr_loc = [x_cur, y_cur]
                        x_pos, y_pos = stuff.pos
                        next_loc = [x_pos, y_pos]

                        for location in agent.model.streets[agent.curr_street][agent.curr_side]:
                            if next_loc == location:
                                print("Can use this step as it is inside the current street")
                                can_use_street = True
                                break

                        if can_use_street is True:
                            break

                        print(f"Next location {next_loc} is not inside current street. Checking if inside intersection")

                        for val in agent.model.intersection:
                            print(f"Value is {val}")
                            if curr_loc == val:
                                agent.inside_int = True
                                print("Current value inside intersection")

                                break # cannot use this step
                            elif next_loc == val:

                                print("Current value is inside intersection")
                                for key in agent.model.streets:
                                    for vals in agent.model.streets[key]:
                                        for side in agent.model.streets[key][vals]:

                                            if agent.final_des == side:
                                                agent.curr_street = key # this will be which street
                                                agent.curr_side = vals # this will be which side of the street

                                print("Next location will be inside intersection")
                                can_use_street = True

            if cannot_use_step is True:
                continue
            elif can_use_street is False:
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

            # Possible gments for an agent
            possible_steps = agent.model.grid.get_neighborhood(
                agent.pos, moore=False, include_center=False
            )

            print(f"Possible steps: {possible_steps}")

            depurated_steps = []

            for steps in possible_steps:
                print(f"\n\n | Checking in current step {steps} \n")
                cannot_use_step = False
                can_use_street = False
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
                            x_cur, y_cur = agent.pos
                            curr_loc = [x_cur, y_cur]
                            x_pos, y_pos = stuff.pos
                            next_loc = [x_pos, y_pos]

                            for location in agent.model.streets[agent.curr_street][agent.curr_side]:
                                if next_loc == location:
                                    print("Can use this step as it is inside the current street")
                                    can_use_street = True
                                    break

                            print(f"Next location {next_loc} is not inside current street. Checking if inside intersection")

                            if can_use_street is True:
                                break

                            for val in agent.model.intersection:
                                print(f"Value is {val}")
                                if curr_loc == val:
                                    agent.inside_int = True
                                    print("Current value not inside intersection")
                                    break # cannot use this step
                                elif next_loc == val:

                                    for key in agent.model.streets:
                                        for vals in agent.model.streets[key]:
                                            for side in agent.model.streets[key][vals]:

                                                if agent.final_des == side:
                                                    agent.curr_street = key # this will be which street
                                                    agent.curr_side = vals # this will be which side of the street

                                    print("Next location will be inside intersection")
                                    can_use_street = True

                if cannot_use_step is True:
                    continue
                elif can_use_street is False:
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

            print(best)

            agent.model.grid.move_agent(agent, tuple(e for e in best))

    if agent.status == 2:
        for i in range(agent.status):

            # Possible gments for an agent
            possible_steps = agent.model.grid.get_neighborhood(
                agent.pos, moore=False, include_center=False
            )

            depurated_steps = []

            for steps in possible_steps:
                print(f"\n\n | Checking in current step {steps} \n")
                cannot_use_step = False
                can_use_street = False
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
                            x_cur, y_cur = agent.pos
                            curr_loc = [x_cur, y_cur]
                            x_pos, y_pos = stuff.pos
                            next_loc = [x_pos, y_pos]

                            for location in agent.model.streets[agent.curr_street][agent.curr_side]:
                                if next_loc == location:
                                    print("Can use this step as it is inside the current street")
                                    can_use_street = True
                                    break

                            print(f"Next location {next_loc} is not inside current street. Checking if inside intersection")

                            if can_use_street is True:
                                break

                            for val in agent.model.intersection:
                                print(f"Value is {val}")
                                if curr_loc == val:
                                    agent.inside_int = True
                                    print("Current value not inside intersection")
                                    break # cannot use this step
                                elif next_loc == val:

                                    for key in agent.model.streets:
                                        for vals in agent.model.streets[key]:
                                            for side in agent.model.streets[key][vals]:

                                                if agent.final_des == side:
                                                    agent.curr_street = key # this will be which street
                                                    agent.curr_side = vals # this will be which side of the street

                                    print("Next location will be inside intersection")
                                    can_use_street = True

                if cannot_use_step is True:
                    continue
                elif can_use_street is False:
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

    if agent.status == 3:

        for i in range(agent.status):

            possible_steps = agent.model.grid.get_neighborhood(
                agent.pos, moore=False, include_center=False
            )

            print(f"Possible steps: {possible_steps}")

            depurated_steps = []

            for steps in possible_steps:
                print(f"\n\n | Checking in current step {steps} \n")
                cannot_use_step = False
                can_use_street = False
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
                                # CHECK THIS BECAUSE DOES NOT MAKE SENSE
                        else:
                            x_cur, y_cur = agent.pos
                            curr_loc = [x_cur, y_cur]
                            x_pos, y_pos = stuff.pos
                            next_loc = [x_pos, y_pos]


                            for location in agent.model.streets[agent.curr_street][agent.curr_side]:
                                if next_loc == location:
                                    print("Can use this step as it is inside the current street")
                                    can_use_street = True
                                    break

                            print(f"Next location {next_loc} is not inside current street. Checking if inside intersection")

                            if can_use_street is True:
                                break

                            for val in agent.model.intersection:
                                print(f"Value is {val}")
                                if curr_loc == val:
                                    agent.inside_int = True
                                    print("Current value not inside intersection")
                                    break # cannot use this step
                                elif next_loc == val:

                                    for key in agent.model.streets:
                                        for vals in agent.model.streets[key]:
                                            for side in agent.model.streets[key][vals]:

                                                if agent.final_des == side:
                                                    agent.curr_street = key # this will be which street
                                                    agent.curr_side = vals # this will be which side of the street

                                    print("Next location will be inside intersection")
                                    can_use_street = True


                if cannot_use_step is True:
                    continue
                elif can_use_street is False:
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


# Some useful methods that are not dependent of an agent
def get_distance(p, q):
    """ Returns euclidean distance from A to B"""
    return math.sqrt((q[1] - p[1])**2 + (q[0] - p[0])**2)


class Sidewalk(mesa.Agent):
    """An agent that sims the sidewalk of the street"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class DebugAgents(mesa.Agent):
    def __init__(self, unique_id, status, model):
        super().__init__(unique_id, model)
        self.status = status


class TrafficLight(mesa.Agent):
    """ Traffic light agent """

    def __init__(self, unique_id, direction, model):
        super().__init__(unique_id, model)
        self.status = 0
        self.direction = direction

    def step(self):
        if self.model.yellow_light is True:
            if self.status == 3:
                self.status = 2
                return

        if self.model.prio == []:
            # print("No queue found. Traffic lights will be set to 0")
            self.status = 0
            return
        else:
            if self.direction == self.model.prio[0]:
                self.status = 3
            else:
                self.status = 1


class Ambulance(mesa.Agent):
    """An ambulance agent"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 3 # 0 is normal, 1 is pressured, 2 is desesperated, 3 is ambulance
        self.velocity = 4 # it will travel only a meter at the time

        # Reference location with name
        self.curr_side = ""
        self.curr_street = ""
        self.final_des = []
        self.inside_int = False

    def step(self):
        des_x, des_y = self.pos
        curr_pos = [des_x, des_y]

        if curr_pos == self.final_des:
            self.model.kill_agents.append(self)
            return
        else:
            move(self, self.final_des)
            pass


class Car(mesa.Agent):
    """An agent that sims a roomba"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 0 # 0 is normal, 1 is pressured, 2 is desesperated
        self.velocity = 0 # it will travel only a meter at the time

        # Reference location with name
        self.curr_side = ""
        self.curr_street = ""
        self.final_des = []
        self.inside_int = False

    def step(self):
        des_x, des_y = self.pos
        curr_pos = [des_x, des_y]

        if curr_pos == self.final_des:
            self.model.kill_agents.append(self)
            return
        else:
            move(self, self.final_des)
            pass


# INTERSECTION GO HERE
class IntersectionModel(mesa.Model):

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

        self.prio = []
        self.time = 0

        self.tf_cycle = False
        self.vel_cycle = False

        self.yellow_light = False

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

        # TESTING DETECTION OF TRAFFIC LIGHTS

        # # Down
        # tx = [19, 21, 18]
        # ty = [i for i in range(18, 20)]

        # for x in tx:
        #     for y in ty:
        #         agent = Car(self.unique_ids, self)
        #         self.grid.place_agent(agent, (x, y))
        #         self.unique_ids += 1

        # # Up
        # tx = [19, 20]
        # ty = [i for i in range(29, 31)]

        # for x in tx:
        #     for y in ty:
        #         agent = Car(self.unique_ids, self)
        #         self.grid.place_agent(agent, (x, y))
        #         self.unique_ids += 1

        # agent = Car(self.unique_ids, self)
        # self.grid.place_agent(agent, (22, 30))
        # self.unique_ids += 1

        # # Left
        # ty = [22, 24, 25, 26]
        # tx = [i for i in range(15, 17)]

        # for x in tx:
        #     for y in ty:
        #         agent = Car(self.unique_ids, self)
        #         self.grid.place_agent(agent, (x, y))
        #         self.unique_ids += 1

        # agent = Car(self.unique_ids, self)
        # self.grid.place_agent(agent, (15, 27))
        # self.unique_ids += 1

        for key in self.streets:
            for vals in self.streets[key]:
                for side in self.streets[key][vals]:
                    x, y = side
                    agent = DebugAgents(self.unique_ids, "street", self)
                    self.grid.place_agent(agent, (x, y))
                    self.unique_ids += 1


    """ GET TRAFFIC LIGHTS READ  """
    def get_tf_reads(self):
        s_up = [agents for agents in self.tl_scheduler.agents if agents.direction == "up"]
        s_down = [agents for agents in self.tl_scheduler.agents if agents.direction == "down"]
        s_left = [agents for agents in self.tl_scheduler.agents if agents.direction == "left"]
        s_right = [agents for agents in self.tl_scheduler.agents if agents.direction == "right"]

        decide = {}
        count = 0

        for one in s_up:
            res_up = list()
            # print(f"Up: searching with sensor in position {one.pos}")

            for i in range(1, 5):
                aux = (one.pos[0], one.pos[1] + i)
                res_up.append(one.model.grid.get_cell_list_contents(aux))

            for val in res_up:
                for stuff in val:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
                        count += 1

        if (count != 0):
            decide["up"] = count

        count = 0

        for two in s_down:
            res_down = list()
            # print(f"Down: searching with sensor in position {two.pos}")

            for i in range(1, 5):
                aux = (two.pos[0], two.pos[1] - i)
                res_down.append(two.model.grid.get_cell_list_contents(aux))

            for val in res_down:
                for stuff in val:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
                        count += 1

        if (count != 0):
            decide["down"] = count

        count = 0

        for three in s_left:
            res_left = list()
            # print(f"Left: {three}")

            for i in range(1, 5):
                aux = (three.pos[0] - i, three.pos[1])
                res_left.append(three.model.grid.get_cell_list_contents(aux))

            for val in res_left:
                for stuff in val:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
                        count += 1

        if (count != 0):
            decide["left"] = count

        count = 0

        for four in s_right:
            res_right = list()
            # print(f"Right: {four}")

            for i in range(1, 5):
                aux = (four.pos[0] + i, four.pos[1])
                res_right.append(four.model.grid.get_cell_list_contents(aux))

            for val in res_right:
                for stuff in val:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
                        count += 1

        if (count != 0):
            decide["right"] = count

        print(f"The traffic prio will be {decide}")
        if decide == {}:
            return []
        else:
            return sorted(decide, key=decide.get, reverse=True)


    """ STEP FOR SENSOR """
    def get_vel_reads(self):
        s_up = [agents for agents in self.tl_scheduler.agents if agents.direction == "up"]
        s_down = [agents for agents in self.tl_scheduler.agents if agents.direction == "down"]
        s_left = [agents for agents in self.tl_scheduler.agents if agents.direction == "left"]
        s_right = [agents for agents in self.tl_scheduler.agents if agents.direction == "right"]

        decide = {}
        count = 0
        vel = 0

        for one in s_up:
            res_up = list()
            # print(f"Up: searching with sensor in position {one.pos}")

            for i in range(7, 18):
                aux = (one.pos[0], one.pos[1] + i)
                res_up.append(self.grid.get_cell_list_contents(aux))

            for val in res_up:
                for stuff in val:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
                        count += 1
                        vel += stuff.velocity

        if (count != 0):
            decide["up"] = vel/count

        count = 0
        vel = 0

        for two in s_down:
            res_down = list()
            # print(f"Down: searching with sensor in position {two.pos}")

            for i in range(5, 18):
                aux = (two.pos[0], two.pos[1] - i)
                res_down.append(self.grid.get_cell_list_contents(aux))

            for val in res_down:
                for stuff in val:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
                        count += 1
                        vel += vel

        if (count != 0):
            decide["down"] = vel/count

        count = 0
        vel = 0

        for three in s_left:
            res_left = list()
            # print(f"Left: {three}")

            for i in range(5, 18):
                aux = (three.pos[0] - i, three.pos[1])
                res_left.append(self.grid.get_cell_list_contents(aux))

            for val in res_left:
                for stuff in val:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
                        count += 1
                        vel += vel

        if (count != 0):
            decide["left"] = vel/count

        count = 0
        vel = 0

        for four in s_right:
            res_right = list()
            # print(f"Right: {four}")

            for i in range(5, 18):
                aux = (four.pos[0] + i, four.pos[1])
                res_right.append(self.grid.get_cell_list_contents(aux))

            for val in res_right:
                for stuff in val:
                    if isinstance(stuff, Car) or isinstance(stuff, Ambulance):
                        count += 1
                        vel += vel

        if (count != 0):
            decide["right"] = vel/count

        print(f"The velocity prio will be {decide}")
        if decide == {}:
            return []
        else:
            return sorted(decide, key=decide.get, reverse=True)


    # SPAWN VEHICLES
    def spawnVehicles(self):
        random.shuffle(self.spawn)

        for location in self.spawn:
            if self.curr_cars == self.max_cars:
                return

            spawn_prob = round(random.uniform(0, 1), 2)

            if spawn_prob > .30:
                x, y = location # extract the location
                spawn_pos = [x, y]

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
                    if (get_distance(location, destination) <= 10):
                        continue
                    else:
                        agent.final_des = destination
                        x_end, y_end = destination

                        # Get current street name
                        for key in self.streets:
                            for vals in self.streets[key]:
                                for side in self.streets[key][vals]:

                                    if spawn_pos == side:
                                        agent.curr_street = key # this will be which street
                                        agent.curr_side = vals # this will be which side of the street
                        break

                if self.debug is True:
                    print(f" [[ Car ]] spawned at ({x}. {y}) with status of {status_debug}")
                    print(f"    ::- Will go to {agent.final_des}")

                move(agent, agent.final_des)
                self.unique_ids += 1
                self.curr_cars += 1

            elif spawn_prob < .20:
                x, y = location # extract the location
                spawn_pos = [x, y]
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

                        for key in self.streets:
                            for vals in self.streets[key]:
                                for side in self.streets[key][vals]:

                                    if spawn_pos == side:
                                        agent.curr_street = key # this will be which street
                                        agent.curr_side = vals # this will be which side of the street
                        break

                if self.debug is True:
                    print(f" [[ Ambulance ]] spawned at ({x}. {y}) with status of {status_debug}")
                    print(f"    ::- Will go to {agent.final_des}")

                move(agent, agent.final_des)
                self.unique_ids += 1
                self.curr_cars += 1
            else:
                continue


    def check_inter_empty(self):
        vehicles = [agents for agents in self.vh_scheduler.agents]

        for location in self.intersection:
            for vehicle in vehicles:
                x_v, y_v = vehicle.pos
                compare = [x_v, y_v]

                if compare == location:
                    return False

        return True


    def step(self):

        # if self.debug is True:
        #     print(f"The max number of cars is {self.max_cars}")
        #     print(f"The current number of cars is {self.curr_cars}")

        if self.curr_cars < self.max_cars:
            self.spawnVehicles()

        print("Vehicles have spawned!")
        print(self.intersection)

        if self.tf_cycle is True: # if there is a cycle active

            print(":::- Traffic cycle is running!")
            print(self.time)

            if self.time == 20:
                # Set current traffic light in green to yellow
                self.yellow_light = True
                self.tl_scheduler.step() # move vehicles
                self.time += 1

            if self.time == 30:

                # Do while intersection is not empty
                int_empty = self.check_inter_empty()

                if int_empty is True:
                    self.tf_time = 0
                    self.tf_cycle = False
                else:
                    self.vh_scheduler.step() # move vehicles

            else:
                self.vh_scheduler.step() # move vehicles
                self.time += 1

        elif self.vel_cycle is True:

            print(":::- Velocity cycle is running!")
            print(self.time)

            if self.time == 10:
                # Set current traffic light in green to yellow
                self.yellow_light = True
                self.tl_scheduler.step() # move vehicles
                self.time += 1

            elif self.time == 20: # max time

                # Do while intersection is not empty
                int_empty = self.check_inter_empty()
                print(f"Intersection is empty?: {int_empty}")

                if int_empty is True and self.prio == []:
                    print("Setting time to 0")
                    self.time = 0
                    self.vel_cycle = False
                    self.yellow_light = False
                elif int_empty is True and self.prio != []:
                    self.prio.pop(0)
                    self.yellow_light = False
                    self.tl_scheduler.step() # move vehicles
                    self.time = 0
                else:
                    self.vh_scheduler.step() # move vehicles

            else:
                self.vh_scheduler.step() # move vehicles
                self.time += 1
        else:
            print("No cycle is running! Scanning for priority")
            self.prio = self.get_tf_reads() # traffic has priority

            if self.prio == []: # if no traffic then get vel reads
                self.prio = self.get_vel_reads()

                if self.prio == []:
                    print("No vel nor tf reads found")
                    self.tl_scheduler.step()
                else:
                    print("Vel cycle found!")
                    self.vel_cycle = True
                    self.tl_scheduler.step()

            else: # tf prio found. Start cycle
                tf_cycle = True
                self.tl_scheduler.step()

            self.vh_scheduler.step()

        for to_kill in self.kill_agents:
            self.grid.remove_agent(to_kill)
            self.vh_scheduler.remove(to_kill)
            self.kill_agents.remove(to_kill)
            self.curr_cars -= 1
