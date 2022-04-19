from manim import *
config.background_color = YELLOW_A
config["background_color"] = YELLOW_A


###########################################################################################
##############################  Escena 1  #################################################
###########################################################################################

#Escena_1: Dinero en el tiempo
class Escena_1(Scene):
    def construct(self):
        #Graficas/Lineas
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=5,
            color=GRAY,
            include_tip=True,
            label_direction=UP,
            include_ticks=False
        )
        l0.shift(1*DOWN+0.4*LEFT)

        l1 = NumberLine(
            x_range=[1, 7, 1],
            length=12,
            color=PURE_BLUE,
            include_tip=True,
            label_direction=UP,
            include_ticks=True,
            tick_size=0.40
        )

        l1.shift(2*DOWN)

        #Textos

        texto_1= Tex("El monto inicial invertido lo conocemos como “principal” y al monto\n"
        "recibido después del periodo de tiempo lo conocemos como el \n"
        " “valor acumulado”.", color= BLACK, font_size=38)
        mob_1= SurroundingRectangle(texto_1, corner_radius=0.1, color= BLACK)
        k_0=VGroup(texto_1,mob_1)
        k_0.shift(1.5*UP)

        #Objetos
        inner_1 = Text("Principal", color= PURE_RED).scale(0.5)
        mob_1 = SurroundingRectangle(inner_1, corner_radius=0.1, color= PURE_RED)  
        k_1=VGroup(inner_1,mob_1)
        k_1.shift(4*LEFT + 1*DOWN)

        inner_2 = Text("Valor Acumulado", color= PURE_RED).scale(0.5) 
        mob_2 = SurroundingRectangle(inner_2, corner_radius=0.1, color= PURE_RED)  
        k_2=VGroup(inner_2,mob_2)
        k_2.shift(4*RIGHT + 1*DOWN)

        inner_3 = Text("k", color= PURE_BLUE).scale(0.5)
        mob_3 = SurroundingRectangle(inner_3, corner_radius=0.1, color= PURE_BLUE)  
        k_3=VGroup(inner_3,mob_3)
        k_3.shift(4*LEFT + 2.75*DOWN)

        inner_4 = Text("n", color= PURE_BLUE).scale(0.5) 
        mob_4 = SurroundingRectangle(inner_4, corner_radius=0.1, color= PURE_BLUE)  
        k_4=VGroup(inner_4,mob_4)
        k_4.shift(4*RIGHT + 2.75*DOWN)

        texto_2=Text("Monto", color= BLACK).scale(0.5)
        texto_2.shift(6*LEFT + 1.15*DOWN)
        texto_3=Text("Tiempo", color= BLACK).scale(0.5)
        texto_3.shift(6*LEFT + 2.75*DOWN)

        t_t= Text("t", color= GRAY).scale(0.5)
        t_t.shift(0.75*DOWN + 0.4*LEFT)
        

        #Escena
        self.play(FadeIn(k_0), FadeIn(l1), FadeIn(texto_2), FadeIn(texto_3), run_time = 4)
        self.wait(2)
        self.play(Write(k_1), Write(k_3))
        self.wait(2)
        self.play(Write(k_2), Write(k_4))
        self.wait(2)
        self.play(Write(l0), Write(t_t) )
        self.wait(2)
        self.play(Write(l0), Write(t_t))
        self.wait(2)


###########################################################################################
##############################  Escena 2  #################################################
###########################################################################################

