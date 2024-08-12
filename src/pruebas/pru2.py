##--Draw and drop--##
from flet import * 

class pr1(UserControl):
    def __init__(self,page):
        super().__init__(expand=True)      # Clase de herencia que toma las caracteristicas del Frame
    
        file_picker = FilePicker(on_result=on_file_picked)

        self.cnt = Container(
            bgcolor="blue",
            width=200,
            height=500,
            content= Column([
                ElevatedButton("Upload",on_click= lambda _:self.PickerFile.)
            ])
        )

        ## MAIN ##
        self.frameMain = Container(
            content=Column(
                controls=[
                    #self.dropImg
                    #self.btnUp
                    self.cnt
                ]
            )
        )

    

    def prUpload(e:FilePickerResultEvent):
            print(e)
        
    def build(self):
        return self.frameMain
    
def main(page: Page):
    page.add(pr1(page))

app(main)
    

