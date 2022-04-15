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

        #Textos
        txt_1= Tex("La capitalización \\textbf{continua} está definida de la siguiente manera:", 
        color= BLACK, font_size=38)
        txt_1.shift(2*UP)
        

        txt_2= Tex("$C_{n} = C_{0} \hspace{0.25cm} e^{\delta t}$", 
        color= PURE_RED, font_size=36)
        txt_2.shift(1*UP)

        rtxt_2=self.rectangulo_texto(txt_2)

        txt_3= Tex("Donde: ", 
        color= BLACK, font_size=32)
        txt_3.shift(2*LEFT)

        txt_4=BulletedList("$C_n$= Capital  Resultante al tiempo n.", 
        "$C_0$= Capital inicial",
        "$\delta$ = Fuerza de interes",
        "t = Tiempo medido en AÑOS.", font_size=30)
        txt_4.shift(2*DOWN)
        txt_4.set_color(BLACK)

        ##### Entrada subescena 1 #####
        self.play(Write(txt_1))
        self.wait()
        self.play(Write(rtxt_2))
        self.wait()
        self.play(Write(txt_3), Write(txt_4))
        self.wait(2)
        self.play(FadeOut(txt_1), FadeOut(rtxt_2), FadeOut(txt_3), FadeOut(txt_4))
        self.wait()







###########################################################################################
##############################  Escena 2  #################################################
###########################################################################################


class Escena_2(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):
#################### Primera Subescena #####################################################

        txt_1= Tex("Por definición tenemos que:", 
        color= BLACK, font_size=38)
        txt_1.shift(1.2*UP)

        txt_2= Tex("$i_t = \\frac{A(t)-A(t-1)}{A(t-1)}$", 
        color= PURE_RED, font_size=45)

        txt_3=Tex("Por lo tanto:", 
        color= BLACK, font_size=38)
        txt_3.shift(1.2*UP)

        txt_4=Tex("$i_{t+1} = \\frac{A(t+1)-A(t)}{A(t)}$", 
        color= PURE_RED, font_size=45)

        txt_5= Tex("Generalizando tenemos la siguiente expresión:", 
        color= BLACK, font_size=38)
        txt_5.shift(1.2*UP)

        txt_6= Tex("$i_{t+\Delta}  = \\frac{A(t+\Delta)-A(t)}{A(t)}$", 
        color= PURE_RED, font_size=45)

        txt_7= Tex("\\textit{Tasa efectiva en el periodo de tiempo $\Delta$}", 
        color= BLACK, font_size=30)
        txt_7.shift(0.9*DOWN)

        txt_8= Tex("Dividiendo entre delta la expresión tenemos:", 
        color= BLACK, font_size=38)
        txt_8.shift(0.8*UP)

        txt_9= Tex("$\\frac{i_{t+\Delta}}{\Delta}  = \\frac{A(t+\Delta)-A(t)}{A(t) * \Delta}$", 
        color= PURE_RED, font_size=45)
        txt_9.shift(0.3*DOWN)

        txt_10= Tex("Ahora tomamos el límite:", 
        color= BLACK, font_size=38)
        txt_10.shift(2.5*UP)

        txt_11= Tex("$\lim\limits_{\Delta \\to 0} \\frac{i_{t+\Delta}}{\Delta}  = \lim\limits_{\Delta \\to 0} \\frac{A(t+\Delta)-A(t)}{A(t) * \Delta}$", 
        color= PURE_RED, font_size=45)
        txt_11.shift(1.5*UP)

        txt_12= Tex("Sacamos A(t) fuera del límite pues no depende de delta:", 
        color= BLACK, font_size=38)
        txt_12.shift(2.5*UP)

        txt_13= Tex("$\lim\limits_{\Delta \\to 0} \\frac{A(t+\Delta)-A(t)}{A(t) * \Delta}  = \\frac{1}{A(t)} \lim\limits_{\Delta \\to 0} \\frac{A(t+\Delta)-A(t)}{\Delta}$", 
        color= PURE_RED, font_size=45)
        txt_13.shift(1.5*UP)

        txt_14= Tex("El límite de la expresión anterior define la derivada de la función de monto A(t) en el instante t.", 
        color= BLACK, font_size=38)
        txt_14.shift(0.5*DOWN)

        txt_15= Tex("$\\frac{1}{A(t)} \lim\limits_{\Delta \\to 0} \\frac{A(t+\Delta)-A(t)}{\Delta} = \\frac{A'(t)}{A(t)}$", 
        color= PURE_RED, font_size=45)
        txt_15.shift(2*DOWN)
        rtxt_15=self.rectangulo_texto(txt_15)
        rtxt_15.generate_target()
        rtxt_15.target.shift(5*UP)

        simb= Tex("$ --- \circledast$", 
        color= PURE_RED, font_size=45)
        simb.shift(2*DOWN + 4*RIGHT)
        simb.generate_target()
        simb.target.shift(5*UP)

        rect_1 = Rectangle(color=BLACK, height=3.5, width=9)
        rect_1.shift(0.4*UP)

        rect_2 = Rectangle(color=BLACK, height=4.5, width=10)
        rect_2.shift(0.4*UP)

        self.play(Write(rect_1),Write(rect_2),Write(txt_1),Write(txt_2))
        self.wait(3)
        self.play(ReplacementTransform(txt_1,txt_3),ReplacementTransform(txt_2,txt_4))
        self.wait(3)
        self.play(ReplacementTransform(txt_3,txt_5),ReplacementTransform(txt_4,txt_6), FadeIn(txt_7))
        self.wait(3)
        self.play(FadeOut(txt_7),ReplacementTransform(txt_5,txt_9),ReplacementTransform(txt_6,txt_8))
        self.wait(3)
        self.play(FadeOut(rect_1), FadeOut(rect_2), ReplacementTransform(txt_9,txt_11),ReplacementTransform(txt_8,txt_10))
        self.wait(3)
        self.play(ReplacementTransform(txt_11,txt_13),ReplacementTransform(txt_10,txt_12))
        self.wait(3)
        self.play(Write(txt_14))
        self.wait(0.5)
        self.play(Write(rtxt_15), Write(simb))
        self.wait(3)
        self.play(FadeOut(txt_12), FadeOut(txt_13),FadeOut(txt_14))
        self.play(MoveToTarget(rtxt_15),MoveToTarget(simb))
        self.wait()

