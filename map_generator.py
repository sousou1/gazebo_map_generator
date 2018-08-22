import math

result_str = ''

user_name = 'sou'

map_array = [[[3, 3], [1, 0]],
[[2, 1], [0, 0]]]

# 二次元で指定
# [[2,1], [3,2], [4,1], [5,1]] [[3,2], [4,1], [0,0], [2,3]]
# 一つ目でmapデータの種類(road1~8) 2つ目で回転角(1がデータそのままで、1増えるごとに右回り)

y_count = 0
for y in map_array:
	y_count += 1

y_middle = int(y_count / 2)

y_count = 0
road_count = 1
for y in map_array:
  x_count = 0
  for x in y:
    if x[0] != 0:
      result_str += '''
    <model name="road''' + str(road_count) + '''">
      <pose>''' + str(x_count) + ' ' + str(y_middle - y_count) + ' ' + '0  0 0 ' + "{0:.5f}".format(1.57079 - x[1] * 1.57079) + '''</pose>
      <static>true</static>
      <link name="body">
        <visual name="visual">
          <geometry>
            <mesh>
               <uri>file:///home/''' + user_name + '/catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/road_meshes/road'
      result_str += str(x[0]) + '''.dae</uri>
               <scale>0.5 0.5 0.5</scale>
               </mesh>
          </geometry>
        </visual>
      </link>
    </model>'''
    road_count += 1
    x_count += 1
  y_count += 1

print(result_str)

outfile_path = 'output_map.txt'

with open(outfile_path, mode='w') as f:
  f.write(result_str)
