import collections
import os
import os.path as osp
import subprocess
from collections import OrderedDict

import yaml

def write_experiment_metadata(entrypoint, exp_dir):
    print(entrypoint)
    os.makedirs(exp_dir, exist_ok=True)
    dump_experiment_metadata_to_file(osp.join(exp_dir, "experiment_metadata.yaml"), entrypoint)

def dump_experiment_metadata_to_file(yaml_path, entrypoint):
    """Write the metadata for an experiment to a file"""
    # Order so that the experiment_name is at the top
    exp_data = collections.OrderedDict()
    exp_data['experiment_name'] = osp.basename(osp.dirname(yaml_path))
    exp_data['command'] = ' '.join(entrypoint)

    for k, v in collect_git_data().items():
        exp_data[k] = v

    with open(yaml_path, 'w') as f:
        yaml.dump(exp_data, f, default_flow_style=False)

def collect_git_data():
    d = collections.OrderedDict()
    try:
        d['commit'] = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode('utf-8').strip()
        d['diff'] = subprocess.check_output(["git", "diff"]).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        print("WARNING: Failed to get commit information from git. Run `git status` to debug")
        d['commit'] = '[unknown]'
        d['diff'] = '[unknown]'
    try:
        # Repository is optional, so we fail silently if it's not available
        d['repository'] = subprocess.check_output(["git", "remote", 'get-url'], stderr=open(os.devnull, 'wb')).decode(
            'utf-8').strip()
    except subprocess.CalledProcessError:
        d['repository'] = '[unknown]'
    return d

# PyYaml doesn't know how to serialized ordereddicts by default, so we add a representer
# http://stackoverflow.com/questions/16782112/can-pyyaml-dump-dict-items-in-non-alphabetical-order
def _represent_ordereddict(dumper, data):
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

yaml.add_representer(OrderedDict, _represent_ordereddict)
