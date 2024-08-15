from flet import *
from src.app.filExcel.filtroExcel import filter
from src.views.VentanaCreate.Verificaciones import verificaciones
from src.views.VentanaCreate.createFicha.createPdf import CreatePdf
#from src.views.VentanaCreate.createFicha.createPdf import CreatePdf

#Notas : para el usuario se puede agregar cerrar su seción, ver su historial de modificaciónes etc..
# python -m venv venv
#pip install -r requirements.txt

# Librerias de Prueba con los inputs 
from src.views.VentanaCreate.InptsForm.Inpts_FichaTecVentas import Inpts_FichaTec_Ventas
from src.views.VentanaCreate.InptsForm.Inpts_Extrc import InptsExtrc
from src.views.VentanaCreate.InptsForm.Inpts_ImprDig import Inpst_ImprDig
from src.views.VentanaCreate.InptsForm.Inpts_Lam import Inpts_Lam
from src.views.VentanaCreate.InptsForm.Inpts_Refil import Inpts_Refil
from src.views.VentanaCreate.InptsForm.Inpts_Convrs import Inpts_Convrs
from src.views.VentanaCreate.Verificaciones import verificaciones      # <---- DESCOMENTAR ESTO
from src.Controllers.appInserts import appInserts
from src.views.VentanaCreate.Mdls import opnMdlImg

class createPrind(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame

        self.color_teal = "teal"
        self.page = page

        self.Inpts = Inpts_FichaTec_Ventas(page)    # Inputs FichaTecnica
        self.InptsExtrc = InptsExtrc(page)          # Inputs Extrusión
        self.InptsImpDig = Inpst_ImprDig(page)      # Inputs Impresión Digital
        self.InptsLam = Inpts_Lam(page)
        self.InptsRefl = Inpts_Refil(page)
        self.InptsConvrs = Inpts_Convrs(page)      # <--- DESCOMENTAR ESTO!!!!!!!!!

        #---Pruebas para el prindcard ---#
        self.prntCrd = CreatePdf()
        # Verifica cada una de las entradas
        self.vrf = verificaciones(page)            #<---- DESCOMENTAR ESTO!!!!!!!!!
        # Qry's de la Base de datos
        self.appInsert = appInserts(page)
        # Modal de Imagenes
        self.mdlImg = opnMdlImg(page)

        # BOTON AGREGAR
        self.btn = FilledButton(
            text="ADD",
            adaptive=True,
            style=ButtonStyle(
                bgcolor="#21A742",
                color={
                    ControlState.HOVERED: colors.RED,
                    ControlState.HOVERED: colors.BLACK,
                },
                overlay_color=colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=200,
                shape={
                    ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                    ControlState.DEFAULT: RoundedRectangleBorder(radius=3),
                },
            ),
            #on_click= lambda e: self.Inpts.clean_fields(e), 
            on_click= self.eventInsert
        )

        # PESTAÑAS
        self.Pestañas = Tabs(
            label_color="#45484b",
            indicator_color="#acdbdf",
            indicator_border_radius=30,
            divider_color="#fc4795",
            on_change=self.navTabs,
            tab_alignment=TabAlignment.CENTER,

            tabs=[ Tab( text="FICHA / VENTAS" ),
                Tab( text="EXTRUSIÓN" ),
                Tab( text="IMPRESIÓN DIGITAL" ),
                Tab( text="LAMINADO" ),
                Tab( text="REFILADO" ),
                Tab( text="CONVERSION" ),
                Tab( text="IMG" ),
            ]
        )

        # SUBMENU LAMINASIÓN
        self.subMenuLam = Container(   # Contenedor SUBMENU
            #expand=True,
            bgcolor="yellow",
            padding=3,
            content= 
                Row([           # --- SUBMENU PARA SECCIÓNAR LAS LAMINACIÓNES --- #
                    FilledButton(
                        expand=True,
                        height=20,
                        text = "Texto 1",
                        style = ButtonStyle(
                            #bgcolor="#616F67",
                            shape={
                            #ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                            ControlState.DEFAULT: RoundedRectangleBorder(radius=2)
                            },
                        ),
                        on_click= self.navLam
                    ),
                    FilledButton(
                        expand=True,
                        #border_radius=0,
                        height=20,
                        text = "Texto 2",
                        style = ButtonStyle(
                            #bgcolor="#616F67",
                            shape={
                            #ControlState.HOVERED: RoundedRectangleBorder(radius=15),
                            ControlState.DEFAULT: RoundedRectangleBorder(radius=2)
                            },
                        ),
                        on_click= self.navLam
                    )        
                ])
        )

        # CONTENEDOR PARA EL ENCABEZADO LAMINACIÓN
        self.headerLam = Container(           
            bgcolor=self.color_teal,
            padding=0,
            content = 
                Column([
                    #expand=True,
                    Container(
                        Text("LAMINACIÓN",color="white"),
                        alignment=alignment.center,
                        bgcolor="white",
                        margin=margin.only(bottom=4),
                    ),
                    self.subMenuLam
                ]),
        )

        # HEADER 
        self.cntHeader = Container(
            #expand=True,
            bgcolor="white",
            padding=0,
            #height=80,
            #padding=5,
            content= Column(
                controls=[
                    Container(      #-- CONTENEDOR INICIO Y USUARIO --
                        #expand=True,
                        #height=100,
                        bgcolor="white",
                        border=border.only(bottom=border.BorderSide(1, "#858585")),
                        #margin=margin.only(bottom=3,left=0,right=0,top=0),
                        alignment=alignment.center,
                        content= Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    TextButton("INICIO",
                                               icon=icons.HOME,
                                               on_click=  lambda _: self.page.go('/')),
                                    #bgcolor="RED",
                                ), 
                                Container(
                                    IconButton(icon=icons.ACCOUNT_CIRCLE,
                                               icon_color="violet",
                                               on_click=  lambda _: self.page.go('/')), #Agregar el registro de usuarios
                                    #bgcolor="RED",
                                ),             
                            ]
                        )
                    ),
                    Container(      # -- CONTENEDOR MENU PRINCIPAL --
                        #height=100,
                        bgcolor="e5e5e5cd",
                        border=border.only(bottom=border.BorderSide(1, "#858585")),
                        margin=margin.only(bottom=3,left=0,right=0,top=0),
                        shadow=BoxShadow(
                            spread_radius=5,   # No se expande hacia dentro ni hacia afuera
                            blur_radius=5,    # Incrementa el desenfoque para suavizar la sombra
                            offset=Offset(1, 4),  # Desplaza la sombra más hacia abajo
                            color=colors.BLACK26 
                        ),
                        content= Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                self.Pestañas # Añadir las pestañas
                            ]
                        )
                    )
                ]
            )
        )

