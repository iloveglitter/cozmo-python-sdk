#!/usr/bin/env python3

# Copyright (c) 2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''This example demonstrates how you can define custom objects.

The example defines a custom cube, wall and box. When Cozmo sees the markers
for those objects he will assume an object of that size and shape is there,
and report the object as being observed.
'''

import time

import cozmo
from cozmo.objects import CustomObjectMarkers, CustomObjectTypes


def custom_objects(robot: cozmo.robot.Robot):

    # define a unique cube (100mm x 100mm x 100mm) with a 90mm x 90mm Diamonds2 image on every face
    cube_obj = robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                              CustomObjectMarkers.Diamonds2,
                                              100,
                                              90, 90, True)
    print("Defined cube %s" % cube_obj)

    # define a unique wall (100mm x 100mm (x10mm thick for all walls)) with a 90mm x 90mm Circles2 image on front and back
    wall_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType00,
                                              CustomObjectMarkers.Circles2,
                                              100, 100,
                                              90, 90, True)
    print("Defined wall %s" % wall_obj)

    # define a unique box (120mm x 110mm x100mm thick for all walls) with a different 90mm x 90mm image on each of the 6 faces
    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType01,
                                            CustomObjectMarkers.Hexagons2, CustomObjectMarkers.Circles3,    # front back
                                            CustomObjectMarkers.Circles4, CustomObjectMarkers.Circles5,     # top bottom
                                            CustomObjectMarkers.Triangles2, CustomObjectMarkers.Triangles3, # left right
                                            120, 110, 100,
                                            90, 90, True)
    print("Defined box %s" % box_obj)

    print("Show the above icons to Cozmo and you will see the related object ID specified in Cozmo's view window")

    print("Press CTRL-C to quit")
    while True:
        time.sleep(.1)


cozmo.run_program(custom_objects, use_viewer=True, force_viewer_on_top=True)