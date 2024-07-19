from flet import *
from src.app.filExcel.filtroExcel import filter
from src.views.VentanaCreate.InptFich_Vents import InptsTable

#Notas : para el usuario se puede agregar cerrar su seción, ver su historial de modificaciónes etc..

# Librerias de Prueba con los inputs 
from src.views.VentanaCreate.InptsForm.Inpts_FichaTecVentas import Inpts_FichaTec_Ventas
from src.views.VentanaCreate.InptsForm.Inpts_Extrc import InptsExtrc
from src.views.VentanaCreate.InptsForm.Inpts_ImprDig import Inpst_ImprDig
from src.views.VentanaCreate.InptsForm.Inpts_Lam import Inpts_Lam
from src.views.VentanaCreate.InptsForm.Inpts_Refil import Inpts_Refil



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

        # btn Agregar
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
                    on_click= self.upd
        )

        # Pestañas
        self.Pestañas = Tabs(
            label_color="red",
            indicator_color="Red",
            indicator_border_radius=60,
            divider_color="#fc4795",
            on_change=self.navTabs,
            tab_alignment=TabAlignment.CENTER,

            tabs=[ Tab( text="FICHA / VENTAS" ),
                Tab( text="EXTRUSIÓN" ),
                Tab( text="IMPRESIÓN DIGITAL" ),
                Tab( text="LAMINADO" ),
                Tab( text="REFILADO" ),
                Tab( text="CONVERSION" )
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

        self.headerLam = Container(    # CONTENEDOR PARA EL ENCABEZADO        
            bgcolor=self.color_teal,
            content = 
                Column([
                    #expand=True,
                    Container(
                        Text("LAMINACIÓN",color="white"),
                        alignment=alignment.center,
                        bgcolor="#858585",
                    ),
                    self.subMenuLam
                    ]),
        )

        # Header
        self.cntHeader = Container(
            #expand=True,
            bgcolor=self.color_teal,
            #height=80,
            padding=5,
            content= Column(
                controls=[
                    Container(      #-- Contenedor de Inicio y Usuario --
                        #expand=True,
                        #height=100,
                        bgcolor="green",
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
                    Container(      # Contenedor para las Pestañas
                        #height=100,
                        bgcolor="green",
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
                Container(    # Tamaño Ficha Tecnica
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

                                            Text("Desarrollo a Imprimir"),
                                            self.InptsImpDig.grosorCore,
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
                                        
                                            Text("Orientación de Bobina en Rack"),
                                            self.InptsLam.orntBobRck,
                                        
                                            Text("Tipo de Empaque para Bobina"),
                                            self.InptsLam.tipEmpqBob,
                                            
                                            Text("Etiquetado"),
                                            self.InptsLam.etiquetado,

                                            Text("Pesar Producto Por : "),
                                            self.InptsLam.psNtPromBob,

                                            Text("Peso Neto Promedio de Bobina"),
                                            self.InptsLam.psNtPromBob
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

                                            Text("Orientación de Bobina en Tarima"),
                                            self.InptsLam.LN1orntBobTam,
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

                                            Text("Orientación de Bobina en Tarima"),
                                            self.InptsLam.LN2orntBobTam,
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

                                            Text("Orientación de Bobina en Tarima"),
                                            self.InptsLam.LN3orntBobTam,
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

                                            Text("Orientación de Bobina en Tarima"),
                                            self.InptsLam.LN4orntBobTam,
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

                                            # NOTA : Agregar 7 entradas por cada sección (Son 3 secciónes en total de 21)
                                            Text("Proceso a Realizar "),
                                            self.InptsImpDig.mtrlImpr,

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsRefl.anchBobRefDbl,
                                            ),

                                            #DropBox de Inputs
                                            Container(
                                                #Text("Ingresar !"),
                                                bgcolor="#B6DE3A",
                                                border_radius=5,
                                                alignment=alignment.center,
                                                padding=5,
                                                content= self.InptsImpDig.calMtrlImpr_Tol,
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
                        #alignment=alignment.center,
                        content= Column(
                            expand=True,
                            scroll="auto",
                            controls=[
                                Container(
                                    #alignment=alignment.center,
                                    content=Column(
                                        controls=[
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
                                        ]
                                    ),
                                    
                                )
                                
                            ]
                        )
                    )
                ])
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
            bgcolor="#737373",
            padding=2,
            content=Column(
                controls=[
                    self.cntHeader,
                    self.vtnFicha_Ventas,       # Contenedor de FICHA / VENTAS como Inicio
                    self.cntBtn,
                ]
            )
        )

#################### PRUEBAS #######################
    
    def ji(self):
        pass
        
        #self.id_product.update(
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
            Container(
                bgcolor="blue",
                width=100,
                height=100
            ),
            Container(
                bgcolor="green",
                width=100,
                height=100
            ),
        ]

        self.frameMain.content.controls = [self.cntHeader]
        self.frameMain.content.controls.append(dic[id])
        self.frameMain.content.controls.append(self.cntBtn)

        self.update()

          # Limpiar Labels
    
    def clean_fields(self,e):
        self.Inpts.id_product.value = ""
        self.Inpts.cliente.value = ""
        self.Inpts.producto.value = ""
        self.Inpts.fecha_Elav.value = ""
        self.Inpts.fecha_Rev.value = ""
        self.update()

    def add_fields(self):
        self.Inpts.id_product.value = "Value"
        self.Inpts.cliente.value = "Value"
        self.Inpts.producto.value = "Value"
        self.Inpts.fecha_Elav.value = "Value"
        self.Inpts.fecha_Rev.value = "Value"
        self.update()
    
    def upd(self,e):
        #self.Inpts.pruData()
        self.Inpts.prCero()
        self.update()
  
    def build(self):
        return self.frameMain

def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.add(createPrind(page))
    #margin=margin.only(top=-5)

#app(main)