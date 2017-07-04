"""Pydacity main application code"""

import json
import subprocess
from rop import read_only_properties

FFPROBE_CMD_TEMPLATE = 'ffprobe -v quiet -print_format json -show_format -show_streams -i {0}'

@read_only_properties('filename', 'duration', 'sample_rate', 'channels', 'bitrate', 'codec', 'size', 'bit_per_sample')
class AudioFile(object):

    def __init__(self, filename):
        self.filename = filename
        output = self.__ffprobe_stats()

        self.duration = output['duration']
        self.sample_rate = output['sample_rate']
        self.channels = output['channels']
        self.codec = output['codec']
        self.bitrate = output['bitrate']
        self.size = output['size']
        self.bits_per_sample = output['bits_per_sample']

    def __ffprobe_stats(self):
        result = subprocess.check_output(FFPROBE_CMD_TEMPLATE.format(self.filename).split())
        string_result = result.decode('utf-8')

        # assume 1 stream
        json_result_stream = json.loads(string_result)['streams'][0]
        json_result_format = json.loads(string_result)['format']

        return {'duration': float(json_result_stream['duration']),
                'sample_rate': int(json_result_stream['sample_rate']),
                'channels': int(json_result_stream['channels']),
                'bits_per_sample': int(json_result_stream['bits_per_sample']),
                'bitrate': int(json_result_stream['bit_rate']),
                'codec': json_result_stream['codec_name'],
                'size': int(json_result_format['size'])}
