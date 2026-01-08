from htmlBuilder import HTMLPage, HTMLBuilder

def main():
    builder = HTMLBuilder()
    (builder.add_title("Mypage").
     add_heading("Welcome to Builder Pattern").
     add_paragraph("This is a paragraph").
     add_paragraph("This is a paragraph2"))

    page = builder.build()


    print(page.render_html())

    second_builder = HTMLBuilder()
    (second_builder.add_heading("Welcome to Builder Pattern").add_title("secondPage"))
    second_page = second_builder.build()
    print(second_page.render_html())






if __name__ == "__main__":
    main()