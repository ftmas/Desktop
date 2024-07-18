import flet as ft

# define a song class as our model
class Song(object):
 def __init__(self, song_name: str, artist_name: str, audio: str, img: str):
        super(Song, self).__init__()
        self.song_name = song_name
        self.artist_name = artist_name
        self.audio = audio
        self.img = img
#define a proeprties for this class to access each attribute
 @property
 def name(self):
    return self.song_name
 @property
 def artist(self):
    return self.artist_name
 @property
 def audio_path(self):
    return self.audio
 @property
 def img_path(self):
    return self.img
# next , define a directory class where we store individual songs
class AudioDirectory(object):
   playlist: list = [
        Song(
            song_name="Street Cafe",
            artist_name="Blonker",
            audio="Blonker - Street Cafe.mp3",
            img="1.jpg",

        ),
        Song(
            song_name="Little Flower",
            artist_name="Fausto Papetti",
            audio="Fausto Papetti - Little Flower.mp3",
            img="2.png",

        ),
        Song(
            song_name="Sur Un Air Du Vivaldi",
            artist_name="Paul Mauriat",
            audio="Paul Mauriat - Sur Un Air Du Vivaldi.mp3",
            img="3.png",

        ),
        Song(
            song_name="Moment",
            artist_name="Kenny G ",
            audio="Kenny G - Moment.mp3",
            img="4.jpg",

        ),
        Song(
            song_name="Pop Corn",
            artist_name="Eric Simon",
            audio="Eric Simon - Pop Corn.mp3",
            img="5.jpg",

        ),
        Song(
            song_name="Hotel California",
            artist_name="Anthony Ventura",
            audio="Anthony Ventura - Hotel California.mp3",
            img="6.jpg",

        ),
        Song(
            song_name="Bi Tabi Instrumental",
            artist_name="Shadmehr Aghili.mp3",
            audio="Bi Tabi Instrumental Shadmehr Aghili.mp3",
            img="7.jpg",

        ),
        Song(
            song_name="Unknown",
            artist_name="Earth",
            audio="Earth.mp3",
            img="8.jpg",

        ),
        Song(
            song_name="Emmanuel",
            artist_name="Fausto Papetti",
            audio="Fausto Papetti - Emmanuel.mp3",
            img="9.jpg",

        ),
        Song(
            song_name="(Everything I Do) I do It For You",
            artist_name="Francis Goya",
            audio="Francis Goya - (Everything I Do) I do It For You.mp3",
            img="10.jpg",

        ),
        Song(
            song_name="Gipsy",
            artist_name="Francis Goya",
            audio="Francis Goya - Gipsy.mp3",
            img="11.jpg",

        ),
        Song(
            song_name="Silent Whisper",
            artist_name="Kenny G",
            audio="Kenny G - Silent Whisper.mp3",
            img="12.jpg",

        ),
        Song(
            song_name="Romeo and Juliet",
            artist_name="Nino Rota",
            audio="Nino Rota - Romeo and Juliet.mp3",
            img="13.jpg",

        ),
        Song(
            song_name="La Cumparsita",
            artist_name="Richard Clayderman",
            audio="Richard Clayderman - La Cumparsita.mp3",
            img="14.jpg",

        ),
        Song(
            song_name="Seasons",
            artist_name="Richard Klayderman",
            audio="Richard Klayderman - Seasons.mp3",
            img="15.jpg",

        ),
        Song(
            song_name="Unknown",
            artist_name="Water",
            audio="Water.mp3",
            img="16.jpg",

        ),

    ]

  # our first page/view is the playlist
# our first page/view is the playlist
class Playlist(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super(Playlist, self).__init__(
            route="/playlist",
            horizontal_alignment="center"  # type: ignore
        )

        self.page = page
        self.playlist : list[Song] = AudioDirectory.playlist

        self.controls = [  # type: ignore
            ft.Row(
                [
                    ft.Text("PLAYLIST", size=40, weight="bold"),  # type: ignore
                ], 
                alignment="center"  # type: ignore
            ),
            ft.Divider(height=10, color="purple"),
        ]

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


def create_song_row(self, song_name , artist_name, song:Song):
    return ft.Container(
        content= ft.Row(
            [
                ft.Text(f"Title:{song.name}"),
                ft.Text(artist_name),
            ],
            alignment= "spaceBetween" # type: ignore     
    ),
    data= song, # song = the song model, i.e. Song class
    padding=10,
    on_click=self.toggle_song
    )
def toggle_song(self, e):
    
    # to pass data between views , we store them in the page.session
    # recall that the data of the control is the song model
    # with all the song details and audio path
    self.page.session.set("song", e.control.data)
    self.page.go("/song")
    
# before setting up the button that shows thr current song , define a current song class
class CurrentSong(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super(CurrentSong, self).__init__(
            route="/song",
            padding=20,
            horizontal_alignment="center",  # type: ignore
            vertical_alignment="center"  # type: ignore
        )
        self.page = page
        # we can access the session data like this ...
        self.song = self.page.session.get("song")

        # next, we define some vars for the current song
        self.duration: int = 0
        self.start : int = 0
        self.end: int = 0
        self.is_playing: bool = False

        #next, define some UI variables
        self.text_start = ft.Text(self.format_time(self.start)) # type: ignore
        self.text_end = ft.Text(self.format_time(self.start)) # type: ignore
        self.slider = ft.Slider(min=0, thumb_color="transparent",on_change_end=None)
        
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route):
        page.views.clear()

        if page.route == "/playlist":
           page.views.append(Playlist(page))
        if page.route == "/song":
           song = CurrentSong(page)
           page.views.append(song)
        page.update()

    page.on_route_change = router
    page.go("/playlist")
ft.app(target=main , assets_dir="assets")