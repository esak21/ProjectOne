from dataclasses import dataclass
from typing import Self
class HTMLBuilder:
    def __init__(self ):
        self.title = ""
        self.body = []

    def add_title(self, title:str) -> Self:
        self.title = title
        return self

    def add_heading(self, heading:str) -> Self:
        self.body.append(f"<h1>{heading}</h1>")
        return self

    def add_paragraph(self, paragraph:str) -> Self:
        self.body.append(f"<p>{paragraph}</p>")
        return self

    def build(self):
        return HTMLPage(self.title, "\n".join(self.body))



@dataclass(frozen=True)
class HTMLPage:
    title: str
    body: str


    def render_html (self):
        return f"""<!DOCTYPE html>
                    <html>
                    <head>
                        <title>{self.title}</title>
                    </head>
                        <body>{self.body}</body>
                    </html>
                """