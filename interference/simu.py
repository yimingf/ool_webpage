import numpy as np
import matplotlib.pyplot as plt
import Module_In as In
import OpenGL, OpenGL_accelerate
from Module_In import Light_source, Light_screen

pi = 3.1415926

def SpIn(source1, source2, screen):
    distance = np.sqrt(np.square(source1.x - source2.x) + np.square(source1.y - source2.y))
    k = 2*pi/Light_source.w_length
    if (screen.a == 0 and screen.b == 0):
        a = np.arange(Light_source.minx - 5*distance,
                      Light_source.maxx + 5*distance,
                      (Light_source.maxx - Light_source.minx + 5 *distance)/100.0)
        b = np.arange(Light_source.miny - 5*distance,
                      Light_source.maxy + 5*distance,
                      (Light_source.maxy - Light_source.miny + 5 *distance)/100.0)
        x, y = np.meshgrid(a, b)
        r = np.sqrt((np.square(x-source1.x)+np.square(y-source1.y)))
        U1=np.expm1(1j*k*r)+1;
        r2 = np.sqrt((np.square(x-source2.x)+np.square(y-source2.y)))
        U2=np.expm1(1j*k*r2)+1;
        A=U1+U2;
        I=np.absolute(A)*np.absolute(A);
        plt.pcolor(x,y,I);
        plt.gray()
        plt.axis([a[0],a[-1],b[0],b[-1]])
        plt.savefig('./inf.jpg')
        plt.close()
        plt.plot([source1.x,source2.x],[source1.y,source2.y],'o')
        plt.text(source1.x-1,source1.y-1,'S1')
        plt.text(source2.x-1,source2.y-1,'S2')
        plt.axis([a[0],a[-1],b[0],b[-1]])
        plt.savefig('./pos.jpg')
    else:
        dis1 = np.abs(screen.a*source1.x+screen.b*source1.y+screen.c)/np.sqrt(np.square(screen.a)+np.square(screen.b))
        dis2 = np.abs(screen.a*source2.x+screen.b*source2.y+screen.c)/np.sqrt(np.square(screen.a)+np.square(screen.b))
        if (dis1+dis2 == distance*np.abs(screen.b)/np.sqrt(np.square(screen.a)+np.square(screen.b))):
            print('no result')
            return
        else:
            centerx = (source1.x+source2.x)/2
            centery = (source1.y+source2.y)/2
            interx = (screen.b*screen.b*centerx-screen.a*screen.b*centery-screen.a*screen.c)/(screen.a*screen.a+screen.b*screen.b)
            intery = (screen.a*screen.a*centery-screen.a*screen.b*centerx-screen.b*screen.c)/(screen.a*screen.a+screen.b*screen.b)
            a = np.arange(-100.0*distance,100.0*distance, 200.0*distance/100.0)
            x, y = np.meshgrid(a, a)
            if (screen.a != 0 and screen.b != 0):
                r=np.sqrt(np.square(source1.x-(interx+x*np.sqrt(screen.a*screen.a+screen.b*screen.b)/screen.a))+\
                          np.square(source1.y-(intery+y*np.sqrt(screen.a*screen.a+screen.b*screen.b)/screen.b))+y*y)
                U1=np.expm1(1j*k*r)+1;
                r2=np.sqrt(np.square(source2.x-(interx+x*np.sqrt(screen.a*screen.a+screen.b*screen.b)/screen.a))+\
                          np.square(source2.y-(intery+y*np.sqrt(screen.a*screen.a+screen.b*screen.b)/screen.b))+y*y)
                U2=np.expm1(1j*k*r2)+1;
                A=U1+U2;
                I=np.absolute(A)*np.absolute(A);
                plt.pcolor(x,y,I);
                plt.gray()
                plt.axis([a[0],a[-1],a[0],a[-1]])
                plt.savefig('./inf.jpg')
                plt.close()
                plt.hold(True)
                x = [-100,100]
                y = [(-screen.c-screen.a*-100)/screen.b,(-screen.c-screen.a*100)/screen.b]
                plt.plot(x,y)
                plt.axis([min(Light_source.minx,interx)-5*distance,\
                              max(Light_source.maxx,interx)+5*distance,\
                              min(Light_source.miny,intery)-5*distance,\
                              max(Light_source.maxx,intery)-5*distance])
                plt.plot([source1.x,source2.x],[source1.y,source2.y],'o')
                plt.text(source1.x-1,source1.y-1,'S1')
                plt.text(source2.x-1,source2.y-1,'S2')
                
                
                plt.savefig('./pos.jpg')
            else:
                if(screen.a == 0):
                    r=np.sqrt(np.square(source1.x-(interx+x))+np.square(source1.y-intery)+y*y)
                    U1=np.expm1(1j*k*r)+1;
                    r2=np.sqrt(np.square(source2.x-(interx+x))+np.square(source2.y-intery)+y*y)
                    U2=np.expm1(1j*k*r2)+1;
                    A=U1+U2;
                    I=np.absolute(A)*np.absolute(A);
                    plt.pcolor(x,y,I);
                    plt.gray()
                    plt.axis([a[0],a[-1],a[0],a[-1]])
                    plt.savefig('./inf.jpg')
                    plt.close()
                    plt.plot([source1.x,source2.x],[source1.y,source2.y],'o')
                    plt.hold()
                    plt.text(source1.x-1,source1.y-1,'S1')
                    plt.text(source2.x-1,source2.y-1,'S2')
                    x = [-100,100]
                    y = [intery,intery]
                    plt.plot(x,y)
                    plt.axis([min(Light_source.minx,interx)-5*distance,\
                                  max(Light_source.maxx,interx)+5*distance,\
                                  min(Light_source.miny,intery)-5*distance,\
                                  max(Light_source.maxx,intery)-5*distance])
                    plt.savefig('./pos.jpg')
                else:
                    if(screen.b == 0):
                        r=np.sqrt(np.square(source1.y-(intery+x))+np.square(source1.x-interx)+y*y)
                        U1=np.expm1(1j*k*r)+1;
                        r2=np.sqrt(np.square(source2.y-(intery+x))+np.square(source2.x-interx)+y*y)
                        U2=np.expm1(1j*k*r2)+1;
                        A=U1+U2;
                        I=np.absolute(A)*np.absolute(A);
                        plt.pcolor(x,y,I);
                        plt.gray()
                        plt.axis([a[0],a[-1],a[0],a[-1]])
                        plt.savefig('./inf.jpg')
                        plt.close()
                        plt.plot([source1.x,source2.x],[source1.y,source2.y],'o')
                        plt.hold()
                        plt.text(source1.x-1,source1.y-1,'S1')
                        plt.text(source2.x-1,source2.y-1,'S2')
                        x = [interx,interx]
                        y = [-100,100]
                        plt.plot(x,y)
                        plt.axis([min(Light_source.minx,interx)-5*distance,\
                                      max(Light_source.maxx,interx)+5*distance,\
                                      min(Light_source.miny,intery)-5*distance,\
                                      max(Light_source.maxx,intery)-5*distance])
                        plt.savefig('./pos.jpg')
#source1 = Light_source(-1,1,0.5)
#source2 = Light_source(1,1,0.5)
#screen = Light_screen(1,0,10)
#SpIn(source1, source2, screen)