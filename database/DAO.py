from database.DB_connect import DBConnect
from model.artist import Artist
from model.playlist import Playlist
from model.track import Track


class DAO():

    @staticmethod
    def getAllArtists():
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        #NOTA: QUESTA QUERY GARANTISCE GIA CHE GLI ARTISTI RESTITUITI ABBIANO ALMENO UN TRACK
        query = "select distinct a.* from artist a ,track t,album al where a.ArtistId =al.ArtistId and al.AlbumId =t.AlbumId order by a.Name" #in ordine alfabetico by NAME
        cursor.execute(query)

        for row in cursor:
            results.append(Artist(row["ArtistId"],row["Name"]))
        cursor.close()
        conn.close()

        for artist in results:
           artist.Tracks=DAO.getTracksforArtist(artist.ArtistId)
        return results

    @staticmethod
    def getTracksforArtist(artistId):
        #gli passo l'artist e lo popolo con i suoi tracks
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query="select distinct t.TrackId from track t,artist a ,album al where t.AlbumId = al.AlbumId and a.ArtistId =al.ArtistId and a.ArtistId = %s order by t.TrackId"

        cursor.execute(query, (artistId,))  # Prendi l'AlbumId dell'oggetto che hai ricevuto in input e lo usi per %s.
        for row in cursor:
            results.append(row["TrackId"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getPlaylistsforArtist(a):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        #HO GIA GARANTITO CHE LE PLAYLIST SONO DISTINTE
        query ="select distinct pl.PlaylistId from track t,artist a ,album al,playlisttrack p ,playlist pl where t.AlbumId = al.AlbumId and a.ArtistId =al.ArtistId and a.ArtistId =%s and t.TrackId is not null and t.TrackId =p.TrackId and p.PlaylistId =pl.PlaylistId"

        cursor.execute(query,
                       (a.ArtistId,))  # Prendi l'AlbumId dell'oggetto che hai ricevuto in input e lo usi per %s.
        for row in cursor:
            results.append(row["PlaylistId"]) #LE PLAYLIST IN CUI COMPARE ALMENO UN BRANO DELL'ARTISTA a.

        cursor.close()
        conn.close()
        return results


