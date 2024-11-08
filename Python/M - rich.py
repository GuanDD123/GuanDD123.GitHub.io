import rich


def color():
    WHITE = '#aaaaaa'
    YELLOW = 'bright_yellow'
    GREEN = 'bright_green'
    RED = 'bright_red'
    CYAN = 'bright_cyan'


def print_():
    rich.print(f'[color]{object}',
               sep=str,
               end=str)


def progress():
    from rich.progress import (
        Progress,
        TextColumn, SpinnerColumn, BarColumn, DownloadColumn, TransferSpeedColumn,
        TimeElapsedColumn, TimeRemainingColumn
    )

    progress = Progress(
        TextColumn('[progress.description]{task.description}', style=str['color']),  # 显示文本
        SpinnerColumn(),  # 显示“微调”动画
        BarColumn(  # 显示条形图
            bar_width=int),
        '[progress.percentage]{task.percentage:>3.1f}%',
        '•',
        DownloadColumn(binary_units=True),  # 显示下载进度（假设步骤为字节）
        '•',
        TransferSpeedColumn(),  # 显示传输速度（假设步长为字节）
        '•',
        TimeElapsedColumn(),  # 显示经过的时间
        TimeRemainingColumn(),  # 显示估计的剩余时间
        transient=True  # 进度显示在退出时消失
    )

    task_id = progress.add_task(description=str,
                                total=float)
    progress.update(task_id=task_id,
                    advance=float)
    progress.remove_task(task_id=task_id)


def table():
    from rich.table import Table

    table = Table(title=str, title_style=str['color'],  # 表格上方显示的文本
                  style=str['color'],  # 设置表格线条的颜色
                  show_lines=True,  # 显示行之间的线条、页眉/页脚
                  expand=True,  # 表格最大化显示
                  header_style=str['color'])  # 设置标题行文本颜色

    table.add_column(header=str,
                     header_style=str['color'])  # 设置标题行文本颜色

    table.add_row(f'[color]{object}', ...)

    rich.print(table)
