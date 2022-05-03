from manim import *
config.background_color = YELLOW_A
config["background_color"] = YELLOW_A


###########################################################################################
##############################  Escena 1  #################################################
###########################################################################################

#Esta escena no sera ocupada en este video, sin embargo en proximos si.
class Escena_1(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # Grafica y sus ejes
        ax = Axes(x_range=[0, 13], y_range=[90, 200 , 10])
        graph = ax.plot(lambda x: 100*(1.05)**x, color=RED, x_range=[0, 13])

        #Valores de los ejes

        x_pos = [x for x in range(1, 13)]
        x_vals = ["2011", "2012", "2013", "2014", "2015", "2016", "2017","2018","2019","2020","2021","2022"]
        x_dict = dict(zip(x_pos, x_vals))
        ax.add_coordinates(x_dict, range(90,200,10))


        #Titulos de los ejes
        axxes_labels = ax.get_axis_labels(
            Tex("Años").scale(0.75), Tex("Monto").scale(0.75)
        )
       
        # Punto inicial y final
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color= PURE_BLUE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        #Labels
        label_1 = ax.get_graph_label(graph, "4.11 \% ", x_val=2, direction=DOWN , buff= 0.5, color= WHITE, dot=True)
        label_2 = ax.get_graph_label(graph, "4.02 \% ", x_val=4, direction=DOWN, buff= 0.5,color= WHITE, dot=True)
        label_3 = ax.get_graph_label(graph, "2.82 \% ", x_val=6, direction=DOWN, buff= 0.5,color= WHITE, dot=True)
        label_4 = ax.get_graph_label(graph, "4.90 \% ", x_val=8, direction=DOWN, buff= 0.55,color= WHITE, dot=True)
        label_5 = ax.get_graph_label(graph, "3.64 \% ", x_val=10, direction=DOWN, buff= 0.55,color= WHITE, dot=True)
        label_6 = ax.get_graph_label(graph, "5.35 \% ", x_val=12, direction=DOWN, buff= 0.65,color= WHITE, dot=True)
        labels= VGroup(label_1,label_2,label_3,label_4,label_5,label_6)

        #Imagenes
        shirt = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/billete.png")
        shirt.height=1
        shirt.width=1
        shirt.shift(2.5* DOWN + 6 * LEFT)

        #Creación de Escena

        self.add(ax, graph, dot_1, dot_2, shirt, axxes_labels,labels)
        self.wait(2)
        self.play(self.camera.frame.animate.scale(0.80).move_to(shirt),run_time=2)

     
        def update_curve(mob):
            mob.move_to(shirt.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(shirt, graph, rate_func=linear),run_time=5)
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
        self.wait(2)



###########################################################################################
##############################  Escena 2  #################################################
###########################################################################################

#En esta escena se creara una linea del tiempo, sobre una canasta, en la cual vemos el año y el precio de junio de ese mismo año
#de la canasta basica en México.
class Escena_2(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # Grafica y sus ejes
        ax = Axes(x_range=[0, 32], y_range=[0, 10, 1])
        graph = ax.plot(lambda x: 4.80, color=BLACK, x_range=[0, 32])
       
        # Punto inicial y final
        dot_1 = Dot(ax.i2gp(graph.t_min, graph), color= BLACK)
        dot_2 = Dot(ax.i2gp(graph.t_max, graph), color= BLACK)

        #Labels
        label_1 = ax.get_graph_label(graph, Text("$1006", font_size=24), x_val=1, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_2 = ax.get_graph_label(graph, Text("$1101", font_size=24), x_val=4, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_3 = ax.get_graph_label(graph, Text("$1173", font_size=24), x_val=7, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_4 = ax.get_graph_label(graph, Text("$1225", font_size=24), x_val=10, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_5 = ax.get_graph_label(graph, Text("$1268", font_size=25), x_val=13, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_6 = ax.get_graph_label(graph, Text("$1323", font_size=25), x_val=16, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_7 = ax.get_graph_label(graph, Text("$1422", font_size=25), x_val=19, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_8 = ax.get_graph_label(graph, Text("$1477", font_size=25), x_val=22, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_9 = ax.get_graph_label(graph, Text("$1552", font_size=25), x_val=25, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_10 = ax.get_graph_label(graph, Text("$1640", font_size=25), x_val=28, direction=UP, buff= 0.45,color= BLACK, dot=True)
        label_11 = ax.get_graph_label(graph, Text("$1745", font_size=25), x_val=31, direction=UP, buff= 0.45,color= BLACK, dot=True)

        labels_graph= VGroup(label_1,label_2,label_3,label_4,label_5,label_6,label_7,label_8,label_9,label_10,label_11)

        label_21 = ax.get_graph_label(graph, Text("2011", font_size=28, color= BLACK), x_val=1, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_22 = ax.get_graph_label(graph, Text("2012", font_size=28, color= BLACK), x_val=4, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_23 = ax.get_graph_label(graph, Text("2013", font_size=28, color= BLACK), x_val=7, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_24 = ax.get_graph_label(graph, Text("2014", font_size=28, color= BLACK), x_val=10, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_25 = ax.get_graph_label(graph, Text("2015", font_size=28, color= BLACK), x_val=13, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_26 = ax.get_graph_label(graph, Text("2016", font_size=28, color= BLACK), x_val=16, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_27 = ax.get_graph_label(graph, Text("2017", font_size=28, color= BLACK), x_val=19, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_28 = ax.get_graph_label(graph, Text("2018", font_size=28, color= BLACK), x_val=22, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_29 = ax.get_graph_label(graph, Text("2019", font_size=28, color= BLACK), x_val=25, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_30 = ax.get_graph_label(graph, Text("2020", font_size=28, color= BLACK), x_val=28, direction=DOWN, buff= 0.5,color= BLACK, dot=True)
        label_31 = ax.get_graph_label(graph, Text("2021", font_size=28, color= BLACK), x_val=31, direction=DOWN, buff= 0.5,color= BLACK, dot=True)


        labels_graph_2= VGroup(label_21,label_22,label_23,label_24,label_25,label_26,label_27,label_28,label_29,label_30,label_31)

        text= Text("Para calcular la inflación se usan los precios de la canasta básica,\n puesto que se trata de una generalización de bienes que consumen \n la mayoría de las familias mexicanas.",
                    color= BLACK, font_size=27, font="Noto Sans")
        text.shift(2*UP)

        text1= Text("INPC: Índice Nacional de Precios al Consumidor",
                    color= BLACK, font_size=27, font="Noto Sans")
        text1.shift(2*DOWN)


        #Imagenes
        shirt = ImageMobject("C:/Users/ignam/Desktop/ProyectoManim/canastaf.png")
        shirt.height=1
        shirt.width=1
        shirt.shift(0.10*DOWN + 6 * LEFT)

        #Creación de Escena
        self.add(graph, dot_1, dot_2, shirt, labels_graph, labels_graph_2)
        self.play(Write(text))
        self.wait(9)
        self.play(Write(text1))
        self.wait(3)
        self.play(self.camera.frame.animate.scale(0.90).move_to(shirt),run_time=2)

     
        def update_curve(mob):
            mob.move_to(shirt.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(shirt, graph, rate_func=linear),run_time=5)
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))
        self.wait(5)




###########################################################################################
##############################  Escena 3  #################################################
###########################################################################################

#En esta escena presentaremos la formula que se utiliza para calcular la inflación en México
#INPC= Indice Nacional de Precios al Consumidor

class Escena_3(Scene):
    def construct(self):
        #Textos
        text=MathTex(
            "\\text{Porcentaje de inflación}=", "{INPC_{Actual} - INPC_{Anterior}", "\\over" ,"INPC_{Anterior}}", " * 100"
        )
        text.set_color(BLACK)
        
        text_2= Text("¿Cómo se calcula el porcentaje de inflación \n entre el año anterior y el actual?", color= BLACK)

        #Creación de escena
        text_2.shift(2*UP)
        self.play(Write(text_2))
        self.wait(5)

        text.shift(1*DOWN)
        self.play(Write(text[0]))
        self.wait(3)

        text[1].set_color(PURE_RED)
        self.play(Write(text[1]))
        self.wait(4)

        text[1].set_color(BLACK)
        text[3].set_color(PURE_RED)
        self.add(text[2])
        self.play(Write(text[3]))
        self.play(ReplacementTransform(text[1],text[1]))
        self.wait(1)

        text[3].set_color(BLACK)
        text[4].set_color(PURE_RED)
        self.play(Write(text[4]))
        self.play(ReplacementTransform(text[3],text[3]))
        self.wait(2)

        text[4].set_color(BLACK)
        self.play(ReplacementTransform(text[4],text[4]))
        self.wait(4)



        



