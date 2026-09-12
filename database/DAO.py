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
        query = "select distinct a.* from artist a ,track t,album al where a.ArtistId =al.ArtistId and al.AlbumId =t.AlbumId order by a.Name"
        cursor.execute(query)

        for row in cursor:
            results.append(Artist(row["ArtistId"],row["Name"]))
        cursor.close()
        conn.close()

        for artist in results:
           artist.Tracks=DAO.getTracksForArtist(artist.ArtistId)
        return results

    @staticmethod
    def getTracksforArtist(artist):
        #gli passo l'artist e lo popolo con i suoi tracks
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query="select distinct t. from track t,artist a ,album al where t.AlbumId = al.AlbumId and a.ArtistId =al.ArtistId and a.ArtistId = %s order by t.Name"

        cursor.execute(query, (artist.ArtistId,))  # Prendi l'AlbumId dell'oggetto che hai ricevuto in input e lo usi per %s.
        for row in cursor:
            results.append(Track(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getPlaylistsforArtist(a):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query ="select pl.* from track t,artist a ,album al,playlisttrack p ,playlist pl where t.AlbumId = al.AlbumId and a.ArtistId =al.ArtistId and a.ArtistId =%s and t.TrackId is not null and t.TrackId =p.TrackId and p.PlaylistId =pl.PlaylistId order by t.Name"

        cursor.execute(query,
                       (a.ArtistId,))  # Prendi l'AlbumId dell'oggetto che hai ricevuto in input e lo usi per %s.
        for row in cursor:
            results.append(Playlist(**row))
            a.Playlist = results

        cursor.close()
        conn.close()