#################### Segunda Subescena #####################################################

        t_1= Tex("La función A(t) es igual a la función de acumulación por las k unidades monetarias que se van a acumular.", 
        color= BLACK, font_size=38)
        t_1.shift(1.5*UP)

        t_2= Tex("$(1) --- A(t) = a(t) * k  \hspace{0.5cm} \\Longrightarrow \hspace{0.5cm} (2) --- A'(t) = a'(t) * k $", color= PURE_RED, font_size=40)
        t_2.shift(0.5*UP)

        t_3= Tex("Entonces por la regla de la cadena tenemos: ", 
        color= BLACK, font_size=38)
        t_3.shift(1.5*UP)

        t_5= Tex("Reemplazando (1) y (2) en $\circledast$ tenemos: ", 
        color= BLACK, font_size=38)
        t_5.shift(0.5*DOWN)

        t_6= Tex("$\\frac{1}{A(t)} \lim\limits_{\Delta \\to 0} \\frac{A(t+\Delta)-A(t)}{\Delta} = \\frac{a'(t) * k}{a(t) * k}$", color= PURE_RED, font_size=43)
        t_6.shift(1.6*DOWN)


        self.play(Write(t_1), Write(t_2))
        self.wait(2)
        self.play(ReplacementTransform(t_1,t_3))
        self.wait(2)
        self.play(Write(t_5), Write(t_6))
        self.wait(2)
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

