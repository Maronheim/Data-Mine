from modules.pipeline.pipeline_controller import pipeline

if __name__ == "main":
    config = {
        'data_sources': {
            'jobs': 'data/jobs.csv',
            'stocks': 'data/market_data.csv'
        }
    }

    pipe = pipeline(config)
    pipe.run()