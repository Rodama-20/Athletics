"""
Exception classes for the CJAJB Athletics app.
"""


class NoTableError(Exception):
    """
    Exception raised when a table is not found.
    """

    def __init__(self, discipline: str, table_name: str, *args: object) -> None:
        self.message = f"Table '{table_name}' does not exist for {discipline}."
        super().__init__(*args)
