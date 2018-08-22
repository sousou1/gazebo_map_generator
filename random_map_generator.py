import math
import random

result_str = ''

user_name = 'sou'

map_array = []


outfile_path = 'output_random.txt'

make_map_x = 10
make_map_y = 10

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
  floor_type_and_next_map.append([[3, before_dir], [(3 + before_dir) % 4]])
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
  floor_type_and_next_map.append([[8, before_dir], [(0 + before_dir) % 4, (1 + before_dir) % 4, (2 + before_dir) % 4, 3]])

  random_floor_type = random.choice(floor_type_and_next_map)
  # ランダムに決定し、map_arrayを上書き
  if map_array[y][x][0] == 0:
    map_array[y][x] = random_floor_type[0]

  for direct in random_floor_type[1]:
    if direct == 0:
      try:
        if map_array[y - 1][x][0] == 0:
          map_re(map_array, (direct + 2) % 4, x, y - 1)
      except:
        None
    if direct == 1:
      try:
        if map_array[y][x - 1][0] == 0:
          map_re(map_array, (direct + 2) % 4, x - 1, y)
      except:
        None
    if direct == 2:
      try:
        if map_array[y + 1][x][0] == 0:
          map_re(map_array, (direct + 2) % 4, x, y + 1)
      except:
        None
    if direct == 3:
      try:
        if map_array[y][x + 1][0] == 0:
          map_re(map_array, (direct + 2) % 4, x + 1, y)
      except:
        None

map_array = make_zero_map(make_map_x, make_map_y)
map_re(map_array, 1, 5, 5)
print(map_array)
print(map_cnt)








  

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


#print(result_str)
with open(outfile_path, mode='w') as f:
  f.write(result_str)
