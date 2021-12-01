#!/usr/bin/env python
# Node som abonnerer på fpmg_raw og fpmg_filtered
import rospy
from sensordata.msg import RawValue
from sensordata.msg import FilteredValue
# Bruker matplotlib for å plotte data i en bildefil i package-mappen.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class visualizer:
    def __init__(self):
        self.raw_values = []
        self.raw_values_indexes = []
        self.filtered_values = []
        self.filtered_values_indexes = []

    def receive_raw_value(self, data):
        self.raw_values.append(data.raw_value)
        self.raw_values_indexes.append(len(self.raw_values_indexes))

        if len(self.raw_values_indexes) % 5 == 0:
            self.visualize()

    def receive_filtered_value(self, data):
        if data.filtered_value == 0:
            return

        self.filtered_values.append(data.filtered_value)
        self.filtered_values_indexes.append(len(self.filtered_values_indexes))

    def start_subscription(self):
        rospy.init_node('visualizer', anonymous=True)
        rospy.loginfo("Startet visualisering av data")
        rospy.Subscriber('fpmg_raw', RawValue, self.receive_raw_value)
        rospy.Subscriber('fpmg_filtered', FilteredValue, self.receive_filtered_value)
        rospy.spin()

    def visualize(self):
        plt.plot(self.raw_values_indexes, self.raw_values, color='r', linestyle='dashed', label="Raw values")

        plt.plot(self.filtered_values_indexes, self.filtered_values, color='g', linestyle='dashed', label="Filtered values")
        plt.xlabel('Indeks')
        plt.ylabel('Puls')
        plt.legend()
        plt.savefig('/home/ubuntu/oblig3/raw_and_filtered_values.png')
        rospy.loginfo("-----Lagret figur-----")

if __name__ == '__main__':
    visualizer = visualizer()
    visualizer.start_subscription()
