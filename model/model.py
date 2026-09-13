import networkx as nx

from database.DAO import DAO



class Model:
    def __init__(self):
        self._graph = nx.Graph()

  # Esiste	un	arco	tra	due	artisti	distinti	A1	e	A2
# se	esiste	almeno	una	playlist	che	contiene	almeno	un	brano	di	A1	e	almeno	un	brano	di	A2.	Il	peso
# dell'arco	è	pari	al	numero	di	playlist	distinte	in	comune	tra	i	due	artisti.

    def buildGraph(self):
        # RECUPERO TUTTI GLI ARTISTI CHE HANNO ALMENO UN BRANO
        artists = DAO.getAllArtists()

        # AGGIUNGO GLI ARTISTI COME VERTICI DEL GRAFO
        self._graph.add_nodes_from(artists)

        # CONFRONTO OGNI ARTISTA CON GLI ARTISTI SUCCESSIVI
        for i, artist1 in enumerate(artists):
            for artist2 in artists[i + 1:]:

                # RECUPERO LE PLAYLIST DELL'ARTISTA 1
                playlist1 = set(DAO.getPlaylistsforArtist(artist1))

                # RECUPERO LE PLAYLIST DELL'ARTISTA 2
                playlist2 = set(DAO.getPlaylistsforArtist(artist2))

                # TROVO LE PLAYLIST PRESENTI IN ENTRAMBI GLI ARTISTI
                comuni = playlist1.intersection(playlist2)

                # IL PESO È IL NUMERO DI PLAYLIST DISTINTE IN COMUNE
                peso = len(comuni)

                # SE ESISTE ALMENO UNA PLAYLIST IN COMUNE, CREO L'ARCO
                if peso > 0:
                    self._graph.add_edge(artist1, artist2, weight=peso)


    def getNodes(self):
        return len(self._graph.nodes())

    def getEdges(self):
        return len(self._graph.edges())


