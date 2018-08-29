import math
import random
import sys

result_str = ''

user_name = 'sou'

outfile_path = 'meiro.world'

args = sys.argv
make_map_x = int(args[1])
make_map_y = int(args[2])

map_cnt = 0

def make_zero_map(x, y):
  l = [0, 0] * x
  result_array = [[[0] * 2 for i in range(x)] for m in range(y)]
  return result_array

# あるx, yの値の床に対して、どっちに床が伸びているかをチェック、床が伸びている先が0なら床を追加し、追加した床に対してこの再帰をかける
# befor_dirは
# 2
#1 3
# 0
def map_re(map_array, before_dir , x, y):
  # floor_type と　next_mapを配列で持つ
  # [[2,1] , [0 , 1, 2]のように
  global map_cnt
  map_cnt += 1

  floor_type_and_next_map = []
  floor_type_and_next_map.append([[1, (1 + before_dir) % 4], [(2 + before_dir) % 4]])
  floor_type_and_next_map.append([[1, (3 + before_dir) % 4], [(2 + before_dir) % 4]])  
  floor_type_and_next_map.append([[2, (1 + before_dir) % 4], [(2 + before_dir) % 4]])
  floor_type_and_next_map.append([[2, (3 + before_dir) % 4], [(2 + before_dir) % 4]])
  floor_type_and_next_map.append([[3, (0 + before_dir) % 4], [(3 + before_dir) % 4]])
  floor_type_and_next_map.append([[3, (1 + before_dir) % 4], [(1 + before_dir) % 4]])
  floor_type_and_next_map.append([[4, (1 + before_dir) % 4], [(2 + before_dir) % 4]])
  floor_type_and_next_map.append([[4, (3 + before_dir) % 4], [(2 + before_dir) % 4]]) 
  floor_type_and_next_map.append([[5, (1 + before_dir) % 4], [(2 + before_dir) % 4]])
  floor_type_and_next_map.append([[5, (3 + before_dir) % 4], [(2 + before_dir) % 4]]) 
  floor_type_and_next_map.append([[6, (1 + before_dir) % 4], [(2 + before_dir) % 4]])
  floor_type_and_next_map.append([[6, (3 + before_dir) % 4], [(2 + before_dir) % 4]]) 
  floor_type_and_next_map.append([[7, (1 + before_dir) % 4], [(2 + before_dir) % 4, (3 + before_dir) % 4]])
  floor_type_and_next_map.append([[7, (2 + before_dir) % 4], [(1 + before_dir) % 4, (3 + before_dir) % 4]]) 
  floor_type_and_next_map.append([[7, (3 + before_dir) % 4], [(1 + before_dir) % 4, (2 + before_dir) % 4]]) 
  floor_type_and_next_map.append([[8, (0 + before_dir) % 4], [0, 1, 2, 3]])

  random_floor_type = random.choice(floor_type_and_next_map)
  # ランダムに決定し、map_arrayを上書き
  if map_array[y][x][0] == 0:
    map_array[y][x] = random_floor_type[0]
  print(map_array)

  for direct in random_floor_type[1]:
    print(direct)
    if direct == 0:
      if y != make_map_y - 1:
        if map_array[y + 1][x][0] == 0:
          map_re(map_array, (direct + 2) % 4, x, y + 1)
    if direct == 1:
      if x != 0:
        if map_array[y][x - 1][0] == 0:
          map_re(map_array, (direct + 2) % 4, x - 1, y)
    if direct == 2:
      if y != 0:
        if map_array[y - 1][x][0] == 0:
          map_re(map_array, (direct + 2) % 4, x, y - 1)
    if direct == 3:
      if x != make_map_x - 1:
        if map_array[y][x + 1][0] == 0:
          map_re(map_array, (direct + 2) % 4, x + 1, y)

while True:
  map_array = []
  map_array = make_zero_map(make_map_x, make_map_y)
  map_re(map_array, 1, 0, 0)
  if map_array[make_map_y - 1][make_map_x - 1][0] != 0:
    break
print(map_cnt)



result_str += '''<?xml version="1.0"?>
<sdf version="1.4">
  <world name="default">
    <model name='ground_plane'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>100</mu>
                <mu2>50</mu2>
              </ode>
              <torsional>
                <ode/>
              </torsional>
            </friction>
            <contact>
              <ode/>
            </contact>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='visual'>
          <transparency>1</transparency>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
    </model>
    <include>
      <uri>model://sun</uri>
    </include>

    <model name="floor">
      <pose>-5 0 -0.4612  0 0 0</pose>
      <static>true</static>
      <link name="body">
        <visual name="visual">
          <geometry>
            <mesh>
               <uri>file:///home/sou/catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/road_meshes/floor.dae</uri>
               <scale>
               '''
result_str += str(10 + make_map_x) + ' ' + str(10 + make_map_y) + ''' 0.5</scale>
               </mesh>
          </geometry>
        </visual>
      </link>
    </model>'''




  

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

result_str += '''
    <light name='user_directional_light_0' type='directional'>
      <pose frame=''>1.50806 1.18329 3 0 -0 0</pose>
      <diffuse>0.5 0.5 0.5 1</diffuse>
      <specular>0.1 0.1 0.1 1</specular>
      <direction>0.1 0.1 -0.9</direction>
      <attenuation>
        <range>20</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
      <grid>false</grid>
      <origin_visual>false</origin_visual>
    </scene>

    <light name='user_directional_light_1' type='directional'>
      <pose frame=''>1.50806 1.18329 3 0 -0 0</pose>
      <diffuse>0.5 0.7 0.5 1</diffuse>
      <specular>0.1 0.1 0.1 1</specular>
      <direction>0.1 0.1 -0.9</direction>
      <attenuation>
        <range>20</range>
        <constant>0.5</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <cast_shadows>1</cast_shadows>
    </light>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
      <grid>false</grid>
      <origin_visual>false</origin_visual>
    </scene>


    <gui fullscreen='0'>
      <camera name='user_camera'>
        <pose frame=''>2.73267 0.822723 '''
result_str += str(10 + make_map_x * 1.5)

result_str += '''-1e-06 1.5538 1.56418</pose>
        <view_controller>orbit</view_controller>
        <projection_type>perspective</projection_type>
      </camera>
    </gui>

  </world>
</sdf>'''

#print(result_str)
with open(outfile_path, mode='w') as f:
  f.write(result_str)
