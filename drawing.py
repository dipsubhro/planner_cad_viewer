import ezdxf
import math
from ezdxf.enums import TextEntityAlignment

def create_lifting_plan_drawing(filename, params, results):
    doc = ezdxf.new()
    msp = doc.modelspace()

    load_length = params.get("Load Length", 10) or 10
    load_width = params.get("Load Width", 2) or 2
    load_height = params.get("Load Height", 2)
    num_slings = params.get("Number of Slings", 4)
    sling_length = params.get("Sling Length", 5)

    cog_x = results.get("Center of Gravity (X)", load_length / 2)
    cog_y = results.get("Center of Gravity (Y)", load_width / 2)
    sling_angle = results.get("Sling Angle", 0)
    sling_tension = results.get("Sling Tension", 0)
    crane_utilization = results.get("Crane Utilization", 0)

    load_points = [
        (0, 0),
        (load_length, 0),
        (load_length, load_width),
        (0, load_width),
        (0, 0)
    ]
    msp.add_lwpolyline(load_points)
    
    msp.add_circle((cog_x, cog_y), radius=0.1, dxfattribs={'color': 1})
    msp.add_text("COG", dxfattribs={'height': 0.25, 'color': 1}).set_placement(
        (cog_x, cog_y + 0.2),
        align=TextEntityAlignment.CENTER
    )

    hook_point_x = cog_x
    hook_point_y = cog_y + sling_length * abs(math.sin(math.radians(sling_angle))) if sling_angle else cog_y + sling_length
    
    attachment_points = []
    if num_slings == 2:
        attachment_points = [(0, cog_y), (load_length, cog_y)]
    elif num_slings == 4:
        attachment_points = [
            (params.get("Sling Attachment Point X1", 0) + load_length/2, params.get("Sling Attachment Point Y1", 0) + load_width/2),
            (params.get("Sling Attachment Point X2", 0) + load_length/2, params.get("Sling Attachment Point Y2", 0) + load_width/2),
            (params.get("Sling Attachment Point X3", 0) + load_length/2, params.get("Sling Attachment Point Y3", 0) + load_width/2),
            (params.get("Sling Attachment Point X4", 0) + load_length/2, params.get("Sling Attachment Point Y4", 0) + load_width/2),
        ]

    for point in attachment_points:
        msp.add_line(point, (hook_point_x, hook_point_y), dxfattribs={'color': 2})

    msp.add_circle((hook_point_x, hook_point_y), radius=0.2, dxfattribs={'color': 3})
    msp.add_line((hook_point_x, hook_point_y), (hook_point_x, hook_point_y + 1), dxfattribs={'color': 3})

    text_y_start = load_width + 2
    text_y_increment = 0.5
    
    annotations = [
        f"Load Weight: {params.get('Load Weight', 0)} kg",
        f"Sling Angle: {sling_angle:.2f} degrees",
        f"Sling Tension: {sling_tension:.2f} kg",
        f"Crane Utilization: {crane_utilization:.2f}%"
    ]
    
    for i, text in enumerate(annotations):
        msp.add_text(text, dxfattribs={'height': 0.25}).set_placement(
            (load_length + 1, text_y_start - i * text_y_increment),
            align=TextEntityAlignment.LEFT
        )

    doc.saveas(filename)
    print(f"Lifting plan drawing saved to '{filename}'")

if __name__ == '__main__':
    import math
    example_params = {
        "Load Weight": 10000,
        "Load Length": 6,
        "Load Width": 2.5,
        "Number of Slings": 4,
        "Sling Length": 5,
        "Sling Attachment Point X1": -2,
        "Sling Attachment Point Y1": 1,
        "Sling Attachment Point X2": 2,
        "Sling Attachment Point Y2": 1,
        "Sling Attachment Point X3": -2,
        "Sling Attachment Point Y3": -1,
        "Sling Attachment Point X4": 2,
        "Sling Attachment Point Y4": -1,
    }
    example_results = {
        "Center of Gravity (X)": 3.0,
        "Center of Gravity (Y)": 1.25,
        "Sling Angle": 60.0,
        "Sling Tension": 2886.75,
        "Crane Utilization": 42.0
    }
    create_lifting_plan_drawing("lifting_plan_example.dxf", example_params, example_results)
