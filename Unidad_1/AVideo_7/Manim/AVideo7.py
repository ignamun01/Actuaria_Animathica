from tkinter import LEFT, RIGHT
from manim import *
config.background_color = YELLOW_A
config["background_color"] = YELLOW_A


###########################################################################################
##############################  Escena 4  #################################################
###########################################################################################

#Escena_1: Definicion Tasa Nominal
class Escena_1(Scene):
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):
        

        #Textos
        t_1= Tex("Una tasa nominal anual capitalizable mensualmente se representa como", " $i^{(12)}$",", pues aun cuando\n"
        "la tasa esta expresada en terminos anuales está capitaliza 12 periodos en un año.", color= BLACK, font_size=34)
        t_1.shift(2*UP)
        t_1[1].set_color(PURE_RED)
        t_2= Tex("Una tasa nominal anual capitalizable bimestralmente se representa como"," $i^{(6)}$", " ya que hay 6 bimestres\n"
        "en un año entonces vamos a capitalizar 6 periodos en un año.", color= BLACK, font_size=34)
        t_2.shift(1*DOWN)
        t_2[1].set_color(PURE_RED)


        t_3=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_4=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_5=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_6=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_7=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_8=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_9=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_10=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_11=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_12=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_13=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        t_14=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        n_3=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        n_4=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        n_5=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        n_6=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        n_7=Text("$1", color= BLACK, font_size=22, font="Noto Sans")
        n_8=Text("$1", color= BLACK, font_size=22, font="Noto Sans")



        dict_1= {1:t_3,2:t_4,3:t_5,4:t_6,5:t_7,6:t_8}
        dict_2= {1:n_3,2:n_4,3:n_5,4:n_6,5:n_7,6:n_8, 7:t_9,8:t_10, 9:t_11, 10:t_12,11:t_13,12:t_14}

        #Lineas del tiempo
        l0 = NumberLine(
            x_range=[1, 13, 1],
            length=10,
            color=BLACK,
            include_tip=True,
            label_direction=UP,
            include_ticks=True,
            font_size=20
        )
        l0.shift(0.6*UP)
        l0.add_labels(dict_2)


        l0_1 = NumberLine(
            x_range=[1, 13, 1],
            length=10,
            color=BLACK,
            include_tip=True,
            label_direction=DOWN,
            include_ticks=True,
            font_size=28,
            include_numbers=True
        )
        l0_1.shift(0.6*UP)
        l0_1.numbers.set_color(BLACK)


        l1 = NumberLine(
            x_range=[1, 7, 1],
            length=10,
            color=BLACK,
            include_tip=True,
            label_direction=UP,
            include_ticks=True,
            include_numbers= False,
            font_size=20
        )
        l1.shift(2.7*DOWN)
        l1.add_labels(dict_1)


        l1_1 = NumberLine(
            x_range=[1, 7, 1],
            length=10,
            color=BLACK,
            include_tip=True,
            label_direction=DOWN,
            include_ticks=True,
            include_numbers= True,
            font_size=28
        )
        l1_1.shift(2.7*DOWN)
        l1_1.numbers.set_color(BLACK)


        self.play(Write(t_1))
        self.wait(2)
        self.play(Write(l0), FadeIn(l0_1))
        self.wait(2)
        self.play(Write(t_2))
        self.wait(1)
        self.play(Write(l1), FadeIn(l1_1))
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)


        #Segunda subescena

        #Textos

        texto_1=Tex("Para poder hacerlas efectivas por periodo\n"
        "simplemente dividimos entre la cantidad de períodos que capitalizan al año.", color= BLACK, font_size=38)



        texto_1.shift(2*UP)

        f_1=Tex("Tasa Nominal Capitalizable k veces al Año", "$i^{(k)}$", color= PURE_RED, font_size=32)
        f_2=Tex("Tasa Efectiva por Periodo de Capitalización", "$\\frac{i^{(k)}}{k}$", color= PURE_RED, font_size=32)
        f_3=Tex("$\Downarrow$", color= PURE_RED, font_size=50)
        
        f_1[0].shift(0.5*UP)
        f_1[1].shift(3*LEFT)
        rf_1= self.rectangulo_texton(f_1)
        f_2[0].shift(1.7*DOWN)
        f_2[1].shift(2.3*DOWN + 3.3*LEFT)
        rf_2= self.rectangulo_texton(f_2)
        f_3.shift(0.8*DOWN)
 
        self.play(Write(texto_1))
        self.wait()
        self.play(Write(rf_1), Write(rf_2),Write(f_3))
        self.wait(2)



