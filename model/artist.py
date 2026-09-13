from dataclasses import dataclass, field


@dataclass
class Artist:
    ArtistId: int
    Name: str

    # CONTIENE GLI ID DEI BRANI DELL'ARTISTA

    # CREO UNA LISTA VUOTA DI TUTTI I BRANI (TRACKID) DELL'ARTISTA
    Tracks: list = field(default_factory=list)

    #INSIEME DELLE PLAYLIST IN CUI COMPARE L'ARTISTA
    #SE LA STESSA PLAYLIST CONTIENE PIÙ BRANI DELLO STESSO ARTISTA, LA PLAYLIST DEVE COMPARIRE UNA SOLA VOLTA.
    #PER QUESTO USIAMO SET, PER ELIMINARE I DUPLICATI
    Playlists: set = field(default_factory=set)

    # SERVE PER POTER USARE UN ARTIST COME NODO DEL GRAFO
    # L'HASH VIENE CALCOLATO USANDO L'ID DELL'ARTISTA
    def __hash__(self):
        return hash(self.ArtistId)

    # DUE ARTISTI SONO CONSIDERATI UGUALI SE HANNO LO STESSO ARTISTID
    def __eq__(self, other):
        return self.ArtistId == other.ArtistId

    # QUANDO STAMPIAMO UN ARTIST, VOGLIAMO VISUALIZZARE IL SUO NOME
    def __str__(self):
        return f"{self.Name}"