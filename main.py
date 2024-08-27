import json
import logging.config
import yaml
from scripts.lateral_movement import simulate_lateral_movement
from scripts.persistence import simulate_persistence
from scripts.data_exfiltration import simulate_data_exfiltration

# Load configuration files
with open('config/apt_config.json', 'r') as f:
    apt_config = json.load(f)

with open('config/logging_config.yaml', 'r') as f:
    logging_config = yaml.safe_load(f)

# Configure logging
logging.config.dictConfig(logging_config)
logger = logging.getLogger('apt_simulation')

def main():
    logger.info("Starting APT Simulation")

    if apt_config['lateral_movement']['enabled']:
        simulate_lateral_movement(apt_config['lateral_movement']['techniques'])
    
    if apt_config['persistence']['enabled']:
        simulate_persistence(apt_config['persistence']['techniques'])
    
    if apt_config['data_exfiltration']['enabled']:
        simulate_data_exfiltration(apt_config['data_exfiltration']['methods'])

    logger.info("APT Simulation Completed")

if __name__ == "__main__":
    main()
