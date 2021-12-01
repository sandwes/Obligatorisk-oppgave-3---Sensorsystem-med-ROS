#!/usr/bin/env python
# Node som lytter etter requests på do_filter_calc og filtrerer bort verdier >110 og <60.
import rospy
from sensordata.srv import do_filter_calc, do_filter_calcResponse


def filter_callback(request):
    raw_value = request.raw_value
# Filtrerer bort >110
    if raw_value > 110:
        return do_filter_calcResponse(0)
# Filtrerer bort <60
    if raw_value < 60:
        return do_filter_calcResponse(0)
    return do_filter_calcResponse(raw_value)

def start_service():
    rospy.init_node("filter_server")
    rospy.loginfo("Startet server for do_filter_calc service...")
    rospy.Service("do_filter_calc", do_filter_calc, filter_callback)
    rospy.spin()

if __name__ == '__main__':
    start_service()
