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

        # 🔴 RECUPERO LE PLAYLIST UNA SOLA VOLTA PER OGNI ARTISTA
        # 🔴 COSI EVITIAMO DI FARE MIGLIAIA DI QUERY AL DATABASE
        for artist in artists:
            artist.Playlists = set(DAO.getPlaylistsforArtist(artist))

        # CONFRONTO OGNI ARTISTA CON GLI ARTISTI SUCCESSIVI
        for i, artist1 in enumerate(artists):
            for artist2 in artists[i + 1:]:

                # RECUPERO LE PLAYLIST DELL'ARTISTA 1
                playlist1 = artist1.Playlists

                # RECUPERO LE PLAYLIST DELL'ARTISTA 2
                playlist2 = artist2.Playlists

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

    def getArtistMaxDegree(self):
        # TROVO L'ARTISTA CON IL GRADO MAGGIORE
        artist = max(self._graph.nodes, key=self._graph.degree) #GRADO: proprietà di un nodo
        grado=self._graph.degree(artist)
        return artist,grado

    def getArtistMaxWeight(self):
        # TROVO L'ARTISTA CON LA SOMMA DEI PESI (DEGLI ARCHI INCIDENTI) MASSIMA
        artist = max(
            self._graph.nodes,
            #per ogni rtista a calcola questa somma sum
            key=lambda a: sum(
                self._graph[a][neighbor]["weight"] #(3) DAMMI L'ARCO CHE COLLEGA a con quel neighbor, in particolare weight
                # (2) for neighbor in "prendi uno alla volta"
                for neighbor in self._graph.neighbors(a) # (1) dammi tutti gli artisti collegati all'artista a
            )
        )

        # CALCOLO LA SOMMA DEI PESI DELL'ARTISTA TROVATO
        somma = sum(
            self._graph[artist][neighbor]["weight"]
            for neighbor in self._graph.neighbors(artist)
        )

        return artist, somma
        return artist
    def getTop10Edges(self):
        # RECUPERO TUTTI GLI ARCHI DEL GRAFO CON IL LORO PESO
        edges = list(self._graph.edges(data=True))

        # ORDINO GLI ARCHI:
        # PRIMA PER PESO DECRESCENTE
        # IN CASO DI PARITÀ PER NOME DEL PRIMO ARTISTA
        # E POI PER NOME DEL SECONDO ARTISTA
        edges.sort(
            key=lambda e: (-e[2]["weight"], e[0].Name, e[1].Name)
        )

        # RESTITUISCO SOLO I PRIMI 10 ARCHI
        return edges[:10]



