import cv2
import pyautogui

def find_best_match(screen, template, scale_range, resize_range = 1):
    best_match_val = 0
    best_match_loc = (0, 0)
    best_match_scale = 1
    best_w, best_h = template.shape[::-1]
    for scale in scale_range:
        resized_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

        # you can set resize_range to scale the size of image, maybe will reduce running time
        resized_screen = cv2.resize(screen, (screen.shape[1] // resize_range, screen.shape[0] // resize_range), interpolation=cv2.INTER_AREA)
        resized_template = cv2.resize(resized_template, (resized_template.shape[1] // resize_range, resized_template.shape[0] // resize_range), interpolation=cv2.INTER_AREA)

        h, w = resized_template.shape
        res = cv2.matchTemplate(resized_screen, resized_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        if max_val > best_match_val:
            best_match_val = max_val
            best_match_loc = max_loc
            best_match_scale = scale
            best_w, best_h = w, h

    return best_match_val, best_match_loc, best_match_scale, best_w, best_h

def click_item(top_left_position, best_match_loc, best_match_scale, screen, w, h):
    top_left = (best_match_loc[0]+top_left_position[0], best_match_loc[1]+top_left_position[1])
    bottom_right = (top_left[0] + int(w * best_match_scale), top_left[1] + int(h * best_match_scale))
    cv2.rectangle(screen, top_left, bottom_right, 255, 2)
    pyautogui.click(x=top_left[0] + w // 2, y=top_left[1] + h // 2)

def find_and_print(screen, taxi_icon_template, scale_range, top_left_position, status):
    best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, taxi_icon_template, scale_range)
    if best_match_val > 0.8:
        click_item(top_left_position, best_match_loc, best_match_scale, screen, w, h)
        print(status)
        return True
    else:
        return False
    
def click_item_and_get_position(top_left_position, best_match_loc, best_match_scale, screen, w, h):
    top_left = (best_match_loc[0]+top_left_position[0], best_match_loc[1]+top_left_position[1])
    bottom_right = (top_left[0] + int(w * best_match_scale), top_left[1] + int(h * best_match_scale))
    cv2.rectangle(screen, top_left, bottom_right, 255, 2)
    pyautogui.click(x=top_left[0] + w // 2, y=top_left[1] + h // 2)

    top_left = (best_match_loc[0], best_match_loc[1])
    bottom_right = (top_left[0] + int(w * best_match_scale), top_left[1] + int(h * best_match_scale))

    return top_left, bottom_right

def find_print_get_position(screen, taxi_icon_template, scale_range, top_left_position, status):
    best_match_val, best_match_loc, best_match_scale, w, h = find_best_match(screen, taxi_icon_template, scale_range)
    if best_match_val > 0.8:
        top_left, bottom_right = click_item_and_get_position(top_left_position, best_match_loc, best_match_scale, screen, w, h)
        print(status)
        return [True, top_left, bottom_right]
    else:
        return [False]