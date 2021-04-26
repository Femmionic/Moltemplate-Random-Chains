#Python script to generate a moltemplate file that puts a specified amount of chains in a simulation box.

import sys
import random

#User input
Np = float(sys.argv[1])
VolumeDensity = float(sys.argv[2])

#Fixed parameters
CL = (Np * 0.5) + 0.5                   #Length of the chains assuming a bond length of 0.5 and a particle diameter of 1.0
BoxSideLength = 5*CL
V = BoxSideLength**3                    #Volume of the simulation box
Vc_total = VolumeDensity*V              #Total volume of chains in the system
Vo = 0.1636246174                       #Volume of the overlap between particles when R=0.5 and Lb=0.5
Vc_single = Np*(0.52359878 - Vo)+Vo     #Volume of a single chain of length CL
Nc = int(round(Vc_total/Vc_single))     #Number of chains in the system

#Writing file
f = open("system.lt", "w+")
f.write("import \"chain.lt\"\n")
f.write("\n")
f.write("#Specify the periodic boundary conditions:\n")
f.write("write_once(\"Data Boundary\") {\n")
f.write("    0 " + str(BoxSideLength) + " xlo xhi\n")
f.write("    0 " + str(BoxSideLength) + " ylo yhi\n")
f.write("    0 " + str(BoxSideLength) + " zlo zhi\n")
f.write("}\n")
f.write("\n")

#Generating random angles and positions
for i in range(0, Nc):
    RandomAngle = random.uniform(0, 360)
    Xrot = random.uniform(-1, 1)
    Yrot = random.uniform(-1, 1)
    Zrot = random.uniform(-1, 1)
    Xmove = random.uniform(0, BoxSideLength)
    Ymove = random.uniform(0, BoxSideLength)
    Zmove = random.uniform(0, BoxSideLength)

    f.write("chain" + str(i) + " = new Chain.rot("
    + str(RandomAngle) + ","
    + str(Xrot) + ","
    + str(Yrot) + ","
    + str(Zrot) + ").move("
    + str(Xmove) + ","
    + str(Ymove) + ","
    + str(Zmove) + ")\n"
    )
