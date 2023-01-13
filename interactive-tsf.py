import tensorflow as tf
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext

context = InteractiveContext()

from tfx.components import StatisticsGen


stat_gen = StatisticsGen(examples=example_gen.outputs['examples'])

context.run(stat_gen)

context.show(stat_gen.outputs['statistics'])
