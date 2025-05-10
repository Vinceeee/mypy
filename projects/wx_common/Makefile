# 定义变量
PYTHON = python3
UV = uv
RUFF = uv run ruff
PROJECT_NAME = wx_common
TEST_DIR = tests
VENV = venv
REQUIREMENTS = requirements.txt
DEV_REQUIREMENTS = requirements-dev.txt

# 默认目标
.DEFAULT_GOAL := help

# 帮助信息
help:
	@echo "可用命令:"
	@echo "  make dev        安装开发环境依赖(使用uv)"
	@echo "  make test       运行测试"
	@echo "  make lint       使用ruff进行代码检查"
	@echo "  make format     使用ruff格式化代码"
	@echo "  make clean      清理临时文件"
	@echo "  make run        运行项目"
	@echo "  make help       显示帮助信息"


# 使用uv安装开发环境依赖
dev:
	@echo "使用uv安装开发环境依赖..."
	$(UV) uv sync

# 运行测试
test:
	@echo "运行测试..."
	$(PYTHON) -m pytest $(TEST_DIR)

# 使用ruff进行代码检查
lint:
	@echo "使用ruff进行代码检查,并尝试修复..."
	$(RUFF) check $(PROJECT_NAME) --fix --unsafe-fixes

# 使用ruff格式化代码
format:
	@echo "使用ruff格式化代码..."
	$(RUFF) format $(PROJECT_NAME)

# 清理临时文件
clean:
	@echo "清理临时文件..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache

# 运行项目
run:
	@echo "启动项目..."
	$(PYTHON) -m $(PROJECT_NAME)

.PHONY: help venv install dev test lint format clean run
