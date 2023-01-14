import os

from PIL import Image, ImageDraw, ImageFont
from Types import Size

Color = (int, int, int)
HEADLINE_FONT = 'Fonts\\Circular\\circularstd-medium.otf'
SUBTEXT_FONT = 'Fonts\\Circular\\circularstd-book.otf'

class PlaylistIcon:

    def __init__(self, filename: str, color: Color, subtext: str, font_name_headline: str=HEADLINE_FONT, font_name_subtext: str=SUBTEXT_FONT, text_color: Color=(0, 0, 0), font_size_headline: int=48, font_size_subtext: int=24, text_location: str='center', icon_size: Size=Size(144, 144), data_type: str='png', month_number_text: str='01') -> None:
        self.filename = filename
        self.filename_separator = "_"
        self.filename_type_separator = "."
        self.data_type = data_type
        self.background_color = color
        self.icon_size = icon_size

        self.text = subtext
        self.font_name_headline = font_name_headline
        self.font_name_subtext = font_name_subtext
        self.font_size_headline = font_size_headline
        self.font_size_subtext = font_size_subtext
        self.font_headline = ImageFont.truetype(self.font_name_headline, self.font_size_headline)
        self.font_subtext = ImageFont.truetype(self.font_name_subtext, self.font_size_subtext)
        self.text_location = text_location
        self.text_color = text_color
        self.month_number_text = month_number_text

        # self.text_with_month_number = self.month_number_text + str('\n') + self.text

        self.path = self.filename + self.filename_separator + self.month_number_text + self.filename_type_separator + self.data_type
        self.image = Image.new(
            mode="RGB",
            size=self.icon_size.as_tuple(),
            color=self.background_color)
        self.add_text_to_img()
        self.save()

    def save(self):
        print('color:' + str(self.background_color))
        print('saving to ' + self.path)
        try:
            self.image.save(self.path, format=self.data_type)
        except Exception as e:
            raise

    def show(self):
        self.image.show()

    def add_text_to_img(self):
        draw = ImageDraw.Draw(self.image)
        if self.text_location == 'center':
            _, _, headline_w_offset, headline_h_offset = draw.textbbox((0,0), self.month_number_text, self.font_headline)
            _, _, subtext_w_offset, subtext_h_offset = draw.textbbox((0,0), self.text, self.font_subtext)
            # print(w_offset, h_offset)
            headline_coords = (int((self.icon_size.width - headline_w_offset)/2), int((self.icon_size.height - headline_h_offset)* (0.4)))
            subtext_coords = (int((self.icon_size.width - subtext_w_offset)/2), int((self.icon_size.height - subtext_h_offset)* 0.75))

            # headline_coords = (center_coords[0], int(center_coords[1]/2))
            # subtext_coord = (center_coords[0], int(center_coords[1]*2))
            # print('center coord:', center_coords)
            # print('headline coord:', headline_coords)
            # print('subtext_coord:', subtext_coords)

        draw.text(headline_coords, self.month_number_text, self.text_color, font=self.font_headline, align='center')
        draw.text(subtext_coords, self.text, self.text_color, font=self.font_subtext, align='center')
        # draw.text(center_coords, self.text_with_month_number, self.text_color, font=self.font, align='center', spacing=10)
