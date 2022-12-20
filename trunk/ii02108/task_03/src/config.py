from inspect import getabsfile
import os
import sys

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


main_theme = 'dark'
btns_color = 'black'
add_tab_button = 'green'
close_tab_button = 'red'
unselected_btn_clr = 'white'
selected_tab_clr = '#388fd1'
unactive_mode_btn = '#FFE4C4'
active_mode_btn = '#F4A460'


path_to_img_create_new_tab = get_script_dir() + '/icons/icon_for_newgraph.png'
path_to_img_close_tab = get_script_dir() + '/icons/icon_for_close_tab.png'

vertex_radius = 30