from .base_import import *


@api_bp.route("/hello", methods=["POST", "GET"])
def hello():
    return "this is flask hello-world !"


@api_bp.route("/one", methods=["POST", "GET"])
def ball_history():
    sql = "SELECT * FROM ball.ball_history WHERE id < 6;"
    ret = sql_engine.execute(sql)

    data = ret.fetchall()
    print("type" + str(type(data)))
    code = {"code": 200, "message": "成功", "data": []}

    code["code"] = 200
    code["data"] = str(data)

    return jsonify(code)


@api_bp.route("/redis", methods=["POST", "GET"])
def redis():
    print(redis_engine.get("yang"))
    redis_engine.set("yang", "asdogoaisydfa")

    return jsonify(redis_engine.get("yang"))


@api_bp.route("/tow", methods=["POST", "GET"])
def ball_history_t():
    session = Session()

    print(session)
    # ball_3001 = session.query(Ball_history).filter_by(issue=3001).one()

    ball_3001 = session.query(Ball_history).all()
    # session.add(Ball_history)

    code = {"code": 200, "message": "成功", "data": []}

    code["code"] = 200
    code["data"] = ball_3001.__repr__()

    return jsonify(code)


@api_bp.route("/three", methods=["POST", "GET"])
def ball_historyss():
    session = Session()

    print(session)
    # ball_3001 = session.query(Ball_history).filter_by(issue=3001).one()

    ball_3001 = session.query(Ball_history).all()

    code = {"code": 200, "message": "成功", "data": []}

    # code["code"] = 200
    # code["data"] = ball_3001.__repr__()

    return jsonify(code)
