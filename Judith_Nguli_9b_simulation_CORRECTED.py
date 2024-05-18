import random



class Agent:

    def __init__(self, id):
        self.id = id
        self.position = None



def find_empty_patch(self, world):

    empty_patches = [(x, y) for x in range(world.size) for y in range(world.size) if world.grid[x][y] is None]

    return random.choice(empty_patches) if empty_patches else None



def move_to(self, position):

    self.position = position





class World:

    def __init__(self, size, num_agents):

        self.size = size

        self.grid = [[None for _ in range(size)] for _ in range(size)]

        self.agents = [Agent(i) for i in range(num_agents)]



def place_agent(self, agent, position):

    x, y = position

    self.grid[x][y] = agent

    agent.move_to(position)



def move_agent(self, agent):

    old_position = agent.position

    new_position = agent.find_empty_patch(self) 
    if new_position:
        if old_position:
            self.grid[old_position[0]][old_position[1]] = None    
            self.place_agent(agent, new_position)



def display(self):

    for row in self.grid:

        print(' '.join(['A' if cell else '.' for cell in row]))

print()





# Initialize the world

world_size = 5

num_agents = 3

num_loops = 5



world = World(world_size, num_agents)



# Place agents randomly in the initial setup

for agent in world.agents:

    position = agent.find_empty_patch(world)

if position:

    world.place_agent(agent, position)



# Simulation loop

for step in range(num_loops):

    print(f"Step {step + 1}:")

world.display()

for agent in world.agents:

    world.move_agent(agent)

world.display()

