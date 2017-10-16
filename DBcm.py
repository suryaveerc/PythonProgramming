from mysql import connector 
class UserDatabase:
    def __init__(self, config: dict) -> None:
        self.configuration = config
    
    def __enter__(self) -> 'cursor':
        self.conn = connector.connect(**self.configuration)
        self.cursor = conn.cursor()
        return self.cursor
    
    def __exit__(self) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    