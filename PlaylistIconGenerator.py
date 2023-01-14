import os
import seaborn as sb

from PlaylistIcon import PlaylistIcon
from Types import Size

Color = (int, int, int)

HEADLINE_FONT = 'Fonts\\Circular\\circularstd-medium.otf'
HEADLINE_FONT_TO_SIZE_RATIO = 13/36
SUBTEXT_FONT = 'Fonts\\Circular\\circularstd-book.otf'
SUBTEXT_FONT_TO_SIZE_RATIO = 1/9
TEXT_COLOR = (42, 42, 42)

HEADLINE_TEXTS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']


class PlaylistIconGenerator:

    def __init__(self, name: str, base_color: Color, subtext_text: str, icon_size: Size=Size(300, 300), data_type: str='png'):
        self.name = name
        self.base_color = base_color
        self.icon_size = icon_size
        self.data_type = data_type
        self.subtext_text = subtext_text

        self.create_directory()
        self.headline_texts = HEADLINE_TEXTS
        # self.headline_texts = ['05', '06', '07', '08', '09', '10', '11', '12']
        self.image_count = len(self.headline_texts)

        self.color_list = self.generate_rgb_color_palette()
        self.image_list = self.generate_image_list()

    def create_directory(self):
        directory_exists = os.path.exists(self.name)
        if not directory_exists:
            os.makedirs(self.name)

    def generate_image_list(self):
        if len(self.headline_texts) != len(self.color_list):
            raise Exception('Number of headlines "%(num_headlines)s" does not match number of colors "%(num_colors)s".', num_headlines=len(self.headline_texts), num_colors=len(self.color_list))

        image_list = []
        for idx, headline in enumerate(self.headline_texts):
            print(headline, idx)

            icon_params = {
                'filename': self.name + '\\' + self.subtext_text,
                'color' : self.color_list[idx],
                'month_number_text': headline,
                'subtext': self.subtext_text,
                'font_name_headline': HEADLINE_FONT,
                'font_name_subtext': SUBTEXT_FONT,
                'font_size_headline': int(self.icon_size.height*HEADLINE_FONT_TO_SIZE_RATIO),
                'font_size_subtext': int(self.icon_size.height*SUBTEXT_FONT_TO_SIZE_RATIO),
                'text_color': TEXT_COLOR,
                'text_location': 'center',
                'icon_size': self.icon_size,
                'data_type': self.data_type
            }
            if headline == 'Top-Songs':
                # icon_params['month_number_text'] = 'Top-Songs'
                icon_params['font_size_headline'] = 54
            image_list.append(PlaylistIcon(**icon_params))
        return image_list

    def rgb2hex(self, rgb):
        """Returns the hex string in the form '#ababab' of a color given as rgb in the form (10,20,30).
        Possible ``rgb`` values include:
            - 3 tupel (red, green, blue) each value valid from 0-255
        Calling this function with ``rgb=None`` will return '#ffffff'.
        Parameters
        ----------
        rgb : 3-tupel
            Each entry in the tupel has to be Integer from 0-255.
        Returns
        -------
        string representing the given color in HEX in the form '#ababab'.
        """
        return '#%02x%02x%02x' % rgb

    def generate_rgb_color_palette(self):

        palette = sb.color_palette('light:' + self.rgb2hex(self.base_color), n_colors=self.image_count)

        return [(int(col[0] * 256), int(col[1] * 256), int(col[2] * 256)) for col in palette]
