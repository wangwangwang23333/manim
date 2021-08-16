from manim import *
config["tex_template"] = TexTemplateLibrary.simple

class Ascend(Scene):
    def construct(self):
        #标题
        title = Title("Ascend or Discend")
        self.play(Create(title))

        image=ImageMobject("logo.png").move_to(RIGHT*6+UP*3)
        self.add(image)

        text=Text("int student[5]={1,2,3,4,5};",t2c={'[3:13]': RED},color=BLUE,slant=ITALIC).scale(1)
        text.shift(UP*2)
        self.play(Create(text))

        #画5个长度大小不等的矩形
        arrs=[1,2,3,4,5]
        rects=[]
        rectGroup=VGroup()
        for i,item in enumerate(arrs):
            rect=Rectangle(width=0.5,height=item*0.5)
            rect.set_fill(PINK, opacity=0.5)
            if i==0:
                rect.shift(3*LEFT+2*DOWN)
                pass
            else:
                rect.align_to(rects[0],DOWN)
                rect.shift(3*LEFT+RIGHT*1.5*i)
                print(RIGHT)
            
            #变量值
            rectValue=Text(str(item))
            rectValue.next_to(rect,UP)
            rectGroup.add(rectValue)

            rects.append(rect)
            rectGroup.add(rect)
        
        self.play(Create(rectGroup))

        arrayIndexGroup=VGroup()
        for i in range(5):
            #标记变量名
            arrayIndex=TexMobject("student","["+str(i)+"]",color=RED,slant=ITALIC).scale(0.6)
            arrayIndex.next_to(rects[i],DOWN)
            arrayIndexGroup.add(arrayIndex)
            rectGroup.add(arrayIndexGroup)
        
        self.play(Create(arrayIndexGroup))

        self.wait(3)

        #升序箭头
        ascendingArrow=Arrow([-3.5,-0.8,0],[4,1.6,0])
        self.play(Create(ascendingArrow))
        self.wait(3)
        rectGroup.add(ascendingArrow)

        #升序标签
        ascendingLabel=Text("升序数组")
        ascendingLabel.next_to(ascendingArrow,DOWN)
        self.play(Transform(rectGroup,ascendingLabel))
        self.wait(3)
        self.remove(rectGroup)
        #移动到合适的位置
        self.play(ApplyMethod(ascendingLabel.shift,UP),run_time=3)


#降序数组演示
class Discend(Scene):
    def construct(self):
        #标题
        title = Title("Ascend or Discend")
        self.play(Create(title))

        image=ImageMobject("logo.png").move_to(RIGHT*6+UP*3)
        self.add(image)

        text=Text("int student[5]={5,4,3,2,1};",t2c={'[3:13]': RED},color=BLUE,slant=ITALIC).scale(1)
        text.shift(UP*2)
        self.play(Create(text))

        #画5个长度大小不等的矩形
        arrs=[5,4,3,2,1]
        rects=[]
        rectGroup=VGroup()
        for i,item in enumerate(arrs):
            rect=Rectangle(width=0.5,height=item*0.5)
            rect.set_fill(PINK, opacity=0.5)
            if i==0:
                rect.shift(3*LEFT+2*DOWN)
                pass
            else:
                rect.align_to(rects[0],DOWN)
                rect.shift(3*LEFT+RIGHT*1.5*i)
                print(RIGHT)
            
            #变量值
            rectValue=Text(str(item))
            rectValue.next_to(rect,UP)
            rectGroup.add(rectValue)

            rects.append(rect)
            rectGroup.add(rect)
        
        self.play(Create(rectGroup))

        arrayIndexGroup=VGroup()
        for i in range(5):
            #标记变量名
            arrayIndex=TexMobject("student","["+str(i)+"]",color=RED,slant=ITALIC).scale(0.6)
            arrayIndex.next_to(rects[i],DOWN)
            arrayIndexGroup.add(arrayIndex)
            rectGroup.add(arrayIndexGroup)
        
        self.play(Create(arrayIndexGroup))

        self.wait(3)

        #升序箭头
        ascendingArrow=Arrow([-3.5,1.6,0],[4,-0.8,0])
        self.play(Create(ascendingArrow))
        self.wait(3)
        rectGroup.add(ascendingArrow)

        #升序标签
        ascendingLabel=Text("降序数组")
        ascendingLabel.next_to(ascendingArrow,DOWN)
        self.play(Transform(rectGroup,ascendingLabel))
        self.wait(3)
        self.remove(rectGroup)
        #移动到合适的位置
        self.play(ApplyMethod(ascendingLabel.shift,UP),run_time=3)

