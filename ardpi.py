from program.program import Program
from program.libraries.system import System

try:

    System = System()
    Program = Program()

    print "ArdPi Booting..."

    #System start up program
    System.run()

    #Automation program run just on start up
    Program.startUp()

    #Running the main code
    while True:

        Program.mainProgram()

except:

    while True:

        System.fault()

finally:

    System.cleanUp()
