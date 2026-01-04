from PlaylistIconGenerator import PlaylistIconGenerator
from PlaylistIcon import PlaylistIcon
from Types import Size
from constants import SOUNDCLOUD_ICON_SIZE

test_playlist_icon_args = {
    'filename': 'test_playlist_icon',
    'color': (187, 42, 42),
    'subtext': '2021',
    'font_name_headline' : 'Fonts\\Circular\\circularstd-medium.otf',
    'font_name_subtext' : 'Fonts\\Circular\\circularstd-book.otf',
    'font_size_headline': 52,
    'font_size_subtext': 16,
    'text_location': 'center',
    'text_color': (42, 42, 42),
    'icon_size': Size(144, 144),
    'data_type': 'png',
    'month_number_text': '12',
}

BASE_COLOR_2021 = (255, 105, 235)
BASE_COLOR_2022 = (80, 125, 200)
BASE_COLOR_2023 = (255, 115, 30)    # Probably wrong
BASE_COLOR_2024 = (255, 115, 30)    # Probably wrong
BASE_COLOR_2025 = (255, 115, 30)    # Probably wrong
BASE_COLOR_2026 = (254, 59, 34)

test_playlist_icon_generator_args = {
    'name': '2026_Spotify',
    'base_color': BASE_COLOR_2026,
    'subtext_text': '2026',
    'icon_size': SOUNDCLOUD_ICON_SIZE,
}

if __name__ == '__main__':
    icon_generator = PlaylistIconGenerator(**test_playlist_icon_generator_args)
    # icon = PlaylistIcon(**test_playlist_icon_args)
    # print(vars(icon))
    # icon.show()
    # icon.save()
