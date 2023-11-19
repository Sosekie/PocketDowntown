import cv2

def load_template():
    
    # 载入出租车标识的图像作为模板
    taxi_icon_template_path = './image/taxi_icon.jpg'
    taxi_icon_template = cv2.imread(taxi_icon_template_path, 0)
    # 载入特殊出租车标识的图像作为模板
    taxi_star_template_path = './image/taxi_star.jpg'
    taxi_star_template = cv2.imread(taxi_star_template_path, 0)
    # 载入出租车外形的图像作为模板
    taxi_shape_template_path = './image/taxi_shape.jpg'
    taxi_shape_template = cv2.imread(taxi_shape_template_path, 0)
    # 载入向右行驶的图像作为模板
    go_right_template_path = './image/go_right.jpg'
    go_right_template = cv2.imread(go_right_template_path, 0)
    # 载入向左行驶的图像作为模板
    go_left_template_path = './image/go_left.jpg'
    go_left_template = cv2.imread(go_left_template_path, 0)

    # 载入继续的图像作为模板
    continue_template_path = './image/continue.jpg'
    continue_template = cv2.imread(continue_template_path, 0)
    # 载入好！的图像作为模板
    ok_template_path = './image/ok.jpg'
    ok_template = cv2.imread(ok_template_path, 0)
    # 载入再说的图像作为模板
    later_template_path = './image/later.jpg'
    later_template = cv2.imread(later_template_path, 0)

    return taxi_icon_template, taxi_star_template, taxi_shape_template, go_right_template, go_left_template, continue_template, ok_template, later_template