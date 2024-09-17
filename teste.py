'''
1-
i = 0
for element in elements:
    # Do something with i and element
    i += 1
'''
import tkinter as tk
import math

# Elements on the roulette
elements = ["Impar", "Par"]

# Constants
width = 600
height = 600
num_sectors = len(elements)
spin_duration = 3000  # Duration of the spin in milliseconds
spin_steps = 100  # Number of spin steps to simulate spinning

# Colors
COLORS = ["#78b152", "#217100"]  # Default colors


def draw_wheel(canvas, colors, elements, rotation_angle=0):
    canvas.delete("all")
    center_x = width / 2
    center_y = height / 2 #I am declaring both centers so i can use them as parameters after
    radius = min(center_x, center_y) - 20 # this one ensures that the radius of the circle will fit inside the canvas, not only that i put a 
                                          #- 20 to serve as a padding function. It makes so my wheel keeps away from the edges when created
    angle_per_element = 360 / num_sectors # as it says here i can cast as much elements as i want and it will be calculated later on
    
    for i in range(num_sectors):  # i found this enumerate function. It is built in and it is equals to number 1-. I like it.
        start_angle = i * angle_per_element + rotation_angle # this logic is used so i can allocate how many elements as i want. That means start angle =0
                                            # so i(index) * angle_per_element = 0 since it was already calculated before.
        end_angle = (i + 1) * angle_per_element + rotation_angle # In the same way, it ends where the next one begins (1 * angle_per_element) 120 with bobo test element
        color = colors[i]
        canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                          start=start_angle % 360, extent=angle_per_element, fill=color, outline="black")
        text_angle = math.radians(start_angle + angle_per_element / 2)
        text_x = center_x + (radius / 2) * math.cos(text_angle) # those two make sure it is correctly angled with exis x and y
        text_y = center_y - (radius / 2) * math.sin(text_angle)
        canvas.create_text(text_x, text_y, text=elements[i], font=("Comic Sans", 16, "bold")) #this creates the texts that were specified earlier ant attributes the texts contents and font
 # Draw the arrow
    arrow_length = 40
    arrow_width = 20
    arrow_x1 = center_x - arrow_width / 2
    arrow_x2 = center_x + arrow_width / 2
    arrow_y1 = 10
    arrow_y2 = arrow_y1 + arrow_length
    canvas.create_polygon(arrow_x1, arrow_y1, arrow_x2, arrow_y1, center_x, arrow_y2, fill="orange", outline="black")
def animate_spin(canvas, colors, elements, end_angle, result_label, result_color, step=0):
    if step >= spin_steps: #this is the stop condition
        draw_wheel(canvas, colors, elements, rotation_angle=end_angle % 360)
        result_label.config(text=" One More Time!!!")
        return

    # This here will update the angles
    current_angle = (step * 360 / spin_steps) % 360
    draw_wheel(canvas, colors, elements, rotation_angle=current_angle)
    canvas.after(int(spin_duration / spin_steps), animate_spin, canvas, colors, elements, end_angle, result_label, result_color, step + 1) #i hated learning how to do this, lost some good hours of sleep

def spin_wheel(elements, label):      
    try:
        user_number = int(text_input.get("1.0", "end-1c").strip())
        if user_number % 2 == 0:
            print(user_number)
            result_color = "#217100"  # Green Dark for "Impar"
            desired_result = "Par"
        else:
            result_color = "#78b152"  # Green for "Par"
            desired_result = "Impar"
        
        # Set colors and calculate end angle
        colors = [result_color] + [color for color in COLORS if color != result_color] #this is witchcraft. Basically it will make sure the color of the result is always the one we defined
        end_angle = elements.index(desired_result) * (360 / num_sectors)

        # Clear previous result
        label.config(text="Spinning...")

        # Start spinning animation
        animate_spin(canvas, colors, elements, end_angle, label, result_color)
        
    except:
        label.config(text="Please enter a valid number") # Used this just to be fancy

# Set up the main window
root = tk.Tk()
root.title("Roulette")

# Set up canvas to draw the roulette
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Draw the initial roulette wheel
draw_wheel(canvas, COLORS, elements)

# Set up the result label, it is like a div
result_label = tk.Label(root, text="Whose wisdom you seek here?", font=("Arial", 16))  #creates the div camp where text label will appear
                        #root: a parent container where the label will be placed, in my case is the main window.
                              #text= it says what will be shown on the label. It will change after the roulette is spun. 
result_label.pack(pady=10) #.pack -> adds the label to the window and control its positioning. It is a layout manager taht i am caling
#pady=10 adds 10 pixels of vertical padding (padding y) above and below. It makes so things have space between them, they won't overlay.

# Set up the text input area
text_input = tk.Text(root, height=2, width=20)
text_input.pack()

# Set up the spin button
spin_button = tk.Button(root, text="Spin", font=("Arial", 16), command=lambda: spin_wheel(elements, result_label))
spin_button.pack(pady=10)


# Run the Tkinter event loop
root.mainloop()
