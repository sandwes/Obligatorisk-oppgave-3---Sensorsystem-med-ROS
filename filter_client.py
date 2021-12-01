#!/usr/bin/env python
# Node som abonnerer på fpmg_raw og forespør den filtrerte verdien av service do_filter_calc.
import rospy
from sensordata.srv import do_filter_calc, do_filter_calcResponse
from sensordata.msg import RawValue
from sensordata.msg import FilteredValue


def publish_to_visualizer(pub, filtered_value):
    filtered_value_msg = FilteredValue()
    filtered_value_msg.filtered_value = filtered_value
    pub.publish(filtered_value_msg)


def filter_client(data):
    raw_value = data.raw_value
#     Etter å ha mottatt den filterte verdien blir den publisert som FilteredValue til fpmg_filtered
    filtered_pub = rospy.Publisher('fpmg_filtered', FilteredValue, queue_size=10)

    rospy.wait_for_service("do_filter_calc")
    filter_service = rospy.ServiceProxy("do_filter_calc", do_filter_calc)
    filtered_value = filter_service(raw_value)
    publish_to_visualizer(filtered_pub, filtered_value.filtered_value)

# abonnerer på fpmg_raw
def subscriber():
    rospy.init_node('filter_client', anonymous=True)
    rospy.loginfo("Startet subscription av published raw values...")
    rospy.loginfo("Startet publishing av filtered values...")
    rospy.Subscriber('fpmg_raw', RawValue, filter_client)
    rospy.spin()


if __name__ == '__main__':
    subscriber()
