import cv2
import numpy as np
import pyautogui
import time
from get_screenshot import get_screenshot
from find_best_match import find_best_match, find_and_print, find_print_and_double_click

def auto_stock(scale_range, top_left_position, bottom_right_position, template):

    taxi_icon_template, taxi_star_template, taxi_shape_template, go_right_template, go_left_template, continue_template, ok_template, later_template, close_template, get_item_template, items_template, item_notice_template = template

    # mask the top half
    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
    status = "click later"
    find_and_print(screen, later_template, scale_range, top_left_position, status)

    screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
    height = screen.shape[0]
    dividing_line = 2 * height // 3
    width = screen.shape[1]
    dividing_line_width = width // 3
    screen[:dividing_line, :] = 0
    # match items
    status = "need items"
    if find_and_print(screen, items_template, scale_range, top_left_position, status):
        # mask the bottom half
        screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
        status = "close"
        find_and_print(screen, close_template, scale_range, top_left_position, status)
        
        screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
        screen[dividing_line:, :] = 0
        screen[:, :dividing_line_width] = 0
        screen[:, 2*dividing_line_width:] = 0
        status = "click items"
        if find_print_and_double_click(screen, items_template, scale_range, top_left_position, status):
            screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
            status = "get items"
            find_and_print(screen, get_item_template, scale_range, top_left_position, status)
            

    status = "notice items"
    if find_and_print(screen, item_notice_template, scale_range, top_left_position, status):
        # mask the bottom half
        screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
        screen[dividing_line:, :] = 0
        status = "click notice"
        if find_and_print(screen, item_notice_template, scale_range, top_left_position, status):
            screen, top_left_position, bottom_right_position = get_screenshot(top_left_position, bottom_right_position)
            status = "get items"
            find_and_print(screen, get_item_template, scale_range, top_left_position, status)
    
    status = "close"
    find_and_print(screen, close_template, scale_range, top_left_position, status)
