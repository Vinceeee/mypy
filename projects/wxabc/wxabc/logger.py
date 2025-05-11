from loguru import logger
from opentelemetry import trace
from typing import List, Any, Callable, Optional


class LoggerConfig:
    """日志处理器配置类"""

    def __init__(
        self,
        sink: Any = lambda msg: print(msg, end=""),
        format: Optional[str] = None,
        level: str = "INFO",
        enqueue: bool = True,
        backtrace: bool = True,
        diagnose: bool = True,
        filter: Optional[Callable] = None,
        **kwargs: Any,
    ):
        self.sink = sink
        self.format = format or (
            "{time:YYYY-MM-DD HH:mm:ss.SSS} | "
            "<level>{level: <8}</level> | "
            "<cyan>{extra[traceid]}</cyan> | "
            "<cyan>{file}:{line}</cyan> | "
            "<level>{message}</level>"
        )
        self.level = level
        self.enqueue = enqueue
        self.backtrace = backtrace
        self.diagnose = diagnose
        self.filter = filter
        self.kwargs = kwargs


def configure_logger(handlers: List[LoggerConfig]) -> None:
    """配置日志处理器

    Args:
        handlers: 日志处理器配置列表
    """
    logger.remove()

    # 获取当前trace_id
    current_span = trace.get_current_span()
    trace_id = current_span.get_span_context().trace_id if current_span.is_recording() else "no-trace"

    for handler in handlers:
        # 如果filter未设置，使用默认的trace_id过滤器
        filter_func = handler.filter or (lambda record: record.update(extra={"traceid": trace_id}) or True)

        logger.add(
            sink=handler.sink,
            format=handler.format,
            level=handler.level,
            enqueue=handler.enqueue,
            backtrace=handler.backtrace,
            diagnose=handler.diagnose,
            filter=filter_func,
            **handler.kwargs,
        )


# 默认配置 - 控制台输出
default_console_handler = LoggerConfig()

# 初始化默认logger
configure_logger([default_console_handler])
