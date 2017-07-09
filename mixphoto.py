import tkinter as TK
import tkinter.ttk as TTk
import tkinter.filedialog as FD
import tkinter.dialog as DL
import tkinter.messagebox as MB
from PIL import Image as IM
from PIL import ImageTk as ITk
from PIL import ImageChops as ICs
from PIL import ImageOps as IOs
from PIL import ImageEnhance as IEh


class MixPhoto:
    def __init__(self):
#root和basic frame
        self.root=TK.Tk()
        self.root.title('MixPhoto--图像混合软件')
        self.root.geometry('1180x585')
        self.frame_basic=TK.Frame(self.root,bg='#E7E7E7')
        self.root.resizable(0,0)
#全局变量
        self.filename1=''
        self.filename2=''
        self.filename3=''
        self.mt=TK.StringVar()
        self.mt.set('all')
        self.eh1=TK.StringVar()
        self.eh2=TK.StringVar()
        self.eh3=TK.StringVar()
        self.eh4=TK.StringVar()
        self.s1_value=TK.DoubleVar()
#顶部paned及图像labelframe
        self.paned_top=TTk.Panedwindow(self.frame_basic,orient=TK.HORIZONTAL)
        self.labelframe_result=TTk.LabelFrame(self.paned_top,text='预览',labelanchor='n')
        self.labelframe_result.rowconfigure(0,weight=8)
        self.labelframe_result.rowconfigure(1,weight=1)
        self.labelframe_result.rowconfigure(2,weight=1)
        self.labelframe_source=TTk.LabelFrame(self.paned_top,text='图像源',labelanchor='n')
        self.labelframe_source.rowconfigure(0,weight=4)
        self.labelframe_source.rowconfigure(1,weight=1)
        self.labelframe_source.rowconfigure(2,weight=4)
        self.labelframe_source.rowconfigure(3,weight=1)
#顶部paned中的画布和按钮等元素
        self.canvas_result=TK.Canvas(self.labelframe_result,height=425,width=755,bg='#2C2C2C')
        self.b1=TTk.Button(self.labelframe_result,text='刷新显示',command=self.choose_mixtype)
        self.b9=TTk.Button(self.labelframe_result,text='旋转图片',command=self.rotate_result)
        self.l1=TTk.Label(self.labelframe_result)
        self.l2=TTk.Label(self.labelframe_result,text='混合度：')
        self.s1=TTk.Scale(self.labelframe_result,from_=0,to=100,orient=TK.HORIZONTAL,variable=self.s1_value,length=600,
            command=self.show_scale)
        self.s1.set(50)
        self.canvas_source1=TK.Canvas(self.labelframe_source,height=225,width=400,bg='#2C2C2C')
        self.canvas_source2=TK.Canvas(self.labelframe_source,height=225,width=400,bg='#2C2C2C')
        self.b2=TTk.Button(self.labelframe_source,text='选择图像',command=self.getfile1)
        self.b3=TTk.Button(self.labelframe_source,text='选择图像',command=self.getfile2)
        self.b7=TTk.Button(self.labelframe_source,text='旋转图像',command=self.rotate1)
        self.b8=TTk.Button(self.labelframe_source,text='旋转图像',command=self.rotate2)
#底部paned及按钮labelframe
        self.paned_bottom=TTk.PanedWindow(self.frame_basic,orient=TK.HORIZONTAL)
        self.labelframe_mixtype=TTk.LabelFrame(self.paned_bottom,text='混合模式',labelanchor='n')
        self.labelframe_enhance=TTk.LabelFrame(self.paned_bottom,text='增强选项',labelanchor='n')
        self.labelframe_about=TTk.LabelFrame(self.paned_bottom,text='关于',labelanchor='n')
