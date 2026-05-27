import os
import cv2
import matplotlib
try:
    matplotlib.use('TkAgg') 
except:
    pass

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- 1. Define Your Local Image Path Here ---
IMG_PATH = r'C:\Users\mathe\Downloads\Traffic night.v1i.yolov8\train\images\00044.jpg' 

if not os.path.exists(IMG_PATH):
    print(f'ERROR: File not found at: {IMG_PATH}')
    exit()

img = cv2.imread(IMG_PATH)
if img is None:
    print('ERROR: cv2 could not read the file.')
    exit()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
H, W = img.shape[:2]

# --- 2. Set Up Interaction ---
clicked_points = []
temporary_lines = []
temporary_markers = []

fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(img_rgb)
ax.set_title(
    'Draw in a CLOCKWISE circle:\n'
    '1. Top-Left  ➔  2. Top-Right\n'
    '        ⇧                 ⇩\n'
    '4. Bottom-Left ⇦ 3. Bottom-Right',
    fontsize=14, fontweight='bold'
)

# --- 3. Define Click Logic ---
def onclick(event):
    if event.xdata is None: return
    
    if len(clicked_points) < 4:
        x, y = int(event.xdata), int(event.ydata)
        clicked_points.append((x, y))

        # Assign colors based on the new clockwise order
        if len(clicked_points) == 1: 
            color = 'cyan'
            label = f'1: TL ({x},{y})'
        elif len(clicked_points) == 2: 
            color = 'lime'
            label = f'2: TR ({x},{y})'
        elif len(clicked_points) == 3: 
            color = 'yellow'
            label = f'3: BR ({x},{y})'
        else: 
            color = 'orange'
            label = f'4: BL ({x},{y})'
        
        # Draw point and label
        marker, = ax.plot(x, y, 'o', color=color, markersize=10, zorder=5)
        temporary_markers.append(marker)
        ax.annotate(label, (x, y), color=color, fontsize=11, fontweight='bold', 
                    xytext=(x+10, y-15), zorder=6)

        # Draw connecting lines as you click
        if len(clicked_points) > 1:
            line, = ax.plot([clicked_points[-2][0], x], 
                            [clicked_points[-2][1], y], 
                            '-', color='lime', linewidth=2, zorder=4)
            temporary_lines.append(line)

        # Complete the shape on the 4th click
        if len(clicked_points) == 4:
            # Draw the final closing line (Bottom-Left to Top-Left)
            line_close, = ax.plot([x, clicked_points[0][0]], 
                                    [y, clicked_points[0][1]], 
                                    '-', color='lime', linewidth=2, zorder=4)
            
            # Fill the shape
            poly = patches.Polygon(clicked_points, closed=True, 
                                   linewidth=2, edgecolor='lime', 
                                   facecolor='lime', alpha=0.25, zorder=3)
            ax.add_patch(poly)
            ax.set_title('ROI Selected! Check terminal for values.', color='lime', fontweight='bold')
            fig.canvas.draw()
            
            # Print the values ready for your traffic logic
            print('\n' + '='*50)
            print('  COPY THESE VALUES (CLOCKWISE ORDER):')
            print('='*50)
            print(f'  ROI_TL_X = {round(clicked_points[0][0]/W, 4)}  # Top-Left')
            print(f'  ROI_TL_Y = {round(clicked_points[0][1]/H, 4)}')
            print(f'  ROI_TR_X = {round(clicked_points[1][0]/W, 4)}  # Top-Right')
            print(f'  ROI_TR_Y = {round(clicked_points[1][1]/H, 4)}')
            print(f'  ROI_BR_X = {round(clicked_points[2][0]/W, 4)}  # Bottom-Right')
            print(f'  ROI_BR_Y = {round(clicked_points[2][1]/H, 4)}')
            print(f'  ROI_BL_X = {round(clicked_points[3][0]/W, 4)}  # Bottom-Left')
            print(f'  ROI_BL_Y = {round(clicked_points[3][1]/H, 4)}')
            print('='*50)

    fig.canvas.draw()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.tight_layout()
plt.show()