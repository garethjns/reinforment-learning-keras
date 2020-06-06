import gym

from agents.pong.environment_processing.fire_start_wrapper import FireStartWrapper
from agents.pong.environment_processing.frame_buffer_wrapper import FrameBufferWrapper
from agents.pong.environment_processing.image_process_wrapper import ImageProcessWrapper
from agents.pong.environment_processing.max_and_skip_wrapper import MaxAndSkipWrapper

GYM_ENV = gym.make("Pong-v0")

ENV_STACK = FrameBufferWrapper(FireStartWrapper(ImageProcessWrapper(MaxAndSkipWrapper(GYM_ENV))))
ENV_DIFF = FrameBufferWrapper(FireStartWrapper(ImageProcessWrapper(MaxAndSkipWrapper(GYM_ENV))),
                              buffer_length=2,
                              buffer_function='diff')
