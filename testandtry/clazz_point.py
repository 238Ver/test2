import sys
class Point:
    def __init__(self,object1,object2,object3,object4):
        # self.__point_id = object1
        self.__motion_state = object1
        self.__type = object2
        self.__position_longitudinal_distance = object3
        self.__position_lateral_distance = object4

    # @property
    # def points_(self):
    #     return self.__points

    # @property
    # def point_id(self):
    #     return self.__point_id

    @property
    def motion_state(self):
        return self.__motion_state

    @property
    def type(self):
        return self.__type

    @property
    def position_longitudinal_distance(self):
        return self.__position_longitudinal_distance

    @property
    def position_lateral_distance(self):
        return self.__position_lateral_distance

    # @point_id.setter
    # def point_id(self, value):
    #     self.__point_id= value

    @motion_state.setter
    def motion_state(self, value):
        self.__motion_state = value

    @type.setter
    def type(self, value):
        self.__type = value

    @position_longitudinal_distance.setter
    def postion_longitudinal_distance(self, value):
        self.__position_longitudinal_distance = value

    @position_lateral_distance.setter
    def postion_lateral_distance(self, value):
        self.__position_lateral_distance = value

#
# liming = Point(2,0,7.985663890838623,-4.787961483001709)
#
# print(liming.motion_state ,liming.type , liming.position_longitudinal_distance , liming.position_lateral_distance)
