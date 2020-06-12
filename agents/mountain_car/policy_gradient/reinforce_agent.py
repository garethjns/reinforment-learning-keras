from dataclasses import dataclass

from agents.agent_helpers.virtual_gpu import VirtualGPU
from agents.cart_pole.policy_gradient.reinforce_agent import ReinforceAgent as CartReinforceAgent


@dataclass
class ReinforceAgent(CartReinforceAgent):
    env_spec: str = "MountainCar-v0"
    learning_rate: float = 0.001

    @staticmethod
    def _final_reward(reward: float) -> float:
        return 250

    @classmethod
    def example(cls, n_episodes: int = 1000, render: bool = True) -> "ReinforceAgent":
        """Run a quick example with n_episodes and otherwise default settings."""
        VirtualGPU(128)
        agent = cls("MountainCar-v0")
        agent.train(verbose=True, render=render,
                    update_every=1,
                    max_episode_steps=1000,
                    n_episodes=n_episodes)

        return agent


if __name__ == "__main__":
    agent_ = ReinforceAgent.example(render=False)
    agent_.save("reinforce_agent_mountain_car.pkl")
