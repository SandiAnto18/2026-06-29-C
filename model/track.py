from dataclasses import dataclass

@dataclass
class Track:
    TrackId: int
    Name: str
    AlbumId:int
    MediaTypeId:int
    GenreId:int
    Composer:str
    Milliseconds:int
    Bytes:int
    UnitPrice: float #DECIMAL

    def __hash__(self):
        return hash(self.TrackId)
    #TRACKID ORDINATI DA 1 A ...
    #CONFRONTA 2 TRACKID:SONO UGUALI SE HANNO LO STESSO TRACKID
    #simile a distinct ma qua trattiamo oggetti track con stesso trackid ma info diverse
    #python li considera uguali per trackid non per il resto delle info contenute in ogni oggetto.
    def __eq__(self, other):
        return self.TrackId == other.TrackId
    #PER RAPPRESENTARLO SOLO COME STRINGA NOME DEL BRANO
    def __str__(self):
        return f"{self.Name}"