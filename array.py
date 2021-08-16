from manim import *
config["tex_template"] = TexTemplateLibrary.simple


class HelloWorld(Scene):
    def construct(self):
        image=ImageMobject("logo.png").move_to(RIGHT*6+UP*3)
        self.add(image)


        text=MarkupText("什么是数组？").scale(1)
        self.play(Create(text),run_time=1)

        #这句话上移
        self.play(ApplyMethod(text.shift,UP*3),run_time=3)
        self.wait(1)

        #声明整数
        text1=Text("int student;",t2c={'[3:-1]': RED},color=BLUE,slant=ITALIC).scale(1)
        text1.next_to(text,2*DOWN+LEFT)
        self.play(Create(text1),run_time=1)

        #画一个盒子
        box1=Square().scale(0.5)
        box1.set_fill(PINK, opacity=0.5)
        box1.next_to(text1,3*RIGHT)
        self.play(Create(box1))

        #标出变量名
        box1Name=Text("student",color=RED,slant=ITALIC).scale(0.4)
        box1Name.next_to(box1,0)
        self.play(Create(box1Name))

        #声明数组
        text2=Text("int student[4];",t2c={'[3:-5]': RED},color=BLUE,slant=ITALIC).scale(1)
        text2.next_to(text1,3*DOWN)
        self.play(Create(text2),run_time=3)

        #画4个盒子
        boxes=[]
        for i in range(4):
            box=Square().scale(0.7)
            box.set_fill(PINK, opacity=0.5)
            if i==0:
                box.next_to(text2,2*DOWN)
            else:
                box.next_to(boxes[-1],2*RIGHT)
            boxes.append(box)
            self.play(Create(box))

            #创建标签
            texts=Text("student["+str(i)+"]",color=RED,slant=ITALIC).scale(0.4)
            texts.next_to(box,0)
            self.play(Create(texts))
        

# 数组的使用
class UseOfArray(Scene):
    def construct(self):
        image=ImageMobject("logo.png").move_to(RIGHT*6+UP*3)
        self.add(image)

        #声明数组
        text=Text("int student[4];",t2c={'[3:-5]': RED},color=BLUE,slant=ITALIC).scale(1)
        text.shift(LEFT+3*UP)
        self.play(Create(text),run_time=3)

        #数组名
        arrayName=Text("数组名").scale(0.7)
        arrayName.shift(2*LEFT+UP)
        self.play(Create(arrayName),run_time=2)
        arrow1=Arrow(arrayName,[-2,3,0])
        self.play(Create(arrow1),run_time=2)

        #数组大小
        arraySize=Text("数组大小").scale(0.7)
        arraySize.next_to(arrayName,2*RIGHT)
        self.play(Create(arraySize),run_time=2)
        arrow2=Arrow(arraySize,[0.5,3,0])
        self.play(Create(arrow2),run_time=2)

        #数组中的每一个元素
        everyElement=Text("数组中的4个元素为：").scale(0.7)
        everyElement.next_to(arrayName,2*DOWN)
        self.play(Create(everyElement))

        #展示4个盒子
        textArray=[]
        boxes=[]
        for i in range(4):
            box=Square().scale(0.7)
            box.set_fill(PINK, opacity=0.5)
            if i==0:
                box.next_to(everyElement,LEFT+DOWN*2)
            else:
                box.next_to(boxes[-1],2*RIGHT)
            boxes.append(box)
            self.play(Create(box))

            #创建标签
            texts=TexMobject("student","["+str(i)+"]",color=RED,slant=ITALIC).scale(0.6)
            texts.next_to(box,0)
            textArray.append(texts)
            self.play(Create(texts))

        self.wait(3)
        
        #放大元素
        animations=[
            ScaleInPlace(boxes[0],2),
            ScaleInPlace(textArray[0],2),
            FadeOut(everyElement),
            FadeOut(text),
            FadeOut(arrayName),
            FadeOut(arraySize),
            FadeOut(arrow1),
            FadeOut(arrow2),  
        ]
        for i in range(1,4):
            animations.append(FadeOut(textArray[i]))
            animations.append(FadeOut(boxes[i]))

        
        self.play(AnimationGroup(*animations))

        #移动位置
        self.play(ApplyMethod(boxes[0].move_to,0))
        self.play(ApplyMethod(textArray[0].move_to,0))

        #消除
        self.play(FadeOut(boxes[0]))

        #分离
        self.play(ApplyMethod(textArray[0][0].shift,LEFT))
        self.play(ApplyMethod(textArray[0][1].shift,RIGHT))

        #名称
        arrayName=Text("数组名").scale(0.7)
        arrayName.next_to(textArray[0][0],DOWN)
        self.play(Create(arrayName),run_time=2)

        #下标
        arrayIndex=Text("下标").scale(0.7)
        arrayIndex.next_to(textArray[0][1],DOWN)
        self.play(Create(arrayIndex),run_time=2)

        #创建+号
        addText=Text("+").scale(1)
        addText.next_to(arrayName,RIGHT*1.5)
        self.play(Create(addText),run_time=2)

        #移动下标
        self.play(ApplyMethod(arrayIndex.shift,LEFT*1.2+0.15*UP))

        #组合
        textGroup=VGroup(arrayName,addText,arrayIndex)

        #元素
        AnyElement=Text("数组中的元素").scale(1)
        AnyElement.shift(DOWN*1.5)
        self.play(Transform(textGroup,AnyElement))


