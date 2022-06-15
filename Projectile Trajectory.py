import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation
import numpy as np
import math as math
import time

#y=xtanθ−gx22v2cos2θ

gravity = 9.8
is_valid = False
x_data = []
y_data = []
x_lim = 0
y_lim = 0

def convert_deg_to_radian(angle):
    radian = angle * (math.pi/180)
    return(float(radian))

def calculate_time_of_flight(velocity, radian):
    time_of_flight = (2 * (velocity * (np.sin(radian))) / gravity)
    return time_of_flight

def calculate_total_displacment(velocity, radian):
    total_displacment = (math.pow(velocity, 2) * (np.sin(2 * radian)) / gravity)
    global x_lim
    x_lim = int(total_displacment)
    return total_displacment

def calculate_max_height(velocity, radian):
    total_displacment = (math.pow(velocity, 2) * (math.pow(np.sin(radian), 2)) / (2 * gravity))
    global y_lim
    y_lim = int(total_displacment)
    return total_displacment

def find_y_from_x(x_cord):
    y_cord = (x_cord * (np.tan(angle))) - ((gravity * (math.pow(x_cord, 2))) / (2 * (math.pow(velocity, 2) * math.pow(np.cos(angle), 2))))
    return y_cord
    
def animation_frame(number):
    x_data.append(number)
    y_data.append(find_y_from_x(number))

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,

def take_user_velocity():
    while is_valid == False:
        velocity = input("What is your desired velocity for the ball? (ft/s): ")
        if not velocity.isnumeric():
            print("Sorry, your velocity must only contain numbers.") 
            continue
        return(float(velocity))

def take_user_angle():
    while is_valid == False:
        angle = input("What is your desired launch angle in degrees for the ball?: ")
        if not angle.isnumeric():
            print("Sorry, your angle must only contain numbers.") 
            continue
        return(float(convert_deg_to_radian(float(angle))))

if __name__ == "__main__":
    velocity = take_user_velocity()
    angle = take_user_angle()

    print("Total flight timeime: " + "{:.2f}".format(calculate_time_of_flight(velocity, angle)))
    print("Total distance: " + "{:.2f}".format(calculate_total_displacment(velocity, angle)))
    print("Max hieght: " + "{:.2f}".format(calculate_max_height(velocity, angle)))

    fig, ax = plot.subplots()
    fig.patch.set_facecolor((0.078, 0.078, 0.078))
    ax.set_xlim(0, x_lim + (x_lim * .1))
    ax.set_ylim(0, y_lim + (y_lim * .1))
    ax.set_facecolor((0.078, 0.078, 0.078))
    ax.spines['bottom'].set_color((.309, .309, .309))

    ax.spines['top'].set_color((.309, .309, .309)) 
    ax.spines['right'].set_color((.309, .309, .309))
    ax.spines['left'].set_color((.309, .309, .309))
    ax.tick_params(axis='x', colors=(.309, .309, .309))
    ax.tick_params(axis='y', colors=(.309, .309, .309))
    plot.xlabel("Distance (ft)", color = ('white'), labelpad = 7)
    plot.ylabel("Height (ft)", color = ('white'), labelpad = 10)
    line, = ax.plot(0,0, color = ('white'), solid_capstyle='round', linewidth = 3)

    if x_lim > y_lim:
        limmiter = x_lim
    else:
        limmiter = y_lim
        
    ax = plot.gca()
    ax.set_xlim([0, limmiter * 1.1])
    ax.set_ylim([0, limmiter * 1.1])

    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 500, .1), interval = 10)
    plot.show()