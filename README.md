```shell
export FLASK_APP=flaskr
export FLASK_ENV=development

flask init-db
flask run

# 安装项目
pip install -e .


# 运行测试
coverage run -m pytest
# 代码覆盖率报告
coverage report

# 构建和安装
pip install wheel
python setup.py bdist_wheel

# 构建的文件为 dist/flaskr-1.0.0-py3-none-any.whl 。
# 文件名由项目名称、版 本号和一些关于项目安装要求的标记组成。
# 复制这个文件到另一台机器， 创建一个新的虚拟环境 ，然后用 pip 安装这个文件。
pip install flaskr-1.0.0-py3-none-any.whl


# Pip 会安装项目和相关依赖。
# 既然这是一个不同的机器，那么需要再次运行 init-db 命令，在实例文件夹中 创建数据库。
export FLASK_APP=flaskr
flask init-db

# 当 Flask 探测到它已被安装（不在编辑模式下），它会与前文不同，
# 使用 venv/var/flaskr-instance 作为实例文件夹。

# 运行服务器
pip install waitress
waitress-serve --call 'flaskr:create_app'


```