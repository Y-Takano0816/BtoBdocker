import subprocess
import time
import signal


try:

    autoware_path = '/home/autoware/Autoware'

    tf_out_file = open('log/tf_out.log', 'w')
    tf_err_file = open('log/tf_err.log', 'w')
    tf_loader = subprocess.Popen('. ' + autoware_path + '/install/setup.sh; roslaunch tf/tf.launch', shell=True, stdout=tf_out_file, stderr=tf_err_file)

    points_map_loader_out_file = open('log/points_map_loader_out.log', 'w')
    points_map_loader_err_file = open('log/points_map_loader_err.log', 'w')
    point_map_loader = subprocess.Popen('. ' + autoware_path + '/install/setup.sh; rosrun map_file points_map_loader noupdate pointcloud_map/0.2-bin/*.pcd', shell=True, stdout=points_map_loader_out_file, stderr=points_map_loader_err_file)

    vector_map_loader_out_file = open('log/vector_map_loader_out.log', 'w')
    vector_map_loader_err_file = open('log/vector_map_loader_err.log', 'w')
    vector_map_loader = subprocess.Popen('. ' + autoware_path + '/install/setup.sh; rosrun map_file vector_map_loader vector_map/Ver1.20/*.csv', shell=True, stdout=vector_map_loader_out_file, stderr=vector_map_loader_err_file)

  #  input('twist_filterノードを起動し、Enterを押してください。')




#ndt_matchingの入力ここから
    rosbag_play = subprocess.Popen(['rosbag', 'play', 'ndt_matching_topics.bag', '/predict_pose:=/predict_pose_test', '/ndt_pose:=/ndt_pose_test', '/localizer_pose:=/localizer_pose_test', '/estimate_twist:=/estimate_twist_test', '/estimated_vel_mps:=/estimated_vel_mps_test', '/estimated_vel_kmph:=/estimated_vel_kmph_test', '/estimated_vel:=/estimated_vel_test', '/time_ndt_matching:=/time_ndt_matching_test', '/ndt_stat:=/ndt_stat_test', '/ndt_reliability:=/ndt_reliability_test'], stdin=subprocess.DEVNULL)
#ndt_matchingの入力ここまで

#ndt_matchingの出力ここから

    predict_pose_test_file = open('result/predict_pose_test', 'w')
    dump_predict_pose_test = subprocess.Popen(['rostopic', 'echo', '/predict_pose_test', '-p'], stdout=predict_pose_test_file)

    predict_pose_file = open('result/predict_pose', 'w')
    dump_predict_pose = subprocess.Popen(['rostopic', 'echo', '/predict_pose', '-p'], stdout=predict_pose_file)

    ndt_pose_test_file = open('result/ndt_pose_test', 'w')
    dump_ndt_pose_test = subprocess.Popen(['rostopic', 'echo', '/ndt_pose_test', '-p'], stdout=ndt_pose_test_file)

    ndt_pose_file = open('result/ndt_pose', 'w')
    dump_ndt_pose = subprocess.Popen(['rostopic', 'echo', '/ndt_pose', '-p'], stdout=ndt_pose_file)

    localizer_pose_test_file = open('result/localizer_pose_test', 'w')
    dump_localizer_pose_test = subprocess.Popen(['rostopic', 'echo', '/localizer_pose_test', '-p'], stdout=localizer_pose_test_file)

    localizer_pose_file = open('result/localizer_pose', 'w')
    dump_localizer_pose = subprocess.Popen(['rostopic', 'echo', '/localizer_pose', '-p'], stdout=localizer_pose_file)

    estimate_twist_test_file = open('result/estimate_twist_test', 'w')
    dump_estimate_twist_test = subprocess.Popen(['rostopic', 'echo', '/estimate_twist_test', '-p'], stdout=estimate_twist_test_file)

    estimate_twist_file = open('result/estimate_twist', 'w')
    dump_estimate_twist = subprocess.Popen(['rostopic', 'echo', '/estimate_twist', '-p'], stdout=estimate_twist_file)

    estimated_vel_mps_test_file = open('result/estimated_vel_mps_test', 'w')
    dump_estimated_vel_mps_test = subprocess.Popen(['rostopic', 'echo', '/estimated_vel_mps_test', '-p'], stdout=estimated_vel_mps_test_file)

    estimated_vel_mps_file = open('result/estimated_vel_mps', 'w')
    dump_estimated_vel_mps = subprocess.Popen(['rostopic', 'echo', '/estimated_vel_mps', '-p'], stdout=estimated_vel_mps_file)

    estimated_vel_kmph_test_file = open('result/estimated_vel_kmph_test', 'w')
    dump_estimated_vel_kmph_test = subprocess.Popen(['rostopic', 'echo', '/estimated_vel_kmph_test', '-p'], stdout=estimated_vel_kmph_test_file)

    estimated_vel_kmph_file = open('result/estimated_vel_kmph', 'w')
    dump_estimated_vel_kmph = subprocess.Popen(['rostopic', 'echo', '/estimated_vel_kmph', '-p'], stdout=estimated_vel_kmph_file)

    estimated_vel_test_file = open('result/estimated_vel_test', 'w')
    dump_estimated_vel_test = subprocess.Popen(['rostopic', 'echo', '/estimated_vel_test', '-p'], stdout=estimated_vel_test_file)

    estimated_vel_file = open('result/estimated_vel', 'w')
    dump_estimated_vel = subprocess.Popen(['rostopic', 'echo', '/estimated_vel', '-p'], stdout=estimated_vel_file)

    time_ndt_matching_test_file = open('result/time_ndt_matching_test', 'w')
    dump_time_ndt_matching_test = subprocess.Popen(['rostopic', 'echo', '/time_ndt_matching_test', '-p'], stdout=time_ndt_matching_test_file)

    time_ndt_matching_file = open('result/time_ndt_matching', 'w')
    dump_time_ndt_matching = subprocess.Popen(['rostopic', 'echo', '/time_ndt_matching', '-p'], stdout=time_ndt_matching_file)

    ndt_stat_test_file = open('result/ndt_stat_test', 'w')
    dump_ndt_stat_test = subprocess.Popen(['rostopic', 'echo', '/ndt_stat_test', '-p'], stdout=ndt_stat_test_file)

    ndt_stat_file = open('result/ndt_stat', 'w')
    dump_ndt_stat = subprocess.Popen(['rostopic', 'echo', '/ndt_stat', '-p'], stdout=ndt_stat_file)

    ndt_reliability_test_file = open('result/ndt_reliability_test', 'w')
    dump_ndt_reliability_test = subprocess.Popen(['rostopic', 'echo', '/ndt_reliability_test', '-p'], stdout=ndt_reliability_test_file)

    ndt_reliability_file = open('result/ndt_reliability', 'w')
    dump_ndt_reliability = subprocess.Popen(['rostopic', 'echo', '/ndt_reliability', '-p'], stdout=ndt_reliability_file)

