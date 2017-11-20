from jointCtlComp import *
from taskCtlComp import *


#Uncomment the individual lines to operate the code.


#P Controller
#jointCtlComp(['P'], 1, 0)


#PD Controller
#jointCtlComp(['PD'], 1, 0)

#PD Controller with gravity compensation
#jointCtlComp(['PD_Grav'], 1, 0)

#PID Controller
#jointCtlComp(['PID'], 1, 0)

#Model Based Controller
#jointCtlComp(['ModelBased'], 1, 0)



##Joint space control for following a fixed trajectory

#P Controller
jointCtlComp(['P'], 0, 0)

#PD Controller
jointCtlComp(['PD'], 0, 0)

#PID Controller
jointCtlComp(['PD_Grav'], 0, 0)

#Model Based Controller
jointCtlComp(['PID'], 0, 0)




##Task space control with a fixed desired position

#Jacobian Transpose Controller
taskCtlComp(['JacTrans'], 0, 'exampleJoint')

#Jacobian Pseudo-Inverse Controller
taskCtlComp(['JacPseudo'], 0, 'exampleJoint')

#Jacobian Damped Pseudo-Inverse Controller
taskCtlComp(['JacDPseudo'], 0, 'exampleJoint')

#Jacobian Pseudo-Inverse Control with Null Space Component
taskCtlComp(['JacNullSpace'], 0, 'exampleJoint')
