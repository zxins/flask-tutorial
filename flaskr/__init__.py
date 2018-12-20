# -*- coding:utf-8 -*-

import os
from flask import Flask


def create_app(test_config=None):
    """
    instance_relative_config=True 告诉应用配置文件是相对于
    instance folder 的相对路径。实例文件夹在 flaskr 包的外面，
    用于存放本地数据（例如配置密钥和数据库），不应当 提交到版本控制系统。
    """
    app = Flask(__name__, instance_relative_config=True)

    # 默认配置
    app.config.from_mapping(
        SECRET_KEY='KEY',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # 非测试, 从文件加载配置(如果存在)
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 加载传进来的配置
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)

    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from flaskr import db
    db.init_app(app)

    from flaskr import auth
    app.register_blueprint(auth.bp)

    return app
