from fpdf import FPDF


def main():
    PDF = FPDF()

    name = input("Name: ")

    text = f"{name} took CS50"

    PDF.set_font("Helvetica", style="B", size=16)
    text_width = PDF.get_string_width(text)
    img_width = 100
    xPosition = (PDF.w - img_width) / 2

    PDF.add_page()
    PDF.set_text_color(0, 0, 0)

    PDF.cell(0, 10, "CS50 Shirtificate", align="C")
    PDF.image("shirtificate.png", x=xPosition, y=50, w=img_width)
    PDF.set_text_color(255, 255, 255)

    x = (PDF.w - text_width) / 2
    PDF.text(x, 85, text)
    PDF.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
