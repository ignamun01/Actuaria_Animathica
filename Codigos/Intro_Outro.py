from manim import *
from numpy import SHIFT_OVERFLOW
     
class IntroPro(Scene):
    
    def construct(self):
        # creation of circle
        radius = 1
        circ = Circle(radius,fill_color=WHITE, fill_opacity=1, color=WHITE)
        circ.shift(1*UP)
        self.play(DrawBorderThenFill(circ))
        
        t_7 = Tex('''$f$''', color=BLACK, font_size=144)
        t_7.shift(1*UP+0.05*LEFT)
        t_6= Tex('''$xyz$''',color= BLACK,font_size=30)
        t_6.shift(0.20*RIGHT+0.45*DOWN+1*UP)
        anm= Text('ANIMATHICA')
        anm.shift(1*DOWN)
        sal= Text('Bienvenido de nuevo',color='WHITE',font_size=28)
        sal.shift(2*DOWN)
        
        self.play(Write(t_7),Write(t_6))
        self.play(DrawBorderThenFill(anm))
        self.play(Create(sal),run_time=1)
        self.wait(0.5)
        
        self.play(Flash(circ,line_length=0.3,
            num_lines=30, color=YELLOW,
            flash_radius=radius+SMALL_BUFF,
            time_width=0.2, run_time=2,
            rate_func = rush_from))
        self.wait(1)




class OutroPro(Scene):
    
    def construct(self):
        # creation of circle
        radius = 1
        circ = Circle(radius,fill_color=WHITE, fill_opacity=1, color=WHITE)
        #circ.shift(1*UP)
        self.play(DrawBorderThenFill(circ))

        #Creacion de texto
        t_7 = Tex('''$f$''', color=BLACK, font_size=144)
        t_7.shift(0.05*LEFT)
        t_6= Tex('''$xyz$''',color= BLACK,font_size=30)
        t_6.shift(0.20*RIGHT+0.45*DOWN)
        anm= Text('ANIMATHICA')
        anm.shift(2*DOWN)
        sus= Text('Suscribete y dale like',color='WHITE',font_size=28)
        sus.shift(3*DOWN)

        #INICIO DE ANIMACION
        self.play(Write(t_7),Write(t_6))
        self.play(DrawBorderThenFill(anm))
        self.play(FadeIn(sus))
        self.wait(1)
        
        self.play(Flash(circ,line_length=0.3,
            num_lines=30, color=YELLOW,
            flash_radius=radius+SMALL_BUFF,
            time_width=0.2, run_time=1.5,
            rate_func = rush_from))
        self.wait(0.5)
