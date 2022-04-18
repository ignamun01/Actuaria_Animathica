from manim import *
config.background_color = YELLOW_A
config["background_color"] = YELLOW_A

###########################################################################################
##############################  Escena 1  #################################################
###########################################################################################

class Escena_1(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):
        # Construccion de ejes
        ax_1 = Axes(
            x_range=[0, 51, 6],
            y_range=[5, 120, 20],
            x_length=5,
            y_length=4,
            axis_config={'color' : BLACK , 'include_ticks': True}
        )

        # Posicion de Ejes
        ax_1.shift(0.4*UP)


        # Creación de Curvas
        curve_1 = ax_1.plot(lambda x: 15*(1+0.05*x), color=BLACK, x_range=[0,42])
        areac1 = ax_1.get_area(curve_1, color = BLACK, opacity=0.5)
        curve_2 = ax_1.plot(lambda x: 15*(1+0.05)**x, color=PURE_RED, x_range=[0,42])
        areac2 = ax_1.get_area(curve_2, color = PURE_RED, opacity=0.5, bounded_graph=curve_1)

        curves = VGroup(curve_1, curve_2)

        dot_1 = Dot(ax_1.i2gp(curve_1.t_min, curve_1), color=BLACK, radius=0.10)
        dot_2 = Dot(ax_1.i2gp(curve_2.t_min, curve_2), color=PURE_RED, radius=0.10)

        #Texto

        pres= Tex("\\textbf{Interés Compuesto vs Interés Simple}", 
        color= BLACK, font_size=40)
        pres.shift(3.2*UP)
        txt_1=self.rectangulo_texto(pres)

        txt_2= Tex("\\textit{Como vemos en la gráfica, conforme avanza el tiempo la diferencia entre el interés compuesto y el interés simple es gigante.} ", 
        color= BLACK, font_size=36)
        txt_2.shift(2.7*DOWN)

        txt_3= Tex("\\textit{Esto se debe a que en el interés compuesto, los intereses obtenidos en un periodo se suman al capital y estos generan nuevos intereses para el siguiente periodo.} ", 
        color= BLACK, font_size=36)
        txt_3.shift(2.7*DOWN)

        txt_4= Tex("\\textit{Mientras que en el interés simple los intereses de un periodo a otro siempre son los mismos.} ", 
        color= BLACK, font_size=36)
        txt_4.shift(2.7*DOWN)

        #Creación de escena
        self.add(ax_1, curves, dot_1, dot_2)
        self.play(Write(txt_1))
        self.wait(2)
        self.play(MoveAlongPath(dot_1, curve_1, rate_func=linear), 
        MoveAlongPath(dot_2, curve_2, rate_func=linear), Write(txt_2), run_time=4)
        self.wait(3)
        self.play(Write(areac1)) 
        self.play(Write(areac2), ReplacementTransform(txt_2,txt_3))
        self.wait(4)
        self.play(ReplacementTransform(txt_3,txt_4))
        self.wait(4)



###########################################################################################
##############################  Escena 2  #################################################
###########################################################################################



class Escena_2(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=GRAY_BROWN, fill_opacity=0.15, buff=0.3, corner_radius=0.1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):
        txt_1= Tex("Supongamos que obtenemos un préstamo en el banco de \$10,000 con vencimiento a 5 años, ", 
        "el cual se paga anualmente a una tasa del 5\% anual efectivo. ", 
        color= BLACK, font_size=38)
        txt_1.shift(2.6*UP)
        rtxt_1=self.rectangulo_texton(txt_1)

        t3= Tex("Identificamos los datos del enunciado:",
        color= BLACK, font_size=36)
        t3.shift(1*UP)

        t4=BulletedList("$i = 5\%$", 
        "n = 5 años ", 
        "$C_0 = \$10,000$",font_size=32)
        t4.set_color(BLACK)
        t4.shift(1*DOWN)

        t5= Tex("Calculemos cuánto pagaremos al final del préstamo bajo un esquema de \\textbf{interés simple}:",
        color= BLACK, font_size=36)
        t5.shift(0.8*UP)

        txt_2=Tex("$C_5 = 10,000 * (1+0.05*5) $", color= BLACK, font_size=38)
        txt_2.shift(0.5*DOWN)

        txt_3=Tex("$C_5 = \$12,500$", color= PURE_RED, font_size=38)
        txt_3.shift(1.5*DOWN)
        rtxt_3 = self.rectangulo_texto(txt_3)

        txt_4=Tex("Calculemos cuánto pagaremos al final del préstamo bajo un esquema de \\textbf{interés compuesto:}", 
        color= BLACK, font_size=36)
        txt_4.shift(0.8*UP)

        txt_5=Tex("$C_5 = 10,000 * (1+0.05)^5 $", color= BLACK, font_size=38)
        txt_5.shift(0.5*DOWN)

        txt_6=Tex("$C_5 = \$12,762.81563$", color= PURE_RED, font_size=38)
        txt_6.shift(1.5*DOWN)
        rtxt_6 = self.rectangulo_texto(txt_6)


        self.play(Write(rtxt_1))
        self.wait(2)
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(2)
        self.play(FadeOut(t3), FadeOut(t4))
        self.wait()
        self.play(Write(t5),Write(txt_2))
        self.wait(2)
        self.play(Write(rtxt_3))
        self.wait(2)
        self.play(ReplacementTransform(t5,txt_4), FadeOut(txt_2), FadeOut(rtxt_3))
        self.wait(2)
        self.play(Write(txt_5))
        self.wait(2)
        self.play(Write(rtxt_6))
        self.wait(2)


