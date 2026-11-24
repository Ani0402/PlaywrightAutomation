
class Reusable:
   
    def highlight_element(self, locator, color="red"):
        locator.evaluate(
            f"""(el) => {{
                el.style.border = '3px solid {color}';
                el.style.backgroundColor = 'rgba(255, 255, 0, 0.3)';
            }}"""
        )