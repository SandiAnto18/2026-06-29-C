import networkx as nx

from database.DAO import DAO



class Model:
    def __init__(self):
        self._graph = nx.Graph()

  # Esiste	un	arco	tra	due	artisti	distinti	A1	e	A2
# se	esiste	almeno	una	playlist	che	contiene	almeno	un	brano	di	A1	e	almeno	un	brano	di	A2.	Il	peso
# dell'arco	è	pari	al	numero	di	playlist	distinte	in	comune	tra	i	due	artisti.

    def buildGraph(self):
        artists=DAO.getAllArtists()
        for artist in artists:
            DAO.getTracksforArtist(artist)
        self._graph.add_nodes_from(artists)

        for i, artist1 in enumerate(artists):  # scorre la lista albums e restituisce la posizione i e il suo ogg.album
            # album1 [i=0 a1,i=1 a2, i=2 a3]
            # il 2do for prende solo gli album successivi alla posizone i e crea gli archi tra le coppie, senza duplicati
            for artist2 in artists[i + 1:]:  # album2 scorre gli album che vengono dopo quell'indice
                # così non paragoni un album con se stesso e non ripeti coppie al contrario.
                if self._sharePlaylist(artist1, artist2):  # se _shareGenre diche che condividono un genere
                    self._graph.add_edge(artist1, artist2)  # al


    def _sharePlaylist(self,artist1,artist2):
        if artist1.Tracks is None or artist2.Tracks is None: #insieme di brani non vuota
            return False
    #verifico se hanno una playlist incomune
        playlist1=set(playlist.PlaylistId for playlist in artist1.Playlist if playlist.PlaylistId is not None )
        playlist2=set(playlist.PlaylistId for playlist in artist2.Playlist if playlist.PlaylistId is not None )
   #verifico intersezione tra le playlist
        return len(playlist1.intersection(playlist2)) > 0










    def getNodes(self):
        return len(self._graph.nodes())

    def getEdges(self):
        return len(self._graph.edges())


