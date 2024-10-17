import math
import random

import pygame

import config as cf

# exports
def handler(all_particles):
    all_particles[:] = [
        update_particle(particle) for particle in all_particles
        if (particle[2] > 0)
    ]
    for particle in all_particles:
        pygame.draw.circle(
            cf.SCREEN,
            particle[3],
            (int(particle[0][0]), int(particle[0][1])),
            int(particle[2])
        )

def spawn_many_colors(part_per_color, part_list):
    for color in cf.COLORLIST:
        spawn_colors_center(part_per_color, part_list, color)


# local
def update_particle(particle):
    particle[0][0] += particle[1][0]
    particle[0][1] += particle[1][1]
    particle[2] -= 0.1
    return particle

def spawn_colors_center(num_part, part_list, color):
    for _ in range(num_part):
        # Initial position at the center of the screen
        x_pos = cf.SCREEN_RECT.centerx
        y_pos = cf.SCREEN_RECT.centery

        # Generate random x and y velocities
        x_vel = random.uniform(-1, 1)
        y_vel = random.uniform(-1, 1)

        # Calculate the magnitude of the velocity vector
        magnitude = math.sqrt(x_vel ** 2 + y_vel ** 2)

        # Normalize the vector and scale it by a desired magnitude
        if magnitude != 0:  # Avoid division by zero
            x_magnitude = random.uniform(0, 8)  # Adjust this value for speed control
            x_vel = (x_vel / magnitude) * x_magnitude
            y_magnitude = x_magnitude * cf.AXIS_RATIO
            y_vel = (y_vel / magnitude) * y_magnitude

        # Random size for the particle
        size = random.randint(4, 20)

        # Append the particle to the list
        part_list.append([[x_pos, y_pos],  # Position
                          [x_vel, y_vel],  # Velocity
                          size,            # Size
                          color])          # Color