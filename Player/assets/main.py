import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))


ft.app(main)


def generate_playlist_ui(self):
    for song in self.playlists:
        self.controls.append(
        self.create_song_row(
            # you can also use the properties defined in the Song class here...
            song_name=song.song_name,
            artist_name=song.artist,
            song=song,
        )
        )
