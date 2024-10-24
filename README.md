# YoloLab

Workstations to run different Yolo Versions based on hardware specifics

- If Host is accessed via SSH for development, remember to open ports
- All containers contains also Jupyter Notebook
- All containers contains OpenCV
- Activating Camera GUI can be tricky if outside of network_mode : 'host'
- If unable to acess camera run  ->  xhost +Local:*
                                     xeyes on host and inside container to check if GUI is working properly
  
 -If problem still persists take a look on articles related to on 'how to allow docker to access host hardware'

Jupyter VERSIONS CAN BE ACCESSED VIA:

V3  : PORT 8093
V5  : PORT 8085
V10 : PORT 8100
V11 : PORT 8111

For other open ports check Dockerfiles

<div><a href="https://hub.docker.com/repositories/josevaldojnr"> Docker HUB Repository</a></div>
