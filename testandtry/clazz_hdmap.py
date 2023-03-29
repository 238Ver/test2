import sys

class HdMap:
    def __init__(self, object1, object2, object3, object4, object5, object6, object7, object8
                 ,object9, object10, object11, object12, object13, object14, object15, object16,object17):
        self.__linkid = object1
        self.__link_length= object2
        self.__type = object3
        # self.__laneatrr = object4
        # self.__lines = object5
        self.__ground_markings = object6
        self.__traffic_light = object7
        # self.traffic_info
        self.__complex_intersection = object9
        self.__successive_link_ids = object10
        self.__is_routing_path = object11
        self.__split_merge_list = object12
        self.__grade = object13
        self.__is_in_tunnel = object14
        self.__is_in_toll_booth = object15
        self.__is_in_certified_road = object16
        self.is_in_odd = object17

    @property
    def linkid(self):
        return self.__linkid

    @property
    def link_length(self):
        return self.__link_length

    @property
    def type(self):
        return self.__type

    @property
    def lane_attributelists(self):
        pass

    @property
    def lines(self):
        pass

    @property
    def ground_markings(self):
        return self.__ground_markings

    @property
    def traffic_light(self):
        return self.__traffic_light

    @property
    def traffic_info(self):
        pass

    @property
    def complex_intersection(self):
        return self.__complex_intersection

    @property
    def successive_link_ids(self):
        return self.__successive_link_ids

    @property
    def is_routing_path(self):
        return self.__is_routing_path

    @property
    def split_merge_list(self):
        return self.__split_merge_list

    @property
    def grade(self):
        return self.__grade

    @property
    def is_in_tunnel(self):
        return self.__is_in_tunnel

    @property
    def is_in_toll_booth(self):
        return self.__is_in_toll_booth

    @property
    def is_in_certified_road(self):
        return self.__is_in_certified_road

    @property
    def is_in_odd(self):
        return self.__is_in_odd

    @linkid.setter
    def linkid(self, value):
        self.__linkid = value

    @link_length.setter
    def link_length(self, value):
        self.__link_length = value

    @type.setter
    def type(self, value):
        self.__type = value

    @ground_markings.setter
    def ground_markings(self, value):
        self.__ground_markings = value

    @traffic_info.setter
    def traffic_info(self,value):
        self.__traffic_info = value

    @lane_attributelists.setter
    def lane_attributelists(self, value):
        pass

    @lines.setter
    def lines(self, value):
        pass

    @traffic_light.setter
    def traffic_light(self, value):
        self.__traffic_light = value

    @complex_intersection.setter
    def complex_intersection(self, value):
        self.__complex_intersection = value

    @successive_link_ids.setter
    def successive_link_ids(self, value):
        self.__successive_link_ids = value

    @is_routing_path.setter
    def is_routing_path(self, value):
        self.__is_routing_path = value

    @split_merge_list.setter
    def split_merge_list(self, value):
        self.__split_merge_list = value

    @grade.setter
    def grade(self, value):
        self.__grade = value

    @is_in_tunnel.setter
    def is_in_tunnel(self, value):
        self.__is_in_tunnel = value

    @is_in_toll_booth.setter
    def is_in_toll_booth(self, value):
        self.__is_in_toll_booth = value

    @is_in_certified_road.setter
    def is_in_certified_road(self, value):
        self.__is_in_certified_road = value

    @is_in_odd.setter
    def is_in_odd(self, value):
        self.__is_in_odd = value
#
# liming = Point(2,0,7.985663890838623,-4.787961483001709)
#
# print(liming.motion_state ,liming.type , liming.position_longitudinal_distance , liming.position_lateral_distance)