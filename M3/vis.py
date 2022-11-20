from inter_model import *
import mesa

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}

    if isinstance(agent, Sidewalk):
        portrayal["Color"] = "brown"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.3
    elif isinstance(agent, Car):
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.3
    elif isinstance(agent, Ambulance):
            portrayal["Color"] = "blue"
            portrayal["Layer"] = 1
            portrayal["r"] = 0.5
    elif isinstance(agent, TrafficLight):
        if (agent.status == 1): # if stop in step
            portrayal["Color"] = "red"
            portrayal["Layer"] = 1
            portrayal["r"] = 0.5
        elif (agent.status == 2): #
            portrayal["Color"] = "yellow"
            portrayal["Layer"] = 1
            portrayal["r"] = 0.5
        elif (agent.status == 3): #
            portrayal["Color"] = "green"
            portrayal["Layer"] = 1
            portrayal["r"] = 0.5
        else:
            portrayal["Color"] = "black"
            portrayal["Layer"] = 1
            portrayal["r"] = 0.5
    elif isinstance(agent, Sensor):
            portrayal["Color"] = "blue"
            portrayal["Layer"] = 1
            portrayal["r"] = 0


    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal, 50, 50, 500, 500)

server = mesa.visualization.ModularServer(
        IntersectionModel, [grid], "Intersection model", {"max_cars_num" : 20}
)

server.port = 8521 # The default
server.launch()
