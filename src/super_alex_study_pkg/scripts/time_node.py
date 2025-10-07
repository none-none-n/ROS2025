#!/usr/bin/env python
import rospy
import datetime
import time

def time_publisher():
    rospy.init_node('time_publisher', anonymous=True)
    rate = rospy.Rate(0.2)  # 0.2 Hz = каждые 5 секунд
    
    while not rospy.is_shutdown():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rospy.loginfo("Текущее время: %s", current_time)
        rate.sleep()

if __name__ == '__main__':
    try:
        time_publisher()
    except rospy.ROSInterruptException:
        pass
