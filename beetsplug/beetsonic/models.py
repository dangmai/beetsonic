class BeetModel:
    def __init__(self, lib):
        self.lib = lib

    def get_indexes(self):
        with self.lib.transaction() as tx:
            rows = tx.query("SELECT DISTINCT albumartist FROM albums")
        all_artists = [row[0] for row in rows]
        return all_artists
