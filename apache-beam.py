import apache_beam
import re

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

input = "myrandomtext"

pipeline_options = PipelineOptions()

with beam.Pipeline(options=pipeline_options) as p:

  # Read the text file[pattern] into a PCollection.
  lines = p | 'Read' >> ReadFromText(input)
  
  counts = (
      lines
      | 'Split' >> beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x))
      | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
      | 'GroupAndSum' >> beam.CombinePerKey(sum))
  
  # Format the counts into a PCollection of strings.
  def format_result(word_count):
    (word, count) = word_count
    if count > 4:
       return '%s: %d' % (word, count)
  
  output = counts | 'Format' >> beam.Map(format_result)
 
  output | WriteToText('/tmp/output')
