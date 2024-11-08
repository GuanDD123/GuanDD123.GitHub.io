class Memoization:
    '''备忘 (memoization)：可以把耗时的函数得到的结果保存起来'''

    from functools import cache
    '''cache
    是对 @lru_cache 的简单包装

    适合短期运行的命令行脚本使用

    被装饰的函数所接受的参数必须可哈希
    '''

    from functools import lru_cache
    '''lru_cache
    适合长期运行的进程使用

    maxsize 参数限制内存用量上限（默认为 128）
    type 参数决定是否把不同参数类型得到的结果分开保存（默认为 False）

    被装饰的函数所接受的参数必须可哈希，因为 lru_cache 使用 dict 存储结果，字典的键取自传入的位置参数和关键字参数
    '''


class GenericFunction:
    '''
    泛化函数 (generic function)
    单分派泛化函数，指根据第一个参数的类型，以不同方式执行相同操作的一组函数
    '''

    from functools import singledispatch
    '''singledispatch
    @singledispatch 标记基函数
    各个专门函数使用 @base_function_name.register 装饰

    如果不想为装饰的类型添加类型提示，可以把类型传给 @base_function_name.register 装饰器
    '''