###########################################################################################
##############################  Escena 2  #################################################
###########################################################################################

#Escena_2: Conversiones de tasas
class Escena_2(Scene):
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=GRAY_BROWN, fill_opacity=0.15, buff=0.3, corner_radius=0.1)
        grupo = VGroup(rect,objeto)
        return grupo

    def rectangulo_textot(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

        #Textos
        t_0= Tex("José invierte 2000 pesos en el banco a 1 año. El banco le ofrece "
        "una tasa nominal anual capitalizable bimestralmente del 7.5\%. \hspace{5cm}"
        "¿Cuánto tendrá al final del año?", color= BLACK, font_size=36)
        t_0.shift(2.2*UP)

        rt_0=self.rectangulo_texton(t_0)

        t_1= Tex("Como nuestra tasa es nominal y no efectiva, la dividiremos entre 6 "
        "para hacerla efectiva por periodo (cada 2 meses).", color= BLACK, font_size=34)
        t_1.shift(0.5*UP)

        t_2= Tex("Interés Bimestral= $\\frac{i^{(6)}}{6} = \\frac{7.5\%}{6} = 1.25\%$", color= PURE_RED, font_size=36)
        t_2.shift(0.8*DOWN)
        t_3= Text("Entonces el interés que estaremos acumulando bimestralmente será del 1.25%.", color= BLACK, font_size=22, slant=ITALIC)
        t_3.shift(1.8*DOWN)

        self.play(Write(rt_0)) 
        self.play(Write(t_1))
        self.wait()
        self.play(Write(t_2))
        self.wait(2)
        self.play(Write(t_3))
        self.wait()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)

        t_4=Tex("También podemos realizar conversiones de tasas de interés efectivas entre "
        "periodos, es decir podemos convertir una tasa efectiva mensual a una tasa efectiva "
        "semestral y así sucesivamente entre cualquier periodo.", color= BLACK, font_size=36)
        t_4.shift(2.25*UP)
        rt_4=self.rectangulo_textot(t_4)
        t_5= Tex("$1 + i = (1 + \\frac{i^{(k)}}{k})^k$", color= PURE_RED, font_size=34)
        t_5.shift(0.5*UP)
        t_6=Text("Donde:", color= BLACK, font_size=26)
        t_7= BulletedList("i= tasa efectiva anual.", 
        "$i^{(k)}$= tasa nominal capitalizable k periodos al año.",
        "k= número de periodos capitalizables al año.", font_size=30)
        t_6.shift(0.5*DOWN)
        t_7.set_color(BLACK)
        t_7.shift(2*DOWN)

        mob = SurroundingRectangle(t_5, corner_radius=0.1, color=PURE_RED) 

        self.play(Write(rt_4))
        self.wait()
        self.play(Write(t_5), Write(mob))
        self.wait()
        self.play(Write(t_6))
        self.wait()
        self.play(Write(t_7))
        self.wait(2)



###########################################################################################
##############################  Escena 3  #################################################
###########################################################################################

