from manim import *
config.background_color = YELLOW_A
config["background_color"] = YELLOW_A



###########################################################################################
##############################  Escena 1  #################################################
###########################################################################################


class Escena_1(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

##############################Primera subescena######################################

        #Textos
        txt_1= Tex("La expresión de Valor Presente para \\textbf{un solo flujo} de efectivo es la siguiente:", 
        color= BLACK, font_size=36)
        txt_1.shift(2.5*UP)
        rtxt_1=self.rectangulo_texton(txt_1)

        txt_2= Tex("$VP = \\cfrac{\LARGE F}{\prod\limits_{i=1}^{n} (1+r)} = \\cfrac{\LARGE F}{(1+r)^n}$", 
        color= PURE_RED, font_size=36)
        txt_2.shift(1*UP)

        txt_3= Tex("Donde: ", 
        color= BLACK, font_size=32)
        txt_3.shift(0.5*DOWN + 5*LEFT)

        txt_4=BulletedList("$F$= Flujo de Efectivo", 
        "$n$= Número de periodos para traer al presente el flujo de efectivo.",
        "r = Tasa de interés", font_size=30)
        txt_4.shift(2*DOWN)
        txt_4.set_color(BLACK)

        ##### Entrada subescena 1 #####
        self.play(Write(rtxt_1))
        self.wait()
        self.play(Write(txt_2))
        self.wait()
        self.play(Write(txt_3), Write(txt_4))
        self.wait(2)
        self.play(FadeOut(rtxt_1), FadeOut(txt_2), FadeOut(txt_3), FadeOut(txt_4))
        self.wait()

#####################Segunda subescena######################################

        #Textos
        txt_1= Tex("La expresión de Valor Presente para \\textbf{varios flujos} de efectivo es:", 
        color= BLACK, font_size=36)
        txt_1.shift(2.7*UP)
        rtxt_1=self.rectangulo_texton(txt_1)

        txt_2= Tex("$VP = F_0 + \\cfrac{\LARGE F_1}{(1+r)} + \\cfrac{\LARGE F_2}{(1+r)^2} + \\cfrac{\LARGE F_3}{(1+r)^3} + ... + \\cfrac{\LARGE F_n}{(1+r)^n}$", 
        color= PURE_RED, font_size=30)
        txt_2.shift(1.4*UP)

        txt_21= Tex("$VP = F_0 + \sum\limits_{i=1}^{n} \\frac{\LARGE F_i}{(1+r)^i} = \sum\limits_{i=0}^{n} \\frac{\LARGE F_i}{(1+r)^i} $", 
        color= PURE_RED, font_size=36)
        txt_21.shift(0.2*UP)

        txt_3= Tex("Donde: ", 
        color= BLACK, font_size=32)
        txt_3.shift(0.6*DOWN + 5*LEFT)

        txt_4=BulletedList("VP = Valor Presente",
        "$F_i$ = Flujo de Efectivo del tiempo i",
        "r = Tasa de interés", 
        "$n$ = Número de periodos para llevar al presente el flujo de efectivo.",
        font_size=30)
        txt_4.shift(2.5*DOWN)
        txt_4.set_color(BLACK)

        ##### Entrada subescena 2 #####
        self.play(Write(rtxt_1))
        self.wait()
        self.play(Write(txt_2))
        self.wait()
        self.play(Write(txt_21))
        self.wait()
        self.play(Write(txt_3), Write(txt_4))
        self.wait(2)
        self.play(FadeOut(rtxt_1), FadeOut(txt_2), FadeOut(txt_3), FadeOut(txt_4), FadeOut(txt_21))
        self.wait()

        txt_5= Tex("Por practicidad denotaremos:", 
        color= BLACK, font_size=36)
        txt_5.shift(1.7*UP)

        txt_6= Tex("$(\\frac{1}{1+r})^t$", 
        color= BLACK, font_size=36)
        txt_6.shift(2*LEFT + 0.7*UP)
        rtxt_6=self.rectangulo_texton(txt_6)

        txt_7= Tex("$ e^{- \delta * t} $", 
        color= BLACK, font_size=36)
        txt_7.shift(1.8*RIGHT + 0.7*UP)
        rtxt_7=self.rectangulo_texton(txt_7)

        txt_8= Tex("$\\mathbf{v^t}$", 
        color= PURE_RED, font_size=60)
        txt_8.shift(0.8*DOWN)
        rtxt_8=self.rectangulo_texto(txt_8)

        flecha_1= Tex("$\searrow$", 
        color= PURE_RED, font_size=60)
        flecha_1.shift(1*LEFT+0.3*DOWN)

        flecha_2= Tex("$\swarrow$", 
        color= PURE_RED, font_size=60)
        flecha_2.shift(1*RIGHT+0.3*DOWN)

        rect_1 = Rectangle(color=BLACK, height=3.5, width=9)
        rect_1.shift(0.4*UP)

        rect_2 = Rectangle(color=BLACK, height=4.5, width=10)
        rect_2.shift(0.4*UP)

        self.play(Write(txt_5), Write(rect_1), Write(rect_2))
        self.wait()
        self.play(Write(rtxt_6), Write(rtxt_7))
        self.wait(2)
        self.play(Write(rtxt_8), Write(flecha_1), Write(flecha_2))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )






