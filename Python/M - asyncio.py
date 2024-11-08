import asyncio


def _():
    '''
    可等待对象，指可以在 await 语句中使用的对象；
    有三种主要类型: 协程、任务、Future
    '''


async def declare_coroutine():
    pass


def run_coroutine():
    asyncio.run(main=declare_coroutine())  # 可运行最高层级的入口点协程函数
    # 可以自动创建事件循环，并在协程执行完毕后关闭事件循环

    async def f():
        await declare_coroutine()  # 运行单个协程
        task = asyncio.create_task(coro=declare_coroutine())  # 该任务会在事件循环中执行，如果当前线程没有在运行的循环则会引发 RuntimeError
        await asyncio.gather(task, task, ...)  # 并发执行多个任务


async def sleep():
    await asyncio.sleep(delay=float)  # 挂起当前任务，允许其他任务运行


async def max_concurrency():
    async with asyncio.Semaphore(value=int):
        pass
