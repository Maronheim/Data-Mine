from modules.pipeline.pipeline_controller import pipeline

if __name__ == "__main__":
    config = {
        'data_files': {
            'jobs': 'modules/data/data_files/jobs.csv',
            'stocks': 'modules/data/data_files/market_data.csv'
        }
    }

    pipe = pipeline(config)
    pipe.run()