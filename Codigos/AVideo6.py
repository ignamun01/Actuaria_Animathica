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

        #####################Primera subescena######################################

        #Textos
        txt_1= Text("La fórmula que utilizaremos para calcular el interés compuesto será la siguiente:", 
        color= BLACK, font_size=28, font="Noto Sans",t2w={'interés compuesto':BOLD})
        txt_1.shift(2*UP)

        txt_2= Tex("$C_{n} = C_{0}  (1+i)^{n}$", 
        color= PURE_RED, font_size=36)
        txt_2.shift(1*UP)

        rtxt_2=self.rectangulo_texto(txt_2)

        txt_3= Tex("Donde: ", 
        color= BLACK, font_size=32,)

        txt_4=BulletedList("$C_n$= Capital  Resultante al tiempo n.", 
        "$C_0$= Monto inicial del valor entregado como préstamo o inversión.",
        "i = La tasa de interés del período, expresada en forma decimal.",
        "n = Número de períodos de tiempo en los cuales se va a capitalizar.", font_size=30)
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




        ##################### SEGUNDA SUBESCENA ######################################

        txt_5= Text("Observemos la siguiente línea del tiempo: ", 
        color= BLACK, font_size=28, font="Noto Sans")
        rtxt_5=self.rectangulo_texton(txt_5)
        rtxt_5.shift(1.5*UP)

        t_2=Tex("0", color= BLACK, font_size=16)
        t_3=Tex("1", color= BLACK, font_size=16)
        t_4=Tex("2", color= BLACK, font_size=16)
        t_5=Tex("3", color= BLACK, font_size=16)
        t_6=Tex(".", color= BLACK, font_size=16)
        t_7=Tex(".", color= BLACK, font_size=16)
        t_8=Tex(".", color= BLACK, font_size=16)
        t_9=Tex("n - 1", color= BLACK, font_size=14)
        t_10=Tex("n", color= BLACK, font_size=16)
        dict_1= {0:t_2,1:t_3,2:t_4,3:t_5,4:t_6,5:t_7,6:t_8,7:t_9,8:t_10}


        l1 = NumberLine(
            x_range=[0, 9, 1],
            length=12,
            color=PURE_BLUE,
            include_tip=True,
            label_direction=DOWN,
            include_ticks=True,
            tick_size=0.20,
            line_to_number_buff=0.40
        )

        l1.shift(1*DOWN)
        l1.add_labels(dict_1)


        ##################### Objetos Tiempo 0 ############################
        txt_6= Tex("Posicionémonos en \\textbf{tiempo t=0} donde nuestro capital es $C_0$,\n"
        "el cual es el capital inicial.", 
        color= BLACK, font_size=38)
        rtxt_6=self.rectangulo_texton(txt_6)
        rtxt_6.shift(2*UP)

        t_21=Tex("\\textbf{$C_0$}", color= BLACK, font_size=28)
        t_21.shift(6* LEFT + 0.3*DOWN)


        ##################### Objetos Tiempo 1 ############################
        txt_7= Tex("Ahora, queremos saber cuánto tendremos de intereses en el \\textbf{periodo 1}.\n"
        "Lo cual sería igual a $C_1 = C_0(1+i)^1 = C_0(1+i)$", 
        color= BLACK, font_size=38)
        rtxt_7=self.rectangulo_texton(txt_7)
        rtxt_7.shift(2*UP)

        t_22=Tex("\\textbf{$C_0 (1+i)$}", color= BLACK, font_size=26)
        t_22.shift(4.8* LEFT + 0.3*DOWN)


        ##################### Objetos Tiempo 2 ############################
        txt_8= Tex("Para el \\textbf{periodo 2}, entra en juego la magia del interés compuesto.", 
        color= BLACK, font_size=38)
        rtxt_8=self.rectangulo_texton(txt_8)
        rtxt_8.shift(3*UP)

        txt_8_1= Tex("Esto se debe a que para el \\textbf{periodo 2}, el capital inicial que se usará\\\\para calcular los nuevos intereses será el capital acumulado en\\\\"
        "el periodo 1 con todo e intereses, es decir:\\\\"
        "a) $C_2 = C_1(1+i)$\\\\ o bien\\\\"
        "b) $C_2 = C_0(1+i)^{2}$",
        color= BLACK, font_size=38)

    
        rtxt_8_1=self.rectangulo_texton(txt_8_1)
        rtxt_8_1.shift(2*UP)

        t_23=Tex("\\textbf{$C_0 (1+i)^2$}", color= BLACK, font_size=26)
        t_23.shift(3.3* LEFT + 0.3*DOWN)




        ##################### Objetos Tiempo 3 ############################
        txt_9= Tex("Siguiendo esta lógica para saber los intereses acumulados hasta el\n"
        "\\textbf{tiempo 3}, tenemos la siguiente expresión: ", 
        color= BLACK, font_size=38)
        rtxt_9=self.rectangulo_texton(txt_9)
        rtxt_9.shift(1.5*UP)

        t_24=Tex("\\textbf{$C_0 (1+i)^3$}", color= BLACK, font_size=26)
        t_24.shift(1.9* LEFT + 0.3*DOWN)


        ##################### Objetos Tiempo n-1 ############################


        t_25=Tex("\\textbf{$C_0 (1+i)^{n-1}$}", color= BLACK, font_size=24)
        t_25.shift(3.3* RIGHT + 0.3*DOWN)


        ##################### Objetos Tiempo n ############################
        txt_10= Tex("Generalizando esta expresión para cualquier \\textbf{tiempo n} de vencimiento,"
        "los intereses acumulados más el capital inicial se calculan usando la expresión: \\\\"
        "$C_n = (1+i)^n$", 
        color= BLACK, font_size=38)
        rtxt_10=self.rectangulo_texton(txt_10)
        rtxt_10.shift(2*UP)

        t_26=Tex("\\textbf{$C_0 (1+i)^n$}", color= BLACK, font_size=26)
        t_26.shift(4.85* RIGHT + 0.3*DOWN)


        muñeco = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/muñeco.png")
        muñeco.height=0.5
        muñeco.width=0.5
        muñeco.shift(2.5*DOWN+6*LEFT)

        muñeco.generate_target()
        muñeco.target.shift(1.3*RIGHT)


        #####Entrada a subscena 2#####
        self.play(Write(rtxt_5))
        self.play(Write(l1))
        self.play(ReplacementTransform(rtxt_5,rtxt_6))
        self.wait()
        self.play(Write(t_21),FadeIn(muñeco))
        self.wait()

        #Movimiento al 1
        self.play(MoveToTarget(muñeco))
        self.wait()
        self.play(Write(t_22), ReplacementTransform(rtxt_6,rtxt_7))
        self.wait()

        #Movimiento al 2
        muñeco.generate_target()
        muñeco.target.shift(1.4*RIGHT)
        self.play(MoveToTarget(muñeco))
        self.wait()
        self.play(Write(t_23), ReplacementTransform(rtxt_7,rtxt_8))
        self.wait(2)
        self.play(ReplacementTransform(rtxt_8,rtxt_8_1))
        self.wait()

        #Movimiento al 3
        muñeco.generate_target()
        muñeco.target.shift(1.25*RIGHT)
        self.play(MoveToTarget(muñeco))
        self.wait()
        self.play(Write(t_24), ReplacementTransform(rtxt_8_1,rtxt_9))
        self.wait()

        #Movimiento al n-1
        muñeco.generate_target()
        muñeco.target.shift(5.4*RIGHT)
        self.play(MoveToTarget(muñeco))
        self.wait()
        self.play(Write(t_25), ReplacementTransform(rtxt_9,rtxt_10))
        self.wait()

        #Movimiento al n
        muñeco.generate_target()
        muñeco.target.shift(1.45*RIGHT)
        self.play(MoveToTarget(muñeco))
        self.wait()
        self.play(Write(t_26))
        self.wait()