#Escena_3: Ejemplos de Conversiones de Tasas
class Escena_3(Scene):
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=GRAY_BROWN, fill_opacity=0.15, buff=0.3, corner_radius=0.1)
        grupo = VGroup(rect,objeto)
        return grupo

    def rectangulo_textot(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

        ##########################EJEMPLO 1 #################################

        #Textos
        t_1= Text("Veamos dos ejemplos de conversiones:", color= BLACK, font_size=40, line_spacing=1, font="Noto Sans")
        t_2=Tex("1- Supongamos que queremos convertir de una tasa efectiva del 5\% anual a una tasa efectiva semestral.", color= BLACK, font_size=32)
        t_2.shift(2.25*UP)
        rt_2=self.rectangulo_texton(t_2)

        t_3=Tex("$i_{anual}$ = $5\%$", color= BLACK, font_size=32)
        t_3.shift(1*UP + 2*LEFT)
        
        t_4=Tex("$i_{semestral}$ = $\\frac{i^{(2)}}{2}$ = $?\%$", color= BLACK, font_size=32)
        t_4.shift(1*UP+ 2.5*RIGHT)
        
        t_5=Tex("$\Rightarrow$", color= BLACK, font_size=34)
        t_5.shift(1*UP)

        t_6=Tex("Tenemos lo siguiente: ", color= BLACK, font_size=32)
        t_6.shift(3*LEFT+ 0.25*UP)

        t_7=Tex("$(1+0.05)$ = $(1+ \\frac{i^{(2)}}{2})^2$", "  , de donde despejamos $\\frac{i^{(2)}}{2}$",
        color= BLACK, font_size=32)
        t_7.shift(0.5*DOWN)
        t_7[0].set_color(PURE_RED)

        t_8=Tex("$\sqrt{(1+0.05)} - 1$ = $\\frac{i^{(2)}}{2}$", color= PURE_RED, font_size=32)
        t_8.shift(0.5*DOWN + 2*LEFT)

        t_9= Tex("$\Rightarrow$ ", " $\\frac{i^{(2)}}{2}$ = $2.469\%$", color= PURE_RED, font_size=32)
        t_9.shift(1.5*DOWN)

        t_10=Tex("\\textit{Lo cual dice que semestralmente se acumula el} $2.469\%$ \\textit{de interés.}", color= BLACK, font_size=32 )
        t_10.shift(2.5*DOWN)

        self.play(Write(t_1))
        self.wait(1)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        

        #Escena
        self.play(Write(rt_2))
        self.wait()
        self.play(Write(t_3), Write(t_4), Write(t_5))
        self.wait()
        self.play(Write(t_6))
        self.play(Write(t_7))
        self.wait(3)
        self.play(ReplacementTransform(t_7[0],t_8)) 
        self.wait(3)
        self.play(Write(t_9))
        self.wait(2)
        self.play(Write(t_10))
        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2) 


        ##########################EJEMPLO 2 #################################

        """ txt_1=Tex("2- Pasar de una tasa de interés nominal trimestral del $7\%$ a una tasa de\n"
        "interés efectiva mensual.", color= BLACK, font_size=32)
        txt_1.shift(2.25*UP)
        rtxt_1 = self.rectangulo_texton(txt_1)


        txt_2=Tex("$i^{(4)}$ = $7\%$", color= BLACK, font_size=32)
        txt_2.shift(1*UP + 2*LEFT)
        
        txt_3=Tex("$i_{mensual}$ = $\\frac{i^{(12)}}{12}$ = $?\%$", color= BLACK, font_size=32)
        txt_3.shift(1*UP+ 2.5*RIGHT)
        
        txt_4=Tex("$\Rightarrow$", color= BLACK, font_size=34)
        txt_4.shift(1*UP)

        txt_5=Tex("$(1+ \\frac{i^{(12)}}{12})^{12}$ = $(1+\\frac{i^{(4)}}{4})^4$",
        color=PURE_RED, font_size=34)
        txt_5.shift(0.7*DOWN)

        txt_6=Tex("$(1+ \\frac{i^{(12)}}{12})$ = $\sqrt[3]{(1+0.0175)}$", 
        color=BLACK, font_size=34)
        txt_6.shift(1.5*DOWN+0.53*RIGHT)

        txt_7=Tex("$\\frac{i^{(12)}}{12}$ = $\sqrt[3]{(1.0175)} - 1$", 
        color=BLACK, font_size=34)
        txt_7.shift(2.3*DOWN+1.3*RIGHT)

        txt_8=Tex("Tenemos lo siguiente:", color= BLACK, font_size=34)

        txt_9= Tex("$\Rightarrow$ ", " $\\frac{i^{(12)}}{12}$ = $0.5799\%$", color= PURE_RED, font_size=32)
        txt_9.shift(3.2*DOWN+ 0.2*RIGHT)
        

        self.play(Write(rtxt_1))
        self.wait()
        self.play(Write(txt_2), Write(txt_3), Write(txt_4))
        self.wait()
        self.play(Write(txt_8))
        self.wait()
        self.play(Write(txt_5))
        self.wait()
        self.play(Write(txt_6))
        self.wait()
        self.play(Write(txt_7))
        self.wait() 
        self.play(Write(txt_9))
        self.wait(2) """


###########################################################################################
##############################  Escena 6  #################################################
###########################################################################################

