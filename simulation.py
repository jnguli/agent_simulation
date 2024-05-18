import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, empty_patches):
        if empty_patches:
            self.x, self.y = random.choice(empty_patches)

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = [self.create_agent() for _ in range(num_agents)]
        self.place_agents()
    
    def create_agent(self):
        return Agent(random.randint(0, self.size - 1), random.randint(0, self.size - 1))
    
    def place_agents(self):
        for agent in self.agents:
            while self.grid[agent.x][agent.y] is not None:
                agent.x, agent.y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.grid[agent.x][agent.y] = agent
    
    def get_empty_patches(self):
        empty_patches = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] is None]
        return empty_patches
    
    def move_agents(self):
        for agent in self.agents:
            self.grid[agent.x][agent.y] = None
            empty_patches = self.get_empty_patches()
            agent.move(empty_patches)
            self.grid[agent.x][agent.y] = agent
    
    def display(self):
        for row in self.grid:
            print(' '.join(['A' if cell else '.' for cell in row]))
        print()

def main():
    size = 5
    num_agents = 5
    num_iterations = 10
    
    world = World(size, num_agents)
    
    for _ in range(num_iterations):
        world.display()
        world.move_agents()
    
    world.display()

if __name__ == "__main__":
    main()