###########################################################################################
##############################  Escena 2  #################################################
###########################################################################################


class Escena_2(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

##############################Primera subescena######################################

        #Textos
        txt_1= Tex("La expresión de Valor Futuro para \\textbf{un solo flujo} de efectivo es la siguiente:", 
        color= BLACK, font_size=36)
        txt_1.shift(2.5*UP)
        rtxt_1=self.rectangulo_texton(txt_1)

        txt_2= Tex("$VF =  F \prod\limits_{i=1}^{n} (1+r) = F (1+r)^n $", 
        color= PURE_RED, font_size=38)
        txt_2.shift(1*UP)

        txt_3= Tex("Donde: ", 
        color= BLACK, font_size=32)
        txt_3.shift(0.5*DOWN + 5*LEFT)

        txt_4=BulletedList("$F$= Flujo de Efectivo", 
        "$n$= Número de periodos para llevar al futuro el flujo de efectivo.",
        "r = Tasa de interés", font_size=30)
        txt_4.shift(2*DOWN)
        txt_4.set_color(BLACK)

        ##### Entrada subescena 1 #####
        self.play(Write(rtxt_1))
        self.wait()
        self.play(Write(txt_2))
        self.wait()
        self.play(Write(txt_3), Write(txt_4))
        self.wait(2)
        self.play(FadeOut(rtxt_1), FadeOut(txt_2), FadeOut(txt_3), FadeOut(txt_4))
        self.wait()

#####################Segunda subescena######################################

        #Textos
        txt_1= Tex("La expresión de Valor Futuro para \\textbf{varios flujos} de efectivo es:", 
        color= BLACK, font_size=36)
        txt_1.shift(2.7*UP)
        rtxt_1=self.rectangulo_texton(txt_1)

        txt_2= Tex("$VF = \sum\limits_{i=0}^{n} F_i (1+r)^{n-i} = F_0 (1+r)^n + F_n (1+r)^{(n-n)} + \sum\limits_{i=1}^{n-1} F_i (1+r)^{n-i}$", 
        color= PURE_RED, font_size=30)
        txt_2.shift(1.4*UP)

        txt_21= Tex("$VF = F_0 (1+r)^n + \sum\limits_{i=1}^{n-1} F_i (1+r)^{n-i} + F_n$", 
        color= PURE_RED, font_size=36)
        txt_21.shift(0.2*UP)

        txt_3= Tex("Donde: ", 
        color= BLACK, font_size=32)
        txt_3.shift(0.8*DOWN + 5*LEFT)

        txt_4=BulletedList("$F_i$ = Flujo de Efectivo del tiempo i",
        "r = Tasa de interés", 
        "$n$ = Número de periodos para llevar al presente el flujo de efectivo.",
        font_size=30)
        txt_4.shift(2.4*DOWN)
        txt_4.set_color(BLACK)

        ##### Entrada subescena 2 #####
        self.play(Write(rtxt_1))
        self.wait()
        self.play(Write(txt_2))
        self.wait()
        self.play(Write(txt_21))
        self.wait()
        self.play(Write(txt_3), Write(txt_4))
        self.wait(2)
        self.play(FadeOut(rtxt_1), FadeOut(txt_2), FadeOut(txt_3), FadeOut(txt_4), FadeOut(txt_21))
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


##################### Tercera subescena######################################

        t0=Tex("Supongamos que conocemos el valor final de nuestra \hspace{10 cm} inversión(VF)  y la tasa de interés involucrada(r).",
        color= BLACK, font_size=32)
        t0.shift(1.8*UP)

        t0_1=Tex("\\textit{¿Cuál es el valor de nuestra inversión a dia de hoy?}",
        color= BLACK, font_size=34)
        t0_1.shift(0.7*DOWN)
        
        t1=Tex("Para conocer esto es necesario traer a valor presente \hspace{10 cm}todos los flujos de efectivo que se encuentran \hspace{10 cm}en el futuro.",
        color= BLACK, font_size=36)
        t1.shift(0.2*DOWN)

        t2= Tex("$VF = F (1+r)^n $", 
        color= PURE_RED, font_size=36)
        t2.shift(0.5*UP)
        rt2=self.rectangulo_texto(t2)

        t3= Tex("$VP = \\frac{VF}{(1+r)^n}$", 
        color= PURE_RED, font_size=36)
        t3.shift(0.6*UP)
        rt3=self.rectangulo_texto(t3)
        rt3.generate_target()
        rt3.target.shift(1*UP)

        t4= Tex("$VP = F = \\frac{VF}{(1+r)^n}$", 
        color= PURE_RED, font_size=36)
        t4.shift(0.6*UP)
        rt4=self.rectangulo_texto(t4)

        t7=Tex("\\textit{Esto es muy importante porque nos indica que hay \\textbf{una relación entre el Valor Futuro y el Valor presente}, a partir de uno siempre podemos encontrar el otro mientras exista una tasa de interés de por medio.}",
        color= BLACK, font_size=36)
        t7.shift(3*DOWN)

        rect_1 = Rectangle(color=BLACK, height=4, width=9)
        rect_1.shift(0.4*UP)

        rect_2 = Rectangle(color=BLACK, height=5, width=10)
        rect_2.shift(0.4*UP)

        self.play(Write(rect_1), Write(rect_2), Write(rt2), Write(t0), Write(t0_1))
        self.wait(3)
        self.play(Unwrite(t0), FadeOut(t0_1))
        self.wait(0.5)
        self.play(ReplacementTransform(rt2,rt3))
        self.wait(1)
        self.play(Write(t1), MoveToTarget(rt3))
        self.wait(4)
        self.play(Write(t7))
        self.wait(4)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )





