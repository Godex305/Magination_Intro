from manim import *
import random
config.pixel_height=1080
config.pixel_width=1920
config.frame_height=9
config.frame_width=16

class MaginationIntro(Scene):
    def construct(self):
        grid = NumberPlane()
        #self.add(grid)
        colors = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK]
        w1 = Text("मेजि",font="Tiro Devanagari Hindi",font_size=72,color=random.choice(colors)).scale(2).shift(0.45*UP)
        w2 = Text('N',font_size=72,color=random.choice(colors)).scale(2)
        w3 = Text('A',font_size=72,color=random.choice(colors)).scale(2)
        w4 = Text('T',font_size=72,color=random.choice(colors)).scale(2)
        w5 = Text('I',font_size=72,color=random.choice(colors)).scale(2)
        w6 = Text('O',font_size=72,color=random.choice(colors)).scale(2)
        w7 = Text('N',font_size=72,color=random.choice(colors)).scale(2)   
        c=Cross(color=random.choice(colors),fill_opacity=0.5).scale(0.7)
        s = Square(color=random.choice(colors),fill_opacity=0.5).scale(0.7)
        t = RegularPolygon(3,color=random.choice(colors),fill_opacity=0.5).scale(0.7)
        p = RegularPolygon(5,color=random.choice(colors),fill_opacity=0.5).scale(0.7)
        h = Rectangle(height = 1, width = 2 ,color=random.choice(colors),fill_opacity=0.5).scale(0.7)
        hep = RegularPolygon(7,color=random.choice(colors),fill_opacity=0.5).scale(0.7)
        oct = Ellipse(width=2,height = 1,color=random.choice(colors),fill_opacity=0.5).scale(0.7)

        polys = VGroup(*[c,s,t,p,h,hep,oct] ).arrange(RIGHT)
        self.add(polys)
        self.play(Rotate(shapes, 3*PI, run_time = 3) for shapes in polys)
        words = VGroup(*[(w1,w2,w3,w4,w5,w6,w7) for j in range(7)]).arrange(RIGHT)
        Logo = self.play(AnimationGroup(*[
            Transform(c,words[0]),
            Transform(s,words[1]),
            Transform(t,words[2]),
            Transform(p,words[3]),
            Transform(h,words[4]),
            Transform(hep,words[5]),
            Transform(oct,words[6]),
            ], lag_ratio=0))
        self.play(AnimationGroup(Indicate(word) for word in words))
        Slogan = Text("helps you to think...", font_size=30)
        Slogan.move_to([5,-1.2,0])
        self.play(Write(Slogan))
        self.play(FadeOut(*self.mobjects))

class ComingSoon(Scene):
    def construct(self):
        comingsoon = Text("Coming Soon",font_size=60).scale(3)
        self.play(Write(comingsoon),buff = 0.8)
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

class Credits(Scene):
    def construct(self):
        by = Text("by").scale(0.7)
        by.move_to([-4.5,0,0])
        JayJhala = Text("Jay Jhala").scale(2)
        JayJhala.next_to(by,RIGHT)
        And = Text('&').scale(0.7)
        And.next_to(JayJhala,RIGHT)
        team = Text("Team").scale(1.5)
        team.next_to(And,RIGHT)
        self.play(FadeIn(by))
        self.play(Write(JayJhala,run_time=2))
        self.play(Write(And))
        self.play(FadeIn(team,run_time=2))