#底部paned中的按钮等元素
        self.r1=TTk.Radiobutton(self.labelframe_mixtype,text='全局混合',variable=self.mt,value='all')
        self.r2=TTk.Radiobutton(self.labelframe_mixtype,text='左右混合',variable=self.mt,value='lr')
        self.r3=TTk.Radiobutton(self.labelframe_mixtype,text='填充混合',variable=self.mt,value='fill')
        self.r4=TTk.Radiobutton(self.labelframe_mixtype,text='高光混合',variable=self.mt,value='light')
        self.r5=TTk.Radiobutton(self.labelframe_mixtype,text='阴影混合',variable=self.mt,value='dark')
        self.r6=TTk.Radiobutton(self.labelframe_mixtype,text='反差混合',variable=self.mt,value='difference')
        self.r7=TTk.Radiobutton(self.labelframe_mixtype,text='乘法混合(亮)',variable=self.mt,value='screen')
        self.r8=TTk.Radiobutton(self.labelframe_mixtype,text='乘法混合(暗)',variable=self.mt,value='multiply')
        self.c1=TTk.Checkbutton(self.labelframe_enhance,text='锐化',variable=self.eh1,onvalue='yes',offvalue='no')
        self.c2=TTk.Checkbutton(self.labelframe_enhance,text='色彩',variable=self.eh2,onvalue='yes',offvalue='no')
        self.c3=TTk.Checkbutton(self.labelframe_enhance,text='均方',variable=self.eh3,onvalue='yes',offvalue='no')
        self.c4=TTk.Checkbutton(self.labelframe_enhance,text='对比',variable=self.eh4,onvalue='yes',offvalue='no')
        self.b4=TTk.Button(self.labelframe_about,text='保存',command=self.save_result)
        self.b5=TTk.Button(self.labelframe_about,text='帮助',command=self.help)
        self.b6=TTk.Button(self.labelframe_about,text='退出',command=self.root.quit)
#顶部paned中的元素布局
        self.canvas_result.grid(row=0,column=0,columnspan=4,sticky=TK.S+TK.N+TK.E+TK.W)
        self.b1.grid(row=1,column=0,columnspan=2,sticky=TK.S+TK.N+TK.E+TK.W)
        self.b9.grid(row=1,column=2,columnspan=2,sticky=TK.S+TK.N+TK.E+TK.W)
        self.canvas_source1.grid(row=0,column=0,columnspan=2)
        self.b2.grid(row=1,column=0)
        self.b7.grid(row=1,column=1)
        self.canvas_source2.grid(row=2,column=0,columnspan=2)
        self.b3.grid(row=3,column=0)
        self.b8.grid(row=3,column=1)
        self.l1.grid(row=2,column=1,columnspan=3)
        self.l2.grid(row=3,column=0,columnspan=1,sticky=TK.E)
        self.s1.grid(row=3,column=1,columnspan=3,sticky=TK.W)
#底部paned中的元素布局
        self.r1.grid(row=0,column=0)
        self.r2.grid(row=0,column=1)
        self.r3.grid(row=0,column=2)
        self.r4.grid(row=0,column=3)
        self.r5.grid(row=0,column=4)
        self.r6.grid(row=0,column=5)
        self.r7.grid(row=0,column=6)
        self.r8.grid(row=0,column=7)
        self.c1.grid(row=0,column=0)
        self.c2.grid(row=0,column=1)
        self.c3.grid(row=0,column=2)
        self.c4.grid(row=0,column=3)
        self.b4.grid(row=0,column=0)
        self.b5.grid(row=0,column=1)
        self.b6.grid(row=0,column=2)
#paned元素布局
        self.paned_top.add(self.labelframe_result)
        self.paned_top.add(self.labelframe_source)
        self.paned_top.grid(row=0,column=0)
        self.paned_bottom.add(self.labelframe_mixtype)
        self.paned_bottom.add(self.labelframe_enhance)
        self.paned_bottom.add(self.labelframe_about)
        self.paned_bottom.grid(row=1,column=0)
