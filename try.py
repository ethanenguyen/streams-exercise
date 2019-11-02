"""
USAGE: `python try.py 123456`
"""

import io
import sys

from stream_exercise import StreamProcessor

# value = sys.argv[1]
value = '234761640930110349378289194'

my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()
print("Processed {} and got {}".format(value, result))