###########################################################################################
##############################  Escena 3  #################################################
###########################################################################################

class Escena_3(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

####################### Primera Subescena #######################################
        t0_1= Tex("$VP_n = \\cfrac{F_n}{(1+0.05)^n} $", 
        color= PURE_RED, font_size=36)
        t0_1.shift(0.5*UP)

        t0_2=Tex("\\textbf{Perspectiva de Valor Presente}",
        color= BLACK, font_size=38)
        t0_2.shift(1.8*UP)


        t0_3=Tex("No tenemos flujo de efectivo a tiempo 0 por lo tanto $F_0$ = 0.",
        color= BLACK, font_size=34)
        t0_3.shift(1*DOWN)

        t0_4= Tex("${VP}_0 = \\cfrac{F_0}{(1+0.05)^0} = 0 $", 
        color= PURE_RED, font_size=36)
        t0_4.shift(0.5*UP)

        t0_5=Tex("Para el \\textbf{año 0}: ",
        color= BLACK, font_size=38)
        t0_5.shift(1.8*UP)


        t1_1= Tex("${VP}_1 = \\cfrac{F_1}{(1+0.05)^1} = \\cfrac{1,000,000}{(1.05)} = 952,380.9524 $", 
        color= PURE_RED, font_size=36)
        t1_1.shift(0.5*UP)

        t1_2=BulletedList(" Pago del año 1 = $ \$ 1,000,000 $", font_size=36)
        t1_2.shift(1*DOWN)
        t1_2.set_color(BLACK)

        t1_3=Tex("Para el \\textbf{año 1} tenemos:",
        color= BLACK, font_size=38)
        t1_3.shift(1.8*UP)


        t2_1= Tex("${VP}_2 = \\cfrac{F_2}{(1+0.05)^2} = \\cfrac{1,000,000}{(1.05)^2}= 907,029.4785 $", 
        color= PURE_RED, font_size=36)
        t2_1.shift(0.5*UP)

        t2_2=BulletedList(" Pago del año 2= $ \$ 1,000,000 $", font_size=36)
        t2_2.shift(1*DOWN)
        t2_2.set_color(BLACK)

        t2_3=Tex("Para el \\textbf{año 2} tenemos: ",
        color= BLACK, font_size=38)
        t2_3.shift(1.8*UP)


        tn_1= Tex("$VP = \\frac{1,000,000}{(1.05)^1} + \\frac{1,000,000}{(1.05)^2} + \\frac{4,000,000}{(1.05)^3} + \\frac{4,000,000}{(1.05)^4} + \\frac{6,000,000}{(1.05)^5} $", 
        color= PURE_RED, font_size=36)

        tn_1_1= Tex("$VP = 13,306,727.72 $", 
        color= PURE_RED, font_size=36)
        tn_1_1.shift(1*DOWN)
        rt_1=self.rectangulo_texto(tn_1_1)
        

        tn_2=Tex("Siguiendo esta lógica y usando la expresión de Valor Presente para varios flujos de efectivo tenemos que:",
        color= BLACK, font_size=36)
        tn_2.shift(1.5*UP)

        rect_1 = Rectangle(color=BLACK, height=4, width=12.5)
        rect_1.shift(0.4*UP)

        rect_2 = Rectangle(color=BLACK, height=4.5, width=13)
        rect_2.shift(0.4*UP)


        #######Entrada a Escena#########

        self.play(Write(rect_1), Write(rect_2), Write(t0_1), Write(t0_2))
        self.wait(2)
        self.play(ReplacementTransform(t0_1, t0_4), ReplacementTransform(t0_2, t0_3), Write(t0_5))
        self.wait(2)
        self.play(ReplacementTransform(t0_4,t1_1),ReplacementTransform(t0_3, t1_2), ReplacementTransform(t0_5, t1_3))
        self.wait(2)
        self.play(ReplacementTransform(t1_1, t2_1),ReplacementTransform(t1_2, t2_2), ReplacementTransform(t1_3, t2_3))
        self.wait(2)
        self.play(FadeOut(t2_3),ReplacementTransform(t2_1, tn_1),ReplacementTransform(t2_2, tn_2))
        self.play(Write(rt_1))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

####################### Segunda Subescena #######################################

        t1= Tex("Restando el $VP$ obtenido y nuestra inversión tenemos \hspace{10 cm} que el Retorno será de:", 
        color= BLACK, font_size=31)
        t1.shift(1.5*UP)

        t2=Tex("\\textbf{ROI = \$ 13,306,727.7 - \$ 11,000,000}",
        color= PURE_RED, font_size=34)
        t2.shift(0.3*UP)

        t3=Tex("\\textbf{ROI = \$ 2,306,727.723}",
        color= PURE_RED, font_size=34)
        t3.shift(0.5*DOWN)
        
        t4=Tex("\\textit{En este caso nos conviene invertir en el proyecto debido a que tendremos una ganancia bruta de} \\textbf{2,306,727.723}.",
        color= BLACK, font_size=34)
        t4.shift(2.5*DOWN)

        t5=Tex("Esto también se puede hacer usando un enfoque de valor futuro y valor presente al mismo tiempo.",
        color= BLACK, font_size=34)
        t5.shift(2.5*DOWN)

        t5=Tex("Esto también se puede hacer usando un enfoque de valor futuro y valor presente \\textbf{al mismo tiempo}.",
        color= BLACK, font_size=34)
        t5.shift(2.5*DOWN)

        rect_1 = Rectangle(color=BLACK, height=3.5, width=8.5)
        rect_1.shift(0.6*UP)

        rect_2 = Rectangle(color=BLACK, height=4, width=9)
        rect_2.shift(0.6*UP)

        self.play(Write(rect_1), Write(rect_2),Write(t1), Write(t2), Write(t3))
        self.wait(3)
        self.play(Write(t4))
        self.wait()
        self.play(ReplacementTransform(t4,t5))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )



