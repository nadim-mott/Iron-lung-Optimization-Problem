import math


def calculate_bearing(x1, y1, x2, y2):
    """
    Calculates the bearing (in degrees) between the point (x1,y1) and (x2,y2) on a 2D grid.
    >>> calculate_bearing(0,0,1,0)
    90.0
    """
    delta_x = x2 - x1
    delta_y = y2 - y1

    angle_rad = math.atan2(delta_x, delta_y)

    angle_degrees = math.degrees(angle_rad)

    bearing = (angle_degrees + 360) % 360

    return bearing


def find_trajectory(coords: list[tuple[float]]) -> list[dict[str, float]]:
    """
    Returns a list where each entry is a dictionary representing a point on a map
    where "x" and "y" correspond to the x and y coordinates respectively and "angle" corresponds to the bearing to
    get to the next point

    >>> find_trajectory([(0,0),(0,1),(1,0)]) == [{'x': 0, 'y': 0, 'angle': 0.0},{'x': 0, 'y': 1, 'angle': 135.0},{'x': 1, 'y': 0, 'angle': 0.0}]
    True
    """
    results = []
    for i in range(0, len(coords) - 1):
        coord = coords[i]
        next_coord = coords[i + 1]
        coord_info = {}
        coord_info["x"] = coord[0]
        coord_info["y"] = coord[1]
        coord_info["angle"] = calculate_bearing(coord[0], coord[1], next_coord[0], next_coord[1])
        results.append(coord_info)
    results.append({"x": coords[-1][0], "y": coords[-1][1], "angle": 0.0})
    return results

def dispay_trajectory(trajectory: list[dict[str,float]]) -> None:
    """Prints the trajectory generated in the format of find_trajectory"""
    for point in trajectory:
        print(f'x:{round(point["x"],2)}, y:{round(point["y"],2)}, angle:{round(point["angle"],2)}')

def steam_guide_table_display(trajectory: list[dict[str,float]]) -> str:
    """Generates a string for the trajectory that turns it into a table in the steam guide"""

    steam_tab = "    "
    table = f"[table]\n    [tr]\n        [th]x[/th]\n        [th]y[/th]\n        [th]angle[/th]\n    [/tr]\n"
    for point in trajectory:
        table += f'{steam_tab}[tr]\n{steam_tab * 2}[th]{round(point["x"],2)}[/th]\n{steam_tab * 2}[th]{round(point["y"],2)}[/th]\n{steam_tab * 2}[th]{round(point["angle"],2)}[/th]\n{steam_tab}[/tr]\n'
    table += "[/table]"
    return table

my_path = [
    (182.30, 116.71),
    (175, 200),
    (300, 200),
    (360, 275),
    (375, 325),
    (562, 325),
    (562, 513),
    (385, 513),
    (365, 550),
    (365, 563),
    (390, 692),
    (575, 692),
    (600, 762),
    (675, 775),
    (675, 828)
    # (<x-coordinate>, <y-coordinate>)
]
dispay_trajectory(find_trajectory(my_path))
