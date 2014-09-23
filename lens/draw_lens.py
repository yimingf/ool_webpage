from PIL import Image, ImageDraw
import sys
sys.path.append("..")
from Module_In import Lens
sys.path.pop()
DEFAULT_WIDTH = 640
DEFAULT_HEIGHT = 480
LENS_THICKNESS = 20
LENS_HEIGHT = 100
LENS_FOCUS = 8

def draw_lens_on(pic,lens):
	draw = ImageDraw.Draw(pic)
	y = DEFAULT_HEIGHT/2
	x = lens.pos
	if lens.focus > 0 :
		line_len = LENS_THICKNESS-2*LENS_FOCUS
	elif lens.focus < 0 :
		line_len = LENS_THICKNESS

	lens_box=[(x-line_len/2,y-LENS_HEIGHT/2),
	          (x+line_len/2,y-LENS_HEIGHT/2),
	          (x-line_len/2,y+LENS_HEIGHT/2),
	          (x+line_len/2,y+LENS_HEIGHT/2)]

	draw.line(lens_box[:2], fill=0, width=2)
	draw.line(lens_box[2:], fill=0, width=2)
	left_box = [lens_box[0][0]-LENS_FOCUS,lens_box[0][1],
	            lens_box[2][0]+LENS_FOCUS,lens_box[2][1]]
	right_box = [lens_box[1][0]-LENS_FOCUS,lens_box[1][1],
	             lens_box[3][0]+LENS_FOCUS,lens_box[3][1]]
	left_box = list(map(int, left_box))
	right_box = list(map(int, right_box))
	if lens.focus>0 :
		draw.arc(left_box,90,270,fill=0)
		draw.arc(right_box,-90,90,fill=0)
	elif lens.focus<0 :
		draw.arc(left_box,-90,90,fill=0)
		draw.arc(right_box,90,270,fill=0)
	return pic

if __name__ == '__main__':
	temp = Image.new("RGBA",(640,480),(255,255,255))
	temp = draw_lens_on(temp,Lens(320,1))
	temp.save("delete_me.jpg")