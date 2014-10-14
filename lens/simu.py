import string
import numpy as np
import matplotlib.pyplot as plt
import Module_In
from Module_In import Light_source, Lens
import draw_lens
from PIL import Image, ImageDraw
  
def ImagePos(source, lens1, lens2):
    temp = Image.new("RGBA",(640,480),(255,255,255))
    if (lens1.pos == lens2.pos):
        return
    else:
        if (lens1.pos > lens2.pos):
            temp = lens1
            lens1 = lens2
            lens2 = temp
        #drawlens(lens1.pos)
        #drawlens(lens2.pos)
        obj_dis1 = lens1.pos
        plt.hold(True)
        '''
        temp = draw_lens.draw_lens_on(temp,lens1)
        plt.imshow(temp);
        temp = draw_lens.draw_lens_on(temp,lens2)
        plt.imshow(temp);
        '''
        if (source.y == 1 and obj_dis1 == lens1.focus): #point source at focus
            img_dis1 = np.Inf
            obj_dis2 = img_dis1
            img_dis2 = lens2.focus
            plt.plot([0,lens1.pos],[0,-2],'b',
                     [0,lens1.pos],[0,-1],'b',
                     [0,lens1.pos],[0,0],'b',
                     [0,lens1.pos],[0,1],'b',
                     [0,lens1.pos],[0,2],'b')
            plt.plot([lens1.pos,lens2.pos],[-2,-2],'b',
                     [lens1.pos,lens2.pos],[-1,-1],'b',
                     [lens1.pos,lens2.pos],[0,0],'b',
                     [lens1.pos,lens2.pos],[1,1],'b',
                     [lens1.pos,lens2.pos],[2,2],'b')
            if (img_dis2>0):
                plt.plot([lens2.pos,lens2.pos+img_dis2],[-2,0],'b',
                         [lens2.pos,lens2.pos+img_dis2],[-1,0],'b',
                         [lens2.pos,lens2.pos+img_dis2],[0,0],'b',
                         [lens2.pos,lens2.pos+img_dis2],[1,0],'b',
                         [lens2.pos,lens2.pos+img_dis2],[2,0],'b')
            else:
                plt.plot([lens2.pos,lens2.pos+img_dis2],[-2,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[-1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[0,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[2,0],'b--')
                plt.plot([lens2.pos,lens2.pos-img_dis2],[-2,-4],'b',
                         [lens2.pos,lens2.pos-img_dis2],[-1,-2],'b',
                         [lens2.pos,lens2.pos-img_dis2],[0,0],'b',
                         [lens2.pos,lens2.pos-img_dis2],[1,2],'b',
                         [lens2.pos,lens2.pos-img_dis2],[2,4],'b')
            return
        if(source.y == 1):
            img_dis1 = 1.0*obj_dis1*lens1.focus/(obj_dis1 - lens1.focus)
            obj_dis2 = lens2.pos - (img_dis1 + lens1.pos)
            img_dis2 = 1.0*obj_dis2*lens2.focus/(obj_dis2 - lens2.focus)
        else:
            obj_dis1 = np.Inf
            img_dis1 = lens1.focus
            obj_dis2 = lens2.pos - (img_dis1 + lens1.pos)
            img_dis2 = obj_dis2*lens2.focus/(obj_dis2 - lens2.focus)
        if (img_dis1 > 0 and obj_dis2 > 0):
            if (source.y == 1):
                plt.plot([0,lens1.pos],[0,-2],'b',
                         [0,lens1.pos],[0,-1],'b',
                         [0,lens1.pos],[0,0],'b',
                         [0,lens1.pos],[0,1],'b',
                         [0,lens1.pos],[0,2],'b')
            else:
                plt.plot([0,lens1.pos],[-2,-2],'b',
                         [0,lens1.pos],[-1,-1],'b',
                         [0,lens1.pos],[0,0],'b',
                         [0,lens1.pos],[1,1],'b',
                         [0,lens1.pos],[2,2],'b')
            plt.plot([lens1.pos,lens1.pos+img_dis1,lens2.pos],[-2,0,2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                [lens1.pos,lens1.pos+img_dis1,lens2.pos],[-1,0,1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                [lens1.pos,lens1.pos+img_dis1,lens2.pos],[0,0,0],'b',
                [lens1.pos,lens1.pos+img_dis1,lens2.pos],[1,0,-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                [lens1.pos,lens1.pos+img_dis1,lens2.pos],[2,0,-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b')
            if (img_dis2 > 0):
                plt.plot([lens2.pos+img_dis2,lens2.pos],[0,2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,0],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b')
            else:
                plt.plot([lens2.pos,lens2.pos+img_dis2],[-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[0*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[1*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[2*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--')
                plt.plot([lens2.pos,lens2.pos-img_dis2],[-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1,
                    -4*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos,lens2.pos-img_dis2],[-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1,-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos,lens2.pos-img_dis2],[0,0],'b',
                         [lens2.pos,lens2.pos-img_dis2],[1*(lens2.pos-lens1.pos-img_dis1)/img_dis1,2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos,lens2.pos-img_dis2],[2*(lens2.pos-lens1.pos-img_dis1)/img_dis1,4*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b')
        elif (img_dis1 > 0 and obj_dis2 < 0):
            plt.plot([0,lens1.pos],[0,-2],'b',
                 [0,lens1.pos],[0,-1],'b',
                 [0,lens1.pos],[0,0],'b',
                 [0,lens1.pos],[0,1],'b',
                 [0,lens1.pos],[0,2],'b')
            plt.plot([lens1.pos,lens2.pos],[-2,2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                     [lens1.pos,lens2.pos],[-1,1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                     [lens1.pos,lens2.pos],[0,0],'b',
                     [lens1.pos,lens2.pos],[1,-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                     [lens1.pos,lens2.pos],[2,-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b')
            plt.plot([lens1.pos+img_dis1,lens2.pos],[0,2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b--',
                     [lens1.pos+img_dis1,lens2.pos],[0,1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b--',
                     [lens1.pos+img_dis1,lens2.pos],[0,0],'b--',
                     [lens1.pos+img_dis1,lens2.pos],[0,-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b--',
                     [lens1.pos+img_dis1,lens2.pos],[0,-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b--')
            if (img_dis2 > 0):
                plt.plot([lens2.pos+img_dis2,lens2.pos],[0,2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,0],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b')
            else:
                plt.plot([lens2.pos,lens2.pos+img_dis2],[-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[0*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[1*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[2*(lens2.pos-lens1.pos-img_dis1)/img_dis1,0],'b--')
                plt.plot([lens2.pos,lens2.pos-img_dis2],[-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1,-4*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos,lens2.pos-img_dis2],[-1*(lens2.pos-lens1.pos-img_dis1)/img_dis1,-2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos,lens2.pos-img_dis2],[0,0],'b',
                         [lens2.pos,lens2.pos-img_dis2],[1*(lens2.pos-lens1.pos-img_dis1)/img_dis1,2*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b',
                         [lens2.pos,lens2.pos-img_dis2],[2*(lens2.pos-lens1.pos-img_dis1)/img_dis1,4*(lens2.pos-lens1.pos-img_dis1)/img_dis1],'b')
        elif (img_dis1 < 0):
            if(source.y == 1):
                plt.plot([0,lens1.pos],[0,2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                         [0,lens1.pos],[0,1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                         [0,lens1.pos],[0,0],'b',
                         [0,lens1.pos],[0,-1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                         [0,lens1.pos],[0,-2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b')
            else:
                plt.plot([0,lens1.pos],[2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1),2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                         [0,lens1.pos],[1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1),1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                         [0,lens1.pos],[0,0],'b',
                         [0,lens1.pos],[-1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1),-1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                         [0,lens1.pos],[-2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1),-2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b')
            plt.plot([lens1.pos+img_dis1,lens1.pos],[0,2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b--',
                     [lens1.pos+img_dis1,lens1.pos],[0,1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b--',
                     [lens1.pos+img_dis1,lens1.pos],[0,0],'b--',
                     [lens1.pos+img_dis1,lens1.pos],[0,-1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b--',
                     [lens1.pos+img_dis1,lens1.pos],[0,-2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b--')
            plt.plot([lens2.pos,lens1.pos],[2,2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                     [lens2.pos,lens1.pos],[1,1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                     [lens2.pos,lens1.pos],[0,0],'b',
                     [lens2.pos,lens1.pos],[-1,-1.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b',
                     [lens2.pos,lens1.pos],[-2,-2.0*(-img_dis1)/(lens2.pos-lens1.pos-img_dis1)],'b')
            if (img_dis2 > 0):
                plt.plot([lens2.pos+img_dis2,lens2.pos],[0,2],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,1],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,0],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,-1],'b',
                         [lens2.pos+img_dis2,lens2.pos],[0,-2],'b')
            else:
                plt.plot([lens2.pos,lens2.pos+img_dis2],[-2,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[-1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[0,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[1,0],'b--',
                         [lens2.pos,lens2.pos+img_dis2],[2,0],'b--')
                plt.plot([lens2.pos,lens2.pos-img_dis2],[-2,-4],'b',
                         [lens2.pos,lens2.pos-img_dis2],[-1,-2],'b',
                         [lens2.pos,lens2.pos-img_dis2],[0,0],'b',
                         [lens2.pos,lens2.pos-img_dis2],[1,2],'b',
                         [lens2.pos,lens2.pos-img_dis2],[2,4],'b')
    plt.savefig('./lens/static/lens/pos.jpg')
    #plt.savefig('./pos.jpg')

#source = Light_source(0,1)
#lens1 = Lens(4,-2)
#lens2 = Lens(3,1)
#ImagePos(source, lens1, lens2)
