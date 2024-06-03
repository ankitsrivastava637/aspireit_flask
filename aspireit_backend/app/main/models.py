class BufferObject:
    def __init__(self, user_id, buffer_type, buffer_data):
        self.user_id = user_id
        self.buffer_type = buffer_type
        self.buffer_data = buffer_data

    @staticmethod
    def from_dict(data):
        return BufferObject(
            user_id=data.get('user_id'), 
            buffer_type=data.get('buffer_type'), 
            buffer_data=data.get('buffer_data')
        )

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'buffer_type': self.buffer_type,
            'buffer_data': self.buffer_data
        }