#!/usr/bin/env python

import rclpy
import time
from rclpy.node import Node
from ichthus_can_msgs.msg import Pid
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
import matplotlib.pyplot as plt


class Pid_graph(Node):

  def __init__(self):
    super().__init__("pid_graph")
    self.ref_subs = self.create_subscription(
      Float64, "ref_vel", self.ref_callback, 10)
    self.whl_spd_subs = self.create_subscription(
      Float64MultiArray, "WHL_SPD11", self.whl_callback, 10)
    self.start_time = time.time()
    self.whl_spd_axis = []
    self.whl_time_axis = []
    self.ref_vel = 0
    self.ref_subs
    self.fig = plt.figure()

  def whl_callback(self, data): 
    arrive_time = time.time()
    time_index = arrive_time - self.start_time
    curr_spd = 0
    idx = 0
    for idx in range (4):
      curr_spd = curr_spd + data.data[idx]
    curr_spd = curr_spd / 4
    self.whl_spd_axis.append(curr_spd)
    self.whl_time_axis.append(time_index)

    #plt.yscale('linear')
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Wheel Velocity", fontsize=14)
    plt.axhline(self.ref_vel, color="red", linestyle="-", label="Ref")
    plt.legend()
    plt.plot(self.whl_time_axis, self.whl_spd_axis, color="black")
    plt.draw()
    plt.pause(0.2)
    self.fig.clear()

  def ref_callback(self, data):
    self.ref_vel = data.data


def main(args=None):
  rclpy.init(args=args)
  pid_graph = Pid_graph()

  rclpy.spin(pid_graph)

  pid_graph.destroy_node()
  rclpy.shutdown()


if __name__ == "__main__":
  main()