#无序数组
class NoOrderArray(Scene):
    def construct(self):
        #标题
        title = Title("Ascend or Discend")
        self.play(Create(title))

        image=ImageMobject("logo.png").move_to(RIGHT*6+UP*3)
        self.add(image)

        text=Text("int student[5]={3,2,5,4,1};",t2c={'[3:13]': RED},color=BLUE,slant=ITALIC).scale(1)
        text.shift(UP*2)
        self.play(Create(text))

        #画5个长度大小不等的矩形
        arrs=[3,2,5,4,1]
        rects=[]
        rectGroup=VGroup()
        for i,item in enumerate(arrs):
            rect=Rectangle(width=0.5,height=item*0.5)
            rect.set_fill(PINK, opacity=0.5)
            if i==0:
                rect.shift(3*LEFT+2*DOWN)
                pass
            else:
                rect.align_to(rects[0],DOWN)
                rect.shift(3*LEFT+RIGHT*1.5*i)
                print(RIGHT)
            
            #变量值
            rectValue=Text(str(item))
            rectValue.next_to(rect,UP)
            rectGroup.add(rectValue)

            rects.append(rect)
            rectGroup.add(rect)
        
        self.play(Create(rectGroup))

        arrayIndexGroup=VGroup()
        for i in range(5):
            #标记变量名
            arrayIndex=TexMobject("student","["+str(i)+"]",color=RED,slant=ITALIC).scale(0.6)
            arrayIndex.next_to(rects[i],DOWN)
            arrayIndexGroup.add(arrayIndex)
            rectGroup.add(arrayIndexGroup)
        
        self.play(Create(arrayIndexGroup))

        self.wait(3)

        #升序箭头
        ascendingArrow=Arrow([-3.5,1.6,0],[4,-0.8,0])
        self.play(Create(ascendingArrow))
        self.wait(3)

        self.play(FadeOut(ascendingArrow))

        #升序箭头
        ascendingArrow=Arrow([-3.5,-0.8,0],[4,1.6,0])
        self.play(Create(ascendingArrow))
        self.wait(3)

        self.play(FadeOut(ascendingArrow))
        
        

        #升序标签
        ascendingLabel=Text("无序数组")
        ascendingLabel.next_to(ascendingArrow,DOWN)
        self.play(Transform(rectGroup,ascendingLabel))
        self.wait(3)
        self.remove(rectGroup)
        #移动到合适的位置
        self.play(ApplyMethod(ascendingLabel.shift,UP),run_time=3)

