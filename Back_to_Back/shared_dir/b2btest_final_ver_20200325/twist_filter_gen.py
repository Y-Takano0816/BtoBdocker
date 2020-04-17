import subprocess
import sys

if len(sys.argv) < 2:
        print('ERROR: 引数にAutowareのPathを指定してください')
        exit()
source_bag = sys.argv[1] #テストしたいAutowareのPathを取得

# subprocess.run(('rosbag', 'filter', source_bag, 'twist_filter_topics.bag', 'topic == \'/config/twist_filter\' or topic == \'/twist_raw\' or topic == \'/twist_cmd\''))

# subprocess.run(('rosbag', 'filter', 'all_topics_01.bag', 'twist_filter_topics.bag', 'topic == \'/config/twist_filter\' or topic == \'/twist_raw\' or topic == \'/twist_cmd\''))

# subprocess.run(('rosbag', 'filter', 'all_topics_01.bag', 'pure_pursuit_topics.bag', 'topic == \'/current_velocity\' or topic == \'/config/waypoint_follower\' or topic == \'/current_pose\' or topic == \'/final_waypoints\' or topic == \'/next_target_mark\' or topic == \'/ctrl_cmd\' or topic == \'/twist_raw\' or topic == \'/trajectory_circle_mark\''))

subprocess.run(('rosbag', 'filter', source_bag, 'ndt_matching_topics.bag', 'topic == \'/config/ndt\' or topic == \'/gnss_pose\' or topic == \'/points_map\' or topic == \'/initialpose\' or topic == \'/filtered_points\''))


# publish: [/predict_pose, /ndt_pose, /localizer_pose,
#     /estimate_twist, /estimated_vel_mps, /estimated_vel_kmph, /estimated_vel, /time_ndt_matching,
#     /ndt_stat, /ndt_reliability]
#   subscribe: [/config/ndt, /gnss_pose, /points_map, /initialpose, /filtered_points]