#################### Primera Subescena #####################################################

        txt_1= Tex("Notemos que resulta la definición de la derivada del logaritmo natural de la función de acumulación:", 
        color= BLACK, font_size=38)
        txt_1.shift(2*UP)

        txt_2= Tex("$\\frac{a'(t) * k}{a(t) * k} = \\frac{d}{dt} ln(a(t))$", 
        color= PURE_RED, font_size=45)
        txt_2.shift(0.8*UP)

        txt_3= Tex("Igualamos la expresión anterior a $\delta$ y resolvemos para a(t).", 
        color= BLACK, font_size=38)
        txt_3.shift(2.5*UP)

        txt_4= Tex("$\delta = \\frac{d}{dt} ln(a(t))$", 
        color= PURE_RED, font_size=40)
        txt_4.shift(1.7*UP)

        txt_5= Tex("$\\Longrightarrow  \int \limits_{0}^{t} \delta \hspace{0.15cm} dt= \int \limits_{0}^{t} \\frac{d}{dt} ln(a(t)) \hspace{0.15cm} dt$", 
        color= PURE_RED, font_size=40)
        txt_5.shift(0.6*UP)

        txt_6= Tex("$\\Longrightarrow  \int \limits_{0}^{t} \delta \hspace{0.15cm} dt= ln(a(t)) - ln(a(0))$", 
        color= PURE_RED, font_size=40)
        txt_6.shift(0.6*DOWN)

        txt_7= Tex("$\\Longrightarrow  \int \limits_{0}^{t} \delta \hspace{0.15cm} dt = ln(\\frac{a(t)}{a(0)})$", 
        color= PURE_RED, font_size=40)
        txt_7.shift(1.7*DOWN)

        txt_8= Tex("$\\Longrightarrow  \int \limits_{0}^{t} \delta \hspace{0.15cm} dt = ln(a(t))$", 
        color= PURE_RED, font_size=40)
        txt_8.shift(2.9*DOWN)
        txt_8.generate_target()
        txt_8.target.shift(5*UP)

        txt_9= Tex("$\\Longrightarrow \delta * t  = ln(a(t))$", 
        color= PURE_RED, font_size=40)
        txt_9.shift(1*UP)

        txt_10= Tex("$\\Longrightarrow e^{\delta * t}  = a(t)$", 
        color= PURE_RED, font_size=40)
        rtxt_10=self.rectangulo_texto(txt_10)

        txt_11= Tex("\\textit{Función de acumulación para una fuerza de interés continua $\delta$.}", 
        color= BLACK, font_size=38)
        txt_11.shift(1*DOWN)


        self.play(Write(txt_1), Write(txt_2))
        self.wait(2)
        self.play(ReplacementTransform(txt_1, txt_3), ReplacementTransform(txt_2, txt_4))
        self.wait(2)
        self.play(Write(txt_5))
        self.wait()
        self.play(Write(txt_6))
        self.wait()
        self.play(Write(txt_7))
        self.wait()
        self.play(Write(txt_8))
        self.wait()
        self.play(FadeOut(txt_3), FadeOut(txt_4), FadeOut(txt_5), FadeOut(txt_6), FadeOut(txt_7))
        self.wait()
        self.play(MoveToTarget(txt_8))
        self.play(Write(txt_9))
        self.wait()
        self.play(Write(rtxt_10))
        self.wait()
        self.play(Write(txt_11))
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

#################### Segunda Subescena #####################################################

        t1= Tex("Con el resultado anterior estamos listos para definir la triple igualdad entre \\textbf{funciones de acumulación}.", 
        color= BLACK, font_size=38)
        t1.shift(2.5*UP)

        t2= Tex("$(1+i) \hspace{0.20cm} = \hspace{0.20cm} (1+(\\frac{i^{(m)})}{m})^m \hspace{0.20cm} = \hspace{0.20cm} e^{\delta}$", 
        color= PURE_RED, font_size=40)
        t2.shift(1*UP)
        rt2=self.rectangulo_texto(t2)

        t3= Tex("Como consecuencia de la expresión $\delta$ = ln(a(t)) tenemos las siguientes fórmulas para calcular la fuerza de interés:", 
        color= BLACK, font_size=38)
        t3.shift(0.5*DOWN)

        t4=BulletedList("$\delta = ln(1+i)$", 
        "$\delta = m*ln((1+(\\frac{i^{(m)})}{m}))$", font_size=30)
        t4.shift(2*DOWN)
        t4.set_color(BLACK)

        self.play(Write(t1))
        self.wait()
        self.play(Write(rt2))
        self.wait()
        self.play(Write(t3),Write(t4))
        self.wait()


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
        txt_1= Tex("Supongamos que Rosa quiere invertir \$100 y el banco le ofrece un producto que tiene",
        " un vencimiento de 5 años y capitaliza con una fuerza de interés $\delta$ = 3\%. \hspace{5cm}¿Cuánto tendrá de capital Rosa al final de su inversión?", 
        color= BLACK, font_size=36)
        txt_1.shift(2.5*UP)
        rtxt_1=self.rectangulo_texton(txt_1)

        t4=BulletedList("$\delta = 3\%$", 
        "t = 5 años ", 
        "$C_0 = \$100$",font_size=32)
        t4.set_color(BLACK)
        t4.shift(0.5*UP)

        t5= Tex("Usando la expresión que tenemos para el interés continuo tenemos que:",
        color= BLACK, font_size=36)
        t5.shift(1.2*DOWN)

        txt_2=Tex("$C_n = C_0 * e^{\delta * n}$", color= BLACK, font_size=38)
        txt_2.shift(2*DOWN)

        txt_3=Tex("$C_5 = 100 * e^{3\% * 5}$", color= BLACK, font_size=38)
        txt_3.shift(2.6*DOWN)

        txt_4=Tex("$ C_5 = \$ 116.1834243 $", color= PURE_RED, font_size=38)
        txt_4.shift(3.3*DOWN)
        rtxt_4=self.rectangulo_texto(txt_4)

        self.play(Write(rtxt_1))
        self.wait(2)
        self.play(Write(t4))
        self.wait(2)
        self.play(Write(t5),Write(txt_2))
        self.wait(2)
        self.play(Write(txt_3))
        self.wait(2)
        self.play(Write(rtxt_4))
        self.wait(2)