###########################################################################################
##############################  Escena 4  #################################################
###########################################################################################

class Escena_4(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=GRAY_BROWN, fill_opacity=0.15, buff=0.3, corner_radius=0.1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

####################### Primera Subescena #######################################
        t0_1= Tex("$VF_t = F_t * (1+0.05)^t $", 
        color= PURE_RED, font_size=36)
        t0_1.shift(0.5*UP)

        t0_2=Tex("\\textbf{Perspectiva de Valor Presente / Valor Futuro}",
        color= BLACK, font_size=38)
        t0_2.shift(1.8*UP)

        t0_6=Tex("La idea es llevar todos los flujos de efectivo a un mismo tiempo y una vez todos en el mismo punto, podemos traernos ese monto a valor presente.",
        color= BLACK, font_size=34)
        t0_6.shift(0.8*DOWN)

        t0_3=Tex("No tenemos flujo de efectivo a tiempo 0 por lo tanto $F_0$ = 0.",
        color= BLACK, font_size=34)
        t0_3.shift(1*DOWN)

        t0_4= Tex("${VF}_0 = F_0 * (1+0.05)^0 = 0 $", 
        color= PURE_RED, font_size=36)
        t0_4.shift(0.5*UP)

        t0_5=Tex("Para el \\textbf{año 0}: ",
        color= BLACK, font_size=38)
        t0_5.shift(1.8*UP)


        t1_1= Tex("${VF}_1 = F_1 * (1+0.05)^4 = 1,000,000 * (1.05)^4 = 1,215,506.25 $", 
        color= PURE_RED, font_size=36)
        t1_1.shift(0.5*UP)

        t1_2=BulletedList(" Pago del año 1 = $ \$ 1,000,000 $", font_size=36)
        t1_2.shift(1*DOWN)
        t1_2.set_color(BLACK)

        t1_3=Tex("Para el \\textbf{año 1} tenemos:",
        color= BLACK, font_size=38)
        t1_3.shift(1.8*UP)


        t2_1= Tex("${VF}_2 = F_2 * (1+0.05)^3 = 1,000,000 *(1.05)^3 =  1,157,625$", 
        color= PURE_RED, font_size=36)
        t2_1.shift(0.5*UP)

        t2_2=BulletedList(" Pago del año 2= $ \$ 1,000,000 $", font_size=36)
        t2_2.shift(1*DOWN)
        t2_2.set_color(BLACK)

        t2_3=Tex("Para el \\textbf{año 2} tenemos: ",
        color= BLACK, font_size=38)
        t2_3.shift(1.8*UP)


        tn_1= Tex("$VF = 1,000,000 * (1.05)^4 + 1,000,000 * (1.05)^3 + 4,000,000 * (1.05)^2 + 4,000,000 * (1.05)^1 + 6,000,000 $", 
        color= PURE_RED, font_size=32)

        tn_1_1= Tex("$VF = 16,983,131.85 $", 
        color= PURE_RED, font_size=36)
        tn_1_1.shift(1*DOWN)
        rt_1=self.rectangulo_texto(tn_1_1)
        

        tn_2=Tex("Siguiendo esta lógica y usando la expresión de Valor Futuro para \hspace{10 cm} varios flujos de efectivo tenemos que:",
        color= BLACK, font_size=36)
        tn_2.shift(1.5*UP)

        rect_1 = Rectangle(color=BLACK, height=4, width=12.5)
        rect_1.shift(0.4*UP)

        rect_2 = Rectangle(color=BLACK, height=4.5, width=13)
        rect_2.shift(0.4*UP)


        #######Entrada a Escena#########

        self.play(Write(rect_1), Write(rect_2), Write(t0_1), Write(t0_2), Write(t0_6))
        self.wait(2)
        self.play(ReplacementTransform(t0_1, t0_4), ReplacementTransform(t0_2, t0_3), Write(t0_5), FadeOut(t0_6))
        self.wait(2)
        self.play(ReplacementTransform(t0_4,t1_1),ReplacementTransform(t0_3, t1_2), ReplacementTransform(t0_5, t1_3))
        self.wait(2)
        self.play(ReplacementTransform(t1_1, t2_1),ReplacementTransform(t1_2, t2_2), ReplacementTransform(t1_3, t2_3))
        self.wait(2)
        self.play(FadeOut(t2_3),ReplacementTransform(t2_1, tn_1),ReplacementTransform(t2_2, tn_2))
        self.play(Write(rt_1))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

####################### Segunda Subescena #######################################

        txt_1= Tex("Traemos a Valor Presente el total de los montos:", 
        color= BLACK, font_size=31)
        txt_1.shift(1.5*UP)

        txt_2=Tex("$\\mathbf{VP = \\cfrac{16,983,131.85}{(1.05)^5} = 13,306,727.72}$",
        color= PURE_RED, font_size=32)
        txt_2.shift(0.3*UP)
        
        t1= Tex("Restando el $VP$ obtenido y nuestra inversión tenemos \hspace{10 cm} que el Retorno será de:", 
        color= BLACK, font_size=30)
        t1.shift(1.7*UP)

        t2=Tex("\\textbf{ROI = \$ 13,306,727.7 - \$ 11,000,000}",
        color= PURE_RED, font_size=34)
        t2.shift(0.7*UP)

        t3=Tex("\\textbf{ROI = \$ 2,306,727.723}",
        color= PURE_RED, font_size=34)
        #t3.shift(0.1*DOWN)
        
        t4=Tex("\\textit{El cual es el mismo retorno que obtuvimos \hspace{10 cm} con el procedimiento anterior.} ",
        color= BLACK, font_size=30)
        t4.shift(0.85*DOWN)

        t5=Tex("Como conclusión, nos conviene invertir en este proyecto pues obtenemos un rendimiento en monto total de \\textbf{2,306,727.723}. ",
        color= BLACK, font_size=34)
        t5.shift(2.5*DOWN)

        t5_1=Tex("Esto también se puede hacer usando un enfoque de valor futuro y valor presente \\textbf{al mismo tiempo}.",
        color= BLACK, font_size=34)
        t5_1.shift(2.5*DOWN)

        rect_1 = Rectangle(color=BLACK, height=4, width=8.5)
        rect_1.shift(0.6*UP)

        rect_2 = Rectangle(color=BLACK, height=4.5, width=9)
        rect_2.shift(0.6*UP)

        self.play(Write(rect_1), Write(rect_2),Write(txt_1), Write(txt_2))
        self.wait(3)
        self.play(ReplacementTransform(txt_1, t1), ReplacementTransform(txt_2,t2), Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.wait()
        self.play(Write(t5))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

####################### Tercera Subescena #######################################

        t1= Tex("Pero, ¿qué hubiera pasado si el monto inicial de la inversión hubiese \hspace{10 cm} sido de 14,000,000? ", 
        color= BLACK, font_size=36)
        t1.shift(2.6*UP)
        rt1=self.rectangulo_texton(t1)

        t3=Tex("Si realizamos la misma operación de retorno de inversión, que utilizamos antes, tenemos:",
        color= BLACK, font_size=34)
        t3.shift(1*UP)

        t4=MathTex(r"ROI &= \$ 13,306,727.7 - \$ 14,000,000 \\ &= -693,272.2771",
        color= PURE_RED, font_size=36)
        t4.shift(0.3*DOWN)
        rt4=self.rectangulo_texto(t4)

        t5=Tex("Tenemos un ", "\\textbf{\\underline{monto negativo}} ", ", lo cual indica que no estaríamos ganando valor del dinero a lo largo del tiempo. ",
        color= BLACK, font_size=34)
        t5.shift(2.2*DOWN)
        t5[1].set_color(PURE_RED)

        self.play(Write(rt1))
        self.wait()
        self.play(Write(t3), Write(rt4))
        self.wait()
        self.play(Write(t5))
        self.wait()



