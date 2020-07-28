from concurrent.futures import ThreadPoolExecutor, as_completed

DEFAULT_WORKERS = 10


def threaded_generator(func, *args, items=(), workers=DEFAULT_WORKERS, **kwargs):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(func, k, v, *args, **kwargs): k for k, v in items}

        for future in as_completed(futures):
            yield futures[future], future.result()


def threaded_task(func, *args, items=(), workers=DEFAULT_WORKERS, **kwargs):
    results = {}

    for future, result in threaded_generator(
            func, items=items, workers=workers, *args, **kwargs
    ):
        results.update({future: result})

    return results
