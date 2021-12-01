#!/usr/bin/env python
# Node som leser inn pulsdata som vi laget fra innmåling gjort i forrige obligatoriske oppgave
import rospy
from sensordata.msg import RawValue

def publish_sensordata(pub):
    file = open("/home/ubuntu/oblig3/pulse.csv", "r")
    for line in file:
        raw_value = float(line)
        pub.publish(raw_value)
        rospy.Rate(1).sleep()

# Publiserer hver linje som en Råverdi til fpmg_raw.
def publisher():
    pub = rospy.Publisher('fpmg_raw', RawValue, queue_size=10)
    rospy.init_node('sensordata_publisher', anonymous=True)
    rospy.loginfo("Startet publishing av raw values...")
    while not rospy.is_shutdown():
        publish_sensordata(pub)


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass