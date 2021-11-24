import sys
import os
import json

sys.path.insert(0, 'src')

from etl import ngram_output



def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''
    test_config = json.load(open('config/data-params.json'))

    if 'test' in targets:
        ngram_output(**test_config)
    # if 'data' in targets:
    #     with open('config/data-params.json') as fh:
    #         data_cfg = json.load(fh)

    #     # make the data target
    #     data = get_data(**data_cfg)

    # if 'features' in targets:
    #     with open('config/features-params.json') as fh:
    #         feats_cfg = json.load(fh)

    #     feats, labels = apply_features(data, **feats_cfg)

    # if 'model' in targets:
    #     with open('config/model-params.json') as fh:
    #         model_cfg = json.load(fh)

    #     # make the data target
    #     model_build(feats, labels, **model_cfg)

    return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)