#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from ichthus_can_msgs.msg import Pid
import matplotlib.pyplot as plt
#import numpy as np

plt.figure(figsize=(10, 5))
plt.xlabel("Time")
plt.ylabel("PID Velocity")
base_line = 0
time_line = 0
flag = 0
time_li = []
ctl_li = []

def callback(data):
  global flag, base_line, time_line
  if flag == 0:
    base_line = rclpy.Time()
    flag = 1
  time_line = rclpy.Time()
  time = time_line - base_line
  print("===================")
  print(time.to_msg())
  ctl_li.append(data.data)
  time_li.append(time.to_msg())
  plt.plot(time_li, ctl_li)
  plt.draw()
  plt.pause(0.2)

def main(args=None):
  rclpy.init()
  node = rclpy.create_node("pid_graph")
  node.create_subscription(Pid, "pid_vel", callback, 10)
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()


if __name__ == "__main__":
  main()
