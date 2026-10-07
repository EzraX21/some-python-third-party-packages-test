from textual.app import App,ComposeResult
from textual.widgets import Button ,Static

class CounterApp(App):
    count = 0 
    def compose(self) -> ComposeResult:
        yield Static('0',id="count")
        yield Button("Increment")

    def on_button_pressed(self,event:Button.Pressed) -> None:
        self.count += 1
        self.query_one('#count',Static).update(str(self.count))


CounterApp().run()