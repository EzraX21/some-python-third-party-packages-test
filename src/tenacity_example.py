import random
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(wait=wait_exponential(min=1, max=10), stop=stop_after_attempt(3))
def call_flaky_api():
    if random.random() < 0.7:
        raise ValueError("API 调用失败")  # 必须抛出异常才会触发重试
    return "ok"

try:
    print(call_flaky_api())
except Exception as e:
    print(f"重试3次后依然失败: {e}")