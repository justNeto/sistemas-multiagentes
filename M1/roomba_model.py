import mesa

class DirtAgent(mesa.Agent):
    """An agent that sims dirt"""

    def __init__(self, unique_id, dirtyness, model):
        super().__init__(unique_id, dirtyness, model)

class RoombaAgent(mesa.Agent):
    """An agent that sims a roomba"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )

        print(possible_steps)
        break

        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    # def clean(self):

    def clean(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        if len(cellmates) > 1:
            print(cellmates)
            # other = self.random.choice(cellmates)
            # other.wealth += 1
            # self.wealth -= 1

    def step(self):
        will_move = self.move() # check if agent can move
        if (will_move):
            self.clean()

class CleaningModel(mesa.Model):
    """A model that creates the space and spawns the required agents"""

    def __init__(self, num_of_roombas, dirt_percentage, room_width, room_height, max_num_batches):

        # Before doing anything check data type of dirt_percentage
        if ((!isinstance(dirt_percentage, int) and (0 <= dirt_percentage) ):
            print("Error: not a percentage betw
            break

        # Declare initial data of the model
        self.roombas = num_of_roombas
        self.dirt = dirt_percentage
        self.batch = max_num_batches

        self.grid = mesa.space.MultiGrid(room_width, room_height, True) # create the space of a width and height room_width, room_height

        self.schedule = mesa.time.RandomActivation(self) # scheduler for steps
        self.running = True # running

        # Populate the grid with dirt agents

        for i in range():


        # Create all the roomba agents
        for i in range(self.roombas):
            agent = RoombaAgent(i, self) # constructor RoombaAgent(id)
            self.schedule.add(agent) # adds agent to scheduler

            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

        # self.datacollector = mesa.DataCollector(
        #     model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        # )

    def step(self):
        #self.datacollector.collect(self)
        self.schedule.step()