#数组的初始化
class InitialOfArray(Scene):
    def construct(self):
        #标题
        title = Title("The Initial of an Array")
        self.play(Create(title))

        image=ImageMobject("logo.png").move_to(RIGHT*6+UP*3)
        self.add(image)

        #数组
        text=Text("int student[4];",t2c={'[3:-5]': RED},color=BLUE,slant=ITALIC).scale(1)
        text.shift(UP*1.5)
        self.play(Create(text))

        #画四个盒子
        textArray=[]
        boxes=[]
        for i in range(4):
            box=Square().scale(0.7)
            box.set_fill(PINK, opacity=0.5)
            if i==0:
                box.next_to(text,LEFT+DOWN*2)
            else:
                box.next_to(boxes[-1],2*RIGHT)
            boxes.append(box)
            self.play(Create(box))

            #创建标签
            texts=TexMobject("student","["+str(i)+"]",color=RED,slant=ITALIC).scale(0.6)
            texts.next_to(box,0)
            textArray.append(texts)
            self.play(Create(texts))

        #初始化状态
        initialState=Text("未被初始化")
        initialState.shift(DOWN*2)
        self.play(Create(initialState))

        self.wait(3)

        #修改初始化
        newText=Text("int student[4]={1,2,3,4};",t2c={'[3:13]': RED},color=BLUE,slant=ITALIC).scale(1)
        newText.shift(UP*1.5)
        self.play(Transform(text,newText))

        textGroup=VGroup()
        labels=[]
        #四个变量值
        for i in range(4):
            arrayValue=Text(str(i+1),color=BLUE)
            arrayValue.next_to(boxes[i],DOWN)
            textGroup.add(arrayValue)
            labels.append(arrayValue)
        
        #变换
        self.play(Transform(initialState,textGroup))

        self.wait(3)

        #数组赋值
        text=Text("student[2]=0;",t2c={'[0:10]': RED},color=BLUE,slant=ITALIC).scale(1)
        text.shift(DOWN*2)
        self.play(Create(text))

        newTextGroup=VGroup()
        for i in range(4):
            if i==2:
                arrayValue=Text("0",color=RED)
            else:
                arrayValue=Text(str(i+1),color=BLUE)
            arrayValue.next_to(labels[i],0)
            newTextGroup.add(arrayValue)

        self.play(Transform(textGroup,newTextGroup))
        
        

        self.wait(3)