# Moltemplate-Random-Chains
This repository contains files that can be used with Moltemplate (https://www.moltemplate.org/) to generate datafiles for the molecular dynamics package LAMMPS (https://lammps.sandia.gov/) with randomly oriented chains of spherical particles.

### REQUIREMENTS
To run this program you need to have Moltemplate (https://www.moltemplate.org/) and Python 3 (https://www.python.org/) installed.

### ASSUMPTIONS
The program makes some assumptions about the system that you want to simulate in LAMMPS:
- You're using atom_style "angle"
- The effective diameter of your particles is 1.0 i.e. σ = 1.0
- The equilibrium bond length is 0.5 resulting in partial overlap of the particles and thus a smoother surface.
- You are using a simulation box with a side length equal to 5 times the length of the chains.

If any of the above isn't true for your system you might need to adjust the Python files in the programs directory to make them suitable for your desired system. Please note, that if you choose to use the files without modifications with different particle diameters or bond lengths, the actual volume density might be different than you indicated when running the script.

### HOW TO RUN
You can use the shell script in this folder to run the program. Before you can run this script you have to give the shell permission to execute it. You can do this by running the following command: 
*chmod +x main.sh* 

After setting the permissions you can run the program using the following command:
*./main.sh < NoParticlesPerChain > < VolumeDensity > < DataFileName >*

The parts within <> are arguments that you need to input. You can replace the brackets and the text within them with the desired number of particles per chain and volume density for your system and the filename you want to use for the generated datafile.
