from perspective_transformation import location_transfomation, zone_transfomation, test_in_transform_range, get_transformation_bound
import math
def ob_angle(user, ob, camera_index, groundtruth, orientation):
    center_xy = location_transfomation(user, camera_index)
    ob_xy = location_transfomation(ob, camera_index)
    dy = -1 * (ob_xy[1]-center_xy[1])
    dx = ob_xy[0] - center_xy[0]
    ob_angle = (math.atan2(dy, dx)*180/math.pi - 90)%360
    ob_angle = (ob_angle - orientation)%360
    print(f'{ob_angle}, {groundtruth}, {ob_angle - groundtruth}')


ob_angle((1091,611), (1049, 539), 0, 360, 0) 
ob_angle((1091,611), (893, 545), 0, 45, 0) 
ob_angle((1091,611), (887, 618), 0, 90, 0)
ob_angle((1091,611), (958, 681), 0, 135, 0) 
ob_angle((1091,611), (1139, 689), 0, 180, 0) 
ob_angle((1091,611), (1279, 645), 0, 225, 0) 
ob_angle((1091,611), (1228, 592), 0, 270, 0) 
ob_angle((1091,611), (1182, 538), 0, 315, 0)  


ob_angle((943,371), (931, 351), 0, 0, 0) 
ob_angle((944,378), (851, 355), 0, 45, 0)
ob_angle((944,378), (838, 375), 0, 90, 0) 
ob_angle((944,378), (859, 390), 0, 135, 0) 
ob_angle((944,378), (962, 402), 0, 180, 0) 
ob_angle((944,378), (1064, 391), 0, 225, 0) 
ob_angle((944,378), (1062, 375), 0, 270, 0) 
ob_angle((944,378), (1019, 349), 0, 315, 0) 

print('-------------------')

ob_angle((544,653), (513, 694), 1, 360, 180) 
ob_angle((544,653), (657, 690), 1, 45, 180)
ob_angle((544,653), (682, 650), 1, 90, 180) 
ob_angle((544,653), (647, 619), 1, 135, 180) 
ob_angle((544,653), (569, 597), 1, 180, 180) 
ob_angle((544,653), (423, 622), 1, 225, 180) 
ob_angle((544,653), (355, 661), 1, 270, 180) 
ob_angle((544,653), (366, 706), 1, 315, 180) 

ob_angle((638,491), (617, 517), 1, 360, 180) 
ob_angle((638,491), (714, 508), 1, 45, 180)
ob_angle((638,491), (719, 490), 1, 90, 180) 
ob_angle((638,491), (717, 480), 1, 135, 180) 
ob_angle((638,491), (648, 472), 1, 180, 180) 
ob_angle((638,491), (554, 485), 1, 225, 180) 
ob_angle((638,491), (509, 501), 1, 270, 180) 
ob_angle((638,491), (528, 515), 1, 315, 180) 

print('-------------------')

ob_angle((1359,779), (1252, 624), 2, 360, 0) 
ob_angle((1359,779), (1139, 709), 2, 45, 0)
ob_angle((1359,779), (1141, 801), 2, 90, 0) 
ob_angle((1359,779), (1227, 854), 2, 135, 0) 
ob_angle((1359,779), (1431, 913), 2, 180, 0) 
ob_angle((1359,779), (1596, 833), 2, 225, 0) 
ob_angle((1359,779), (1572, 748), 2, 270, 0) 
ob_angle((1359,779), (1447, 684), 2, 315, 0) 


ob_angle((1173,513), (1141, 463), 2, 0, 0) 
ob_angle((1173,513), (1106, 506), 2, 45, 0)
ob_angle((1173,513), (1091, 522), 2, 90, 0) 
ob_angle((1173,513), (1096, 544), 2, 135, 0) 
ob_angle((1173,513), (1207, 567), 2, 180, 0) 
ob_angle((1173,513), (1276, 538), 2, 225, 0) 
ob_angle((1173,513), (1286, 513), 2, 270, 0) 
ob_angle((1173,513), (1241, 492), 2, 315, 0)