#Escena_1: Dinero en el tiempo
class Escena_2(Scene):
    def construct(self):
        #Graficas/Lineas
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=5,
            color=GRAY,
            include_tip=True,
            label_direction=UP,
            include_ticks=False
        )
        l0.shift(1*DOWN+0.4*LEFT)

        l1 = NumberLine(
            x_range=[1, 7, 1],
            length=12,
            color=PURE_BLUE,
            include_tip=True,
            label_direction=UP,
            include_ticks=True,
            tick_size=0.40
        )

        l1.shift(2*DOWN)

        #Textos

        texto_1= Tex("Definimos como a(t) a la función de acumulación.", 
        color= BLACK, font_size=38)
        mob_1= SurroundingRectangle(texto_1, corner_radius=0.1, color= BLACK)
        k_0=VGroup(texto_1,mob_1)
        k_0.shift(2.5*UP)

        texto_2= Tex("Al llegar a las $t$ unidades de tiempo con $t>= 0$ tendremos $U*a(t)$ "
        "lo cual denotaremos como $A(t)$, la cual se conoce como función de monto.", 
        color= BLACK, font_size=38)
        mob_2= SurroundingRectangle(texto_2, corner_radius=0.1, color= BLACK)
        k_2_1=VGroup(texto_2,mob_2)
        k_2_1.shift(1*UP)


        #Objetos
        inner_1 = Text("1", color= PURE_RED).scale(0.5)
        mob_1 = SurroundingRectangle(inner_1, corner_radius=0.1, color= PURE_RED)  
        k_1=VGroup(inner_1,mob_1)
        k_1.shift(4*LEFT + 1*DOWN)

        inner_2 = Text("1 * a(t)", color= PURE_RED).scale(0.5) 
        mob_2 = SurroundingRectangle(inner_2, corner_radius=0.1, color= PURE_RED)  
        k_2=VGroup(inner_2,mob_2)
        k_2.shift(4*RIGHT + 1*DOWN)

        inner_3 = Text("0", color= PURE_BLUE).scale(0.5)
        mob_3 = SurroundingRectangle(inner_3, corner_radius=0.1, color= PURE_BLUE)  
        k_3=VGroup(inner_3,mob_3)
        k_3.shift(4*LEFT + 2.75*DOWN)

        inner_4 = Text("t", color= PURE_BLUE).scale(0.5) 
        mob_4 = SurroundingRectangle(inner_4, corner_radius=0.1, color= PURE_BLUE)  
        k_4=VGroup(inner_4,mob_4)
        k_4.shift(4*RIGHT + 2.75*DOWN)

        t_2=Text("Monto", color= BLACK).scale(0.5)
        t_2.shift(6*LEFT + 1.15*DOWN)
        t_3=Text("Tiempo", color= BLACK).scale(0.5)
        t_3.shift(6*LEFT + 2.75*DOWN)

        linea=VGroup(l1, l0, k_1, k_2, k_3, k_4, t_2, t_3)
        
        

        #Escena
        self.play(FadeIn(k_0), run_time = 3)
        self.wait(7)
        self.play(Write(k_2_1),run_time = 5)
        self.wait(7)
        self.play(FadeIn(linea))
        self.wait(1)

        self.play(FadeOut(k_0), FadeOut(k_2_1))
        self.wait(1)

        inner_4_1 = Text("U * a(t)", color= PURE_RED).scale(0.5) 
        mob_4_1 = SurroundingRectangle(inner_4_1, corner_radius=0.1, color= PURE_RED)  
        k_4_1=VGroup(inner_4_1,mob_4_1)
        k_4_1.shift(4*RIGHT)

        inner_5 = Text("U", color= PURE_BLUE).scale(0.5)
        mob_5 = SurroundingRectangle(inner_5, corner_radius=0.1, color= PURE_BLUE)  
        k_5=VGroup(inner_5,mob_5)
        k_5.shift(4*LEFT )

        texto_3= Tex("Si invertimos más de una unidad monetaria al llegar a tiempo $t$ "
        "obtendremos $U*a(t)$ = $A(t)$.", 
        color= BLACK, font_size=38)
        mob_2= SurroundingRectangle(texto_3, corner_radius=0.1, color= BLACK)
        k_3_1=VGroup(texto_3,mob_2)
        k_3_1.shift(1.5*UP)


        linea.generate_target()
        linea.target.shift(1*UP)

        self.play(Write(k_3_1))
        self.wait()
        self.play(MoveToTarget(linea))
        self.wait()
        self.play(ReplacementTransform(k_1, k_5))
        self.play(ReplacementTransform(k_2, k_4_1))
        self.wait(3)





###########################################################################################
##############################  Escena 3  #################################################
###########################################################################################


