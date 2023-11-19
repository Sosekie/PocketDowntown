import cv2
import numpy as np
import pyautogui
import time

def find_best_match(screen, template, scale_range):
    """
    在给定的屏幕截图中查找与模板的最佳匹配。

    :param screen: 屏幕截图
    :param template: 模板图像
    :param scale_range: 缩放范围
    :return: 最佳匹配值、位置、缩放级别和模板的宽高
    """
    best_match_val = 0
    best_match_loc = (0, 0)
    best_match_scale = 1
    best_w, best_h = template.shape[::-1]  # 初始模板宽高

    for scale in scale_range:
        resized_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
        h, w = resized_template.shape
        res = cv2.matchTemplate(screen, resized_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        if max_val > best_match_val:
            best_match_val = max_val
            best_match_loc = max_loc
            best_match_scale = scale
            best_w, best_h = w, h

    return best_match_val, best_match_loc, best_match_scale, best_w, best_h

def click_item(best_match_loc, best_match_scale, screen, w, h):
    top_left = best_match_loc
    bottom_right = (top_left[0] + int(w * best_match_scale), top_left[1] + int(h * best_match_scale))
    cv2.rectangle(screen, top_left, bottom_right, 255, 2)
    pyautogui.click(x=top_left[0] + w // 2, y=top_left[1] + h // 2)

# 定义缩放的范围和步长
scale_range = np.linspace(0.5, 1.5, 20)

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
go_right_template_path = './image/go_right_top.jpg'
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

count_times = 0
count_taxi = 0
taxi_star = False
while True:
    screen_pil = pyautogui.screenshot()
    screen = np.array(screen_pil)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

    # match taxi_icon
    best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, taxi_icon_template, scale_range)
    if best_match_val > 0.8:
        click_item(best_match_loc, best_match_scale, screen, w, h)
        print("find taxi icon")
        count_taxi = count_taxi + 1
    
    # match taxi_star if appear
    if count_times%5 == 0:
        best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, taxi_star_template, scale_range)
        if best_match_val > 0.8:
            click_item(best_match_loc, best_match_scale, screen, w, h)
            print("find taxi star")
            taxi_star = True
    
    # match later if stuck
    if count_times%3 == 0:
        best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, later_template, scale_range)
        if best_match_val > 0.8:
            click_item(best_match_loc, best_match_scale, screen, w, h)
            print("click later")

    # match taxi_shape
    best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, taxi_shape_template, scale_range)
    if best_match_val > 0.8:
        click_item(best_match_loc, best_match_scale, screen, w, h)
        print("find taxi shape")
    
    # match go_right
    best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, go_right_template, scale_range)
    if best_match_val > 0.8:
        top_left = best_match_loc
        bottom_right = (top_left[0] + int(w * best_match_scale), top_left[1] + int(h * best_match_scale))
        cv2.rectangle(screen, top_left, bottom_right, 255, 2)
        print("go right")
        start_time = time.time()
        while time.time() - start_time < 17:
            pyautogui.mouseDown(x=top_left[0] + w // 2, y=top_left[1] + h // 2)

            # point_time = time.time()
            # while time.time() - point_time <= 0.33:
            #     pass
            
            time.sleep(0.25)
            pyautogui.mouseUp()
            time.sleep(0.5)
        print("stop")

    # match continue
    best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, continue_template, scale_range)
    if best_match_val > 0.8:
        click_item(best_match_loc, best_match_scale, screen, w, h)
        print("click continue")

    # match taxi_star_ok
    if taxi_star:
        best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, ok_template, scale_range)
        if best_match_val > 0.9:
            click_item(best_match_loc, best_match_scale, screen, w, h)
            print("click ok")
            taxi_star = False

    count_times = count_times + 1
    print("continue, num of succeed taxi:", count_taxi)
    # time.sleep(0.01)