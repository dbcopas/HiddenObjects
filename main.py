from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

class HiddenObjectGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.scatter = Scatter(do_rotation=False, scale_min=1)
        self.image = Image(source="path_to_large_image.jpg")
        
        self.scatter.add_widget(self.image)
        self.add_widget(self.scatter)
        self.hidden_objects = [
            {"position": (100, 200), "size": (50, 50)},  # Example coordinates and size
            {"position": (500, 600), "size": (40, 60)}
        ]


    def on_touch_down(self, touch):
        # Convert touch location to Scatter's local coordinates
        local_touch = self.scatter.to_local(*touch.pos)

        # Convert local_touch from Scatter's coordinates to the image's current scale and position
        img_x = (local_touch[0] - self.image.x) / self.scatter.scale
        img_y = (local_touch[1] - self.image.y) / self.scatter.scale
        
        for obj in self.hidden_objects:
            x, y = obj["position"]
            w, h = obj["size"]
            
            if x < img_x < x + w and y < img_y < y + h:
                print("Hidden object found!")
                self.hidden_objects.remove(obj)
                break
        
        return super().on_touch_down(touch)

class HiddenObjectApp(App):
    def build(self):
        return HiddenObjectGame()
    
    
if __name__ == "__main__":
    HiddenObjectApp.run()