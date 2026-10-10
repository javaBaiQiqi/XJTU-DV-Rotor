from utils.io.psee_loader import PSEELoader
import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Times New Roman'
Class = "Outer"
file = f'angle1_{Class}_1000.dat'
file_path = rf'E:\MSSP_Experiment\XJTU-DV-Rotor\Data\{Class}\{file}'  # The file path of the dynamic vision data (.dat format)

event_time = 1.8e5  # Select the time duration of dynamic vision data to be extracted
video = PSEELoader(file_path)  # Read the dynamic vision data file
events = video.load_delta_t(event_time)  # Extract data within the selected time window event_time
events['t'].sort()  # Sort event data by timestamp
# Oral_event_samples_clip = [event for event in tqdm(events, desc='Time interception') if 3.1e6 <= event['t'] <=4.8e6]  # Further extract the valid event stream

Img_pos = np.zeros(shape=(480, 640))
for event in events:
    if event['p'] == 1:
        Img_pos[event['y'], event['x']] = 1

plt.figure()
plt.imshow(Img_pos)
plt.savefig(f"fig/{file}.png")
plt.show()

