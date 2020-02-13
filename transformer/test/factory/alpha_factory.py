

class AlphaFactory:

    def __init__(self, tools):
        self.tools = tools

    def mock_user():
        return {
          "user_id": tools.unique_key(),
          "user_name": tools.unique_key(),
          "first_name": tools.unique_key(),
          "middle_name": tools.unique_key(),
          "last_name": tools.unique_key(),
          "birth_date": tools.unique_key(),
          "gender": tools.unique_key(),
          "address_1": tools.unique_key(),
          "address_2": tools.unique_key(),
          "city": tools.unique_key(),
          "state": tools.unique_key(),
          "zip": tools.unique_key(),
        }
