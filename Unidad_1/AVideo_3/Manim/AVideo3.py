from manim import *
config.background_color = YELLOW_A
config["background_color"] = YELLOW_A

###########################################################################################
##############################  Escena 1  #################################################
###########################################################################################

class Escena_1(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # Grafica y sus ejes
        ax = Axes(x_range=[0, 8], y_range=[0, 50 , 10] , axis_config={'color' : BLACK}, x_length=5,y_length=5)
        graph = ax.plot(lambda x: x**2, color=BLACK, x_range=[0, 7])
        ax.shift(0.5*DOWN)
       
        # Punto inicial y final
        dot_1 = Dot(ax.i2gp(graph.t_min, graph), color=BLACK)
        dot_1.shift(0.5 * UP)
        dot_2 = Dot(ax.i2gp(graph.t_max, graph), color=BLACK)
        dot_2.shift(0.5 * UP)


        #Titulo eje y
        y_label = ax.get_y_axis_label(
            Tex("Crecimiento del dinero", color=BLACK).scale(0.65).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=0.3,
        )

        #Titulo eje X
        x_label = ax.get_x_axis_label(
            Tex("Transcurso del tiempo", color=BLACK).scale(0.65),
            edge=DOWN,
            direction=DOWN,
            buff=0.3,
        )

        #Imagenes
        shirt = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/billete.png")
        shirt.height=1
        shirt.width=1
        shirt.shift(2.5* DOWN + 2.5 * LEFT)

        #Textos

        pres= Text("Una tasa de interés hace referencia a la cantidad de dinero que se abona \nen un periodo determinado de tiempo por cada unidad monetaria invertida.", 
        color= BLACK, font_size=28, font="Noto Sans")

        pres.shift(3.25*UP)

        ##Creación de escena

        self.add(ax, graph, dot_1, dot_2, shirt, y_label, x_label,pres)
        self.wait(5)
        self.play(self.camera.frame.animate.scale(0.80).move_to(shirt),run_time=2)

     
        def update_curve(mob):
            mob.move_to(shirt.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(shirt, graph, rate_func=linear),run_time=2)
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
        self.wait(2)



###########################################################################################
##############################  Escena 2  #################################################
###########################################################################################

#TIIE Altas  ---> Mas incentivo al ahorro
class Escena_2(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):
        # Construccion de ejes
        ax_1 = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 2.5, 0.5],
            x_length=5,
            y_length=4,
            axis_config={'color' : BLACK , 'include_ticks': False}
        )

        # Posicion de Ejes
        ax_1.shift(1.5*DOWN)


        # Creación de Curvas
        curve_1 = ax_1.plot(lambda x: x**(1/2), color=BLACK, x_range=[0.05,0.99])
        curve_1_1 = ax_1.plot(lambda x: x**(1/2), color=BLACK, x_range=[1,2.3])
        curve_2 = ax_1.plot(lambda x: 2**(-x+1), color=PURE_RED, x_range=[0.05, 0.99])
        curve_2_1 = ax_1.plot(lambda x: 2**(-x+1), color=PURE_RED, x_range=[1, 2.3])

        l_c1= ax_1.get_graph_label(curve_1_1, label=Text('TIIE', font_size=24)
        , color=BLACK)
        l_c2= ax_1.get_graph_label(curve_2_1, label=Text('Motivación', font_size=24)
        , color=PURE_RED)
        labels=VGroup(l_c1, l_c2)

        curves = VGroup(curve_1, curve_2, curve_1_1, curve_2_1)

        #Imagenes
        shirt = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/triste.png")
        shirt.height=0.8
        shirt.width=0.8
        shirt.shift(1* DOWN +  1.7* RIGHT)

        porcentaje = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/porcentaje.png")
        porcentaje.height=0.8
        porcentaje.width=0.8
        porcentaje.shift(3.2* DOWN +  6.5 * LEFT)

        feliz = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/feliz.png")
        feliz.height=0.8
        feliz.width=0.8

        #Texto

        pres= Text("Dicho lo anterior, si la TIIE es muy alta, implica que el Estado busca incentivar\nel ahorro en la población, pues el interés que se pagaría al obtener un crédito\nsería mayor y por consiguiente, desmotiva a las personas a endeudarse o \nadquirir créditos.", 
        color= BLACK, font_size=28, font="Noto Sans", t2w={'alta':BOLD}, line_spacing=1)
        pres.shift(2*UP)
        txt_1=self.rectangulo_texto(pres)

        #Creación de escena
        self.add(ax_1, curves,labels)
        self.play(Write(txt_1))
        self.wait(11)

        self.play(MoveAlongPath(porcentaje, curve_1, rate_func=linear), 
        MoveAlongPath(feliz, curve_2, rate_func=linear), run_time=4)
        self.remove(feliz)
        self.play(MoveAlongPath(porcentaje, curve_1_1, rate_func=linear), 
        MoveAlongPath(shirt, curve_2_1, rate_func=linear),run_time=4)

        self.wait(5)



###########################################################################################
##############################  Escena 3  #################################################
###########################################################################################