###########################################################################################
##############################  Escena 3  #################################################
###########################################################################################



class Escena_3(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=PURE_RED, fill_opacity=0.15, buff=0.3, corner_radius=0.1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

################################ Primera Subescena ################################
        txt_1= Tex("\\textbf{Caso Interés Compuesto}", 
        color= PURE_RED, font_size=40)
        txt_1.shift(2.6*UP)
        rtxt_1=self.rectangulo_texton(txt_1)

        t3= Tex("Identificamos los datos del problema:",
        color= BLACK, font_size=36)
        t3.shift(1*UP)

        t4=BulletedList("$i = 5\% $ anual efectiva", 
        "t = 10 años ", 
        "$C_0 = \$10,000$",font_size=32)
        t4.set_color(BLACK)
        t4.shift(1*DOWN)

        t5= Tex("Utilizando la expresión del interés compuesto tenemos:",
        color= BLACK, font_size=36)
        t5.shift(0.8*UP)

        txt_2=Tex("$C_{10} = 10,000 * (1+0.05)^{10} $", color= BLACK, font_size=38)
        txt_2.shift(0.5*DOWN)

        txt_3=Tex("$C_{10} = \$ 16,288.94627 $", color= PURE_RED, font_size=38)
        txt_3.shift(1.5*DOWN)
        rtxt_3 = self.rectangulo_texto(txt_3)



        txt_4=Tex("\\textbf{Caso Interés Continuo}", 
        color= PURE_RED, font_size=40)
        txt_4.shift(2.6*UP)
        rtxt_4=self.rectangulo_texton(txt_4)


        t6= Tex("Identificamos los datos del problema:",
        color= BLACK, font_size=36)
        t6.shift(1*UP)

        t7=BulletedList("$i = 5\% $", 
        "t = 10 años ", 
        "$C_0 = \$10,000$",font_size=32)
        t7.set_color(BLACK)
        t7.shift(1*DOWN)

        t8= Tex("Utilizando la expresión del interés continuo tenemos:",
        color= BLACK, font_size=36)
        t8.shift(0.8*UP)

        txt_5=Tex("$C_{10} = 10,000 * e^{10*0.05} $", color= BLACK, font_size=38)
        txt_5.shift(0.5*DOWN)

        txt_6=Tex("$C_{10} = \$16,487.21271$", color= PURE_RED, font_size=38)
        txt_6.shift(1.5*DOWN)
        rtxt_6 = self.rectangulo_texto(txt_6)


        self.play(Write(rtxt_1))
        self.wait(2)
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(2)
        self.play(FadeOut(t3), FadeOut(t4))
        self.wait()
        self.play(Write(t5),Write(txt_2))
        self.wait(2)
        self.play(Write(rtxt_3))
        self.wait(2)
        self.play(ReplacementTransform(rtxt_1,rtxt_4), FadeOut(txt_2), FadeOut(rtxt_3), FadeOut(t5))
        self.wait(2)
        self.play(Write(t6))
        self.play(Write(t7))
        self.wait(2)
        self.play(FadeOut(t6), FadeOut(t7))
        self.wait(2)
        self.play(Write(t8),Write(txt_5))
        self.wait(2)
        self.play(Write(rtxt_6))
        self.wait(4)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


################################ Segunda Subescena ################################

        txt_1= Tex("\\textbf{Caso Interés Compuesto}", 
        color= PURE_RED, font_size=40)
        txt_1.shift(2.6*UP)
        rtxt_1=self.rectangulo_texton(txt_1)

        rtxt_1.shift(1*DOWN+3*LEFT)
        rtxt_4.shift(1*DOWN+3*RIGHT)
        rtxt_3.shift(1.25*UP + 3*LEFT)
        rtxt_6.shift(1.25*UP + 3*RIGHT)

        txt_7= Tex("En este caso nos convendría invertir nuestro dinero bajo un \\textbf{esquema continuo}, pues al final obtendremos un poco más de rendimiento.",
        color= BLACK, font_size=36)
        txt_7.shift(1.8*DOWN)

        flecha_1= Tex("$\Downarrow$",
        color= BLACK, font_size=70)
        flecha_1.shift(0.65*UP + 3*LEFT)

        flecha_2= Tex("$\Downarrow$",
        color= BLACK, font_size=70)
        flecha_2.shift(0.65*UP + 3*RIGHT)

        self.play(Write(rtxt_1), Write(rtxt_4))
        self.wait()
        self.play(Write(rtxt_3),Write(rtxt_6), Write(flecha_1), Write(flecha_2))
        self.wait()
        self.play(Write(txt_7))
        self.wait(4)
