"""Renders the starting layout of an environment."""

from environment import TreasureHunt
import argparse
from utils import get_env_config
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "--env_name", type=str, required=True, help="The PressurePlate configuration to use. See env_configs.py for supported configurations."
)

if __name__ == "__main__":
    args = parser.parse_args()
    env_config = get_env_config(args.env_name)
    env = TreasureHunt(env_config)
    env.render()
    input()
    sys.exit()