#ndt_matchingの出力ここまで





    rosbag_play.wait()

except KeyboardInterrupt:
    rosbag_play.send_signal(signal.SIGINT)
    rosbag_play.wait()

finally:
    time.sleep(1)



#ndt_matching

dump_predict_pose_test.send_signal(signal.SIGINT)
dump_predict_pose_test.wait()
predict_pose_test_file.close()

dump_predict_pose.send_signal(signal.SIGINT)
dump_predict_pose.wait()
predict_pose_file.close()

dump_ndt_pose_test.send_signal(signal.SIGINT)
dump_ndt_pose_test.wait()
ndt_pose_test_file.close()

dump_ndt_pose.send_signal(signal.SIGINT)
dump_ndt_pose.wait()
ndt_pose_file.close()

dump_localizer_pose_test.send_signal(signal.SIGINT)
dump_localizer_pose_test.wait()
localizer_pose_test_file.close()

dump_localizer_pose.send_signal(signal.SIGINT)
dump_localizer_pose.wait()
localizer_pose_file.close()

dump_estimate_twist_test.send_signal(signal.SIGINT)
dump_estimate_twist_test.wait()
estimate_twist_test_file.close()

dump_estimate_twist.send_signal(signal.SIGINT)
dump_estimate_twist.wait()
estimate_twist_file.close()

dump_estimated_vel_mps_test.send_signal(signal.SIGINT)
dump_estimated_vel_mps_test.wait()
estimated_vel_mps_test_file.close()

dump_estimated_vel_mps.send_signal(signal.SIGINT)
dump_estimated_vel_mps.wait()
estimated_vel_mps_file.close()

dump_estimated_vel_kmph_test.send_signal(signal.SIGINT)
dump_estimated_vel_kmph_test.wait()
estimated_vel_kmph_test_file.close()

dump_estimated_vel_kmph.send_signal(signal.SIGINT)
dump_estimated_vel_kmph.wait()
estimated_vel_kmph_file.close()

dump_estimated_vel_test.send_signal(signal.SIGINT)
dump_estimated_vel_test.wait()
estimated_vel_test_file.close()

dump_estimated_vel.send_signal(signal.SIGINT)
dump_estimated_vel.wait()
estimated_vel_file.close()

dump_time_ndt_matching_test.send_signal(signal.SIGINT)
dump_time_ndt_matching_test.wait()
time_ndt_matching_test_file.close()

dump_time_ndt_matching.send_signal(signal.SIGINT)
dump_time_ndt_matching.wait()
time_ndt_matching_file.close()

dump_ndt_stat_test.send_signal(signal.SIGINT)
dump_ndt_stat_test.wait()
ndt_stat_test_file.close()

dump_ndt_stat.send_signal(signal.SIGINT)
dump_ndt_stat.wait()
ndt_stat_file.close()

dump_ndt_reliability_test.send_signal(signal.SIGINT)
dump_ndt_reliability_test.wait()
ndt_reliability_test_file.close()

dump_ndt_reliability.send_signal(signal.SIGINT)
dump_ndt_reliability.wait()
ndt_reliability_file.close()

#ndt_matching














