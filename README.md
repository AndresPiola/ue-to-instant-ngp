
# forked instant-ngp for Unreal Engine workflow
 This version is modified so it can connect with unrea engine using sockets. The flow works this way
 

 1. Unreal project stablish comunication iwht instant ngp
 2. Unreal send the active camera view
 3. Instant ngp translate  the camera matrix values to instant-ngp camera matrix system
 4. Instant-ngp intercept opengl buffer draw so it creates a render image with the new camera values
 5. Instant ngp send that png image to unreal
 6. Unreal receives the ong image and convert it to texture
 
 This work is made available under the Nvidia Source Code License-NC. Click [here](LICENSE.txt) to view a copy of this license.