#################### FORMULARIOS ########################################
        # FICHA / VENTAS
        self.vtnFicha_Ventas = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content=
            Column([
                Container(
                    bgcolor=self.color_teal,
                    content=
                        Row([       # --- ENCABEZADOS DE LAS TABLAS --- #
                            Container(    # Tamaño Ficha Tecnica
                                Text("FICHA TECNICA",color="white"),
                                expand=True,
                                alignment=alignment.center,
                                bgcolor="#858585",
                            ),
                            Container(    # Tamaño Ficha Tecnica
                                Text("VENTAS",color="white"),
                                expand=True,
                                alignment=alignment.center,
                                bgcolor="#858585",
                            ),
                        ])
                ),
                Row(                    # --- TABLAS FICHA / VENTAS ---
                    expand=True,
                    controls=[
                        Container(                  # -- Seccion 1 Ficha Tecnica--
                            expand=True,
                            bgcolor="#858585", 
                            margin=0,
                            padding=15,
                            alignment=alignment.center,
                            content= Column(
                                expand=True,
                                scroll="auto",
                                controls=[
                                    Container(      # FORMULARIO
                                        alignment=alignment.center,
                                        content=Column(
                                            controls=[
                                                Text("Codigo del Producto"),
                                                self.Inpts.id_product,

                                                Text("Cliente"),
                                                self.Inpts.cliente,

                                                Text("Fecha de Elavoración"),
                                                self.Inpts.fecha_Elav,

                                                Text("Fecha de Revición"),
                                                self.Inpts.fecha_Rev,

                                                Text("Nombre del Producto"),
                                                self.Inpts.producto,
                                            ]
                                        ),  
                                    )
                                ]
                            )
                        ),
                        Container(                  # -- Seccion 2 VENTAS --     
                            expand=True,
                            bgcolor="#858585", 
                            margin=0,
                            padding=15,
                            alignment=alignment.center,
                            content= Column(    # Formulario
                                expand=True,
                                scroll="auto",
                                controls=[
                                    Container(
                                        content=Column(
                                                scroll="auto",
                                                controls=[
                                                    Text("Asesor Comercial de la Cuenta"),
                                                    self.Inpts.AsesorCmrcl,

                                                    Text("Tipo de Empaque"),
                                                    self.Inpts.TipEmpq,

                                                    Text("Producto Laminado"),
                                                    self.Inpts.prdcLam,

                                                    Text("Estructura del Producto"),
                                                    self.Inpts.EstrcPrdct,

                                                    Text("Producto que se empaca"),
                                                    self.Inpts.PrdctEmpq
                                                ]
                                            ),
                                        )
                                    ]
                                )
                            )
                        ])
                    ])       
        )
    
        # EXTRUSIÓN
        self.vtnExtr = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content=
            Column([
                Container(   
                    #expand=True,
                    Text("EXTRUSIÓN",color="white"),
                    alignment=alignment.center,
                    bgcolor="#858585",
                ),
                Row(                    # --- Contenedor EXTRUSIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            Text("Tipo de Material a Extruir"),
                                            self.InptsExtrc.tipMtrlExtr,

                                            Text("Dinaje Requerido"),
                                            self.InptsExtrc.dinajeReq,

                                            Text("Formula Extrusión"),
                                            self.InptsExtrc.frmlExtr,

                                            Text("Pigmento de Pelicula"),
                                            self.InptsExtrc.pigmPelc,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                shadow=BoxShadow(
                                                    spread_radius=1,
                                                    blur_radius=15,
                                                    color=colors.AMBER_400,
                                                    offset=Offset(0, 0),
                                                    blur_style=ShadowBlurStyle.OUTER,
                                                ),
                                                content= self.InptsExtrc.calPel_Tol
                                            ),
                                            
                                            Text("Tipo de Bobina"),
                                            self.InptsExtrc.tipBob,

                                            Text("Tipó de Tratado"),
                                            self.InptsExtrc.tipTratado,
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --     
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        #alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    #alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                shadow=BoxShadow(
                                                    spread_radius=1,
                                                    blur_radius=15,
                                                    color=colors.AMBER_400,
                                                    offset=Offset(0, 0),
                                                    blur_style=ShadowBlurStyle.OUTER,
                                                ),
                                                content= self.InptsExtrc.anchBob_Tol
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.anchCore_Tol
                                            ),

                                            Text("Maximo de Empalmes por Bobina"),
                                            self.InptsExtrc.maxEmplBob,

                                            Text("Orientación de Bobina en Tarima"),
                                            self.InptsExtrc.orntBobTam,

                                            Text("Tipó de Empaque para Bonina"),
                                            self.InptsExtrc.tipEmpqBob,

                                            Text("Pesar producto Por"),
                                            self.InptsExtrc.psrPrdct,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.psPromBob
                                            ),
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 3 --   
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.DimBob_Tol
                                            ),

                                            Text("Etiquetado"),
                                            self.InptsExtrc.etiquetado,

                                            #DropBox de Inputs
                                            Container(
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.numBobCma_CmaTrm
                                            ),

                                            Text("Numero de Bobinas en Tarima"),
                                            self.InptsExtrc.numBobTam,
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsExtrc.psNtPromTam
                                            ),

                                            Text("La tarima llevara emplaye"),
                                            self.InptsExtrc.tamEmplaye,

                                            Text("La tarima sera refilada"),
                                            self.InptsExtrc.tamRefila,

                                            ElevatedButton(         # Agregar Images y Observaciónes
                                                text="IMAGENES",
                                                on_click= lambda _: self.mdlImg.open('EXTRC')
                                                #on_click= self.InptsExtrc.open()
                                            )
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    )
                ])
            ])       
        )
    
        # IMPRECIÓN DIGITAL
        self.vtnImprDigtl = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            alignment=alignment.center,
            content=
            Column([
                Container(    # Tamaño Ficha Tecnica
                    #expand=True,
                    Text("IMPRESIÓN DIGITAL",color="white"),
                    alignment=alignment.center,
                    bgcolor="#858585",
                ),
                Row(                    # --- Contenedor EXTRUSIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        #alignment=MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            Text("Material a Imprimir"),
                                            self.InptsImpDig.mtrlImpr,

                                            Text("Dinaje Requerido"),
                                            self.InptsImpDig.dnjReq,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.calMtrlImpr_Tol,
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.anchBobImpr_Tol,
                                            ),

                                            Text("Grosor de Core"),
                                            self.InptsImpDig.grosorCore,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.anchCore_Tol,
                                            ),

                                            Text("Desarrollo a Imprimir"),
                                            self.InptsImpDig.grosorCore,

                                            Text("Repeticiónes al eje"),
                                            self.InptsImpDig.repEje,

                                            Text("Repeticiónes al Desarrollo"),
                                            self.InptsImpDig.repDesr,
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --     
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        #alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    #alignment=alignment.center,
                                    content=Column(
                                        controls=[

                                            Text("Cantidad de Tintas a Imprimir"),
                                            self.InptsImpDig.cntTintasImpr,

                                            Text("Tipo de Impresión"),
                                            self.InptsImpDig.tipImpr,

                                            Text("Tipo de Tintas a Utilizar"),
                                            self.InptsImpDig.tipTintUtlzr,

                                            Text("Tipo de Barniz sobre la Impresión"),
                                            self.InptsImpDig.tipBrnzImpr,

                                            Text("Figura de Embobinado al Salir"),
                                            self.InptsImpDig.figEmbImpr,

                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.vldClr,
                                            ),

                                            Text("Maximo de Empalmes por Bobina"),
                                            self.InptsImpDig.maxEmplmBob,

                                            Text("Tipo de Empaque para Bobina"),
                                            self.InptsImpDig.tipEmpqBob,

                                            Text("Orientación de Bobina en Tarima"),
                                            self.InptsImpDig.orntBobTam,

                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 3 --   
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[

                                            Text("Pesar Producto por:"),
                                            self.InptsImpDig.psrPrdct,

                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.dimtrBob_Tol,
                                            ),

                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.psPromBob,
                                            ),

                                            Text("Etiquetado"),
                                            self.InptsImpDig.etiquetado,

                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.numBobCam_CamTam,
                                            ),

                                            Text("Numero de Bobinas en Tarima"),
                                            self.InptsImpDig.numBobTam,
                                            
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.psNtPromTam,
                                            ),

                                            Text("La Tarima llevara Empalye"),
                                            self.InptsImpDig.tamEmply,

                                            Text("La Tarima llevara Empalye"),
                                            self.InptsImpDig.tamEmply,
                                        
                                            ElevatedButton(         # Agregar Images y Observaciónes
                                                text="IMAGENES",
                                                on_click= lambda _: self.mdlImg.open('IMPRC')
                                                #on_click= self.InptsExtrc.open()
                                            )
                                        ]
                                    ),  
                                ) 
                            ]
                        )
                    )
                ])
            ])       
        )

        # LAMINACIÓN GENERAL VTN 1
        self.vtnLamGnrl = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content=
            Column([
                self.headerLam,         # Encabezado de Laminasión
                Row(                    # --- Contenedor LAMINASIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            Text("Estructura del Producto"),
                                            self.InptsLam.estrcPrdct,

                                            Text("Material Impreso"),
                                            self.InptsLam.mtlImpr,

                                             #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                margin=5,
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsLam.clPlc_Tol,
                                            ),

                                             #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                margin=5,
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsLam.anchBob_Tol,
                                            ),

                                            Text("Tipo de tratado"),
                                            self.InptsLam.tipTratado,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                margin=5,
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsLam.medMngTransf,
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                margin=5,
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsLam.anchCore_Tol,
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                margin=5,
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsLam.dmtrGrsrCore,
                                            ),
                                        ]
                                    ),
                                )    
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --     
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                margin=5,
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsLam.dmtrBob_Tol,
                                            ),

                                            Text("Maximo de Empalmes por Bobina"),
                                            self.InptsLam.mxmEmplBob,

                                            Text("Orientación de Bobina en Rack"),
                                            self.InptsLam.orntBobRck,
                                        
                                            Text("Tipo de Empaque para Bobina"),
                                            self.InptsLam.tipEmpqBob,
                                            
                                            Text("Etiquetado"),
                                            self.InptsLam.etiquetado,

                                            Text("Pesar Producto Por : "),
                                            self.InptsLam.psNtPromBob,

                                            Text("Peso Neto Promedio de Bobina"),
                                            self.InptsLam.psNtPromBob,
                                        
                                            ElevatedButton(         # Agregar Images y Observaciónes
                                                text="IMAGENES",
                                                on_click= lambda _: self.mdlImg.open('LMNSN')
                                                #on_click= self.InptsExtrc.open()
                                            )
                                        ]
                                    ),       
                                ) 
                            ]
                        )
                    )
                ])
            ])       
        )

        # LAMINASIÓNES      VTN 2
        self.vtnLaminas = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            content=
            Column([
                self.headerLam,         # Encabezado de Laminasión
                Row(                    # --- Contenedor LAMINASIÓN ---
                    #expand=True,
                    controls=[
                        Container( 
                            expand=True,                 # -- Seccion 1 --
                            bgcolor="#458585", 
                            alignment=alignment.center,
                            content=
                            Column([Text("LAMINACIÓN N.1")])
                        ),
                        Container( 
                            expand=True,                 # -- Seccion 1 --
                            bgcolor="#458585", 
                            alignment=alignment.center,
                            content=
                            Column([Text("LAMINACIÓN N.2")])
                        ),
                        Container( 
                            expand=True,                 # -- Seccion 1 --
                            bgcolor="#458585", 
                            alignment=alignment.center,
                            content=
                            Column([Text("LAMINACIÓN N.3")])
                        ),
                        Container( 
                            expand=True,                 # -- Seccion 1 --
                            bgcolor="#458585", 
                            alignment=alignment.center,
                            content=
                            Column([Text("LAMINACIÓN N.4")])
                        ),
                        #self.ji()
                ]),

                Row(                    # --- Contenedor LAMINASIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="#458585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content=
                         Column(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[

                                            Text("Material para Laminar"),
                                            self.InptsLam.LN1mtrLam,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsLam.LN1clbPel_Tol
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsLam.LN1anchBob_Tol
                                            ),

                                            Text("Tipo de Tratado"),
                                            self.InptsLam.LN1tipTratado,

                                            Text("Tipo de Laminación"),
                                            self.InptsLam.LN1tipLam,
                                        ]
                                    ),
                                )    
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[

                                            Text("Material para Laminar"),
                                            self.InptsLam.LN2mtrLam,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsLam.LN2clbPel_Tol
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsLam.LN2anchBob_Tol
                                            ),

                                            Text("Tipo de Tratado"),
                                            self.InptsLam.LN2tipTratado,

                                            Text("Tipo de Laminación"),
                                            self.InptsLam.LN2tipLam,
                                        ]
                                    ),
                                )    
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 3 --
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[

                                            Text("Material para Laminar"),
                                            self.InptsLam.LN3mtrLam,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsLam.LN3clbPel_Tol
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsLam.LN3anchBob_Tol
                                            ),

                                            Text("Tipo de Tratado"),
                                            self.InptsLam.LN3tipTratado,

                                            Text("Tipo de Laminación"),
                                            self.InptsLam.LN3tipLam,
                                        ]
                                    ),
                                )    
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 4 --
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[

                                            Text("Material para Laminar"),
                                            self.InptsLam.LN4mtrLam,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsLam.LN4clbPel_Tol
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                alignment=alignment.center,
                                                border_radius=5,
                                                padding=5,
                                                content= self.InptsLam.LN4anchBob_Tol
                                            ),

                                            Text("Tipo de Tratado"),
                                            self.InptsLam.LN4tipTratado,

                                            Text("Tipo de Laminación"),
                                            self.InptsLam.LN4tipLam,
                                        ]
                                    ),
                                )    
                            ]
                        )
                    ),
                ])
            ])       
        )

        # REFILADO
        self.vtnRefilado = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            alignment=alignment.center,
            content=
            Column([
                Container(    # Tamaño Ficha Tecnica
                    #expand=True,
                    Text("REFILADO",color="white"),
                    alignment=alignment.center,
                    bgcolor="#858585",
                ),
                Row(                    # --- Contenedor EXTRUSIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        #alignment=MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[

                                            # NOTA : Agregar 7 entradas por cada sección (Son 3 secciónes en total de 21)
                                            Text("Proceso Refilado"),
                                            self.InptsRefl.procRef,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsRefl.anchBobRefDbl,
                                            ),

                                            Text("Acabado de Bobina"),
                                            self.InptsRefl.acabdBob,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsRefl.anchCre_Tol,
                                            ),

                                            Text("Grosor de Core"),
                                            self.InptsRefl.grsrCore,

                                            Text("Figura de Embobinado"),
                                            self.InptsRefl.figEmb,

                                            Text("La bobina se Refilara / Doblara"),
                                            self.InptsRefl.bobRef_Dbl,
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --     
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        #alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    #alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsRefl.mtrBobRefl,
                                            ),
                                            
                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsRefl.dmtrBob_Tol,
                                            ),

                                            Text("Maximo de Empalmes por Bobina"),
                                            self.InptsRefl.mxEmplBob,

                                            Text("Señalización de Empalme"),
                                            self.InptsRefl.sñlEmplm,

                                            Text("Orientación de Bobina en Tarima"),
                                            self.InptsRefl.orntBobTam,

                                            Text("Tipo de Empaque para Bobina"),
                                            self.InptsRefl.tipEmpqBob,

                                            Text("Pesar Producto por : "),
                                            self.InptsRefl.psrPrdct,

                                        ]
                                    ),   
                                )                  
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 3 --   
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                             #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsRefl.psPromBob,
                                            ),

                                            Text("Etiquetado"),
                                            self.InptsRefl.etiquetado,

                                             #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsRefl.numBobCma_CmsTam,
                                            ), 

                                            Text("Numero de Bobinas en Tarima"),
                                            self.InptsRefl.numBobTam,  

                                             #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsRefl.psPromTam,
                                            ),

                                            Text("La tarima llevara Emplaye"),
                                            self.InptsRefl.tamEmplaye,

                                            Text("La Tarima sera Flejada"),
                                            self.InptsRefl.tamflejada, 

                                            ElevatedButton(         # Agregar Images y Observaciónes
                                                text="IMAGENES",
                                                on_click= lambda _: self.mdlImg.open('RFLD')
                                                #on_click= self.InptsExtrc.open()
                                            )
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    )
                ])
            ])       
        )
        
        # CONVERSIÓN
        self.vtnConversión = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            alignment=alignment.center,
            content=
            Column([
                Container(    # Tamaño Ficha Tecnica
                    #expand=True,
                    Text("REFILADO",color="white"),
                    alignment=alignment.center,
                    bgcolor="#858585",
                ),
                Row(                    # --- Contenedor EXTRUSIÓN ---
                    expand=True,
                    controls=[
                    Container(                  # -- Seccion 1 --
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        #alignment=MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsConvrs.medEmpq,
                                            ),

                                            Text("Tipo de Empaque"),
                                            self.InptsConvrs.tipEmpq,

                                            Text("Tipo de Sello"),
                                            self.InptsConvrs.tipSello,

                                            Text("Tipo de Acabado"),
                                            self.InptsConvrs.tipAcbd,

                                            Text("El producto llevara Perforaciónes"),
                                            self.InptsConvrs.prdctPerf,

                                            Text("Cantidad de Perforaciónes"),
                                            self.InptsConvrs.cntPerf,
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 2 --     
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        #alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    #alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            Text("El producto lleva Suaje"),
                                            self.InptsConvrs.prdctSuaje,

                                            Text("Tipo de Suaje"),
                                            self.InptsConvrs.tipSuaje,

                                            Text("Empacado de Producto"),
                                            self.InptsConvrs.empcdPrdct,

                                            Text("Cantidad de Piezas por Paquete"),
                                            self.InptsConvrs.prdctSuaje,

                                            Text("Tipo de Embalaje"),
                                            self.InptsConvrs.tipEmblj,

                                            Text("Medida del Embalaje"),
                                            self.InptsConvrs.mdEmblj,
                                            
                                            Text("Pesar producto por : "),
                                            self.InptsConvrs.psrPrdct,

                                        ]
                                    ),   
                                )                  
                            ]
                        )
                    ),
                    Container(                  # -- Seccion 3 --   
                        expand=True,
                        bgcolor="#858585", 
                        margin=0,
                        padding=15,
                        alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Column(
                                        controls=[
                                            
                                            Text("Peso neto Promedio de :"),
                                            self.InptsConvrs.psProm,

                                            Text("Etiquetado"),
                                            self.InptsConvrs.psrPrdct,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsConvrs.numBltsCjsCam_CmsTam,
                                            ),

                                             #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsConvrs.numBlts_CjsTam,
                                            ),

                                             #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsConvrs.psPromTam,
                                            ),

                                            Text("La tarima llevara Emplaye"),
                                            self.InptsConvrs.tamEmply,

                                            Text("La tarima sera Refilada"),
                                            self.InptsConvrs.tamFlej,
                                        
                                            ElevatedButton(         # Agregar Images y Observaciónes
                                                text="IMAGENES",
                                                on_click= lambda _: self.mdlImg.open('CNVRSN')
                                                
                                            )
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    )
                ])
            ])       
        )

        # IAMGEN DE BOBINA Y OBSERVACIÓNES
        self.vtnImgs = Container(
            expand=True,
            margin=margin.only(top=-5),
            bgcolor=self.color_teal,
            padding=5,
            alignment=alignment.center,
            content=
                Column([
                    Container(    # Tamaño Ficha Tecnica
                    #expand=True,
                    #Text("REFILADO",color="white"),
                    alignment=alignment.center,
                    bgcolor="#858585",
                )
                ])
        )
    
        # Contenedor de Boton Agregar a la BD
        self.cntBtn = Container(
            #expand=True,
            bgcolor=self.color_teal,
            padding=5,
            border_radius=5,
            content= Row(
                alignment=MainAxisAlignment.END,
                controls=[
                    self.btn
                ]
            )
        )