#TIIE Bajas  ---> Menos incentivo al ahorro
class Escena_3(Scene):
    def rectangulo_texto(self,objeto):
        rect = SurroundingRectangle(objeto,color=BLACK, fill_color=YELLOW_A, fill_opacity=1)
        grupo = VGroup(rect,objeto)
        return grupo

    def construct(self):
        # Construccion de ejes
        ax_1 = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 2.5, 0.5],
            x_length=5,
            y_length=4,
            axis_config={'color' : BLACK, 'include_ticks': False}
        )

        # Posicion de Ejes
        ax_1.shift(1.5*DOWN)


        # Creación de Curvas
        curve_1 = ax_1.plot(lambda x: x**(1/2), color=PURE_RED, x_range=[0.05,0.99])
        curve_1_1 = ax_1.plot(lambda x: x**(1/2), color=PURE_RED, x_range=[1,2.3])
        curve_2 = ax_1.plot(lambda x: 2**(-x+1), color=BLACK, x_range=[0.05, 0.99])
        curve_2_1 = ax_1.plot(lambda x: 2**(-x+1), color=BLACK, x_range=[1, 2.3])

        l_c1= ax_1.get_graph_label(curve_1_1, label=Text('Motivación', font_size=24)
        , color=PURE_RED)
        l_c2= ax_1.get_graph_label(curve_2_1, label=Text('TIIE', font_size=24)
        , color=BLACK)
        labels=VGroup(l_c1, l_c2)

        curves = VGroup(curve_1, curve_2, curve_1_1, curve_2_1)

        #Imagenes
        shirt = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/triste.png")
        shirt.height=0.8
        shirt.width=0.8
        shirt.shift(1* DOWN +  1.7* RIGHT)

        porcentaje = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/porcentaje.png")
        porcentaje.height=0.8
        porcentaje.width=0.8
        porcentaje.shift(3.2* DOWN +  6.5 * LEFT)

        feliz = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/feliz.png")
        feliz.height=0.8
        feliz.width=0.8

        #Texto

        pres= Text("Por otro lado, si la TIIE es muy baja, implica que el Estado busca incentivar\nel gasto en la población, pues el interés que se pagaría al obtener un crédito\nsería menor y por consiguiente, motiva a las personas a endeudarse o \nadquirir créditos", 
        color= BLACK, font_size=28, font="Noto Sans",t2w={'baja':BOLD}, line_spacing=1)
        pres.shift(2*UP)
        txt_1=self.rectangulo_texto(pres)

        #Creación de escena
        self.add(ax_1, curves, labels)
        self.play(Write(txt_1))
        self.wait(10)

        self.play(MoveAlongPath(shirt, curve_1, rate_func=linear), 
        MoveAlongPath(porcentaje, curve_2, rate_func=linear), run_time=5)
        self.remove(shirt)
        self.play(MoveAlongPath(feliz, curve_1_1, rate_func=linear), 
        MoveAlongPath(porcentaje, curve_2_1, rate_func=linear),run_time=5)

        self.wait(5)


###########################################################################################
##############################  Escena 4  #################################################
###########################################################################################

class Escena_4(Scene):
    def construct(self):

        #Textos
        text=MathTex(
            "\\text{Tasa Real =}", "{ (i-r) ", "\\over" ," (1+r) }"
        )
        text.set_color(BLACK)
        
        text_2= Text("La tasa de interés real se define como la ganancia real de intereses descontando\n"
        "el efecto sobre el dinero generado por la inflación. Es decir, es la resta de \n"
        "la tasa de interés menos la tasa de inflación entre uno más la tasa de inflación."
        , color= BLACK, font_size=28, font="Noto Sans", line_spacing=1)

        text_3= Text(" donde i es la tasa de interés y r la tasa de inflación"
        , color= BLACK, font_size=28, font="Noto Sans")
        text_3.shift(2.5*DOWN)

        #Creación de escena
        text_2.shift(2*UP)
        self.play(Write(text_2))
        self.wait(5)

        text.shift(1*DOWN)
        self.play(Write(text[0]))
        self.wait(2)

        self.play(Write(text[1]), Write(text[2]), Write(text[3]))
        self.wait(7)
        self.play(Write(text_3))
        self.wait(9)



###########################################################################################
##############################  Escena 5  #################################################
###########################################################################################

class Escena_5(Scene):
    def construct(self):
        #Textos
        text=MathTex(
            "\\text{Tasa Real =}", "{ (8\%-5\%) ", "\\over" ," (1+5\%) }=","2.8571\%"
        )
        text.set_color(BLACK)
        
        text_2= Text("Si en el año se acumuló una tasa de inflación del 5% y por nuestros productos de \n"
        "inversión obtuvimos un 8% de interés anual, esto quiere decir que nuestra tasa de \n"
        "interés real sobre todo el monto que invertimos es :"
        , color= BLACK, font_size=28, font="Noto Sans", line_spacing=1)

        #Creación de escena
        text_2.shift(2*UP)
        self.play(Write(text_2))
        self.wait(17)

        text.shift(1*DOWN)
        self.play(Write(text[0]), Write(text[1]))
        self.wait(3)

        self.play(Write(text[2]), Write(text[3]))
        self.wait(5)

        self.play(Write(text[4]))
        self.wait(7)

      


