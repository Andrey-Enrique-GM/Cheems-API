
class ResultDto:
    def __init__(self, id: int, success: bool, message: str):
        self.id = id
        self.success = success
        self.message = message


    # Este método convierte el objeto ResultDto en un diccionario para que pueda ser serializado a JSON
    def to_dict(self):
        return {
            "id": self.id,
            "success": self.success,
            "message": self.message
        }
    