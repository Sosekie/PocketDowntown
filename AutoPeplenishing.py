import pyautogui
from get_screenshot import get_screenshot
from find_best_match import find_best_match, find_and_print, find_print_and_double_click

# 主动补货
def auto_replenish(scale_range, top_left_position, bottom_right_position, template, steps, direction):

    taxi_icon_template, taxi_star_template, taxi_shape_template, go_right_template, go_left_template, continue_template, ok_template, later_template, close_template, get_item_template, items_template, item_notice_template, blank_item_template = template

    # move and find
    width = bottom_right_position[0]-top_left_position[0]
    height = bottom_right_position[1]-top_left_position[1]
    if direction=="goRight":
        start_point = (top_left_position[0] + 1*width//2, top_left_position[1] + height//2)
    else:
        start_point = (top_left_position[0] + 2*width//5, top_left_position[1] + height//2)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
    status = "close"
    find_and_print(screen, close_template, scale_range, top_left_position, status)
    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
    status = "click later"
    find_and_print(screen, later_template, scale_range, top_left_position, status)

    for i in range(steps):
        pyautogui.mouseDown(start_point)
        # set move_step to the num of houses in your screen
        move_step = width//14
        if direction=="goRight":
            move_to_where = pyautogui.position().x - move_step
        else:
            move_to_where = pyautogui.position().x + move_step
        pyautogui.moveTo(move_to_where, pyautogui.position().y, duration=0.2)
        pyautogui.mouseUp()
        pyautogui.click()
        pyautogui.click()

        for j in range(2):
            screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
            status = "get items"
            find_and_print(screen, get_item_template, scale_range, top_left_position, status)

        screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
        status = "click later"
        find_and_print(screen, later_template, scale_range, top_left_position, status)
        screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
        status = "close"
        find_and_print(screen, close_template, scale_range, top_left_position, status)
        
        print("search empty item ", i+1, " steps")

# 回到最左边
def back_to_left(scale_range, top_left_position, bottom_right_position, template, steps):

    taxi_icon_template, taxi_star_template, taxi_shape_template, go_right_template, go_left_template, continue_template, ok_template, later_template, close_template, get_item_template, items_template, item_notice_template, blank_item_template = template

    # move and find
    width = bottom_right_position[0]-top_left_position[0]
    height = bottom_right_position[1]-top_left_position[1]
    start_point = (top_left_position[0] + 1*width//10, top_left_position[1] + height//2)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
    status = "close"
    find_and_print(screen, close_template, scale_range, top_left_position, status)
    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
    status = "click later"
    find_and_print(screen, later_template, scale_range, top_left_position, status)

    for i in range(steps):
        pyautogui.mouseDown(start_point)
        move_step = 8*width//10
        pyautogui.moveTo(pyautogui.position().x + move_step, pyautogui.position().y, duration=0.2)
        pyautogui.mouseUp()
        print("move back ", i+1, "steps")

# 回到最右边
def back_to_right(scale_range, top_left_position, bottom_right_position, template, steps):

    taxi_icon_template, taxi_star_template, taxi_shape_template, go_right_template, go_left_template, continue_template, ok_template, later_template, close_template, get_item_template, items_template, item_notice_template, blank_item_template = template

    # move and find
    width = bottom_right_position[0]-top_left_position[0]
    height = bottom_right_position[1]-top_left_position[1]
    start_point = (top_left_position[0] + 9*width//10, top_left_position[1] + height//2)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
    status = "close"
    find_and_print(screen, close_template, scale_range, top_left_position, status)
    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
    status = "click later"
    find_and_print(screen, later_template, scale_range, top_left_position, status)

    for i in range(steps):
        pyautogui.mouseDown(start_point)
        move_step = 8*width//10
        pyautogui.moveTo(pyautogui.position().x - move_step, pyautogui.position().y, duration=0.2)
        pyautogui.mouseUp()
        print("move back ", i+1, "steps")