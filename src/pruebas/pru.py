from flet import *
 
 
def main(page:Page):
	# REMOVE SPACING IN PAGE 
	page.padding = 0
	page.spacing = 0
 
	def shownav(e):
		# THIS SCRIPT IS SHOW YOU SIDEMENU 
		# WHEN BUTTON IS CLICK
		sidemenu.offset=transform.Offset(0,0)
		page.update()
 
	def hidenav(e):
		# THIS SCRIPT IS HIDE AGAIN IF
		# BUTTON IS CLICK THEN SLIDE LEFT 
		# THE SIDE MENU OK
		sidemenu.offset=transform.Offset(-5,0)
		page.update()
 
	# CREATE SIDE MENU
 
	sidemenu = Container(
		content=Text("hello"),
		padding=10,
		bgcolor="yellow",
		# CREATE SIZE WIDTH AND HEIGHT SIDEMENU
		width=page.window_width/4,
		# AND HEIGHT IS FULL HEIGHT 
		height=page.window_height,
 
		# AND HIDE THE SIDE MENU OFFSET
		offset= transform.Offset(-5,0),
		animate_offset=animation.Animation(500)
		# 500 IS DURATION SIDEMENU WHEN OPEN
 
		)
 
	# CREATE LAYER
	layer = Container(
		width=page.window_width,
		height=page.window_height,
		on_click=lambda e: hidenav(e),
		content=Column([
			Container(
			bgcolor="blue",
			content=Row([
			IconButton(
			icon="menu",
			icon_color="white",
			on_click=shownav),
 
			# TITLE APPBAR
			Text("my Pets",size=30,
				color="White")
 
				])
 
				)
 
			])
		)
 
 
 
	page.add(
		Stack([
			layer,
			sidemenu 
			])
		)
 
app(target=main)