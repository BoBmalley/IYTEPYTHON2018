#A11
text = """
Here we first explain the setup that we have designed for data acquisition. As shown in Fig. 2, 
the transparent object to be captured is placed on Turntable #1. Two cameras are used and both are fixed during 
the capture process. Camera #1 is positioned in front of the transparent object and Camera #2 above it. 
Both cameras have their intrinsic parameters and relative positions calibrated [Zhang 2000]. In addition, 
through putting a checkerboard pattern on the turntable, its rotation axis with respect to the two cameras is also 
calibrated. Similar to the previous work [Qian et al. 2016], a monitor is used as light source. Nonetheless, 
instead of manually moving the monitor during acquisition to capture starting locations and orientations of 
incoming rays, we place the monitor on top of Turntable #2. The monitor’s position can then be precisely and 
automatically adjusted. To start the acquisition, we use Turntable #2 to set the monitor at its first position, 
which is calibrated with the cameras through displaying a checkerboard pattern. At this monitor position, we rotate
the transparent target object using Turntable #1 to observe it from a set of (8 by default) directions that 
evenly sample the 360o viewing angle. At each direction, a series of binary Gray codes are displayed for both 
silhouette extraction [Zongker et al. 1999] and environment matting. The latter allows us to determine the pixel 
location on monitor that corresponds to a given ray refracted by the object and observed by Camera #1.
"""
text=text.lower()
text=text.replace('.',' ')
text=text.replace(',',' ')
text=text.replace('[',' ')
text=text.replace(']',' ')
text=text.replace('#',' ')
text=text.split(' ')
counter = {}
for i in text: counter[i] = counter.get(i, 0) + 1
print(sorted([ (freq,word) for word, freq in counter.items() ], reverse=True)[1:2])
