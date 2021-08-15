from manim import *
config["tex_template"] = TexTemplateLibrary.simple


class HelloWorld(Scene):
    def construct(self):
        image=ImageMobject("logo.png").move_to(RIGHT*6+UP*3)
        self.add(image)


        text=MarkupText("我们真的要像这样声明变量吗？").scale(1)
        self.play(Create(text),run_time=3)
        firstLabel=text

        #这句话上移
        self.play(ApplyMethod(text.shift,UP*3),run_time=3)
        self.wait(1)

        scores=[78,45,98,101,87]

        texts=[]

        #声明变量
        for i in range(5):
            text1=Text("int student"+str(i+1)+"= "+str(scores[i])+";",t2c={'[3:11]': RED},color=BLUE,slant=ITALIC).scale(1)
            #设置位置靠近上一句话
            text1.next_to(text,DOWN)
            texts.append(text1)
            self.play(Create(text1),run_time=2)
            text=text1
        
        self.wait(1)
        #整体缩小
        
        self.play(ScaleInPlace(texts[0],0.6),
        ScaleInPlace(texts[1],0.6),   
        ScaleInPlace(texts[2],0.6),
        ScaleInPlace(texts[3],0.6),
        ScaleInPlace(texts[4],0.6),
        run_time=3)

        for i in range(1,5):
            self.play(ApplyMethod(texts[i].shift, (0.2+i*0.2)*UP))

        #self.play(ApplyMethod(texts[0].shift, 0.4*UP), run_time=3)

        #省略号
        text1=Text("这里省略掉很多重复的操作").scale(0.6)
        text1.next_to(texts[4],DOWN)
        self.play(Create(text1),run_time=2)
        label=text1


        #最后一个变量
        text1=Text("int student59= 87;",t2c={'[3:12]': RED},color=BLUE,slant=ITALIC).scale(0.6)
        text1.next_to(label,DOWN)
        self.play(Create(text1),run_time=2)

        #清屏
        animations = [
            FadeOut(firstLabel, shift=DOWN),
            FadeOut(texts[0], shift=DOWN),
            FadeOut(texts[1], shift=DOWN),
            FadeOut(texts[2], shift=DOWN),
            FadeOut(texts[3], shift=DOWN),
            FadeOut(texts[4], shift=DOWN),
            FadeOut(label, shift=DOWN),
            FadeOut(text1, shift=DOWN)
        ]

        self.play(AnimationGroup(*animations, lag_ratio=0.5))

        #其他方法
        text=MarkupText("那么，有没有什么其他方法呢？").scale(1)
        self.play(Create(text),run_time=3)
        firstLabel=text

        #这句话上移
        self.play(ApplyMethod(text.shift,UP*3),run_time=3)
        self.wait(1)

        squares=[]
        animations=[]
        texts=[]
        #画盒子
        for i in range(5):
            square=Square()
            text=Text("student"+str(i)).scale(0.5)
            square.set_fill(PINK, opacity=0.5)  # set the color and transparency
            if i==0:
                square.shift(LEFT*4)
                text.shift(LEFT*4)
            else:
                square.next_to(squares[-1],RIGHT)
                text.next_to(squares[-1],RIGHT*1.6)
            squares.append(square)
            texts.append(text)

            animations.append(Create(square))
            animations.append(Create(text))
        self.play(AnimationGroup(*animations, lag_ratio=0.5))
        self.wait(1)

        text=Text("如果能够像学生一样被编号并且整齐排列，").scale(1)
        text.shift(2*DOWN)
        self.play(Create(text),run_time=3)

        text1=Text("是不是就好管理了呢？").scale(1)
        text1.next_to(text,DOWN)
        self.play(Create(text1),run_time=3)

