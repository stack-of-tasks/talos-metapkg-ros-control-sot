#!/usr/bin/env python
# license removed for brevity
import rospy
from dynamic_graph_bridge_msgs.msg import Vector
from sensor_msgs.msg import JointState

rospy.init_node('sot_reemitter', anonymous=True)
pub = rospy.Publisher('/sot/joint_state', String, queue_size=10)
    
aJS = JointState()
   
def jointreceived(jstates):
    aJS.header.seq = seqnb
    pub.publish(hello_str)
    seqnb = seqnb+1
    seqnb.stamp = ros::Time::now()
    seqnb.frameid = "base_link"
    seqnb.name = "joint_state"
    seqnb.position = jstates.data[6:]
    seqnb.velocity = []
    seqnb.effort = []

def listener():
    rospy.Subscriber("/sot_hpp/state", Vector, jointreceived)
    ros.spin()
    
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
    
