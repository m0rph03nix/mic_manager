#!/usr/bin/env python

import rospy
from subprocess import Popen
from std_srvs.srv import SetBool, SetBoolResponse
class MicManager():

    def __init__(self):
        print("Launch node MicManager")
        rospy.init_node("MicManager")

        s1 = rospy.Service('mic_capture', SetBool, self.capture)
        
        print("Node Init")
        rospy.spin()

    def capture(self, req):

        sbr = SetBoolResponse()
        sbr.success = True
        
        if req.data == True:
            print('ON')
            sbr.message = "ON"
            Popen("amixer set Capture cap", shell=True)
        else:
            print('OFF')
            sbr.message = "OFF"
            Popen("amixer set Capture nocap", shell=True)
        
        return sbr
     

if __name__ == "__main__":
    MM = MicManager()



