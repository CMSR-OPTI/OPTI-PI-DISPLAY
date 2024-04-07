import json
import math

class DataSample:
    temperature : float = float('nan')
    longitude : float = float('nan')
    latitude : float = float('nan')
    accel_x : float = float('nan')
    accel_y : float = float('nan')
    accel_z : float = float('nan')
    time : float = float('nan')

    def set_accel(self,accel_x,accel_y,accel_z):
        self.accel_x = accel_x
        self.accel_y = accel_y
        self.accel_z = accel_z

    def set_loc(self,long,lat):
        self.long = long
        self.lat = lat

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        command_dict = json.loads(json_str)
        command = cls()
        for key, value in command_dict.items():
            setattr(command, key, value)
        return command
    
    @classmethod
    # Assumes all variables that we need to encode are floats
    def make_c_encoder(cls):
        # Initialize an empty list to store format strings for each attribute
        format_strings = []
        
        # Combine attribute format strings into JSON format string
        json_format_string = '{' + ', '.join([f'"{attr_name}": %.6f' for attr_name in cls.__annotations__]) + '}'
        json_format_string = json_format_string.replace('"', '\\"')

        # Extract data from class instance
        variables = ', '.join([attr_name for attr_name in cls.__annotations__])

        encoder_command = f'snprintf(buf,len,"{json_format_string}", {variables});'

        typed_variables = 'float ' + ', float '.join([attr_name for attr_name in cls.__annotations__])

        function = \
f"""int make_json_data_sample(char *buf, size_t len, {typed_variables}) {{
  {encoder_command}
  return 0;
}}
"""

        # Use sprintf to format data according to JSON structure
        # result = json_format_string.format(*data)
        return function
    
if __name__ == "__main__":
    print(DataSample.make_c_encoder())