#Escena_2: Formas de saber la ganancia en un trato monetario.
class Escena_3(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

        #Textos 2_1

        texto_1= Text("Para esto, simplemente dividimos A(t) entre a(t).",color= BLACK, font_size=28)
        texto_1.shift(3*UP)

        txt_1=self.rectangulo_texto(texto_1)
        
        formula_1=Tex("$\\frac{A(t)}{a(t)} = \\frac{u*a(t)}{a(t)} = u$",color= PURE_RED, font_size=40)
        formula_1.shift(2.1*UP)

        texto_2=Tex("Si queremos acumular dinero de tiempo 0 a tiempo t multiplicamos U, \n"
        "que representan a las unidades monetarias, por a(t).",color= BLACK, font_size=38)
        texto_2.shift(1*UP)
        txt_2=self.rectangulo_texto(texto_2)

        formula_2=Tex("Acumular dinero = $ u * a(t) $",color= PURE_RED, font_size=35)
        formula_2.shift(.1*UP)

        texto_3=Tex("Si queremos descontar dinero de tiempo t a tiempo 0 dividimos A(t) entre a(t)",color= BLACK, font_size=38)
        texto_3.shift(1*DOWN)
        txt_3=self.rectangulo_texto(texto_3)

        formula_3=Tex("Descontar dinero = $ \\frac{A(t)}{a(t)} = \\frac{a(t)*u}{a(t)} = u$",color= PURE_RED, font_size=35)
        formula_3.shift(1.9*DOWN)


        #Escena 2_1
        self.play(Write(txt_1), run_time=2)
        self.wait(4)
        self.play(FadeIn(formula_1))
        self.wait(1)
        self.play(Write(txt_2), run_time=5)
        self.wait(2)
        self.play(FadeIn(formula_2),run_time=2)
        self.wait(2)
        self.play(Write(txt_3), run_time=3)
        self.wait(1)
        self.play(FadeIn(formula_3),run_time=2)
        self.wait(1)
        self.play(FadeOut(txt_1,txt_2,txt_3,formula_1,formula_2,formula_3))





###########################################################################################
##############################  Escena 4  #################################################
###########################################################################################

class Escena_4(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto, color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def rectangulo_textor(self,objeto):
        rect = SurroundingRectangle(objeto, color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

        #Textos
        texto_1= Tex("Ahora, ¿Qué es lo que pasa si sé que a tiempo k con k<n tengo X "
        "unidades monetarias y quiero saber cuántas  unidades monetarias Y tendré a tiempo n?",
        color= BLACK, font_size=35)
        texto_1.shift(2.5*UP)
        txt_1=self.rectangulo_texto(texto_1)

        formula_1=Tex("$\\Rightarrow Y= \\frac{X}{a(k)} * a(n) = X * \\frac{a(n)}{a(k)}$",color= PURE_RED, font_size=40)
        formula_1.shift(2.5*DOWN)
        frm=self.rectangulo_textor(formula_1)
    
    #Graficas/Lineas
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=4,
            color=GRAY,
            include_tip=True,
            label_direction=UP,
            include_ticks=False,
            stroke_width=2
        )
        l0.shift(1*DOWN+1*RIGHT)

        l1 = NumberLine(
            x_range=[1, 7, 1],
            length=12,
            color=PURE_BLUE,
            include_tip=True,
            label_direction=UP,
            include_ticks=True,
            tick_size=0.40,
            stroke_width=3
        )

        l1.shift(2*DOWN)


        #Objetos
        inner_1 = Text("X", color= PURE_RED).scale(0.5)
        mob_1 = SurroundingRectangle(inner_1, corner_radius=0.1, color= PURE_RED)  
        k_1=VGroup(inner_1,mob_1)
        k_1.shift(2*LEFT + 1*DOWN)

        inner_2 = Text("Y", color= PURE_RED).scale(0.5) 
        mob_2 = SurroundingRectangle(inner_2, corner_radius=0.1, color= PURE_RED)  
        k_2=VGroup(inner_2,mob_2)
        k_2.shift(4*RIGHT + 1*DOWN)

        inner_3 = Tex("0", color= PURE_BLUE, font_size=35)
        mob_3 = SurroundingRectangle(inner_3, corner_radius=0.1, color= PURE_BLUE)  
        k_3=VGroup(inner_3,mob_3)
        k_3.shift(4*LEFT + 2.75*DOWN)

        inner_4 = Text("n", color= PURE_BLUE).scale(0.5) 
        mob_4 = SurroundingRectangle(inner_4, corner_radius=0.1, color= PURE_BLUE)  
        k_4=VGroup(inner_4,mob_4)
        k_4.shift(4*RIGHT + 2.75*DOWN)

        inner_5 = Text("k", color= PURE_BLUE).scale(0.5)
        mob_5 = SurroundingRectangle(inner_5, corner_radius=0.1, color= PURE_BLUE)  
        k_5=VGroup(inner_5,mob_5)
        k_5.shift(2*LEFT + 2.75*DOWN)

        t_2=Text("Monto", color= BLACK).scale(0.5)
        t_2.shift(6*LEFT + 1.15*DOWN)
        t_3=Text("Tiempo", color= BLACK).scale(0.5)
        t_3.shift(6*LEFT + 2.75*DOWN)

        t_t= Text("t", color= GRAY).scale(0.5)
        t_t.shift(0.75*DOWN + 0.4*LEFT)
        
        linea=VGroup(l1, l0, k_1, k_2, k_3, k_4, k_5, t_2, t_3)
        linea.shift(2*UP)

        #Escena
        self.play(Write(txt_1),run_time=7)
        self.wait(3)
        self.play(Write(linea),run_time=7)
        self.wait(2)
        self.play(Write(frm))
        self.wait(2)


