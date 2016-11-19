"""
Model to get music information from beets.
"""
from beetsplug.beetsonic import utils


class BeetModel(object):
    def __init__(self, lib):
        self.lib = lib

    @staticmethod
    def _create_artist(name, **kwargs):
        # Since beets doesn't track artist ids, we'll make the id the name
        # of the artist, prefixed with the string 'artist:', in order to
        # differentiate between Artist and other metadata types.
        return utils.create_artist('artist:' + name, name, **kwargs)

    def get_album_artists(self):
        """
        Get all album artists
        :return: List of Artist objects
        """
        with self.lib.transaction() as tx:
            rows = tx.query(
                'SELECT DISTINCT albumartist FROM albums ORDER BY albumartist'
            )
        return [self._create_artist(row[0]) for row in rows]

    def get_singletons(self):
        results = self.lib.items(u'singleton:true')
        # return [item for item in results]
        return [utils.create_song(item.id, item.title, album=item.album,
                                  artist=item.artist)
                for item in results]

    def get_last_modified(self):
        with self.lib.transaction() as tx:
            rows = tx.query('SELECT max(mtime) FROM items')
        return rows[0][0]