#排序过程演示
class arraySort(Scene):
    def construct(self):
        #标题
        title = Title("Sort")
        self.play(Create(title))

        image=ImageMobject("logo.png").move_to(RIGHT*6+UP*3)
        self.add(image)

        #画5个长度大小不等的矩形
        arrs=[3,2,5,4,1]
        rects=[]
        rectGroup=VGroup()
        rectWithLabel=[]
        for i,item in enumerate(arrs):
            rect=Rectangle(width=0.5,height=item*0.5)
            rect.set_fill(PINK, opacity=0.5)
            if i==0:
                rect.shift(3*LEFT+DOWN)
                pass
            else:
                rect.align_to(rects[0],DOWN)
                rect.shift(3*LEFT+RIGHT*1.5*i)
            
            #变量值
            rectValue=Text(str(item))
            rectValue.next_to(rect,UP)
            rectGroup.add(rectValue)

            rects.append(rect)
            rectGroup.add(rect)

            rectWithLabel.append(VGroup(rect,rectValue))
        
    
        #排序后的版本
        sortRect=[]
        for i in range(5):
            rect=Rectangle(width=0.5,height=(i+1)*0.5)
            rect.set_fill(RED, opacity=0.5)
            if i==0:
                rect.shift(3*LEFT+1.5*DOWN)
                pass
            else:
                rect.align_to(rects[0],DOWN)
                rect.shift(3*LEFT+RIGHT*1.5*i)
            
            #变量值
            rectValue=Text(str(i+1))
            rectValue.next_to(rect,UP)

            sortRect.append(VGroup(rect,rectValue))
        
        self.play(Create(rectGroup),run_time=4)

        #最小值
        minLabel=Text("最小值").scale(0.6)
        minLabel.next_to(rects[0],UP*5+LEFT*4)
        self.play(Create(minLabel))

        #箭头指在第一个
        minArrow=Arrow([-3,-3,0],[-3,-2,0])
        self.play(Create(minArrow))

        #闪烁
        for i in range(2):
            self.play(FadeOut(rects[0]),run_time=1)
            self.play(FadeIn(rects[0]),run_time=1)
        
        #长度最长的矩形
        rectangle=Rectangle(width=0.5,height=1.5)
        rectangle.set_fill(PINK, opacity=0.5)
        rectangle.align_to(rects[0],DOWN)
        rectangle.shift(4.8*LEFT)
        self.play(Create(rectangle))
        

        #最小值value
        minValue=Text("3").scale(0.6)
        minValue.next_to(minLabel,RIGHT)
        self.play(Create(minValue))

        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[1]),run_time=1)
            self.play(FadeIn(rects[1]),run_time=1)
        
        #矩形长度变化
        newRectangle=Rectangle(width=0.5,height=1.0)
        newRectangle.set_fill(PINK, opacity=0.5)
        newRectangle.align_to(rects[0],DOWN)
        newRectangle.shift(4.8*LEFT)
        self.play(Transform(rectangle,newRectangle))

        newMinValue=Text("2").scale(0.6)
        newMinValue.next_to(minLabel,RIGHT)
        self.play(Transform(minValue,newMinValue))

        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[2]),run_time=1)
            self.play(FadeIn(rects[2]),run_time=1)
        

        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[3]),run_time=1)
            self.play(FadeIn(rects[3]),run_time=1)
        
        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[4]),run_time=1)
            self.play(FadeIn(rects[4]),run_time=1)

        newRectangle=Rectangle(width=0.5,height=0.5)
        newRectangle.set_fill(PINK, opacity=0.5)
        newRectangle.align_to(rects[0],DOWN)
        newRectangle.shift(4.8*LEFT)
        self.play(Transform(rectangle,newRectangle))

        newMinValue=Text("1").scale(0.6)
        newMinValue.next_to(minLabel,RIGHT)
        self.play(Transform(minValue,newMinValue))

        self.wait(3)

        #最小值和第一个元素交换位置
        self.play(ApplyMethod(rectWithLabel[0].shift,6*RIGHT))
        self.play(ApplyMethod(rectWithLabel[4].shift,6*LEFT))

        rectWithLabel[0],rectWithLabel[4]=rectWithLabel[4],rectWithLabel[0]
        rects[0],rects[4]=rects[4],rects[0]

        #0需要变色
        self.play(Transform(rectWithLabel[0],sortRect[0]))

        #清除当前这一轮龚总
        self.play(FadeOut(rectangle),
        FadeOut(minValue))

        #箭头移动回来
        self.play(ApplyMethod(minArrow.shift,4.5*LEFT))

        for i in range(2):
            self.play(FadeOut(rects[1]),run_time=1)
            self.play(FadeIn(rects[1]),run_time=1)
        
        #矩形长度变化
        newRectangle=Rectangle(width=0.5,height=1.0)
        newRectangle.set_fill(PINK, opacity=0.5)
        newRectangle.align_to(rects[0],DOWN)
        newRectangle.shift(4.8*LEFT)
        self.play(Transform(rectangle,newRectangle))

        newMinValue=Text("2").scale(0.6)
        newMinValue.next_to(minLabel,RIGHT)
        self.play(Transform(minValue,newMinValue))

        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[2]),run_time=1)
            self.play(FadeIn(rects[2]),run_time=1)
        

        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[3]),run_time=1)
            self.play(FadeIn(rects[3]),run_time=1)
        
        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[4]),run_time=1)
            self.play(FadeIn(rects[4]),run_time=1)

        #1需要变色
        self.play(Transform(rectWithLabel[1],sortRect[1]))

        #清除当前这一轮龚总
        self.play(FadeOut(rectangle),
        FadeOut(minValue))

        #箭头移动回来
        self.play(ApplyMethod(minArrow.shift,3*LEFT))

        for i in range(2):
            self.play(FadeOut(rects[2]),run_time=1)
            self.play(FadeIn(rects[2]),run_time=1)

        #矩形长度变化
        newRectangle=Rectangle(width=0.5,height=2.5)
        newRectangle.set_fill(PINK, opacity=0.5)
        newRectangle.align_to(rects[0],DOWN)
        newRectangle.shift(4.8*LEFT)
        self.play(Transform(rectangle,newRectangle))

        newMinValue=Text("5").scale(0.6)
        newMinValue.next_to(minLabel,RIGHT)
        self.play(Transform(minValue,newMinValue))


        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[3]),run_time=1)
            self.play(FadeIn(rects[3]),run_time=1)

        #矩形长度变化
        newRectangle=Rectangle(width=0.5,height=2.0)
        newRectangle.set_fill(PINK, opacity=0.5)
        newRectangle.align_to(rects[0],DOWN)
        newRectangle.shift(4.8*LEFT)
        self.play(Transform(rectangle,newRectangle))

        newMinValue=Text("4").scale(0.6)
        newMinValue.next_to(minLabel,RIGHT)
        self.play(Transform(minValue,newMinValue))

        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[4]),run_time=1)
            self.play(FadeIn(rects[4]),run_time=1)

        #矩形长度变化
        newRectangle=Rectangle(width=0.5,height=1.5)
        newRectangle.set_fill(PINK, opacity=0.5)
        newRectangle.align_to(rects[0],DOWN)
        newRectangle.shift(4.8*LEFT)
        self.play(Transform(rectangle,newRectangle))

        newMinValue=Text("3").scale(0.6)
        newMinValue.next_to(minLabel,RIGHT)
        self.play(Transform(minValue,newMinValue))

        #最小值和第3个元素交换位置
        self.play(ApplyMethod(rectWithLabel[2].shift,3*RIGHT))
        self.play(ApplyMethod(rectWithLabel[4].shift,3*LEFT))

        rectWithLabel[2],rectWithLabel[4]=rectWithLabel[4],rectWithLabel[2]
        rects[2],rects[4]=rects[4],rects[2]

        #0需要变色
        self.play(Transform(rectWithLabel[2],sortRect[2]))

        #清除当前这一轮龚总
        self.play(FadeOut(rectangle),
        FadeOut(minValue))

        #箭头移动回来
        self.play(ApplyMethod(minArrow.shift,1.5*LEFT))

        for i in range(2):
            self.play(FadeOut(rects[3]),run_time=1)
            self.play(FadeIn(rects[3]),run_time=1)

        #矩形长度变化
        newRectangle=Rectangle(width=0.5,height=2.0)
        newRectangle.set_fill(PINK, opacity=0.5)
        newRectangle.align_to(rects[0],DOWN)
        newRectangle.shift(4.8*LEFT)
        self.play(Transform(rectangle,newRectangle))

        newMinValue=Text("4").scale(0.6)
        newMinValue.next_to(minLabel,RIGHT)
        self.play(Transform(minValue,newMinValue))

        #箭头向右移动
        self.play(ApplyMethod(minArrow.shift,1.5*RIGHT))

        for i in range(2):
            self.play(FadeOut(rects[4]),run_time=1)
            self.play(FadeIn(rects[4]),run_time=1)
        
        #3需要变色
        self.play(Transform(rectWithLabel[3],sortRect[3]))

        #清除当前这一轮龚总
        self.play(FadeOut(rectangle),
        FadeOut(minValue))

        for i in range(2):
            self.play(FadeOut(rects[4]),run_time=1)
            self.play(FadeIn(rects[4]),run_time=1)
        
        self.play(Transform(rectWithLabel[4],sortRect[4]))

        #排序完成
        self.wait(3)

        self.play(
        FadeOut(minArrow),
        FadeOut(minLabel))

        #绘制一个箭头
        ascendingArrow=Arrow([-3.5,-0.4,0],[4,2,0])
        self.play(Create(ascendingArrow))
        

        #升序标签
        ascendingLabel=Text("升序数组")
        ascendingLabel.next_to(ascendingArrow,UP*0.5)
        self.play(Transform(ascendingArrow,ascendingLabel))
        self.wait(3)
