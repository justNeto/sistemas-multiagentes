from roomba_model import *
import mesa

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}

    if isinstance(agent, DirtAgent):
        portrayal["Color"] = "brown"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
    else:
        portrayal["Color"] = "black"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.3

    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal, 50, 50, 500, 500)

server = mesa.visualization.ModularServer(
        CleaningModel, [grid], "Cleaning model", {"num_of_roombas" : 100 , "dirt_percentage" :  60, "room_width" : 50, "room_height" : 50, "max_num_steps" : 100}
)

server.port = 8521 # The default
server.launch()
