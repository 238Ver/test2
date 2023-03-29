class VehicleDrivingInfo:
    class ObjsFusObjs:
        pass

    esp_yaw_rate_stp_motion = 0
    esp_vehicle_speed_stp_motion = 0
    esp_lat_accel_stp_motion = 0
    esp_long_accel_stp_motion = 0
    sas_steering_angle_stp_motion = 0

    class LinesFusLines:
        pass

    vehicle_pos_lng_hdmap = 0
    vehicle_pos_lat_hdmap = 0
    vehicle_pos_current_link_id_hdmap = 0
    vehicle_pos_current_lane_num_hdma = 0
    path_planning_routing_path_hdmap = 0
    lane_curvature_100m_hdmap = 0
    lane_curvature_200m_hdmap = 0
    lane_curvature_300m_hdmap = 0

    class LinkListHdMap:
        pass

    imageData_image_rawdata_fc = None  # 图片数据,部分数据有

    timestamp_location = 0
    heading_location = 0
    latitude_location = 0
    longitude_location = 0
    altitude_location = 0
    bcm_turn_light_switch_sts_bcmlight = 0

    class PointsFreeSpaceFc:
        pass
