#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from ichthus_can_msgs.msg import Pid
from std_msgs.msg import Float32
import matplotlib.pyplot as plt
#import numpy as np

plt.figure(figsize=(10, 5))
plt.xlabel("Time")
plt.ylabel("PID Velocity")

class Pid_graph(Node):

  def __init__(self):
    super().__init__("pid_graph")
    self.node = self.create_subscription(Pid, "pid_vel", self.callback, 10)
    self.node2 = self.create_subscription(Float32, "flo", self.callback2, 10)
    self.start_time = rclpy.clock.Clock().now()
    self.time_axis = []
    self.pid_axis = []
    self.node
    self.node2

  def callback(data):
    global plt
    arrive_time = rclpy.clock.Clock().now()
    time = arrive_time - self.start_time
    print(time)
    self.pid_axis.append(data.data)
    self.time_axis.append(time)
    plt.plot(self.time_axis, self.pid_axis)
    plt.draw()
    plt.pause(0.2)

  def callback2(data):
    print(data.data)

def main(args=None):
  rclpy.init(args=args)
  pid_graph = Pid_graph()
  plt.show()

  rclpy.spin(pid_graph)

  pid_graph.destroy_node()
  rclpy.shutdown()


if __name__ == "__main__":
  main()
