import sys

# routes_input = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
# "U62,R66,U55,R34,D71,R55,D58,R8"]
# routes_input = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
routes_input = [
    "R1004,D53,L10,U126,R130,U533,R48,D185,L768,U786,L445,U694,L659,D237,R432,\
    U147,R590,U200,R878,D970,L308,D134,R617,U431,L631,D548,L300,D509,R660,U698,\
    L958,U170,R572,U514,R387,D385,L670,D374,R898,U870,L545,D262,L699,D110,R58,\
    D84,R77,D58,L891,U9,R320,D914,L161,D148,L266,D334,R442,D855,R349,D618,R272,\
    U514,R584,D269,R608,U542,L335,U855,L646,D678,R720,U325,L792,U60,L828,D915,\
    L487,D253,L911,U907,R392,D981,R965,D725,R308,D574,L997,D332,L927,D855,R122,\
    D5,L875,D336,L395,U697,R806,U420,R718,D575,L824,U397,L308,D988,L855,U332,\
    R838,U853,L91,U778,R265,U549,L847,D665,L804,D768,L736,D201,L825,U87,L747,\
    D375,L162,U336,R375,U754,R468,U507,R256,D107,L79,U871,L155,D667,L448,D847,\
    L193,U263,R154,U859,R696,D222,R189,D307,R332,U522,L345,D961,L161,U274,L122,\
    U931,L812,D852,R906,D269,R612,D723,L304,U944,R64,D20,R401,D260,L95,U278,\
    R128,U637,L554,D650,L116,D720,R12,D434,R514,U379,L899,D359,R815,D843,L994,\
    U775,R63,D942,R655,D91,L236,U175,L813,D572,R520,U812,L657,D935,L886,D178,\
    R618,U260,R7,D953,L158,D471,R309,D858,R25,U746,R40,U832,L544,D311,R122,\
    D224,L281,D699,R147,D310,R659,D662,L990,U160,L969,D335,L923,U201,R336,D643,\
    R226,D91,R88,U350,L303,U20,L157,U987,L305,U766,R253,D790,R977,U482,R283,\
    U793,R785,D799,L511,D757,L689,D841,L233,U742,L551,D466,R66,U579,L18,U838,\
    R554,D143,L996,U557,L783,D799,R36,D563,L244,U440,L8,D945,L346,D747,L769,\
    U661,L485,U965,L569,U952,R57,U773,L267,U453,R424,U66,R763,U105,R285,D870,\
    L179,U548,L46,U914,L251,U194,L559,U736,R768,D917,R617,D55,R185,D464,L244",
    "L1005,D527,R864,D622,R482,D647,R29,U459,R430,D942,R550,D163,L898,U890,\
    L271,D216,L52,U731,R715,U925,L614,U19,R687,D832,L381,U192,L293,D946,L642,\
    D2,L124,U66,R492,U281,R181,U624,R294,U767,R443,U424,R241,D225,R432,D419,\
    L647,U290,L647,D985,L694,D777,L382,D231,R809,D467,L917,D217,R422,U490,\
    L873,D537,R176,U856,L944,D875,L485,D49,R333,D220,L354,U789,R256,D73,R905,\
    U146,R798,D429,R111,D585,L275,D471,R220,D619,L680,U757,R580,U497,L620,U753,\
    R58,U574,L882,U484,R297,D899,L95,D186,R619,D622,R65,U714,L402,U950,R647,\
    D60,L659,U101,L917,D736,L531,U398,R26,U134,R837,U294,R364,D55,R254,D999,\
    R868,U978,R434,U661,R362,D158,L50,D576,L146,D249,L562,D433,R206,D376,L650,\
    U285,L427,D406,L526,D597,R557,U554,L463,D157,L811,U961,R648,D184,L962,U695,\
    R138,U661,L999,U806,L413,U54,L865,U931,L319,U235,L794,D12,L456,D918,L456,\
    U214,L739,D772,R90,D478,R23,D658,R919,D990,L307,D534,L40,D324,L4,U805,L605,\
    U534,R727,U452,R733,D416,L451,U598,R215,D545,L563,D222,L295,D669,R706,U11,\
    R44,D392,L518,D437,L634,U874,L641,U240,L11,D279,L153,U601,L238,U924,L292,\
    D406,L360,D203,R874,D506,R806,U9,R713,D891,L587,U538,L867,D637,R889,U186,\
    R728,D672,R573,U461,R222,D703,R178,U336,L896,D924,L445,D365,L648,U3,L734,\
    U959,R344,U314,R331,D929,L364,D937,L896,D191,R218,U256,L975,D506,R510,D392,\
    R878,U896,L177,U4,R516,D873,R57,D530,R140,D827,L263,U848,L88,U309,L801,\
    U670,R874,D358,L49,D259,L188,U419,R705,D498,R496,U576,R808,D959,L861,U437,\
    L618,D112,R725,D546,R338,U879,R522,U892,R230,D367,R901,D737,L942,D689,R976,\
    D369,R157",
]

route_instructions = []
routes = []
# Parse input data
for route in routes_input:
    route_instructions.append(
        [(r.strip()[0], int(r.strip()[1:])) for r in route.split(",")]
    )

# Convert to coordinates (starting point being 0,0)
for route in route_instructions:
    current_route = [(0, 0)]
    for direction, length in route:
        coord_x, coord_y = current_route[-1]
        if direction == "U":
            coord_y += length
        elif direction == "D":
            coord_y -= length
        elif direction == "L":
            coord_x -= length
        elif direction == "R":
            coord_x += length

        current_route.append((coord_x, coord_y))

    routes.append(current_route)

# Draw the lines into the coordinate system
grid = {}
intersections = []
for route_index, route in enumerate(routes):
    for index, route_coord in enumerate(route):
        if index < len(route) - 1:
            next_coord = route[index + 1]

            if route_coord[0] == next_coord[0]:
                # Vertical line
                if route_coord[1] > next_coord[1]:
                    direction = -1
                else:
                    direction = 1

                for y_range in range(route_coord[1], next_coord[1], direction):
                    add_coord = (route_coord[0], y_range)
                    if grid.get(add_coord):
                        grid[add_coord] = "X"
                        intersections.append(add_coord)
                    else:
                        grid[add_coord] = route_index + 1
            else:
                # Horizontal line
                if route_coord[0] > next_coord[0]:
                    direction = -1
                else:
                    direction = 1
                for x_range in range(route_coord[0], next_coord[0], direction):
                    add_coord = (x_range, route_coord[1])
                    if grid.get(add_coord):
                        grid[add_coord] = "X"
                        intersections.append(add_coord)
                    else:
                        grid[add_coord] = route_index + 1

grid[(0, 0)] = "o"
intersections.remove((0, 0))

# Calculate distances for intersections
distances = {c: abs(c[0]) + abs(c[1]) for c in intersections}
closest = min(distances.items(), key=lambda item: item[1])

# Plot everything, just for the sake of it
x_min = min(grid, key=lambda item: item[0])[0]
x_max = max(grid, key=lambda item: item[0])[0]
y_min = min(grid, key=lambda item: item[1])[1]
y_max = max(grid, key=lambda item: item[1])[1]

# print(grid)
if len(sys.argv) > 1 and sys.argv[1] == "draw":
    for y_coord in range(y_max + 3, y_min - 2, -1):
        for x_coord in range(x_min - 2, x_max + 3):
            print(grid.get((x_coord, y_coord), "."), end="")
            if x_coord == x_max + 2:
                print("")

print(f"\nMatrix size: {x_max -2} x {y_max - 2}")
print(f"{len(intersections)} intersections")
print(f"Closest intersection is distance is {closest}")
