import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v_initial, angle_degrees, g=9.81):
    """
    Simulate projectile motion given initial velocity and angle.
    
    Parameters:
    v_initial (float): Initial velocity in m/s.
    angle_degrees (float): Launch angle in degrees from the horizontal.
    g (float): Acceleration due to gravity (default 9.81 m/s^2).

    Returns:
    tuple: Arrays of x and y coordinates, maximum height, total distance
    """
    angle_radians = np.radians(angle_degrees)  # Convert angle to radians

    # Calculate initial velocity components
    v_initial_x = v_initial * np.cos(angle_radians)
    v_initial_y = v_initial * np.sin(angle_radians)

    # Time of flight until projectile hits the ground
    t_flight = 2 * v_initial_y / g
    t = np.linspace(0, t_flight, num=100)  # Generate time points

    # Calculate trajectory
    x = v_initial_x * t
    y = v_initial_y * t - 0.5 * g * t**2

    # Maximum height and total distance
    max_height = (v_initial_y**2) / (2 * g)
    total_distance = v_initial_x * t_flight

    return x, y, max_height, total_distance

# Example usage
v_initial = 50  # initial velocity in m/s
angle_degrees = 45  # launch angle in degrees

x, y, max_height, total_distance = projectile_motion(v_initial, angle_degrees)

# Plot the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title("Projectile Motion Trajectory")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()

print(f"Maximum Height: {max_height:.2f} m")
print(f"Total Distance: {total_distance:.2f} m")