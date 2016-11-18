class BeetModel(object):
    def __init__(self, lib):
        self.lib = lib

    def get_album_artists(self):
        with self.lib.transaction() as tx:
            rows = tx.query(
                'SELECT DISTINCT albumartist FROM albums ORDER BY albumartist'
            )
        all_artists = [row[0] for row in rows]
        return all_artists

    def get_singletons(self):
        results = self.lib.items(u'singleton:true')
        return [item for item in results]

    def get_last_modified(self):
        with self.lib.transaction() as tx:
            rows = tx.query('SELECT max(mtime) FROM items')
        return rows[0][0]