#basic frame布局
        self.frame_basic.grid(row=0,column=0)
        self.root.mainloop()

    def show_scale(self,event):
        #使用label l1显示scale s1的value
        self.l1['text']=round(self.s1_value.get(),2)

    def help(self):
        #帮助按钮弹出的dialog
        d=DL.Dialog(None,title='使用帮助',text='1.尽量使用尺寸相同的图像进行混合\n2.仅前三种混合模式可调节混合度\n3.目前只支持RGB'
                                           '模式的JPEG图像',bitmap=DL.DIALOG_ICON,default=0,strings=('好的','关闭'))

    def getfile1(self):
        #打开图像1并进行完整的显示
        self.filename1=FD.askopenfilename()
        self.img1=IM.open(self.filename1)
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        if ratio>=1.77:
            img0=self.img1.resize((400,int(h*400/w)), IM.ANTIALIAS)
        else:
            img0=self.img1.resize((int(w*225/h),225), IM.ANTIALIAS)
        self.photo1=ITk.PhotoImage(img0)
        self.canvas_source1.create_image(203,115,image=self.photo1)
        print(self.filename1)

    def getfile2(self):
        #打开图像2并进行完整的显示
        #如果图像2与图像1比例差别较大，给出警告
        self.filename2=FD.askopenfilename()
        self.img2=IM.open(self.filename2)
        w=self.img2.size[0]
        h=self.img2.size[1]
        w1=self.img1.size[0]
        h1=self.img1.size[1]
        ratio=float(w/h)
        ratio1=float(w1/h1)
        if ratio/ratio1>=1.5 or ratio/ratio1<=0.75:
            MB.showinfo('警告','两图长宽比差别较大，图像2将会被拉伸')
        if ratio>=1.77:
            img0=self.img2.resize((400,int(h*400/w)), IM.ANTIALIAS)
        else:
            img0=self.img2.resize((int(w*225/h),225), IM.ANTIALIAS)
        self.photo2=ITk.PhotoImage(img0)
        self.canvas_source2.create_image(203,115,image=self.photo2)
        print(self.filename2)

    def rotate1(self):
        self.img1=self.img1.transpose(method=IM.ROTATE_90)
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        if ratio>=1.77:
            img0=self.img1.resize((400,int(h*400/w)), IM.ANTIALIAS)
        else:
            img0=self.img1.resize((int(w*225/h),225), IM.ANTIALIAS)
        self.photo1=ITk.PhotoImage(img0)
        self.canvas_source1.create_image(203,115,image=self.photo1)

    def rotate2(self):
        self.img2=self.img2.transpose(method=IM.ROTATE_90)
        w=self.img2.size[0]
        h=self.img2.size[1]
        w1=self.img1.size[0]
        h1=self.img1.size[1]
        ratio=float(w/h)
        ratio1=float(w1/h1)
        if ratio/ratio1>=1.5 or ratio/ratio1<=0.75:
            MB.showinfo('警告','两图长宽比差别较大，图像2将会被拉伸')
        if ratio>=1.77:
            img0=self.img2.resize((400,int(h*400/w)), IM.ANTIALIAS)
        else:
            img0=self.img2.resize((int(w*225/h),225), IM.ANTIALIAS)
        self.photo2=ITk.PhotoImage(img0)
        self.canvas_source2.create_image(203,115,image=self.photo2)


    def save_result(self):
        #保存混合后的图片，以jpg为默认格式

        self.filename3=FD.asksaveasfilename(defaultextension='jpg')
        self.img3.save(self.filename3)

    def choose_mixtype(self):
        if self.mt.get()=='all':
            self.mix_all()
        elif self.mt.get()=='lr':
            self.mix_lr()
        elif self.mt.get()=='light':
            self.mix_light()
        elif self.mt.get()=='dark':
            self.mix_dark()
        elif self.mt.get()=='fill':
            self.mix_fill()
        elif self.mt.get()=='screen':
            self.mix_screen()
        elif self.mt.get()=='difference':
            self.mix_difference()
        elif self.mt.get()=='multiply':
            self.mix_multiply()

        if self.eh1.get()=='yes':
            self.enh_sharp()
        if self.eh2.get()=='yes':
            self.enh_color()
        if self.eh3.get()=='yes':
            self.enh_equalize()
        if self.eh4.get()=='yes':
            self.enh_contrast()
    def enh_sharp(self):
        print('sharp')
        self.img3=IEh.Sharpness(self.img3).enhance(2.0)
        w=self.img3.size[0]
        h=self.img3.size[1]
        ratio=w/h
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)
    def enh_color(self):
        print('color')
        self.img3=IEh.Color(self.img3).enhance(1.5)
        w=self.img3.size[0]
        h=self.img3.size[1]
        ratio=w/h
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)
    def enh_equalize(self):
        print('equalize')
        self.img3=IOs.equalize(self.img3)
        w=self.img3.size[0]
        h=self.img3.size[1]
        ratio=w/h
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)
    def enh_contrast(self):
        print('contrast')
        self.img3=IEh.Contrast(self.img3).enhance(1.5)
        w=self.img3.size[0]
        h=self.img3.size[1]
        ratio=w/h
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

    def mix_all(self):
        #全局混合图片
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        self.img2=self.img2.resize((self.img1.size[0],self.img1.size[1]), IM.ANTIALIAS)
        self.img3=ICs.blend(self.img1,self.img2,self.s1_value.get()/100)
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

    def mix_lr(self):
        #左右混合图片
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        self.img2=self.img2.resize((self.img1.size[0],self.img1.size[1]), IM.ANTIALIAS)
        val=int(self.s1_value.get()*4)
        #根据scale值生成透明度mask
        mask=IM.new(mode='L', size=(400, int(400 * h / w)), color=0)
        if val<=100:
            #scale值靠近图像左侧边缘
            for i in range(val):
                for j in range(mask.size[1]):
                    col=int(255-i*127/val)
                    mask.putpixel((i,j),col)
            for i in range(val,val+100):
                for j in range(mask.size[1]):
                    col=int(128-(i-val)*128/100)
                    mask.putpixel((i,j),col)
        elif val>=300:
            #scale值靠近图像右侧边缘
            for i in range(val-100):
                for j in range(mask.size[1]):
                    col=255
                    mask.putpixel((i,j),col)
            for i in range(val-100,val):
                for j in range(mask.size[1]):
                    col=int(255-(i-val+100)*127/100)
                    mask.putpixel((i,j),col)
            for i in range(val,400):
                for j in range(mask.size[1]):
                    col=int(128-(i-val)*128/(400-val))
                    mask.putpixel((i,j),col)
        else:
            #scale值在图像中部
            for i in range(val-100):
                for j in range(mask.size[1]):
                    col=255
                    mask.putpixel((i,j),col)
            for i in range(val-100,val+100):
                for j in range(mask.size[1]):
                    col=int(255-(i-val+100)*255/200)
                    mask.putpixel((i,j),col)
        #使用resize将mask尺寸快速拉伸到img1尺寸
        mask=mask.resize((w,h), IM.ANTIALIAS)
        self.img3=ICs.composite(self.img1,self.img2,mask)
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

    def mix_light(self):
        #高光混合图片
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        self.img2=self.img2.resize((self.img1.size[0],self.img1.size[1]), IM.ANTIALIAS)
        self.img3=ICs.lighter(self.img1,self.img2)
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

    def mix_dark(self):
        #阴影混合图片
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        self.img2=self.img2.resize((self.img1.size[0],self.img1.size[1]), IM.ANTIALIAS)
        self.img3=ICs.darker(self.img1,self.img2)
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

    def mix_fill(self):
        #填充混合图片
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        im0=self.img1.convert('L')
        im1=IOs.autocontrast(im0,cutoff=self.s1_value.get()/3)
        self.img2=self.img2.resize((self.img1.size[0],self.img1.size[1]), IM.ANTIALIAS)
        self.img3=ICs.composite(self.img1,self.img2,im1)
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

    def mix_difference(self):
        #反差混合
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        self.img2=self.img2.resize((self.img1.size[0],self.img1.size[1]), IM.ANTIALIAS)
        self.img3=ICs.difference(self.img1,self.img2)
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

    def mix_screen(self):
        #乘法混合(亮)
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        self.img2=self.img2.resize((self.img1.size[0],self.img1.size[1]), IM.ANTIALIAS)
        self.img3=ICs.screen(self.img1,self.img2)
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

    def mix_multiply(self):
        #乘法混合(暗)
        w=self.img1.size[0]
        h=self.img1.size[1]
        ratio=float(w/h)
        self.img2=self.img2.resize((self.img1.size[0],self.img1.size[1]), IM.ANTIALIAS)
        self.img3=ICs.multiply(self.img1,self.img2)
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)
    def rotate_result(self):
        self.img3=self.img3.transpose(IM.ROTATE_90)
        w=self.img3.size[0]
        h=self.img3.size[1]
        ratio=w/h
        if ratio>=1.77:
            self.photo3=ITk.PhotoImage(self.img3.resize((755, int(h * 755 / w)), IM.ANTIALIAS))
        else:
            self.photo3=ITk.PhotoImage(self.img3.resize((int(w * 425 / h), 425), IM.ANTIALIAS))
        self.canvas_result.create_image(380,220,image=self.photo3)

mp=MixPhoto()
