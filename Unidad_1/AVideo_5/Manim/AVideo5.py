from manim import *
from numpy import linspace
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

    def construct(self):

        #Textos
        txt_1= Text("La fórmula que utilizaremos para calcular el interés simple será la siguiente:", 
        color= BLACK, font_size=28, font="Noto Sans",t2w={'interés simple':BOLD})
        txt_1.shift(2*UP)

        txt_2= Tex("$C_t = C_0 (1 + i*t)$", 
        color= PURE_RED, font_size=36)
        txt_2.shift(1*UP)

        rtxt_2=self.rectangulo_texto(txt_2)

        txt_3= Tex("Donde: ", 
        color= BLACK, font_size=28,)

        txt_4=BulletedList("$C_t$= Capital  Resultante al tiempo t.", 
        "$C_0$= Capital  inicial al tiempo 0.",
        "i = Tasa de interés.",
        "t = Periodo de tiempo considerado.", font_size=30)
        txt_4.shift(2*DOWN)
        txt_4.set_color(BLACK)

        
        #Creación de escena
        self.play(Write(txt_1))
        self.wait()
        self.play(Write(rtxt_2))
        self.wait()
        self.play(Write(txt_3), Write(txt_4))
        self.wait()

        self.play(Unwrite(txt_1))
        self.wait(2)

        txt_5= Text("Si en la expresión distribuimos el Capital inicial, tenemos que:", 
        color= BLACK, font_size=28, font="Noto Sans",t2w={'Capital inicial':BOLD})
        txt_5.shift(2*UP)

        txt_6= Tex("$C_t = C_0 + C_0 * i * t$", 
        color= PURE_RED, font_size=36)
        txt_6.shift(1*UP)

        rtxt_6=self.rectangulo_texto(txt_6)

        self.play(Write(txt_5))
        self.wait()
        self.play(ReplacementTransform(rtxt_2,rtxt_6))
        self.wait(3)



###########################################################################################
##############################  Escena 2  #################################################
###########################################################################################

class Escena_2(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

        txt_1= Tex("Supongamos que el banco le ofrece un producto de inversión el cual consta de recibir una tasa de interés simple de $3\%$ al año sobre \$100 pesos invertidos durante 5 años.", 
        color= BLACK, font_size=38)
        txt_1.shift(2.7*UP)
        r_t1=self.rectangulo_texto(txt_1)

        txt_2= Text("Analicemos la información que nos dan:", 
        color= BLACK, font_size=26, font="Noto Sans")
        txt_2.shift(1.5*UP)

        txt_3=BulletedList("$C_0$ = 100", "i = $3\%$", "t = 5 Años", font_size=30, buff=0.3)
        txt_3.set_color(BLACK)
        txt_3.shift(0.4*UP)

        txt_4=Text("Usando la expresión que tenemos para el interés simple:",
        color= BLACK, font_size=26, font="Noto Sans")
        txt_4.shift(0.8*DOWN)

        txt_5= Tex("$C_t = 100 (1 + 0.03*5)$", 
        color= PURE_RED, font_size=36)
        txt_5.shift(1.4*DOWN)

        txt_6= Tex("$C_t = \$115 $", 
        color= PURE_RED, font_size=36)
        txt_6.shift(2.1*DOWN)

        txt_7= Text("El capital al final de la inversión que realizamos es de $115.", 
        color= BLACK, font_size=22, font="Noto Sans", slant=ITALIC)
        txt_7.shift(2.8*DOWN)

        #Creación de escena
        self.play(Write(r_t1))
        self.wait()
        self.play(Write(txt_2))
        self.wait()
        self.play(Write(txt_3))
        self.wait(2)
        self.play(Write(txt_4))
        self.wait()
        self.play(Write(txt_5))
        self.wait()
        self.play(Write(txt_6))
        self.wait()
        self.play(Write(txt_7))
        self.wait(3)







###########################################################################################
##############################  Escena 3  #################################################
###########################################################################################

class Escena_3(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

        txt_1= Text("En conclusión podemos ver que el total obtenido es:", 
        color= BLACK, font_size=28, font="Noto Sans", line_spacing=1)
        txt_1.shift(1*UP)

        txt_2= Tex("$C_n = \$115 $", 
        color= PURE_RED, font_size=36)
        r_t2=self.rectangulo_texto(txt_2)

        txt_3= Text("Lo cual representa el Capital Inicial + la Suma de Intereses obtenidos\n"
        "por periodo y es igual a lo que obtuvimos anteriormente.", 
        color= BLACK, font_size=24, font="Noto Sans", slant=ITALIC, line_spacing=1)
        txt_3.shift(1.2*DOWN)

        rect= Rectangle(width=12, height=4, color=BLACK)

        #Creación de escena
        self.play(Write(rect), Write(txt_1))
        self.wait()
        self.play(Write(r_t2))
        self.wait()
        self.play(Write(txt_3))
        self.wait(3)

###########################################################################################
##############################  Escena 4  #################################################
###########################################################################################

class Escena_4(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):
        # Construccion de ejes
        ax_1 = Axes(
            x_range=[0, 6, 1],
            y_range=[90, 120, 5],
            x_length=5,
            y_length=4,
            axis_config={'color' : BLACK , 'include_numbers': True , 'font_size':30,
            'decimal_number_config' : {
                    'num_decimal_places' : 0,
                    'color' : BLACK}}
        )

        # Posicion de Ejes
        ax_1.shift(0.5*DOWN)

        y_label = ax_1.get_y_axis_label(Tex("\\textbf{Monto}",color=BLACK, font_size=26), edge=LEFT, direction=LEFT, buff=0.3)
        x_label = ax_1.get_x_axis_label(Tex("\\textbf{Tiempo}",color=BLACK, font_size=26), edge=DOWN, direction=DOWN, buff=0.2)
        grid_labels = VGroup(x_label, y_label)
        
        # Creación de Curvas
        curve_1 = ax_1.plot(lambda x: 100*(1+0.03*x), color=PURE_RED, x_range=[0,5])
        

        #Texto
        pres= Text("Gráficamente la tasa de interés simple en este ejemplo se ve de la siguiente manera: ", 
        color= BLACK, font_size=24, font="Noto Sans", t2w={'alta':BOLD}, line_spacing=1)
        pres.shift(2.5*UP)
        txt_1=self.rectangulo_texto(pres)

        #Punto
        moving_dot = Dot(ax_1.i2gp(curve_1.t_min, curve_1), color=BLACK, radius=0.15)
        dot_1 = Dot(ax_1.i2gp(curve_1.t_min, curve_1), color= PURE_RED)
        dot_2 = Dot(ax_1.i2gp(curve_1.t_max, curve_1), color= PURE_RED)

        #Creación de escena
        self.add(ax_1, curve_1,txt_1, dot_1, dot_2, grid_labels)
        self.play(Write(txt_1))
        self.wait()
        self.play(MoveAlongPath(moving_dot, curve_1, rate_func=linear), run_time=3)
        self.play(MoveAlongPath(moving_dot, curve_1, rate_func=linear), run_time=3)
        self.play(MoveAlongPath(moving_dot, curve_1, rate_func=linear), run_time=3)
       
        self.wait(5)
