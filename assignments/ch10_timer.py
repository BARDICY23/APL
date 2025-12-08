import time
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        end = time.perf_counter()
        print(f"Execution took {end - self.start:.6f} seconds")
if __name__ == '__main__':
    with Timer():
        for i in range(1000000):
            pass