#Escena_4: Ejemplo del efecto de las tasas en el dinero.
class Escena_4(Scene):
    def rectangulo_texton(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=GRAY_BROWN, fill_opacity=0.15, buff=0.3, corner_radius=0.1)
        grupo = VGroup(rect,objeto)
        return grupo

    def rectangulo_textot(self,objeto):
        rect = SurroundingRectangle(objeto,color=PURE_RED, fill_color=YELLOW_A, fill_opacity=1, corner_radius=0.1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):

        ##########################EJEMPLO 1 #################################

        #Textos
        t_2=Tex("Supongamos que Juan invierte \$100 durante un año a una \hspace{5 cm} tasa nominal del 12\% anual.", color= BLACK, font_size=36)
        t_2.shift(2.5*UP)
        rt_2=self.rectangulo_texton(t_2)

        t_3=Tex("Calculemos el capital más el rendimiento obtenido al final del periodo usando la fórmula de interés simple:", color= BLACK, font_size=32)
        t_3.shift(1*UP)
        
        txt_4=BulletedList("$C_1$= Capital  Resultante al final del año.", 
        "$C_0$= Capital  inicial = \$100",
        "i = Tasa de interés = 12\%",
        "t = Periodo de tiempo considerado = 1 año", font_size=28)
        txt_4.shift(1.9*DOWN)
        txt_4.set_color(BLACK)

        t_4=Tex("$C_1 \hspace{0.10 cm}= \hspace{0.10 cm}C_0 (1 + i*t) \hspace{0.10 cm}= \hspace{0.10 cm}100(1+0.12*1) \hspace{0.10 cm}= \hspace{0.10 cm}100(1.12) \hspace{0.10 cm}= \hspace{0.10 cm} \\textbf{\$112} $", 
        color= PURE_RED, font_size=32)
        
        
        


        #Escena
        self.play(Write(rt_2))
        self.wait()
        self.play(Write(t_3))
        self.wait()
        self.play(Write(t_4), Write(txt_4))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2) 

        ############################## Segunda Escenario #############################
        t_5=Tex("Ahora supongamos que Juan invierte \$100 durante un año con una \hspace{5 cm} tasa nominal del 12\% anual" 
        " capitalizable trimestralmente.", color= BLACK, font_size=36)
        t_5.shift(2.5*UP)
        rt_5=self.rectangulo_texton(t_5)

        t_6=Tex("Como tenemos una tasa anual que capitaliza 4 veces en el año, es necesario convertir esta tasa de interés a una"
        " efectiva por periodo.", 
        color= BLACK, font_size=32)
        t_6.shift(1*UP)

        t_7=Tex("$i^{(4)}$ = $12\%$", color= BLACK, font_size=32)
        t_7.shift(2*LEFT)
        
        t_8=Tex("$i_{trimestral}$ = $\\frac{i^{(4)}}{4}$ = $3\%$", color= BLACK, font_size=32)
        t_8.shift(2.5*RIGHT)
        
        t_9=Tex("$\Rightarrow$", color= BLACK, font_size=34)
        
        t_10=Tex("$C_1 \hspace{0.10 cm}= \hspace{0.10 cm}C_0 (1 + i*1) \hspace{0.10 cm}= \hspace{0.10 cm}100(1+\\frac{0.12}{4})^4 \hspace{0.10 cm}= \hspace{0.10 cm}100(1.03)^4 \hspace{0.10 cm}= \hspace{0.10 cm} \\textbf{\$112.550881} $", 
        color= PURE_RED, font_size=32)
        t_10.shift(2*DOWN)

        t_11=Tex("Calculamos el capital más el rendimiento obtenido al final del periodo usando la fórmula de interés compuesto", color= BLACK, font_size=32)
        t_11.shift(1*DOWN)

        t_12=Tex("$C_1 \hspace{0.10 cm}= \hspace{0.10 cm} \\textbf{\$112.550881} $", 
        color= PURE_RED, font_size=32)
        t_12.shift(2.7*DOWN)
        rt_12=self.rectangulo_textot(t_12)


        self.play(Write(rt_5))
        self.wait()
        self.play(Write(t_6))
        self.wait()
        self.play(Write(t_7), Write(t_8), Write(t_9))
        self.wait(2)
        self.play(Write(t_11), Write(t_10))
        self.wait()
        self.play(Write(rt_12))
        self.wait(2)


       







        





        



