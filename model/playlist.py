from dataclasses import dataclass

@dataclass
class Playlist:
    PlaylistId: int
    Name: str

    def __eq__(self, other):
        return self.PlaylistId == other.PlaylistId
    #PER RAPPRESENTARLO SOLO COME STRINGA NOME DEL BRANO
    def __str__(self):
        return f"{self.Name}"