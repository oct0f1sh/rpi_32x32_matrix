from ezmatrix import *
from pixnum import *
import time
import pytz
from datetime import datetime

def run_anim():
    matrix = EzMatrix()

    cvs = Canvas()

    anim = matrix.rotate_square_canvas(Color(0, 255, 0), cvs)
    anim = matrix.rotate_subsquare_on_anim(Point(2, 2), 27, Color(255, 0, 0), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(4, 4), 23, Color(0, 0, 255), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(6, 6), 19, Color(0, 255, 0), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(8, 8), 15, Color(255, 0, 0), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(10, 10), 11, Color(0, 0, 255), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(12, 12), 7, Color(0, 255, 0), anim)
    anim = matrix.rotate_subsquare_on_anim(Point(14, 14), 3, Color(255, 0, 0), anim)

    while True:
    
        matrix.run_anim(anim, 1)
        
##def disp_num():
##    matrix = EzMatrix()
##    
##    cvs = PixNum.canvas_for_num(2, Color(0, 255, 0))
##    
##    cvs = matrix.add_subcavas(Canvas(), cvs)
##    
##    while True:
##        
##        matrix.draw_canvas(cvs)
        
def test_nums():
    matrix = EzMatrix()
    
    for i in range(10):
        cvs = Canvas()
        
        subcvs_0 = PixNum.canvas_for_num(i - 1, Color(255, 0, 0))
        cvs.add_subcanvas(subcvs_0)
        
        subcvs_1 = PixNum.canvas_for_num(i, Color(0, 0, 255))
        cvs.add_subcanvas(subcvs_1, Point(5, 5))
        
        matrix.draw_canvas(cvs)
        
        time.sleep(1)
        
def clock():
    matrix = EzMatrix()
    
    while True:
        time = datetime.now(pytz.timezone('US/Pacific'))
        time_hr = time.strftime('%H')
        time_mn = time.strftime('%M')
        
        if int(time_hr) > 12:
            time_hr = '0' + str(int(time_hr) - 12)
    
        hr_pos1 = PixNum.canvas_for_num(int(time_hr[0]), Color(255, 0, 0))
        hr_pos2 = PixNum.canvas_for_num(int(time_hr[1]), Color(255, 0, 0))
    
        mn_pos1 = PixNum.canvas_for_num(int(time_mn[0]), Color(0, 0, 255))
        mn_pos2 = PixNum.canvas_for_num(int(time_mn[1]), Color(0, 0, 255))
    
        time_cvs = Canvas(15, 5)
        time_cvs.add_subcanvas(hr_pos1).add_subcanvas(hr_pos2, Point(4, 0)).add_subcanvas(mn_pos1, Point(8, 0)).add_subcanvas(mn_pos2, Point(12, 0))
        
        cvs = Canvas().add_subcanvas(time_cvs, Point(8, 13))
    
        matrix.draw_canvas(cvs)
        
clock()