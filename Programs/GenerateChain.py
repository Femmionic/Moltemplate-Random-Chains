#Python script to generate a moltemplate file containing a chain of user specified length.

import sys

#User input
CL = int(sys.argv[1])

#Writing file
f = open("chain.lt", "w+")
f.write("import \"forcefield.lt\" #contains force-field parameters\n")
f.write("\n")
f.write("Chain inherits ForceField {\n")
f.write("\n")
f.write("    write(\"Data Atoms\") {\n")
f.write("       #atomID   molID  atomType  x     y     z\n")
for x in range(0, CL):
    f.write("        $atom:P" + str(x) + " $mol:. @atom:P 0.000 0.000 " + str(x) + ".000\n")
f.write("     }\n")
f.write("    write(\"Data Bonds\") {\n")
f.write("       #bondID   bondType atomID1  atomID2\n")
for x in range(0, CL-1):
    f.write("        $bond:B" + str(x) + " @bond:B $atom:P" + str(x) + " $atom:P" + str(x+1) + "\n")
f.write("     }\n")
f.write("}\n")