########################################################################

        # Frame Main
        self.frameMain = Container(
            bgcolor="white",
            padding=0,
            content=Column(
                controls=[
                    self.cntHeader,
                    self.vtnFicha_Ventas,       # Contenedor de FICHA / VENTAS como Inicio
                    self.cntBtn,
                ]
            )
        )

#################### PRUEBAS #######################
 
    # Modulo para navergar en el SubMenu de Laminado
    def navLam(self,e):
        id = e.control.text
        dic = {
            "Texto 1" : self.vtnLamGnrl,
            "Texto 2" : self.vtnLaminas
        }

        self.frameMain.content.controls = [self.cntHeader]
        #self.frameMain.content.controls = [self.headerLam]
        self.frameMain.content.controls.append(dic.get(id))
        self.frameMain.content.controls.append(self.cntBtn)
        self.update()
        
    # Modulo para navegar en el Menu Pricipal
    def navTabs(self,e):
        id = e.control.selected_index
        #print(id)
        dic = [
            self.vtnFicha_Ventas,
            self.vtnExtr,
            self.vtnImprDigtl,
            self.vtnLamGnrl,
            self.vtnRefilado,
            self.vtnConversión,
            self.vtnImgs
        ]

        self.frameMain.content.controls = [self.cntHeader]
        self.frameMain.content.controls.append(dic[id])
        self.frameMain.content.controls.append(self.cntBtn)

        self.update()

    # Evento al preciónar el boton crear Ficha
    def eventInsert(self,e):
        #self.prntCrd
        #self.vrf.insrtFicha
        #jer
        #self.prntCrd.jer()
        #self.vrf.insrtFicha()
        #'''
        self.vrf.insrtFicha(
            self.Inpts.tplInptsFichTec(),
            self.Inpts.tplInptsVentas(),
            self.InptsExtrc.tplInptsExtr(),
            self.InptsImpDig.tplInptsImprDig(), # Arreglar el bug, ya que no acepta el ultimo conjunto
            self.InptsLam.tplInptsLam(),
            self.InptsRefl.tplInptsRef(),
            self.InptsConvrs.tplInptsConvrs()
        )
        self.update()#'''

    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.padding = 0
    page.add(createPrind(page))
    #margin=margin.only(top=-5)

#app(main)