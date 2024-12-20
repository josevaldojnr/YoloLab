# YoloLab

Workstations to run different Yolo Versions based on hardware specifics

1 --> Clone Repository<br>
2 --> Install <a href="https://docs.docker.com/manuals/">Docker</a><br>
3 --> Install <a href="https://docs.docker.com/manuals/">Docker Compose</a><br>
4 --> run <code>sudo docker-compose up --build -d</code> at the <code>docker-compose.yml</code> directory<br>



 - If Host is accessed via SSH for development, remember to open ports
 - All containers contains also Jupyter Notebook
 - All containers also have OpenCV
 - Activating Camera GUI can be tricky if outside of <code>network_mode : "host"</code>
 - If unable to acess camera run  ->  <code>xhost +Local:*</code>

 run -> <code>xeyes</code> on host and inside container to check if GUI is working properly
  
 -If problem still persists take a look on articles related to on 'how to allow docker to access host hardware'

Jupyter VERSIONS CAN BE ACCESSED VIA:

<code>V3  : PORT 8093</code><br>
<code>V5  : PORT 8095</code><br>
<code>V10 : PORT 8100</code><br>
<code>V11 : PORT 8111</code><br>

For other open ports check Dockerfiles

<div><a href="https://hub.docker.com/repositories/josevaldojnr"> Docker HUB Repository</a></div>