class Escena_2(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

        txt_1= Tex("Supongamos que el banco le ofrece un producto de inversión el cual consta de recibir una tasa de interés compuesta del $3\%$ al año sobre \$100 invertidos durante 5 años.", 
        color= BLACK, font_size=38)
        txt_1.shift(2.7*UP)
        r_t1=self.rectangulo_texto(txt_1)

        txt_2= Text("Analicemos la información que nos dan:", 
        color= BLACK, font_size=24, font="Noto Sans")
        txt_2.shift(1.5*UP)

        txt_3=BulletedList("$C_0$ = 100", "i = $3\%$", "n = 5 Años", font_size=30, buff=0.3)
        txt_3.set_color(BLACK)
        txt_3.shift(0.4*UP)

        txt_4=Text("Usando la expresión que tenemos para el interés simple:",
        color= BLACK, font_size=24, font="Noto Sans")
        txt_4.shift(0.8*DOWN)

        txt_5= Tex("$C_5 = 100 (1 + 0.03)^5$", 
        color= PURE_RED, font_size=36)
        txt_5.shift(1.4*DOWN)

        txt_6= Tex("$C_5 = \$115.9274074 $", 
        color= PURE_RED, font_size=36)
        txt_6.shift(2.1*DOWN)


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
        self.wait(3)


